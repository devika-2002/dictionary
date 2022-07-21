# # output:-{'7', '5', '1', '9', '2'}
list1=[{"first":"1"}, 
    {"second": "2"}, 
    {"third": "1"}, 
    {"four": "5"}, 
    {"five":"5"}, 
    {"six":"9"},
    {"seven":"7"}]
jay=[]
for i in list1:
    for devika in i.values():
        if devika not in jay:
            jay.append(devika)  
print(set(jay))