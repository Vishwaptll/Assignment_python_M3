#30.Write a Python program to convert a list of tuples into a dictionary.

def list_of_tuples_to_dict(list_of_tuples):
    return {key: value for key, value in list_of_tuples}

list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
result_dict = list_of_tuples_to_dict(list_of_tuples)
print(result_dict)
