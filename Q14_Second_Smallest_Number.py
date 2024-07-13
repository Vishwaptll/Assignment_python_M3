#14.Write a Python program to find the second smallest number in a list.
def second_smallest_sort(input_list):
    sorted_list = sorted(input_list)
    return sorted_list[1]  

my_list = [1,22,21,20,7,10,3]
second_smallest = second_smallest_sort(my_list)

print(f"Original List: {my_list}")
print(f"Second Smallest Number: {second_smallest}")
