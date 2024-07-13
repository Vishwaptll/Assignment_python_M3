#58.Write a Python program to read a random line from a file
import random

def read_random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line.strip()  
filename = 'sample.txt'  

try:
    random_line = read_random_line(filename)
    print("Random line from the file:")
    print(random_line)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except IndexError:
    print(f"Error: File '{filename}' is empty.")
