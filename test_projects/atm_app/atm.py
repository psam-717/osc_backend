"""
ATM Machine Simulation.

Supports account creation (name + 4-digit PIN), login, and three separate
currency sub-accounts (GHS, USD, GBP) for deposit, withdrawal, and balance
checks. Account data is persisted to atm_data.json.
"""

import hashlib
import json
import os
import secrets
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

DATA_FILE = os.path.join(os.path.dirname(__file__), "atm_data.json")

# Supported currencies: code → display info
CURRENCIES: dict[str, dict] = {
    "GHS": {"name": "Cedis",           "symbol": "₵"},
    "USD": {"name": "Dollars",         "symbol": "$"},
    "GBP": {"name": "Pounds Sterling", "symbol": "£"},
}

# Exchange rates expressed in GHS (1 unit of currency = N GHS)
EXCHANGE_RATES: dict[str, Decimal] = {
    "GHS": Decimal("1"),
    "USD": Decimal("15"),
    "GBP": Decimal("19"),
}


class BackAction(Exception):
    """Raised when the user enters 0 to cancel the current operation."""


# ── Input helpers ────────────────────────────────────────────────────────────

def get_pin(prompt: str) -> str:
    """Prompt until a valid 4-digit numeric PIN is entered."""
    while True:
        pin = input(prompt).strip()
        if pin.isdigit() and len(pin) == 4:
            return pin
        print("-> PIN must be exactly 4 digits (numbers only).")


def get_positive_amount(prompt: str) -> Decimal:
    """Prompt until a valid positive number is entered. Enter 0 to cancel."""
    while True:
        raw = input(prompt + " (0 to go back): ").strip()
        if raw == "0":
            raise BackAction
        try:
            value = Decimal(raw)
            if value > 0:
                return value
            print("-> Amount must be greater than zero.")
        except Exception:
            print("-> Invalid input. Please enter a number.")


def get_menu_choice(prompt: str, valid: list[str]) -> str:
    """Prompt until the user enters one of the valid choices."""
    while True:
        choice = input(prompt).strip()
        if choice in valid:
            return choice
        print(f"-> Invalid choice. Please enter one of: {', '.join(valid)}")


def log_transaction(
    accounts: dict, key: str, tx_type: str,
    currency: str, amount: Decimal, balance_after: Decimal
) -> None:
    """Append a timestamped transaction entry to the account's history."""
    accounts[key]["transactions"].append({
        "type": tx_type,
        "currency": currency,
        "amount": str(amount),
        "balance_after": str(balance_after),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })


# ── Data layer ───────────────────────────────────────────────────────────────

