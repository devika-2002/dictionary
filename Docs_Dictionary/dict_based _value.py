# Q39.Write a Python program to filter a dictionary based on values. 
# Original Dictionary:
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

                       # For_loop
# d1={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# d2= {}
# for i,j in d1.items():
#     if j > 170:
#         d2[i] = j
# print(d2)

                        # while_loop
d1={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
convert_list=list(d1)
d2= {}
i=0
while i<len(convert_list):
        if d1[convert_list[i]]>170:
            d2[convert_list[i]]=d1[convert_list[i]]
        i=i+1
print(d2)















# for i,j in d1.items():
#     if j > 170:
#         d2[i] = j
# print(d2)

