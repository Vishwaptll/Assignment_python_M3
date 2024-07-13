#41.Write a Python program to combine two dictionary adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}

def combine_dicts(d1, d2):
    combined_dict = {}
    
    for key in d1.keys() | d2.keys():
        combined_dict[key] = d1.get(key, 0) + d2.get(key, 0)
    
    return combined_dict

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = combine_dicts(d1, d2)

print("Counter:")
print(combined_dict)
