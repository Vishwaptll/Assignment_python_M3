#40.Write a Python program to map two lists into a dictionary

def map_lists_to_dict(keys, values):
    mapped_dict = {keys[i]: values[i] for i in range(min(len(keys), len(values)))}
    return mapped_dict

keys = ['a', 'b', 'c']
values = [11,22,33]

mapped_dict = map_lists_to_dict(keys, values)

print("Mapped dictionary:")
print(mapped_dict)
