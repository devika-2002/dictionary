# Q11.Write a Python script to merge two Python dictionaries


a={'devika':6,"kumari":6}
b={"raj":3,"banshi":6}
for i in a:
    if i in b:
        a[i]+b[i]
a.update(b)
print(a)