# Q48.Write a Python program to find the length of a given dictionary values. 
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}

# a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# print({value:len(value) for key, value in a.items()})



dict={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
convert_list=list(dict)
dict1={}
i=0
while i<len(convert_list):
    a=dict[convert_list[i]]
    dict1[dict[convert_list[i]]]=len(a)   
    i=i+1
print(dict1)
     
    


