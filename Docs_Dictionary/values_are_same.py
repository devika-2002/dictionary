# Q42.Write a Python program to check all values are same in a 
# dictionary. Go to the editor
# Original Dictionary:
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False  
        #    FOR_Loop
# a={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 
# 'Pierre Cox': 12}
# n=int(input("enter the number:-"))
# for i in a:
#     if n==a[i]:
#         print(True)
#         break
#     else:
#         print(False)
#         break
    



a={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
convert_list=list(a)
n=int(input("enter the number:-"))
i=0
while i<len(convert_list):
    if n==a[convert_list[i]]:
        print(True)
        break
    else:
        print(False)
        break
    i=i+1
