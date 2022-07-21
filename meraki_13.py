# # Write a program to print the top 3 highest values of a given dictionary.
# # Output :-expect result:-['e','b','c']
# dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
a=[]
max=0
sec=0
third=0
for i in dict:
    for j in dict:
        if dict[j]>max:
            max=dict[j]
            g=j
        elif dict[j]<sec and dict[j]<max:
            sec=dict[j]
            c=j
        elif dict[j]<third and dict[j]<sec:
            third=dict[j]
            k=j
a.append(g)
a.append(c)
a.append(k)
print(a)

# a=[]
# max=0
# sec=0
# third=0
# for i in dict:
#     for j in dict:
#         if dict[j]>max:
#             max=dict[j]
#             g=j
#         elif dict[j]>sec and dict[j]<max:
#             sec=dict[j]
#             c=j
#         elif dict[j]>third and dict[j]<sec:
#             third=dict[j]
#             k=j
# a.append(g)
# a.append(c)
# a.append(k)
# print(a)


