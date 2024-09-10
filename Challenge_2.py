# Function to find the missing numbers in a sequence
def find_the_missing_numbers(sequence):
    # Find the minimum and maximum numbers in the sequence (This will help us on Creating the full range of numbers)
    minimum = min(sequence)
    maximum = max(sequence)
    
    # Creating the full range of numbers from minimum to maximum
    full_range = set(range(minimum, maximum + 1)) # I added +1 to include the maximum number
    
    # Find the missing numbers by subtracting the sequence from the full range
    missing_numbers = full_range - set(sequence)
    
    return sorted(missing_numbers) # Return the missing numbers in sorted order (ascending)

# Input and function call
try:
    # Get the user input and converting it to a list of integers
    sequence = list(map(int, input("Enter numbers separated by spaces: ").split())) # I used map() to convert the input to integers
    
    # Call the function and print the missing numbers
    missing = find_the_missing_numbers(sequence) # I stored the missing numbers in a variable to check if there are any missing numbers or not 
    
    if missing: 
        print("Missing numbers:", missing)
    else:
        print("No missing numbers.")
        
except ValueError:
    print("Invalid input! Please enter only numbers.")
