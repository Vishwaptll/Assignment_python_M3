#31.How will you create a dictionary using tuples in python?

tuple_list = [('a', 1), ('b', 2), ('c', 3)]

result_dict = {key: value for key, value in tuple_list}

print(result_dict)
