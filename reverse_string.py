#TODO: Define a function called reverse_string that accepts one argument (a string) and uses string slicing to return the string in reverse order.
def reverse_string(s):
    return s[::-1]

#TODO: Provide an option for the user to input a string and print the reversed string.
user_input = input("Enter a string: ")
print("Reversed string:", reverse_string(user_input))