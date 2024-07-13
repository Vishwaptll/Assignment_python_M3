#15.Write a Python program to get unique values from a list

def get_unique_values(input_list):
    unique_values = list(set(input_list))
    return unique_values

my_list = [0,1,2,2,3,4,4,5,5,5,6,6,7,8,8,9]
unique_values = get_unique_values(my_list)

print(f"Original List: {my_list}")
print(f"Unique Values: {unique_values}")