def load_accounts(filepath: str) -> dict:
    """Load accounts from a JSON file. Returns an empty dict if file doesn't exist."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            backup = filepath + ".bak"
            os.rename(filepath, backup)
            print(f"-> Warning: account data was corrupted and has been backed up to {backup}.")
            print("-> Starting with an empty account database.")
            return {}
    # Restore Decimal balances from stored strings
    for account in data.values():
        account["balances"] = {k: Decimal(str(v)) for k, v in account["balances"].items()}
    return data


def save_accounts(filepath: str, accounts: dict) -> None:
    """Persist the accounts dict to a JSON file atomically."""
    tmp = filepath + ".tmp"
    # Serialize Decimal balances as strings for exact round-trip precision
    serializable = {}
    for key, account in accounts.items():
        serializable[key] = {
            **account,
            "balances": {k: str(v) for k, v in account["balances"].items()},
        }
    try:
        with open(tmp, "w") as f:    
            json.dump(serializable, f, indent=2)
        os.replace(tmp, filepath)  
    except OSError as e:
        raise RuntimeError(f"Failed to save account data: {e}") from e


# ── PIN hashing helpers ──────────────────────────────────────────────────────

def generate_salt() -> bytes:
    """Generate a cryptographically random 16-byte salt."""
    return secrets.token_bytes(16)


def hash_pin(pin: str, salt: bytes) -> str:
    """Return a hex digest of the PIN hashed with PBKDF2-HMAC-SHA256."""
    dk = hashlib.pbkdf2_hmac("sha256", pin.encode(), salt, iterations=100_000)
    return dk.hex()


# ── Account logic ────────────────────────────────────────────────────────────

def get_currency_choice() -> str:
    """Display a currency menu and return the selected currency code. Enter 0 to cancel."""
    codes = list(CURRENCIES.keys())
    print("\nSelect currency account:")
    for i, code in enumerate(codes, start=1):
        info = CURRENCIES[code]
        print(f"  [{i}] {info['name']} ({info['symbol']})")
    print("  [0] Back")
    choice = get_menu_choice("Select an option: ", ["0"] + [str(i) for i in range(1, len(codes) + 1)])
    if choice == "0":
        raise BackAction
    return codes[int(choice) - 1]


def create_account(accounts: dict) -> str:
    """
    Guide the user through creating a new account.
    Prompts for a name and a unique 4-digit PIN.
    Initializes three currency sub-accounts (GHS, USD, GBP) at 0.0.
    Returns the account key (PIN hash) on success.
    """
    print("\n--- Create New Account ---")
    name = ""
    while not name:
        name = input("Enter your name: ").strip()
        if not name:
            print("-> Name cannot be empty.")

    while True:
        pin = get_pin("Choose a 4-digit PIN: ")
        salt = generate_salt()
        key = hash_pin(pin, salt)
        if key in accounts:
            print("-> That PIN is already taken. Please choose a different one.")
        else:
            break

    accounts[key] = {
        "name": name,
        "pin_salt": salt.hex(),
        "balances": {code: Decimal("0") for code in CURRENCIES},
        "transactions": [],
    }
    print(f"\nAccount created! Welcome, {name}. All sub-account balances start at 0.00.")
    return key


def login(accounts: dict) -> str | None:
    """
    Prompt the user for their PIN and validate it.
    Allows up to 3 attempts. Returns the account key on success, or None on failure.
    """
    print("\n--- Login ---")
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        pin = get_pin("Enter your 4-digit PIN: ")
        for key, account in accounts.items():
            salt = bytes.fromhex(account["pin_salt"])
            if hash_pin(pin, salt) == key:
                print(f"\nWelcome back, {account['name']}!")
                return key
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"-> Incorrect PIN. {remaining} attempt(s) remaining.")
        else:
            print("-> Too many incorrect attempts. Returning to main menu.")
    return None


# ── ATM operations ───────────────────────────────────────────────────────────

def check_balance(accounts: dict, key: str) -> None:
    """Display all currency sub-account balances for the given account."""
    balances = accounts[key]["balances"]
    print("\nYour balances:")
    for code, info in CURRENCIES.items():
        print(f"  {info['name']:<20} {info['symbol']}{balances[code]:>12,.2f}")


def deposit(accounts: dict, key: str, currency: str, amount: Decimal) -> Decimal:
    """
    Add amount to the specified currency sub-account.
    Logs the transaction. Returns the updated sub-account balance.
    """
    accounts[key]["balances"][currency] += amount
    new_balance = accounts[key]["balances"][currency]
    log_transaction(accounts, key, "deposit", currency, amount, new_balance)
    return new_balance


def withdraw(accounts: dict, key: str, currency: str, amount: Decimal) -> Decimal:
    """
    Deduct amount from the specified currency sub-account.
    Raises ValueError if funds are insufficient.
    Logs the transaction. Returns the updated sub-account balance.
    """
    symbol = CURRENCIES[currency]["symbol"]
    current = accounts[key]["balances"][currency]
    if amount > current:
        raise ValueError(
            f"Insufficient funds. Available {CURRENCIES[currency]['name']} balance: "
            f"{symbol}{current:,.2f}"
        )
    accounts[key]["balances"][currency] -= amount
    new_balance = accounts[key]["balances"][currency]
    log_transaction(accounts, key, "withdrawal", currency, amount, new_balance)
    return new_balance


def view_transactions(accounts: dict, key: str) -> None:
    """Print the last 10 transactions for the account in a formatted table."""
    history = accounts[key]["transactions"]
    if not history:
        print("\nNo transactions yet.")
        return
    recent = history[-10:]
    print(f"\n{'#':<4} {'Timestamp':<20} {'Type':<14} {'Currency':<18} {'Amount':>14}     {'Balance After':>14}")
    print("-" * 92)
    for i, tx in enumerate(recent, start=1):
        code = tx["currency"]
        symbol = CURRENCIES[code]["symbol"]
        currency_name = CURRENCIES[code]["name"]
        amount = Decimal(str(tx["amount"]))
        balance_after = Decimal(str(tx["balance_after"]))
        print(
            f"{i:<4} {tx['timestamp']:<20} {tx['type']:<14} {currency_name:<18} "
            f"{symbol}{amount:>12,.2f}     {symbol}{balance_after:>12,.2f}"
        )


def change_pin(accounts: dict, current_key: str) -> str:
    """
    Let the user change their PIN.
    Verifies the current PIN, prompts for a new one (confirmed twice).
    New PIN must not already be taken. Enter 0 at any prompt to cancel.
    Returns the new account key after updating the accounts dict.
    """
    print("\n--- Change PIN --- (enter 0 to cancel)")
    confirm_raw = input("Confirm your current PIN: ").strip()
    if confirm_raw == "0":
        raise BackAction
    # Verify the entered PIN matches the stored hash
    salt = bytes.fromhex(accounts[current_key]["pin_salt"])
    if hash_pin(confirm_raw, salt) != current_key:
        print("-> Incorrect PIN. PIN change cancelled.")
        return current_key

    while True:
        new_pin = input("Enter new PIN: ").strip()
        if new_pin == "0":
            raise BackAction
        if not (new_pin.isdigit() and len(new_pin) == 4):
            print("-> PIN must be exactly 4 digits (numbers only).")
            continue
        new_salt = generate_salt()
        new_key = hash_pin(new_pin, new_salt)
        if new_key == current_key:
            print("-> New PIN must be different from the current PIN.")
            continue
        if new_key in accounts:
            print("-> That PIN is already in use. Choose a different one.")
            continue
        confirm_new = input("Confirm new PIN: ").strip()
        if confirm_new == "0":
            raise BackAction
        if confirm_new != new_pin:
            print("-> PINs do not match. Try again.")
            continue
        break

    # Copy to new key first; caller saves before we delete, so old key survives any save failure
    accounts[new_key] = {**accounts[current_key], "pin_salt": new_salt.hex()}
    print("PIN changed successfully!")
    return new_key


def transfer(
    accounts: dict, key: str,
    from_currency: str, to_currency: str, amount: Decimal
) -> tuple[Decimal, Decimal]:
    """
    Transfer amount from one currency sub-account to another.
    Converts via GHS as base using EXCHANGE_RATES.
    Raises ValueError if source funds are insufficient.
    Logs transfer_out and transfer_in entries.
    Returns (new_from_balance, new_to_balance).
    """
    from_symbol = CURRENCIES[from_currency]["symbol"]
    current = accounts[key]["balances"][from_currency]
    if amount > current:
        raise ValueError(
            f"Insufficient funds. Available {CURRENCIES[from_currency]['name']} balance: "
            f"{from_symbol}{current:,.2f}"
        )

    # Convert: amount in from_currency → GHS → to_currency
    amount_in_ghs = amount * EXCHANGE_RATES[from_currency]
    converted_amount = (amount_in_ghs / EXCHANGE_RATES[to_currency]).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

    accounts[key]["balances"][from_currency] -= amount
    new_from = accounts[key]["balances"][from_currency]

    accounts[key]["balances"][to_currency] += converted_amount
    new_to = accounts[key]["balances"][to_currency]

    log_transaction(accounts, key, "transfer_out", from_currency, amount, new_from)
    log_transaction(accounts, key, "transfer_in", to_currency, converted_amount, new_to)

    return new_from, new_to


# ── Main ATM flow ────────────────────────────────────────────────────────────

def run_atm() -> None:
    """Run the full ATM session loop."""
    print("=" * 40)
    print("       Welcome to PyATM!")
    print("=" * 40)

    accounts = load_accounts(DATA_FILE)

    while True:
        print("\nMain Menu:")
        print("  [1] Login")
        print("  [2] Create Account")
        print("  [3] Exit")
        choice = get_menu_choice("Select an option: ", ["1", "2", "3"])

        if choice == "3":
            print("\nThank you for using PyATM. Goodbye!")
            break

        if choice == "2":
            key = create_account(accounts)
            try:
                save_accounts(DATA_FILE, accounts)
            except RuntimeError as e:
                print(f"-> Warning: {e}. Your account was created but may not persist after restart.")
        else:
            key = login(accounts)
            if key is None:
                continue

        # ATM session menu
        name = accounts[key]["name"]
        while True:
            print(f"\nATM Menu  ({name})")
            print("  [1] Check Balance")
            print("  [2] Deposit")
            print("  [3] Withdraw")
            print("  [4] Transfer Between Accounts")
            print("  [5] Transaction History")
            print("  [6] Change PIN")
            print("  [7] Logout")
            action = get_menu_choice("Select an option: ", ["1", "2", "3", "4", "5", "6", "7"])

            if action == "7":
                print(f"\nLogged out. See you next time, {name}!")
                break

            elif action == "1":
                check_balance(accounts, key)

            elif action == "2":
                try:
                    currency = get_currency_choice()
                    symbol = CURRENCIES[currency]["symbol"]
                    amount = get_positive_amount(f"Enter deposit amount ({symbol})")
                    new_balance = deposit(accounts, key, currency, amount)
                    try:
                        save_accounts(DATA_FILE, accounts)
                    except RuntimeError as e:
                        print(f"-> Warning: {e}. Transaction recorded in session but not saved to disk.")
                    print(
                        f"Deposited {symbol}{amount:,.2f} into {CURRENCIES[currency]['name']} account. "
                        f"New balance: {symbol}{new_balance:,.2f}"
                    )
                except BackAction:
                    print("Cancelled. Returning to menu.")

            elif action == "3":
                try:
                    currency = get_currency_choice()
                    symbol = CURRENCIES[currency]["symbol"]
                    amount = get_positive_amount(f"Enter withdrawal amount ({symbol})")
                    try:
                        new_balance = withdraw(accounts, key, currency, amount)
                        try:
                            save_accounts(DATA_FILE, accounts)
                        except RuntimeError as e:
                            print(f"-> Warning: {e}. Transaction recorded in session but not saved to disk.")
                        print(
                            f"Withdrew {symbol}{amount:,.2f} from {CURRENCIES[currency]['name']} account. "
                            f"New balance: {symbol}{new_balance:,.2f}"
                        )
                    except ValueError as e:
                        print(f"-> {e}")
                except BackAction:
                    print("Cancelled. Returning to menu.")

            elif action == "4":
                try:
                    print("\n-- Transfer: From --")
                    from_currency = get_currency_choice()
                    print("\n-- Transfer: To --")
                    to_currency = get_currency_choice()
                    if from_currency == to_currency:
                        print("-> Source and destination accounts must be different.")
                        continue
                    from_symbol = CURRENCIES[from_currency]["symbol"]
                    to_symbol = CURRENCIES[to_currency]["symbol"]
                    amount = get_positive_amount(f"Enter amount to transfer ({from_symbol})")
                    try:
                        new_from, new_to = transfer(accounts, key, from_currency, to_currency, amount)
                        converted = (amount * EXCHANGE_RATES[from_currency] / EXCHANGE_RATES[to_currency]).quantize(
                            Decimal("0.01"), rounding=ROUND_HALF_UP
                        )
                        try:
                            save_accounts(DATA_FILE, accounts)
                        except RuntimeError as e:
                            print(f"-> Warning: {e}. Transaction recorded in session but not saved to disk.")
                        print(
                            f"Transferred {from_symbol}{amount:,.2f} → "
                            f"{to_symbol}{converted:,.2f} "
                            f"({CURRENCIES[to_currency]['name']}).\n"
                            f"  {CURRENCIES[from_currency]['name']} balance: {from_symbol}{new_from:,.2f}\n"
                            f"  {CURRENCIES[to_currency]['name']} balance:   {to_symbol}{new_to:,.2f}"
                        )
                    except ValueError as e:
                        print(f"-> {e}")
                except BackAction:
                    print("Cancelled. Returning to menu.")

            elif action == "5":
                view_transactions(accounts, key)

            elif action == "6":
                try:
                    old_key = key
                    key = change_pin(accounts, key)
                    if key != old_key:
                        try:
                            save_accounts(DATA_FILE, accounts)
                            # Delete old key only after a successful save
                            del accounts[old_key]
                            save_accounts(DATA_FILE, accounts)
                        except RuntimeError as e:
                            print(f"-> Warning: {e}. PIN change recorded in session but may not persist.")
                    name = accounts[key]["name"]
                except BackAction:
                    print("Cancelled. Returning to menu.")


if __name__ == "__main__":
    run_atm()
