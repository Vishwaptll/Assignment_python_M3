#7.Write a Python program to remove duplicates from a list.

def remove_duplicates(input_list):
   
    unique_items = list(set(input_list))
    return unique_items


my_list = [1,0,1, 2, 2, 3,13, 4, 4, 5,14,12,14]
result = remove_duplicates(my_list)

print("Original List:", my_list)
print("List with Duplicates Removed:", result)
