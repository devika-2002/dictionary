# Q45.Write a Python program to remove a specified dictionary from a given list. 
# Original list of dictionary:
# [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

                                        # For_loop
# l = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000',
# 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'},
# {'id': '#808000', 'color': 'Olive'}]
# l2 = []
# for i in l:
#     if (i['id'] != '#FF0000'):
#         l2.append(i)
# print(l2)

                            # While_loop
dict=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, 
   {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
i=0
emti_list=[]
while i<len(dict):
    if (dict[i]['id'] != '#FF0000'):
        emti_list.append(dict[i])
    i=i+1
print(emti_list)
