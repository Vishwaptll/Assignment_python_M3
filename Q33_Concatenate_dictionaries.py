#33.Write a Python script to concatenate following dictionaries to create a new one.

def concatenate_dicts(*dicts):
    concatenated_dict = {key: value for d in dicts for key, value in d.items()}
    return concatenated_dict


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}
concatenated_dict = concatenate_dicts(dict1, dict2, dict3)

print("Concatenated dictionary:")
print(concatenated_dict)
