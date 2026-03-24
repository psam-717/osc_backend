# Copilot Instructions

## What This Repo Is

A mentorship workspace for teaching Python and PostgreSQL. The mentor maintains reference implementations and assignment specs; mentees submit their work in dedicated subdirectories.

## Running Code

```bash
# Current Python assignment stub
python main.py

# Reference project: ATM app
python test_projects/atm_app/atm.py

# Reference project: Snake game (requires tkinter, no extra deps)
python test_projects/snake/test.py

# Reference project: Standard deviation utility
python test_projects/standard_deviation.py
```

There is no test framework, build system, linter config, or `requirements.txt`. All projects use the Python standard library only.

## Repository Structure

```
assignments/          # Reference / model implementations (assignment.py → assignment_five.py)
main.py               # Current assignment stub given to mentees
mentees/
  p1/                 # Cohort 1 — one file per mentee: {name}.py
  p2/                 # Cohort 2 — one file per mentee: {name}.py
  p3/                 # Cohort 3 — one subfolder per mentee: {name}/
databases/            # Session notes on databases (Markdown)
test_projects/        # Fully worked example projects (ATM, Snake, std dev)
*.sql                 # In-session SQL practice files (PostgreSQL)
sql_assignment*.md    # SQL assignment specs
osc_new_assignment.md # Current Python assignment spec
git_commit_message.md # AI instructions for generating commit messages
```

## Key Conventions

### Python

- **Type hints everywhere**: `list[str]`, `dict[str, float]`, `str | None` (Python 3.10+ style, no `Optional`).
- **Currency formatting**: monetary values display as `GHS {price:,.2f}` (Ghanaian Cedi).
- **Input validation pattern**: loop + `try/except ValueError`, raise `ValueError` for bad values, never trust raw `input()` for numbers.
- **`BackAction` exception pattern** (see `atm.py`): raise a custom exception to cancel out of nested menus cleanly — don't use flags or `break` chains.
- Functions get docstrings; inline comments used sparingly for non-obvious logic.

### SQL (PostgreSQL)

- Primary keys: `SERIAL PRIMARY KEY`.
- Always use `RETURNING *` on `UPDATE` and `DELETE`.
- Foreign keys declared as named constraints: `CONSTRAINT fk_<name> FOREIGN KEY (...) REFERENCES ...`.
- `CHECK` constraints inline on the column (e.g., `CHECK (rating BETWEEN 1 AND 5)`).
- Keyword casing: SQL keywords in UPPERCASE, identifiers in `snake_case`.

### Assignments

- Each Python assignment builds on the previous (`assignment.py` → `assignment_five.py`); check the progression before adding new features.
- Mentee files go in `mentees/p{N}/{mentee_name}.py` (cohorts 1–2) or `mentees/p3/{mentee_name}/` (cohort 3).
- The current assignment spec is `osc_new_assignment.md`; the stub is `main.py`.

### Commit Messages

Follow the conventional commits spec defined in `git_commit_message.md`:

```
<type>(<scope>): <summary, max 72 chars>
```

Types: `feat`, `fix`, `refactor`, `docs`, `chore`, `style`, `test`, `ci`, `build`, `perf`, `revert`.  
Scope derives from the affected directory or feature (e.g., `assignments`, `atm`, `sql`, `mentees`).  
Use present tense. Split unrelated changes into separate commits.
