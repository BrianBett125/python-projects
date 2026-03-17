# program to write even numbers in c
def get_even_numbers(start, end):
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    return even_numbers

# Taking user input for range
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Calling the function and displaying result
even_list = get_even_numbers(start, end)
print(f"Even numbers between {start} and {end}: {even_list}")

