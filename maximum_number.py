#TODO: Define a function takes a list of numbers and returns the maximum number in the list.
def find_max(numbers):
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

print(find_max([4, 12, 2, 20, 5]))
