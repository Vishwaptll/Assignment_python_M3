#46.Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}]

def combine_values(list_of_dicts):
    combined_dict = {}
    
    for d in list_of_dicts:
        item = d['item']
        amount = d['amount']
        
        if item in combined_dict:
            combined_dict[item] += amount
        else:
            combined_dict[item] = amount
    
    return combined_dict

sample_data = [{'item': 'item1', 'amount': 400},
               {'item': 'item2', 'amount': 300},
               {'item': 'item1', 'amount': 750}]

combined_values = combine_values(sample_data)

print("Counter:")
print(combined_values)
