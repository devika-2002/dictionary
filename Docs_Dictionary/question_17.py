# Q17.Write a Python program to sort a dictionary by key.
# a={'d':1,'e':2,'v':3,'i':4,'k':5,'a':6}
# for i in a:
#     print(i,':',a[i])

a={'d':1,'e':2,'v':3,'i':4,'k':5,'a':6}
b=list(a)
i=0
while i<len(b):
    print(b[i],":",a[b[i]])
    i=i+1