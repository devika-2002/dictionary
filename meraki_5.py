# Create a dictionary from 2 lists, where the elements of 1st list are the keys and 
# the elements of the 2nd list are the corresponding values.
# Output :-{“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}

list1=['one','two','three','four','five']
list2=[1,2,3,4,5,]
x={}
for key in list1:
    for value in list2:
        x[key]=value
        list2.remove(value)
        break
print(x)



# test_keys =['one','two','three','four','five']
# test_values=[1,2,3,4,5,]
# res = {}
# for key in test_keys:
#     for value in test_values:
#         res[key] = value
#         test_values.remove(value)
#         break  
# print ("Resultant dictionary is : " +  str(res))