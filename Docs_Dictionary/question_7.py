# Q7.Write a Python script to concatenate the following dictionaries to create a new one.
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
for i in dic1:
    if i in dic2:
        if i in dic3:
           dic1[i]+dic2[i]+dic3[i]
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

    
