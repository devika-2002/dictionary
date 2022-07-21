# Q5. Sum list of dictionaries with the same key?
# Python code to demonstrate
# return the sum of values of dictionary
# with same keys in list of dictionary
  
# Output:initial dictionary [{‘b’: 10, ‘a’: 5, ‘c’: 90}, {‘b’: 78, ‘a’: 45}, {‘a’: 90, ‘c’: 10}]
#        resultant dictionary : {‘b’: 88, ‘a’: 140, ‘c’: 100}

import collections
ini_dict = [{'a':5, 'b':10, 'c':90}, 
            {'a':45, 'b':78},
            {'a':90, 'c':10}]
print ("initial dictionary", str(ini_dict))
counter = collections.Counter()
for d in ini_dict: 
    counter.update(d)      
result = dict(counter)
print("resultant dictionary : ", str(counter))