# .Write a Python program to filter the height and width of students, which are 
# stored in a dictionary. 
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

d1={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
convert_list=list(d1)
d2= {}
i=0
while i<len(convert_list):
        if d1[convert_list[i]]>=(6, 70):
            d2[convert_list[i]]=d1[convert_list[i]]
        i=i+1
print(d2)



# for i in d1.items():
#     if i[0]>6.0 and i[1]>70:
#         print(d1[i])
    