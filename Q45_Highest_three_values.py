#45.Write a Python program to find the highest 3 values in a dictionary

def highest_three_values(dictionary):
   
    items = list(dictionary.items())
    
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    
    top_three = sorted_items[:3]
    
    return dict(top_three)


my_dict = {'a': 10, 'b': 34, 'c': 500, 'd': 560, 'e': 110, 'f':4500}


highest_values = highest_three_values(my_dict)
print("Highest 3 values are :")
print(highest_values)
