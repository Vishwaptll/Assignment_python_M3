#26.Write a Python program to replace last value of tuples in a list.

def replace_last_value(tuple_list, new_value):
    updated_list = []
    for tup in tuple_list:
        
        if len(tup) > 0:
           
            updated_tuple = tup[:-1] + (new_value,)
            updated_list.append(updated_tuple)
        else:
            updated_list.append((new_value,))
    return updated_list

tuple_list = [(1,3,4), (5,6), (), (7,), (10,11,12)]

new_value = 200
updated_list = replace_last_value(tuple_list, new_value)

print("Original List of Tuples:", tuple_list)
print("Updated List of Tuples:", updated_list)
