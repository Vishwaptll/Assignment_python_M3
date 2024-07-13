#32.Write a Python script to sort (ascending and descending) a dictionary by value.

import operator
def sort_dict_by_value_asc(d):
    return dict(sorted(d.items(), key=operator.itemgetter(1)))


my_dict = {'a': 34, 'b': 23, 'c': 10, 'd': 40}
sorted_dict_asc = sort_dict_by_value_asc(my_dict)
print("Dictionary sorted by value in ascending order:")
print(sorted_dict_asc)
