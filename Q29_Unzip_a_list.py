#29.Write a Python program to unzip a list of tuples into individual lists.

def unzip_list_of_tuples(list_of_tuples):
    unzipped_lists = list(zip(*list_of_tuples))
    return unzipped_lists

list_of_tuples = [(1,2,3), (4,5,6), (10,11,12)]

unzipped_lists = unzip_list_of_tuples(list_of_tuples)

print("Original List of Tuples:", list_of_tuples)
print("Unzipped Lists:")
for index, lst in enumerate(unzipped_lists, 1):
    print(f"List {index}: {lst}")
