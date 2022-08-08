a={
    "brand":"Ford",
    "Mode":"mustang",
    "year":"1964"
}
print(a)

serial_number=['S001', 'S002', 'S003', 'S004']
name_list=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
numbers_list=[85, 98, 89, 92]
dict={}
i=0
while i<len(serial_number):
    dict[serial_number[i]]=name_list[i]
    i=i+1
d=list(dict)
i=0
while i<len(d):
    dict1={}
    dict1[dict[d[i]]]=numbers_list[i]
    dict[serial_number[i]] = dict1
    i=i+1
print(dict)

   