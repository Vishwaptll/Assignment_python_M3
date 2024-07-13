#28.Write a Python program to remove an empty tuple(s) from a list of tuples.

def remove_empty_tuples(tuple_list):
    return [tup for tup in tuple_list if tup]

list_of_tuples = [(1, 2, 3), (), (4, 5), (), (), (6,), (), (7, 8, 9)]

filtered_list = remove_empty_tuples(list_of_tuples)

print("Original List of Tuples:", list_of_tuples)
print("without empty List of Tuples:", filtered_list)
