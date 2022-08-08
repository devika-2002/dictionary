# Q50.Write a Python program to convert a given dictionary into a list of lists. 
# Original Dictionary:
# Convert the said dictionary into a list of lists:
#O/P:- [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]


a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
convert_list=list(a)
emti_list=[]
i=0
while i<len(convert_list):
    emti_list.append(convert_list[i])
    emti_list.append(a[convert_list[i]])
    i=i+1
print(emti_list)




# j=0
# emti_list1=[]
# while j<len(emti_list):
#     emti_list1.append(emti_list[0])
#     j=j+1
# print(emti_list1)


# devika=[]
# for i in a.items():
#     devika.append(list(i))
# print(devika)





# color_dict = {'1' : 'Austin Little', '2' : 'Natasha Howard', '3' : 'Alfred Mullins', '4' : 'Jamie Rowe'}
# devika=[]
# for i in color_dict.items():
#     devika.append(list(i))
# print(devika)