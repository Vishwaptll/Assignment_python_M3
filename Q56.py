#56.How will you set the starting value in generating random numbers?

import random


random.seed(42)
random_number1 = random.random()
random_number2 = random.uniform(2.0, 10.0)
random_integer = random.randint(10_, 1000)

print("Random number 1:", random_number1)
print("Random number 2:", random_number2)
print("Random integer:", random_integer)
