# OSC Backend Mentorship Workspace

A structured learning workspace for mentoring Python and PostgreSQL fundamentals. The repository holds progressive reference implementations, assignment stubs, fully-worked example projects, and per-cohort mentee submissions — covering everything from basic scripting to multi-feature console applications and relational database design.

## Features

- Progressive Python assignments building from dictionary/loop basics to functions, exceptions, and input validation
- Reference console applications: a multi-currency ATM simulation and a classic Snake game
- SQL assignments covering PostgreSQL schema design, constraints, DML, and queries
- Per-cohort mentee submission directories (three active cohorts)
- Assignment specs and session notes kept alongside the code in `docs/` and `databases/`

## Requirements

- **Python 3.10 or later** — assignments use `X | Y` union syntax and `list[T]` generics (no `Optional`)
- **`tkinter`** — bundled with standard Python; required only for the Snake game
- **PostgreSQL** — required only for the SQL assignment files; no Python database client is used
- No third-party Python packages — all projects use the standard library only

## Installation

No installation step is required. Clone the repository and run files directly with Python.

```bash
git clone https://github.com/psam-717/osc_backend.git
cd osc_backend
```

## Usage

### Current assignment stub

```bash
python main.py
```

### ATM machine simulation

```bash
python test_projects/atm_app/atm.py
```

Supports account creation (name + 4-digit PIN), login, and three currency sub-accounts (GHS, USD, GBP) for deposit, withdrawal, balance checks, transfers, transaction history, and PIN changes. Account data is persisted to `test_projects/atm_app/atm_data.json` between sessions.

### Snake game

```bash
python test_projects/snake/test.py
```

### Standard deviation utility

```bash
python test_projects/standard_deviation.py
```

Computes population or sample standard deviation from a list of numbers.

### Functions and exceptions learning module

```bash
python test_projects/github.py
```

### Mixed-list number extractor

```bash
python test_projects/test.py
```

## Project Structure

```
osc_backend/
├── main.py                          # Current assignment stub given to mentees
├── task.txt                         # Quick session notes on database concepts
│
├── assignments/                     # Reference / model implementations (progression)
│   ├── assignment.py                # Session 1 — shopping cart with discount logic
│   ├── assignment_two.py            # Session 2 — price formatting helper
│   ├── assignment_three.py          # Session 3 — discount eligibility functions
│   ├── assignment_four.py           # Session 4 — cart total calculator (function form)
│   └── assignment_five.py           # Session 5 — cart total with quantity tracking
│
├── mentees/
│   ├── p1/                          # Cohort 1 — one file per mentee: {name}.py
│   ├── p2/                          # Cohort 2 — one file per mentee: {name}.py
│   └── p3/                          # Cohort 3 — one subdirectory per mentee: {name}/
│
├── test_projects/                   # Fully worked example projects
│   ├── atm_app/
│   │   ├── atm.py                   # Multi-currency ATM simulation
│   │   └── atm_data.json            # Persisted account data (auto-generated)
│   ├── snake/                       # Classic Snake game (tkinter, no extra deps)
│   ├── standard_deviation.py        # Population and sample std-dev utility
│   ├── osc_two.py                   # Budget calculator (extended reference)
│   ├── github.py                    # Functions and exceptions learning module
│   └── test.py                      # Mixed-list number extraction utility
│
├── databases/                       # Session notes on relational vs. non-relational databases
│
├── docs/
│   └── assignments/                 # Assignment specs (Markdown)
│       ├── osc_new_assignment.md    # Current Python assignment spec (budget calculator)
│       ├── sql_assignment.md        # SQL Session 1 spec — schema design
│       └── sql_assignment_two.md    # SQL Session 2 spec — DML and queries
│
└── sql/                             # In-session SQL practice files
    └── meetings/                    # Per-session SQL work
```

## Configuration

The ATM app reads and writes `test_projects/atm_app/atm_data.json` automatically. No environment variables or external config files are needed. Adjustable constants are defined directly in source files:

| Constant | File | Description |
|----------|------|-------------|
| `CURRENCIES` | `test_projects/atm_app/atm.py` | Supported currency codes and display symbols |
| `EXCHANGE_RATES` | `test_projects/atm_app/atm.py` | Exchange rates relative to GHS (Ghanaian Cedi) |
| `DATA_FILE` | `test_projects/atm_app/atm.py` | Path to the JSON persistence file |

## Testing

There is no automated test suite. All projects are run and verified manually:

```bash
python main.py
python test_projects/atm_app/atm.py
python test_projects/snake/test.py
python test_projects/standard_deviation.py
```

## Contributing

### Adding a new assignment

1. Create the reference implementation in `assignments/assignment_<name>.py`.
2. Update `main.py` with the new stub (functions with `# Your code here` bodies).
3. Add the assignment spec to `docs/assignments/`.

### Adding mentee work

- Cohorts 1 and 2: add `mentees/p{N}/{mentee_name}.py`.
- Cohort 3: add `mentees/p3/{mentee_name}/` with the relevant files inside.

### Coding conventions

- **Type hints everywhere** — use Python 3.10+ style: `list[str]`, `dict[str, float]`, `str | None` (not `Optional`).
- **Currency formatting** — monetary values display as `GHS {value:,.2f}`.
- **Input validation** — use `while True` + `try/except ValueError`; raise `ValueError` for invalid values.
- **`BackAction` exception pattern** (see `atm.py`) — raise a custom exception to cancel out of nested menus; avoid flag variables or `break` chains.
- **SQL conventions** — keywords in UPPERCASE, identifiers in `snake_case`, `SERIAL PRIMARY KEY`, named `CONSTRAINT fk_<name>` for foreign keys, `RETURNING *` on UPDATE/DELETE.
- Functions get docstrings; inline comments used sparingly for non-obvious logic only.

## License

License not specified.
