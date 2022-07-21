# Enter the string:-abcaac
#              O/P:-1
a=input("Enter the sting:-")
dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for j in range(len(a)):
    if dict[a[j]]==1:
        print(j)
        break