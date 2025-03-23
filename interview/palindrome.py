# write a program to check if the number is a palindrome number or not in python

# 1. Using String Reversal (Simple Approach)
print("using string reversal (simple approach")
num = input("Enter a number: ")

if num == num[::-1]:  # Reverse and compare
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# 2. Using a Loop (Mathematical Approach
print("\n\nusing a loop mathematical approach") 
def is_palindrome(n):
    original = n
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return original == reversed_num

# Taking user input
num = int(input("Enter a number: "))

# Checking if it's a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# NOTE
# ✅ Use String Reversal if you want a quick and easy solution.
# ✅ Use Loop (Mathematical Approach) if you want a logical method without converting to a string.
