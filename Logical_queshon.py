d={"jay":[1,2,3],"patel":[5,7,2]}
# [6,14]
for i in d:
    a=d[i]
    j=0
    sum=0
    while j<len(a):
        sum=sum+a[j]
        j=j+1
        d[i]=sum
print(d)
    
    

# a=[{"math":90,"scince":92},{"math":89,"scince":94},{"math":92,"science":88}]
# # o/p:=[92,94,88]
# i=-1
# for i in a:
#     print(a[i])
    