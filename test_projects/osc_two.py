def get_positive_number(prompt: str) -> float:
    """Ask for input until a positive number is received."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("-> Please enter a positive number")
        except ValueError:
            print("-> Input is invalid. It should be a number")


def get_non_numeric_string(prompt: str):
    while True: 
        s = input(prompt)
        
        if not s:
            print("-> Input cannot be empty")
            continue
        
        try:
            float(s)
            print("-> Numbers are not allowed. Please enter strings")
            continue
        except ValueError:
            return s
 
 
def expenses_count():
    while True:
        s = get_positive_number("How many expenses do you have ")
        
        if s > 5:
            print("Expenses cannot be greater than 5")
            continue
        return s
 
def calculate_total_expenses(expenses: list[float]) -> float:
    # Your code here
    total = 0
    invalid_expenses = []
    valid_expenses = []
    for item in expenses:
        if isinstance(item, (float, int)):
            valid_expenses.append(item)
            total += item
        else: 
            invalid_expenses.append(item)
    return total, invalid_expenses


def calculate_remaining_budget(income: float, total_expenses: float) -> float:
    remaining_budget = income - total_expenses
    return remaining_budget

def print_budget_summary(name: str, category: str, income: float,
                         expenses: list[float], remaining: float):
    # Your code here - make it look nice!
    print(f"budget summary for {name}")
    print(f"category {category}")
    print(f"Monthly income {income}")
    print(f"Total expenses {expenses}")
    print(f"Remaining budget: {remaining}")

# ────────────────────────────────────────
if __name__ == "__main__":
    print("Welcome to Personal Budget Calculator!\n")

    user_name = get_non_numeric_string("What is your name? ")
    print(f"Hello {user_name}!\n")
    
    monthly_income = get_positive_number(prompt="Enter your monthly income: ")
    print("\n")
    
    budget_category = get_non_numeric_string("What is the budget category? ")
    
    count_of_expense = expenses_count()
    
    if count_of_expense > 5:
        print("Expenses cannot be more than five now ")
    else: 
        # take expenses
        total_expenses = 0
        for i in range(int(count_of_expense)):
            expense = get_positive_number(f"Enter expense {i + 1}: ")
            total_expenses += expense
    
            
        print("\n", total_expenses)
        
    
    
    
    
