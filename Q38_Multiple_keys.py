#38.Write a Python program to check multiple keys exists in a dictionary

def check_multiple_keys(dictionary, keys):
    return all(key in dictionary for key in keys)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_check = ['a', 'b', 'e','c']

if check_multiple_keys(my_dict, keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
