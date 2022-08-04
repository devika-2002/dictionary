# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

                    # For_loop
# d='w3resource'
# count={}
# for i in d:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)


                    # While_loop
a='w3resource'
dic1={}
i=0
while i<len(a):
    if  a[i] in dic1:
        dic1[a[i]]+=1
    else:
        dic1[a[i]]=1
    i=i+1
print(dic1)