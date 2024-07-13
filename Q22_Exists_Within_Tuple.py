#22.Write a Python program to check whether an element exists within a tuple.

def check_element_in_tuple(tup, element):
    return element in tup

my_tuple = (11,56,4,3,5,7,8,10)
element_to_check = 10

if check_element_in_tuple(my_tuple, element_to_check):
    print(f"Element {element_to_check} exists in the tuple.")
else:
    print(f"Element {element_to_check} does not exist in the tuple.")
