#Write a Python function to get the largest number, smallest num and sum of all from a list.
def get_stats(numbers):
    if not numbers:
        return None, None, 0  
    
    max_num = max(numbers)   
    min_num = min(numbers)   
    total_sum = sum(numbers) 
    
    return max_num, min_num, total_sum
numbers = [12,34,56,2,13]
largest, smallest, total_sum = get_stats(numbers)

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Sum of all numbers: {total_sum}")






