#27.Write a Python program to find the repeated items of a tuple.

from collections import Counter
def find_repeated_items(tup):
    count = Counter(tup)
    
    repeated_items = [item for item, freq in count.items() if freq > 1]
    
    return repeated_items

my_tuple = (11,2,3,4,5,2,3,4,5,12,10)

repeated_items = find_repeated_items(my_tuple)
print("Original Tuple:", my_tuple)
print("Repeated Items:", repeated_items)
