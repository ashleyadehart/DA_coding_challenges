#TODO: Define a function called is_palindrome that accepts a single string.
def is_palindrome(s):

#TODO: Return True if the string is a palindrome, and False otherwise.
    if s == s[::-1]:
        return True
    else:
        return False    

#TODO: Normalize the string by converting it to lowercase and removing spaces (and optionally punctuation). 
def normalize_string(s):
    return ''.join(c.lower() for c in s if c.isalnum())

#TODO: Reverse the normalized string and compare it to the original normalized version, converting it to lowercase and removing spaces (and optionally punctuation).
def is_palindrome(s):
    normalized = normalize_string(s)
    return normalized == normalized[::-1]

#TODO: Provide an option for the user to input a string and print whether it is a palindrome or not.
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    