import math

#TODO: Define a function that takes a list of numbers and returns the maximum number in the list.
def find_max(numbers: list) -> int:
    
#TODO: Check if the list is empty
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty.")
    
#TODO: Initialize the maximum with the first element
    current_max = numbers[0]
    
#TODO: Loop through each number in the list
    for num in numbers:
        if num > current_max:
            current_max = num
    return current_max

#TODO: Test the function with different lists of numbers to ensure it works correctly.
def main() -> None:
    try:
        print(find_max([4, 12, 2, 20, 5]))
        print(find_max([-1, -5, -3, -4]))
        print(find_max([7, 7, 7, 7]))

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
