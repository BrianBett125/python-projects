# print all the elements in a Fibonacci number series in python
def fibonacci_series(n):
    fib_series = [0, 1]  # First two numbers of Fibonacci sequence
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]  # Return only the first 'n' terms

# Taking user input
num_terms = int(input("Enter the number of terms: "))

# Display Fibonacci series
print("Fibonacci Series:", fibonacci_series(num_terms))

