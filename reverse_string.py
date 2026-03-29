import string

#TODO: Define a function called reverse_string that accepts one argument (a string) and uses string slicing to return the string in reverse order.
def reverse_string(s: str) -> str:
    return s[::-1]

def main() -> None:
    try:
        #TODO: Test the function with different input strings to ensure it works correctly.
        print(reverse_string("hello world"))
        print(reverse_string("zero"))
        print(reverse_string("Python"))

        user_input = input("Enter a string to reverse: ")
        print(f"Reversed string: {reverse_string(user_input)}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()