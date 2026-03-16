# Multi-Currency Sub-Accounts Feature

## Overview
Each user account in PyATM holds **three separate sub-accounts**, one per supported currency. There is no conversion between currencies — each sub-account holds and tracks its own balance independently.

## Supported Currencies

| Code | Currency         | Symbol |
|------|------------------|--------|
| GHS  | Cedis            | ₵      |
| USD  | US Dollars       | $      |
| GBP  | Pounds Sterling  | £      |

## Data Model

Each account in `atm_data.json` stores a `balances` dict with all three currencies:

```json
{
  "1234": {
    "name": "Alice",
    "balances": {
      "GHS": 0.0,
      "USD": 0.0,
      "GBP": 0.0
    }
  }
}
```

## User Flow

### Deposit
1. User selects **Deposit** from the ATM menu
2. User is prompted to choose a currency account:
   ```
   Select currency account:
     [1] Cedis (₵)
     [2] Dollars ($)
     [3] Pounds Sterling (£)
   ```
3. User enters the amount
4. The amount is added to the selected currency sub-account

### Withdrawal
1. User selects **Withdraw** from the ATM menu
2. User selects which currency account to withdraw from
3. User enters the amount
4. If sufficient funds exist in that sub-account, the amount is deducted
5. If not, an **Insufficient funds** error is shown for that specific sub-account

### Check Balance
Displays all three sub-account balances at once:
```
Your balances:
  Cedis (₵):           ₵1,200.00
  Dollars ($):         $350.00
  Pounds Sterling (£): £75.00
```

## Implementation Notes
- `deposit(accounts, pin, currency, amount)` — adds to `balances[currency]`
- `withdraw(accounts, pin, currency, amount)` — checks and deducts from `balances[currency]`; raises `ValueError` on insufficient funds
- `check_balance(accounts, pin)` — iterates over all currencies and displays each balance
- `get_currency_choice()` — reusable helper that shows the currency menu and returns the selected currency code (e.g. `"GHS"`)
