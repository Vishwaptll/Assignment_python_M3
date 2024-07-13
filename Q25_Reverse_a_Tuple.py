#25.Write a Python program to reverse a tuple.
def reverse_tuple(tup):
    return tup[::-1]
my_tuple = (11,23,13,14,15,16,17)

reversed_tuple = reverse_tuple(my_tuple)
print("Original Tuple:", my_tuple)
print("Reversed Tuple:", reversed_tuple)
