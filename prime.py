#  ===== TOP "N" NUMBER OF PRIME NUMBERS ======
number_of_primes_to_find = 0
i = 0
while number_of_primes_to_find < 10:
    i += 1
    is_prime_indicator = True
    if i <= 1:
        is_prime_indicator = False
        # special case as 2 is the only even number that is prime
    elif i== 2:
        is_prime_indicator = True

        # Check if n is a multiple of 2 thus all these won't be prime
    elif i % 2 == 0:
        is_prime_indicator = False

    else:
        for j in range(3, int(i**0.5)+1,2):
            if i % j == 0:
                is_prime_indicator = False
                break

    if is_prime_indicator:
        print(i, end=' ')
        number_of_primes_to_find += 1

#  ===== PRIME NUMBERS Between certain range ======

def checkPrime(n):
    # 0 and 1 are not prime numbers
    # negative numbers are not prime
    if n <= 1:
        return 0
    # special case as 2 is the only even number that is prime
    elif n == 2:
        return 1

    # Check if n is a multiple of 2 thus all these won't be prime
    elif n % 2 == 0:
        return 0

    # If not, then just check the odds
    for i in range(3, int((n**0.5)), 2):
        if n % i == 0:
            return 0
    else:
        # As not in any above conditions, it is prime number
        return 1


a, b = 1, 100
for i in range(a, b + 1):
    if checkPrime(i):
        print(i, end=" ")

