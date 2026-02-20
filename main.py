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
    pass


def calculate_remaining_budget(income: float, total_expenses: float) -> float:
    # Your code here
    pass


def print_budget_summary(name: str, category: str, income: float,
                         expenses: list[float], remaining: float):
    # Your code here - make it look nice!
    pass


# ────────────────────────────────────────
if __name__ == "__main__":
    print("Welcome to Personal Budget Calculator!\n")

    # Get user name (simple input, no validation needed)
    user_name = input("What is your name? ").strip()
    print(f"Hello {user_name}!\n")

    # Get income using safe function
    # Get category
    # Get 3 expenses using loop + safe function
    # Calculate totals
    # Print summary
