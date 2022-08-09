# Q52. Write a Python program to find the specified number of maximum values in a given dictionary.
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:

a={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
b=list(a)
max=0
i=0
while i<len(b):
    if a[b[i]]>max:
        max=a[b[i]]
    i=i+1
print("max no is ",max)