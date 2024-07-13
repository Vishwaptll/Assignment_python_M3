#39.Write a Python script to merge two Python dictionaries

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {'a': 11, 'b': 12}
dict2 = {'c': 23, 'd': 40}


merged_dict = merge_dicts(dict1, dict2)

print("Merged dictionary:")
print(merged_dict)
