#63.Write a Python program to returns sum of all divisors of a number

def sum_of_divisors(n):
    sum_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors


num = int(input("Enter a number: "))

result = sum_of_divisors(num)

print(f"The sum of all divisors of {num} is {result}")
