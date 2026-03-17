# compare two numbers using else-if statement and output smaller and
# larger numbers in python
# Taking user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Comparing the numbers using if-elif-else
if num1 > num2:
    print(f"Larger number: {num1}")
    print(f"Smaller number: {num2}")
elif num1 < num2:
    print(f"Larger number: {num2}")
    print(f"Smaller number: {num1}")
else:
    print("Both numbers are equal.")

