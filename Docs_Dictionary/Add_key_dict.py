# Q6.Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

                    #For_Loop#
# d = {0:10, 1:20}
# print(d)
# d.update({2:30})
# print(d)

# d = {0:10, 1:20}
# sum=0
# for i in d:
#     sum+=d[i]
# d.update({2:sum})
# print(d)
                            # While_Loop#
a= {0:10, 1:20}
b=list(a)
i=0
sum=0
while i<len(b):
    sum+=a[i]
    i=i+1
a.update({2:sum})
print(a)
