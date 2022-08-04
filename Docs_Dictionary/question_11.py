# Q11.Write a Python script to merge two Python dictionaries

                # For_Loop
# a={'devika':6,"kumari":6}
# b={"raj":3,"banshi":6}
# for i in a:
#     if i in b:
#         a[i]+b[i]
# a.update(b)
# print(a)

                        # While_loop
a={'devika':6,"kumari":6}
b={"raj":3,"banshi":6}
x=list(a)
y=list(b)
z={}
i=0
while i<len(x):
    z[x[i]]=a[x[i]]
    i=i+1
z.update(b)
print(z)
