# Function to find the missing numbers in a sequence
def find_the_missing_numbers(sequence):
        # Ensure the sequence has at least two numbers
    if len(sequence) < 2:
        return "The sequence must contain at least two numbers."

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
    # Get user input and convert it to a list of integers
    sequence = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    # Check if the input list has at least two numbers
    if len(sequence) < 2:
        print("The sequence must contain at least two numbers.")
    else:
        # Call the function and print the missing numbers
        missing = find_the_missing_numbers(sequence)
        
        if missing:
            print("Missing numbers:", missing)
        else:
            print("No missing numbers.")
        
except ValueError:
    print("Invalid input! Please enter only numbers.")
