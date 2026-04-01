import math

#TODO: Define a function called caesar_cipher that accepts a string text and an integer shift.
def caesar_cipher(text: str, shift: int):
    result = ""
    
#TODO: Return a new string with each alphabetical character shifted by the shift amount. Keep the case (uppercase/lowercase) the same. Do not change non-letter characters like punctuation, spaces, or numbers.
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            result += shifted_char
        else:
            result += char        
    return result

#TODO: Allow the user to input text and shift value, then call the caesar_cipher function with those inputs to display the encrypted text. Furthermore, test the function with different strings and shift values to ensure it works correctly.
def main() -> None:
    try:
        user_text = input("Enter the text to encrypt: ")
        user_shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_cipher(user_text, user_shift)
        print(f"Encrypted text: {encrypted_text}")  

        print(caesar_cipher("Hello, World!", 3))
        print(caesar_cipher("abc", 3))
        print(caesar_cipher("xyz", 2))

    except ValueError:
        print("Invalid input! Please enter a valid number for the shift.")

if __name__ == "__main__":
    main()