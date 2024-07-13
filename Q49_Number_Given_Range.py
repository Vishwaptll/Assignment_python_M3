#49.Write a Python function to check whether a number is in a given range

def in_range(num, start, end):
    return start <= num <= end


number = 99
start_range = 1
end_range = 90

if in_range(number, start_range, end_range):
    print(f"{number} is in the range [{start_range}, {end_range}]")
else:
    print(f"{number} is not in the range [{start_range}, {end_range}]")
