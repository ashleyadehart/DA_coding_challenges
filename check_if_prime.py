import math

#TODO: Define a function called is_prime that takes one integer as input.
def is_prime(n: int):
    n = int(n)

#TODO: Return True if the number is prime and False otherwise.
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False

#TODO: Test the function with different input values to ensure it works correctly.
def main() -> None:
    try:
        print(is_prime(11))
        print(is_prime(15))
        print(is_prime(2))

    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()



