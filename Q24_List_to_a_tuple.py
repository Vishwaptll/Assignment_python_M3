#24.Write a Python program to convert a list to a tuple.

def list_to_tuple(lst):
    return tuple(lst)
my_list = [23,4,1,5,6,7,89]

converted_tuple = list_to_tuple(my_list)

print("Converted Tuple:", converted_tuple)
