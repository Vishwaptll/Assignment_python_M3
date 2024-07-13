#47.Write a Python program to create a dictionary from a string.cNote: Track the count of the letters from the string.cSample string: 'w3resource'

a="w3resource"
char_count = {}
for char in a:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
