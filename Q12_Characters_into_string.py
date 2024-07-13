#12.Write a Python program to convert a list of characters into a string.
def list_to_string(char_list):
    
    string = ''.join(char_list)
    return string

char_list = ['v','i','s','h','w','a']
result_string = list_to_string(char_list)

print(f"Original List of Characters: {char_list}")
print(f"Converted String: {result_string}")
