#9.Write a Python function that takes two lists and returns true if they have at least one common member.
def have_common_member(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
       
    if set1.intersection(set2):
        return True
    else:
        return False
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

print(f"List1: {list1}")
print(f"List2: {list2}")

print(f"Do List1 and List2 have at least one common member? {have_common_member(list1, list2)}")
