#13.Write a Python program to select an item randomly from a list.
import random

def select_random_item(input_list):
   
    random_item = random.choice(input_list)
    return random_item

my_list = [1,2,3,4,5,6,7,8,9,10]
random_item = select_random_item(my_list)

print(f"Original List: {my_list}")
print(f"Randomly Selected Item: {random_item}")
