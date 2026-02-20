''''FUNCTIONS'''
# A function in Python is a named block of reusable code that performs a specific task.

# It lets you:

# give a name to a piece of logic
# run that logic whenever you want (and as many times as you want)
# optionally receive input (arguments/parameters)
# optionally return a result

def greet():
    print("Hello, FastAPI beginner!")

greet()  # Output: Hello, FastAPI beginner!



def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8


def create_user(name: str, age: int = 18):  # Default age
    return f"User {name} created, age {age}."

print(create_user("Alice"))  # Output: User Alice created, age 18.
print(create_user(name="Bob", age=25))  # Keyword arg, Output: User Bob created, age 25.



# EXCEPTIONS

# An exception in programming is an event that
# occurs during program execution that disrupts the normal flow of instructions.

# It represents something “unexpected” or “abnormal” that 
# happened — usually an error or an unusual situation the 
# program wasn’t expecting to handle in the normal path.


# ZeroDivisionError  - 5 / 0
# IndexError - lst[10]
# KeyError - d["name"]
# TypeError - "5" + 3


try:
    number = int(input("Enter a number: "))
    print(f"Double: {number * 2}")
except ValueError:
    print("That's not a valid number!")
   
    
    
def divide(a: int, b: int) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return 0.0
    except TypeError:
        print("Inputs must be numbers!")
        return 0.0
    else:
        print("Division successful.")
        return result
    finally:
        print("Operation attempted.")  # Always runs

print(divide(10, 2))  # Outputs: Division successful. Operation attempted. 5.0
print(divide(10, 0))  # Outputs: Cannot divide by zero! Operation attempted. 0.0



def check_age(age: int):
    if age < 18:
        raise ValueError("Age must be at least 18!")
    return "Access granted."

try:
    print(check_age(15))
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Age must be at least 18!