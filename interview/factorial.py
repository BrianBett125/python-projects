# find the factorial of a given number in python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking user input
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
