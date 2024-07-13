#16.Write a Python program to check whether a list contains a sub list
def is_sublist(main_list, sub_list):
    
    if all(elem in main_list for elem in sub_list):
        return True
    else:
        return False
main_list = [1,2,3,4,5,6,7,8,9]
sub_list1 = [3,4,5,6]
sub_list2 = [8,9,11]

print(f"Main List: {main_list}")
print(f"Sub List 1: {sub_list1}")
print(f"Sub List 2: {sub_list2}")

if is_sublist(main_list, sub_list1):
    print("Sub List 1 is a sublist of Main List")
else:
    print("Sub List 1 is not a sublist of Main List")


if is_sublist(main_list, sub_list2):
    print("Sub List 2 is a sublist of Main List")
else:
    print("Sub List 2 is not a sublist of Main List")
