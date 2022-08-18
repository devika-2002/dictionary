# Q22. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd



# sample={'1':['a','b'], '2':['c','d']}
# for i in sample['1']:
#     for j in sample['2']:
#         result=i+j
#         print(result)

d={'1':['a','b'], '2':['c','d']}
L1,L2=d.values()
for i in L1:
    for j in L2:
        print(i+j) 


