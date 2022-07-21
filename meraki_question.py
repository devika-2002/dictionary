# states_capitals ={
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
# }
# for state in states_capitals:
#     print(states_capitals[state])


# details ={
#     "name":  "Bijender",
#     "age":  17,
#     "class":  "10th"
# }
# for x in details.values():
#     print(x)

# movie ={
#     "name":  "Puli",
#     "hero":  "Vijay",
#     "rating":  7.5
# }
# for x,y in movie.items():
#     print(x,y)

# meal ={
#     "monday":  "Chole chawal",
#     "sunday":  "Fried rice",
#     "wednesday":  "dosa"
# }
# print(len(meal))


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)


dic1={1:10, 2:20}
dic2={3:30,2:40}
for i in dic1:
    if i in dic2:
        dic1[i]+dic2[i]
        
dic1.update (dic2)
print(dic1)
    
    
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for i in dic1:
    if i in dic2:
        if i in dic3:
            dic1[i]+dic2[i]+dic3[i]
dic1.update (dic2)
dic1.update(dic3)
print(dic1)

    
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color":"red"})
# print(thisdict)