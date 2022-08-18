# Q21.Write a Python program to print all unique values in a dictionary. 
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}


# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# # print("Original List: ",L)
# u_value = set(val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)

dict=[{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
emti_list=[]
for i in dict:
    for j in i.values():                                                  
        emti_list.append(j)
print(set(emti_list))
    

# a={1:3,'r':2}
# for i in a:
#     print(i)