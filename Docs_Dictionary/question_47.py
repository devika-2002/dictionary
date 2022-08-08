# Q47.A Python Dictionary contains List as value. Write a Python program to clear the
# list values in the said dictionary. 
# Original Dictionary:
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}
            # For_loop
# D={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for i in D:
#     D[i].clear()
# print(D)

                        # while_loop
dict={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
convert_list=list(dict)
dict1={}
i=0
while i<len(convert_list):
    dict1[convert_list[i]]=[]
    i=i+1
print(dict1)
    
