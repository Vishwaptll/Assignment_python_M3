#64.Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum

decimal_numbers = [3.14, 2.71, 1.618, 0.707, 5.55, 4.2]

max_number, min_number = find_max_min(decimal_numbers)

print(f"The maximum number is: {max_number}")
print(f"The minimum number is: {min_number}")
