# Q13.Write a Python program to sum all the items in a dictionary.

# a={"a":3,"b":7,"j":8}
# sum=0
# for i in a:
#     sum=sum+a[i]
# print(sum)

a={"a":3,"b":7,"j":8}
b=list(a)
i=0
sum=0
while i<len(b):
    sum+=a[b[i]]
    i=i+1
print(sum)