#42.Write a Python program to print all unique values in a dictionary.

def unique_values(dictionary):
    unique_vals = set()
    for value in dictionary.values():
        unique_vals.add(value)
    return unique_vals

my_dict = {'a': 101, 'b': 200, 'c': 100, 'd': 300, 'e': 200, 'f':300, 'g':1000}

unique_values_set = unique_values(my_dict)

print("Unique values in the dictionary:")
print(unique_values_set)
