#6.Write a Python program to count the number of strings where the stringlength is 2 or more and the first and last character are same from a given list of strings
def count_strings_with_same_ends(strings):
    count = 0
    
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    
    return count


string_list = ["aba", "liol", "hgt", "vba", "welcome", "heh"]
count = count_strings_with_same_ends(string_list)

print(f"Number of strings where first and last character are same: {count}")


