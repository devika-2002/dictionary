# Q18.Write a Python program to get the maximum and minimum value in a dictionary.
# dict = {'x':500, 'y':5874, 'z': 560}
# max=0
# for i in dict:
#     if dict[i]>max:
#         max=dict[i]
# print("max no is ",max)
# val=dict.values()
# l=list(val)
# i=0
# min=l[0]
# while i <len(l):
#     if l[i]<min:
#         min=l[i]
#     i=i+1
# print('min no_is',min)





# dict = {'x':500, 'y':5874, 'z': 560}
# max=0
# for i in dict:
#     if dict[i]>max:
#         max=dict[i]
        



dict = {'a':50, 'b':8, 'c': 56,'d':40,'e':68}
convert_list=list(dict)
i=0
emti_list=[]
while i<len(convert_list):
    emti_list.append(dict[convert_list[i]])
    emti_list1=[]
    max=0
    min=10
    j=0
    while j<len(emti_list):
        if emti_list[j]>max:
            max=emti_list[j]
        elif emti_list[j]<min:
            min=emti_list[j]
        j=j+1
    i=i+1
print("max_number:-",max)
print("min_number:-",min)





