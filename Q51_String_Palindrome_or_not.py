#51.Write a Python function that checks whether a passed string is palindrome or not


def is_palindrome(input_string):
    
    processed_string = input_string.lower().replace(" ", "")
    
    reversed_string = processed_string[::-1]
    
    return processed_string == reversed_string

string1 = "A man a plan a canal Panama"
string2 = "vishwa"

if is_palindrome(string1):
    print(f"'{string1}' is a palindrome.")
else:
    print(f"'{string1}' is not a palindrome.")

if is_palindrome(string2):
    print(f"'{string2}' is a palindrome.")
else:
    print(f"'{string2}' is not a palindrome.")
