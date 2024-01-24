def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_next_prime(x):
    """Find the next prime number after x."""
    next_number = x + 1
    while not is_prime(next_number):
        next_number += 1
    return next_number

def prime_difference(x):
    """Find the difference between the next prime and x."""
    if is_prime(x):
        next_prime = find_next_prime(x)
        difference = next_prime - x
        return difference
    else:
        return "Input is not a prime number."

# Example usage:
number_to_check = 17
result = prime_difference(number_to_check)
print(f"The difference between the next prime number after {number_to_check} and {number_to_check} is: {result}")
