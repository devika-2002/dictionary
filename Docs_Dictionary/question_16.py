# Q16.Write a Python program to map two lists into a dictionary.
# keys=["a","b","c","d","e"]
# Values=[1,2,3,4,5]
# zip_object=zip(keys,Values)
# print(dict(zip_object))

# keys=["a","b","c","d","e"]
# Values=[1,2,3,4,5]
# x={}
# for key in keys:
#     for value in Values:
#         x[key]=value
#         Values.remove(value)
#         break
# print(x)

keys=["a","b","c","d","e"]
Values=[1,2,3,4,5]
emti_dict={}
i=0
while i<len(keys):
    emti_dict[keys[i]]=Values[i]
    i=i+1
print(emti_dict)

# x={}
# a="devika"
# for i in a:
#     if i in a[3]:
#         x[a[3]]=a
# print(x)