# Write a program remove the first key value pair from a nested dictionary.
# Example :-
# Input :-
# Code Example
dic= {
1: 'NAVGURUKUL',
2: 'IN',  
  3:{
 'A' : 'WELCOME',
 'B' : 'To',
 'C' : 'DHARAMSALA'}}
for i,j in dic.items():
    del dic[3]["A"]
    break
print(dic)

# for i in dic.items():
#     print(i)
    





