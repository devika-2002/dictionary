# Q15.Write a Python program to remove a key from a dictionary.
                    # for_loop
# myDict = {'a':1,'b':2,'c':3,'d':4}
# print(myDict)
# if 'a' in myDict: 
#     del myDict['a']
# print(myDict)

                        # while_loop
dict = {'a':1,'b':2,'c':3,'d':4}
convert_list=list(dict)
emti_dict={}
i=0
while i<len(dict):
    if dict[convert_list[i]] is not 1:
        emti_dict[convert_list[i]]=dict[convert_list[i]]
    i=i+1
print(emti_dict)