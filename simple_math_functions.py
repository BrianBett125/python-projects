# Suggested filename: simple_math_functions.py

def add(a, b):
    """
    Adds two numbers and returns the sum.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first and returns the result.

    Args:
        a (int or float): The number to subtract from.
        b (int or float): The number to subtract.

    Returns:
        int or float: The difference between a and b.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers and returns the product.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second and returns the quotient.
    Includes error handling for division by zero.

    Args:
        a (int or float): The dividend.
        b (int or float): The divisor.

    Returns:
        int or float: The quotient of a divided by b.
        str: An error message if division by zero is attempted.
    """
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# --- Example Usage ---
if __name__ == "__main__":
    num1 = 10
    num2 = 5

    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")

    num3 = 7
    num4 = 0
    print(f"{num3} / {num4} = {divide(num3, num4)}")

    print(f"Adding 3.5 and 2.1: {add(3.5, 2.1)}")
