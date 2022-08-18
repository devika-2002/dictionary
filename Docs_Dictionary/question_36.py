# Q36.Write a Python program to match key values in two dictionaries. 
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y


# dict={'key1': 1, 'key2': 3, 'key3': 2}
# dict1={'key1': 1, 'key2': 2}
# for i in dict:
#     for j in dict1:
#         if i==j and dict[i]==dict1[j]:
#             print('{}:{} is present in both dict,dict1'.format(i,dict[i]))




d1={'key1': 1, 'key2': 3, 'key3': 2}
d2={'key1': 1, 'key2': 2}
convert_list=list(d1)
convert_list1=list(d2)
i=0
while i<len(convert_list):
    j=0
    while j<len(convert_list1):
        if i==j and d1[convert_list[i]]==d2[convert_list1[j]]:
            print(convert_list[i],':',d2[convert_list1[i]])
            j=j+1
        i=i+1
        