# Q24.
# Write a Python program to combine values in python list of dictionaries. 
# Expected Output: Counter({'item1': 1150, 'item2': 300})
# from typing import Counter


# item_list=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result =Counter()
# for d in item_list:
#     result[d['item']] += d['amount']
# print(result) 


# my_dict = [
# {'item': 'item1', 'amount': 400},
# {'item': 'item2', 'amount': 300},
# {'item': 'item1', 'amount': 750}
# ]
# d = {}
# for x in my_dict :
#     if x['item'] not in d :
#         d.update({x['item'] : x['amount']})
#     else :
#         d[x['item']] = d[x['item']] + x['amount']
# print(d)

d=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
d1={}
for i in d:
    if i['item'] in d1.keys():
        d1[i['item']]+=i['amount']
    else:
        d1[i['item']]=i['amount']
print(d1)