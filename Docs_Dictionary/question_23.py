# Q23.Write a Python program to find the highest 3 values of corresponding keys in 
# a dictionary.
#o/p=100,68,50

dict={"a":100,"b":68,"c":50,"d":40}
a=[]
max=0
sec=0
third=0
for i in dict:
    for j in dict:
        if dict[j]>max:
            max=dict[j]
        elif dict[j]>sec and dict[j]<max:
            sec=dict[j]
        elif dict[j]>third and dict[j]<sec:
            third=dict[j]
a.append(max)
a.append(sec)
a.append(third)
print(a)












