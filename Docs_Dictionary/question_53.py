# Q53.
# Write a Python program to convert a given list of lists to a dictionary. 
# Original list of lists:
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 
# 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}

list=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], 
 [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
emti_dict={}
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        emti_dict[list[i][0]]=list[i][1],list[i][2]
        j=j+1
    i=i+1
print(emti_dict)