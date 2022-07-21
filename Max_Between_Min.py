# my_dict = {'A': 67, 'B': 23, 'C': 45,
#            'D': 56, 'E': 12, 'F': 69}
# O/P:=F  : 69  
#      A  : 67  
#      D  : 56
from collections import Counter
my_dict = {'A': 67, 'B': 23, 'C': 45,
           'D': 56, 'E': 12, 'F': 69}
k = Counter(my_dict)
high = k.most_common(3)
for i in high:
    print(i[0]," :",i[1]," ")
 
 
