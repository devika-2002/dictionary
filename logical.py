# # o/p:=['a',6]['n',2]['t',2]['x',2]['u',1]['g'1]
# list=["a","n","t","a","a","t","n","a","x","u","g","a","x","a"]
# l=[]
# for i in list:
#     c=0
#     for j in list:
#         if i==j:
#             c+=1
#     if  i not in l:
#         l.append(i)
#         print([i,c],end="")

##O/P:- {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# devika={}
# for num in range(1,11):
#     devika[num]=num*num
# print(devika)


# devika={}
# for jay in range(11,21):
#     devika[jay]=dict()
#     for k in range(1,11):
#         devika[jay][k]=jay*k
# print(devika)


# data = {'manoja': [{'subject1': "java", 'marks': 98}, 
#                    {'subject2': "PHP", 'marks': 89}],
#         'manoj': [{'subject1': "java", 'marks': 78},
#                   {'subject2': "PHP", 'marks': 79}],
#         'ramya': [{'subject1': "html", 'marks': 78}]}
  
# # get the list of data
# # using items() method
# for key, values in data.items():
#     for i in values:
#         print(data[i])