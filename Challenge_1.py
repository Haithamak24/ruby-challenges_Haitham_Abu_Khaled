# Fibonacci sequence function
def fibonacci_sequence(n):
    if n <= 0:
        return "Please enter a positive integer!"
    
    sequence = [0, 1]  # The Start Of The Sequence
    
    for i in range(2, n):  # Function that generates Fibonacci sequence
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    
    return sequence

# Here I made an Input validation and function call
try:
    n = int(input("Enter the number of Fibonacci numbers you want: "))
    if n <= 0:
        print("Please enter a positive integer!")
    else:
        print(fibonacci_sequence(n))
except ValueError:
    print("Invalid input! Please enter an integer.")
