import math

# Define a function called is_prime that takes one integer as input.
def is_prime(n):
    n = int(n)

# Return True if the number is prime and False otherwise.    
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False

print(is_prime(11))  # True




