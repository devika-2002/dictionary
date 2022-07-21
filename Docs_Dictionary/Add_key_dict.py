# Q6.Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# d = {0:10, 1:20}
# print(d)
# d.update({2:30})
# print(d)



d = {0:10, 1:20}
sum=0
for i in d:
    sum+=d[i]
d.update({2:sum})
print(d)
        
