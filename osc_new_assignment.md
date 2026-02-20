# Create a small console program that helps a user track a simple monthly budget. 
# The program collects income and expenses, performs calculations, and handles invalid inputs gracefully.

1. Ask the user for:
    - Monthly income (must be a positive float or integer)
    - Name of the budget category (string)
    - Three different expenses in that category (each a positive number)

2. Use different data types intentionally:
    - str → user name, category name
    - float → money amounts (income & expenses)
    - int → number of expense items (fixed to 3 in this version)
    - list → store the expense amounts
    - bool → track whether budget is positive or negative

3. Write at least four separate functions:
    - get_positive_number(prompt: str) → float
    - Repeatedly asks for input until a positive number is entered. Raises and handles exceptions inside.
    - calculate_total_expenses(expenses: list[float]) → float
    - calculate_remaining_budget(income: float, total_expenses: float) → float
    - print_budget_summary(name: str, category: str, income: float, expenses: list[float], remaining: float)
    - Nice formatted output (no return value)

4. Use exceptions to handle:
    - Invalid number input (ValueError from float())
    - Negative or zero values for income/expenses (ValueError raised by your validation)
    - Empty category name

5. Main program flow (in if __name__ == "__main__":):
    - Greet user and ask for name
    - Get monthly income (using your safe input function)
    - Ask for budget category name
    - Collect exactly 3 expenses (loop + safe input function)
    - Calculate total expenses and remaining budget
    - Show friendly summary
    - Tell user if they are over budget (remaining < 0)


## Example of desire output

Welcome to Personal Budget Calculator!

What is your name? Alice
Hello Alice!

Enter your monthly income: abc
→ Sorry, please enter a valid number.
Enter your monthly income: -500
→ Income must be positive. Try again.
Enter your monthly income: 4500

What is the budget category? Food & Groceries

Enter expense 1: 1200
Enter expense 2: 850.50
Enter expense 3: xyz
→ Invalid amount. Please enter a number.
Enter expense 3: 600

Budget Summary for Alice
──────────────────────────────
Category          : Food & Groceries
Monthly Income    : 4500.00
Total Expenses    : 2650.50
Remaining Budget  : 1849.50
→ You are within budget. Great job! ✓

# If over budget
Remaining Budget  : -320.75
→ Warning: You are over budget by 320.75!


# Visit the main.py to get the starter code skeleton