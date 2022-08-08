from lib2to3.pytree import convert


d={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
                # for_loop
# for x in d.values():
#     o = x[4]
#     print(o)

                # while_loop
convert_list=list(d)
i=0
while i<len(convert_list):
    k=d[convert_list[i]]
    l=0
    while l<len(k):
        l=l+1
    i=i+1
    print(k[4])
    