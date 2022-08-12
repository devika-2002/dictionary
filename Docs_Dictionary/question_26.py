# Write a Python program to print a dictionary in table format.
# Sample Output:
# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11

                        # for_loop
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#     print(*row)
 


dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
a,b,c=dict.keys()
print(a,b,c)
x,y,z=dict.values()
d=x,y,z
i=0
while i<len(d):
    print(x[i],y[i],z[i])
    i=i+1