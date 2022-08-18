# Q52. Write a Python program to find the specified number of maximum values in a given dictionary.
# Original Dictionary:
d = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
l=[]
emti_dict={}
for i in d.values():
    l.append(i)
maximum = max(l)   
for j in l:
    if j in emti_dict:
        emti_dict[j]+=1
    else:
        emti_dict[j]=1
print(emti_dict[maximum])