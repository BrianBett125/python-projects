# generate all the prime numbers between one and the given number in python
# using a Loop (Efficient Approach)
print("prime numbers using loop(for small numbers)")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

def prime_numbers(limit):
    primes = [num for num in range(2, limit + 1) if is_prime(num)]
    return primes

# Taking user input
num = int(input("Enter a number: "))

# Display prime numbers
print(f"Prime numbers between 1 and {num}: {prime_numbers(num)}")




# using the Sieve of Eratosthenes (Optimized for Large Inputsts  (100,000+ range))
print("\n\nprime numbers using Sieve of Eratosthenes (Optimized for Large Inputs")
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]

# Taking user input
num = int(input("Enter a number: "))

# Display prime numbers
print(f"Prime numbers between 1 and {num}: {sieve_of_eratosthenes(num)}")

