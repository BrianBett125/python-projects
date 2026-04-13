def get_primes_upto(n: int) -> list:
    """
    Returns a list of all prime numbers up to a given number n using the Sieve of Eratosthenes.
    
    Parameters:
        n (int): The upper limit to find prime numbers (inclusive).
    
    Returns:
        list: A list of prime numbers up to n.
    """
    if n < 2:
        return []  # No primes below 2

    # Initialize a list assuming all numbers from 0 to n are prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    # Eliminate non-primes by marking multiples of each number
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, n + 1, i):
                is_prime[multiple] = False

    # Extract all prime numbers
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes


# Main block to test the function
if __name__ == "__main__":
    upper_limit = 20  # You can change this number to test other values
    primes = get_primes_upto(upper_limit)  # Get prime numbers up to the limit
    print(f"Prime numbers up to {upper_limit} are: {primes}")

    # Expected output:
    # Prime numbers up to 20 are: [2, 3, 5, 7, 11, 13, 17, 19]

