# print all the elements in a Fibonacci number series in python. this 
# program can be implemented using recursion technique
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci_recursive(n - 1)
        series.append(series[-1] + series[-2])
        return series

# Taking user input
num_terms = int(input("Enter the number of terms: "))
print(" ".join(map(str, fibonacci_recursive(num_terms))))
