# Write a program to sort a dictionary in ascending or descending according to its 
# values .
# O/P:={'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
# O/P:={'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}

a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for i in a:
#     if i in a:
#         b=sorted(a.items())
# print("ascending order:",dict(b))
a1=sorted(a,key=a.get)
d=[]
for r in a1:
    c=(r,a[r])
    d.append(c)
    
print(dict(d))