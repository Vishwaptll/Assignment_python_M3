#21.Write a Python program to convert a tuple to a string.
def tuple_to_string(tup):
    
    str_result = ""
      
    for item in tup:
       
        str_result += str(item)   
    return str_result

my_tuple = (11,2,34,2,3)

result_string = tuple_to_string(my_tuple)
print("Tuple converted to string:", result_string)
