#44.Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Sample data: {'1': ['a','b'], '2': ['c','d']}

import itertools

def display_combinations(dictionary):
    
    values = [v for v in dictionary.values()]
      
    combinations = list(itertools.product(*values))
      
    for combo in combinations:
        print(''.join(combo))

sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}

print("All combinations of letters:")
display_combinations(sample_data)
