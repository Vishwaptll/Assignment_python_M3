#11.Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_elements(input_list):
    unique_list = []
    
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list
my_list = [1,2,2,3,4,4,5,6,6,7,8,8,9,10]
result = unique_elements(my_list)

print(f"Original List: {my_list}")
print(f"List with Unique Elements: {result}")

