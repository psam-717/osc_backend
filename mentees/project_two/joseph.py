# Program functions
def get_string_only(prompt: str, title: str) -> str:
    while True:
        value = input(prompt).strip()
        try:
            float(value)
            print("-----------------------------------")
            print(f"❌ {title} should be text!")
            print("-----------------------------------")
        except ValueError:
            return value

def get_positive_number(prompt: str, title: str) -> float:
    """Ask for input until a positive number is received."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("----------------------------------")
                raise ValueError("Value must be positive!")
            return value
        except ValueError:
            print("----------------------------------------------------------------------------")
            print(f"❌Error: {title} should be a valid amount (Eg GH₵200). Please try again.")
            print("----------------------------------------------------------------------------")


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
                         expenses: float, remaining: float):
    # Your code here - make it look nice!
    print("_______________________________")
    print(f"| Budget Summary For {name}  📊|")
    print("_______________________________")
    print(f"| Category          : {category}    ")
    print(f"| Monthly Income    : GH₵ {income}   ")
    print(f"| Total Expenses    : GH₵ {expenses}  ")
    print(f"| Remaining Budget  : GH₵ {remaining} ")
    print("__________________________________________")
    if remaining <= 0:
        print(f"Warning❌: You are over budget by GH₵ {remaining}!")
    else:
        print(f"You are within budget. Great job! ✅")
    print("__________________________________________")



# ────────────────────────────────────────
if __name__ == "__main__":
    print("Welcome to Personal Budget Calculator!💸\n")

    # Get user name (simple input, no validation needed)
    user_name = get_string_only("What is your name? ", "Name")
    print(f"Hello {user_name}!👋😁")
    # Get income using safe function
    monthly_income = get_positive_number("Enter your monthly income(GH₵): ", "Monthly income")
    # Get category
    budget_category = get_string_only("What is the budget category? ", "Budget Category")
    # Get 3 expenses using loop + safe function
    expenses = []
    count = 0
    while count < 3:
        value = get_positive_number(f"Enter expense { count + 1 } (GH₵): ", "Expense")
        expenses.append(value)
        count += 1

    # Calculate totals
    total_expenses = calculate_total_expenses(expenses)
    remaining_budget = calculate_remaining_budget(monthly_income, total_expenses)
    # Print summary
    print_budget_summary(user_name, budget_category, monthly_income, total_expenses, remaining_budget)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             