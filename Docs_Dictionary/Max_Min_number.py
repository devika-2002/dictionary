a={'a':  55, 'b': 14, 'c': 32, 'd': 35}
first=0
sec=0
third=0
min=0
for i in a:
    for i in a :
        for k in a:
            if a[k]>first:
                first=a[k]
            elif a[k]>sec and a[k]<first:
                sec=a[k]
            elif a[k]>third and a[k]<sec:
                third=a[k]
            elif a[k]>min and a[k]<third:
                min=a[k]
print("maxmum_number:-",first)
print("minmum_number:-",min)

