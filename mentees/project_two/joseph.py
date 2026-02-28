# Program functions
def get_positive_number(prompt: str) -> float:
    """Ask for input until a positive number is received."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive!")
            return value
        except ValueError as e:
            print(f"Error: {e}. Please try again.")


def calculate_total_expenses(expenses: list[float]) -> float:
    # Your code here
    total_expenses = 0
    for amount in expenses:
        total_expenses += amount
    return total_expenses


def calculate_remaining_budget(income: float, total_expenses: float) -> float:
    # Your code here
    remaining_budget = income - total_expenses
    return remaining_budget


def print_budget_summary(name: str, category: str, income: float,
                         expenses: list[float], remaining: float):
    # Your code here - make it look nice!
    print("_______________________________")
    print(f"| Budget Summary For {name}  📊|")
    print("_______________________________")
    print(f"| Category          : {category}    ")
    print(f"| Monthly Income    : {income}   ")
    print(f"| Total Expenses    : {expenses}  ")
    print(f"| Remaining Budget  : {remaining} ")
    print("__________________________________________")
    if remaining <= 0:
        print(f"Warning❌: You are over budget by {remaining}!")
    else:
        print(f"You are within budget. Great job! ✅")
    print("__________________________________________")



# ────────────────────────────────────────
if __name__ == "__main__":
    print("Welcome to Personal Budget Calculator!\n")

    # Get user name (simple input, no validation needed)
    user_name = input("What is your name? ").strip()
    print(f"Hello {user_name}!\n")

    # Get income using safe function
    monthly_income = get_positive_number("Enter your monthly income: ")
    # Get category
    budget_category = input("What is the budget category? ")
    # Get 3 expenses using loop + safe function
    expenses = []
    count = 0
    while count < 3:
        value = get_positive_number(f"Enter expense { count + 1 }: ")
        expenses.append(value)
        count += 1

    # Calculate totals
    total_expenses = calculate_total_expenses(expenses)
    remaining_budget = calculate_remaining_budget(monthly_income, total_expenses)
    # Print summary
    print_budget_summary(user_name, budget_category, monthly_income, total_expenses, remaining_budget)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             