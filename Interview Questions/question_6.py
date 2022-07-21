# Q6. Split dictionary keys and values into separate lists?
# intial_dictionary {'a': 'akshat', 'b': 'bhuvan', 'c': 'chandan'}
# keys :  dict_keys(['a', 'b', 'c'])
# values :  dict_values(['akshat', 'bhuvan', 'chandan'])

ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'}
keys = ini_dict.keys()
values = ini_dict.values()
print ("keys : ", str(keys))
print ("values : ", str(values))