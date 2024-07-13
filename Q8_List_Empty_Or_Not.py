#8.Write a Python program to check a list is empty or not
def is_list_empty(input_list):
    if len(input_list) == 0:
        return True
    else:
        return False
list1 = []
list2 = [1,2,3,4,5]

print(f"Is list1 empty? {is_list_empty(list1)}")
print(f"Is list2 empty? {is_list_empty(list2)}")
