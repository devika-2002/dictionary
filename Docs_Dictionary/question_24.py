# Q24.
# Write a Python program to combine values in python list of dictionaries. 
# Expected Output: Counter({'item1': 1150, 'item2': 300})

dict=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
emti_dict={}
for i in dict:
    if i['item'] in emti_dict.keys():
        emti_dict[i['item']]+=i['amount']
    else:
        emti_dict[i['item']]=i['amount']
print(emti_dict)