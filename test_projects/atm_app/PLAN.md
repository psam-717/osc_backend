# ATM App — Code Review Fix Plan

## Problem
Five issues were identified in `atm.py`. This plan fixes all of them using only the Python standard library (no external deps — consistent with this repo's conventions).

## Fixes (in implementation order)

### 1. Corrupted JSON crashes the app *(Medium)*
**Location:** `load_accounts()` — lines 85–90

Wrap `json.load()` in a `try/except json.JSONDecodeError`. On failure, rename the corrupted file to `atm_data.json.bak` (using `os.rename`) and return `{}`, printing a warning to the user.

### 2. Atomic file writes + save error handling *(High)*
**Location:** `save_accounts()` — lines 93–96

Use the write-to-temp-then-rename pattern:
- Write to `atm_data.json.tmp`
- Call `os.replace()` (atomic on all platforms) to swap it in
- Wrap in `try/except OSError` — if the save fails, raise a descriptive `RuntimeError` so callers can inform the user nothing was persisted

### 3. PIN change atomicity *(High)*
**Location:** `change_pin()` — line 262

Change:
```python
accounts[new_pin] = accounts.pop(current_pin)  # destructive before save
```
To:
```python
accounts[new_pin] = accounts[current_pin]       # copy first
# (save happens in run_atm before we delete)
del accounts[current_pin]                        # delete only after successful save
```

### 4. PIN stored in plaintext *(Critical — security)*
**Location:** `create_account()`, `login()`, `change_pin()`, account dict keys

Use `hashlib.pbkdf2_hmac` (stdlib) with a per-account random salt stored alongside the hash. The account dictionary key becomes the **hash hex digest** instead of the raw PIN.

Data structure changes:
```json
{
  "<sha256_hex>": {
    "name": "Alice",
    "pin_salt": "<hex_salt>",
    "balances": {...},
    "transactions": [...]
  }
}
```

New helpers:
- `generate_salt() -> bytes`
- `hash_pin(pin: str, salt: bytes) -> str`

Functions updated: `create_account`, `login`, `change_pin`.

> **Note:** Existing `atm_data.json` (plaintext-PIN format) is incompatible. It will be reset to `{}`.

### 5. Floating-point precision in transfers *(Medium)*
**Location:** `transfer()` — lines 287–293; also `deposit()`, `withdraw()`

Use `decimal.Decimal` (stdlib) for all arithmetic:
- Convert `EXCHANGE_RATES` values to `Decimal`
- `get_positive_amount()` returns `Decimal` instead of `float`
- `deposit`, `withdraw`, `transfer` use `Decimal` arithmetic
- Balances stored in JSON as strings; loaded back as `Decimal`
- Display formatting unchanged (`:,.2f` works on `Decimal`)

## Files Changed
- `atm.py` — all fixes above
- `atm_data.json` — reset to `{}` (incompatible with plaintext-PIN format after fix #4)

## Notes
- All stdlib only: `hashlib`, `os`, `decimal`, `json`
- Fix order: 1 → 2 → 3 → 4 → 5 (each builds on a stable foundation)
- Fix #4 is the most invasive; fixes #1–3 are isolated and surgical
