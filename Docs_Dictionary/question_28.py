# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}


# num_list = [1, 2, 3, 4]
# new_dict = current = {}
# for name in num_list:
#     current[name] = {}
#     current = current[name]
# print(new_dict)
 
 
# num_list = [1, 2, 3, 4]
# current = {}
# a=current
# i=0
# while i<=len(num_list):
#     if i in num_list:
#         current[i] = {}
#         current = current[i]
 
#     i=i+1
# print(a)


a="school"
print(a is "o")