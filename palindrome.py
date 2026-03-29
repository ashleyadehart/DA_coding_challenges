import string

#TODO: Normalize the string by converting it to lowercase and removing spaces (and optionally punctuation). 
def normalize_string(s: str) -> str:
    return ''.join(c.lower() for c in s if c.isalnum())

#TODO: Define a function called is_palindrome that accepts a single string.
def is_palindrome(s: str):

#TODO: Reverse the normalized string and compare it to the original normalized version, converting it to lowercase and removing spaces (and optionally punctuation).
    normalized = normalize_string(s)
    
#TODO: Return True if the string is a palindrome, and False otherwise.
    return normalized == normalized[::-1]

#TODO: Test the function with various input strings, including palindromes and non-palindromes, to ensure it works correctly.
def main() -> None:
    try:
        print(is_palindrome("racecar"))
        print(is_palindrome("hello"))
        print(is_palindrome("A man a plan a canal Panama"))

        # Optional user input
        user_input = input("Enter a string to check if it is a palindrome: ")
        print(f"Is it a palindrome? {is_palindrome(user_input)}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()