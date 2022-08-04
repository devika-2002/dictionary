# Q1.Write a Python program to combine two dictionary adding values for common keys.
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

                # for_loop
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d1:
#     if  i in d2:
#         d2[i]=d1[i]+d2[i]
#     else:
#         d2[i]=d1[i]
# print(d2)


                    # while_lopp??
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
a=list(d1)
b=list(d2)
x={}
i=0
while i<len(a):
    if a[i] in b[i]:
        x[a[i]]=d1[a[i]]+d2[b[i]]
    else:
        x[a[i]]=a[i]=d1[a[i]]
        x[b[i]]=b[i]=d2[b[i]]
    i=i+1
print(x)