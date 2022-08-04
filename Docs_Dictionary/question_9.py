# Q9.Write a Python program to iterate over dictionaries using for loops.

            #    for_loop
d= {'a': 'juice', 'b': 'grill', 'c': 'corn'}
for key in d:
    print(key, d[key])

                # while_loop
a= {'a': 'juice', 'b': 'grill', 'c': 'corn'}
b=list(a)
i=0
while i<len(b):
    print(b[i],a[b[i]])
    i=i+1
