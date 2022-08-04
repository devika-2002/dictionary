a={'a':  55, 'b': 14, 'c': 32, 'd': 35}
val=a.values()
b=list(val)
min=b[0]
i=0
while i<len(b):
    if b[i]<min:
        min=b[i]
    i=i+1
print(min)