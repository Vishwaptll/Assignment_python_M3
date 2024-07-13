#10.Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
def generate_square_list():
    
    squares = []   
    for i in range(1, 31):
        squares.append(i ** 2)    
   
    first_5 = squares[:5]
    last_5 = squares[-5:]
        
    return first_5, last_5
first_5, last_5 = generate_square_list()

print("First 5 elements (squares of numbers from 1 to 30):")
print(first_5)

print("\nLast 5 elements (squares of numbers from 1 to 30):")
print(last_5)
