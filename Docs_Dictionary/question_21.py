# Q21.Write a Python program to print all unique values in a dictionary. 
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S00

# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)

data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
    {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]



# i = 0
# while i<len(data):
#     x = data[i]
#     convert_list = list(x)
#     for j in convert_list:
#         # if j in convert_list:
#         print(j)
#     i=i+1


# a={1:3,'r':2}
# for i in a:
#     print(i)