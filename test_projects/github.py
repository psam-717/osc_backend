"""
Learning module covering Python functions and exception handling.
"""

# FUNCTIONS
# A function in Python is a named block of reusable code that performs a specific task.
 
# It lets you:

# give a name to a piece of logic
# run that logic whenever you want (and as many times as you want)
# optionally receive input (arguments/parameters)
# optionally return a result

def greet() -> str:
    """Returns a greeting message."""
    return "Hello, FastAPI beginner!"   

  
def add_numbers(a: int, b: int) -> int: 
    """Adds two numbers and returns the result."""
    return a + b


def create_user(name: str, age: int = 18) -> str:
    """Creates a user and returns a confirmation message."""
    return f"User {name} created, age {age}."
  

# EXCEPTIONS

# An exception in programming is an event that
# occurs during program execution that disrupts the normal flow of instructions.

# It represents something "unexpected" or "abnormal" that
# happened -- usually an error or an unusual situation the
# program wasn't expecting to handle in the normal path.

# ZeroDivisionError  - 5 / 0
# IndexError - lst[10]
# KeyError - d["name"]
# TypeError - "5" + 3


def divide(a: int, b: int) -> "float | None":
    """
    Divides a by b and returns the result.
    Raises ValueError if b is zero, TypeError if inputs are not numbers.
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero!") from None
    except TypeError:
        raise TypeError("Inputs must be numbers!") from None


def check_age(age: int) -> str:
    """Returns access status based on age."""
    if age < 18:
        raise ValueError("Age must be at least 18!")
    return "Access granted."


if __name__ == "__main__":
    # greet
    print(greet())  # Output: Hello, FastAPI beginner!

    # add_numbers
    print(add_numbers(5, 3))  # Output: 8

    # create_user
    print(create_user("Alice"))              # Output: User Alice created, age 18.
    print(create_user(name="Bob", age=25))   # Output: User Bob created, age 25.

    # input example
    try:
        number = int(input("Enter a number: "))
        print(f"Double: {number * 2}")
    except ValueError:
        print("That's not a valid number!")

    # divide
    try:
        print(divide(10, 2))  # Output: 5.0
        print(divide(10, 0))  # Raises ValueError
    except ValueError as e:
        print(f"Error: {e}")

    # check_age
    try:
        print(check_age(15))
    except ValueError as e:
        print(f"Error: {e}")  # Output: Error: Age must be at least 18!