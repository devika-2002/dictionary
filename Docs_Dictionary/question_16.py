# Q16.Write a Python program to map two lists into a dictionary.
from multiprocessing.sharedctypes import Value
from optparse import Values


keys=["a","b","c","d","e"]
Values=[1,2,3,4,5]
x={}
for key in keys:
    for value in Values:
        x[key]=value
        Values.remove(value)
        break
print(x)