# Q14.Write a Python program to multiply all the items in a dictionary.

                    # for_Loop
a={'a':6,'b':6,'c':9}
mul=1
for i in a:
    mul=mul*a[i]
print(mul)


                # while_loop
a={'a':6,'b':6,'c':9}
b=list(a)
i=0
mul=1
while i<len(b):
    mul=a[b[i]]*mul
    i=i+1
print(mul)
    