#34.Write a Python script to check if a given key already exists in a dictionary

def check_key_in_dict(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False


my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_check = 'd'
if check_key_in_dict(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
