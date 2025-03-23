# print all the elements in a Fibonacci number series in python. this program
# can be implemented using a loop
def fibonacci_loop(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Taking user input
num_terms = int(input("Enter the number of terms: "))
fibonacci_loop(num_terms)
