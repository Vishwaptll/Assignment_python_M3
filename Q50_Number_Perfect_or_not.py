#50.Write a Python function to check whether a number is perfect or not.

def is_perfect_number(number):
    if number <= 0:
        return False
    
    sum_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i
    
    return sum_divisors == number
n = 17

if is_perfect_number(n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
