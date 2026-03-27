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

#TODO: Test the function with various input strings, including palindromes and non-palindromes, to ensure it works correctly.
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))