# Q4. Find keys with duplicate values in the dictionary?

# Output:
# initial_dictionary {'c': 3, 'b': 2, 'd': 2, 'a': 1}
# duplicate values [2]

ini_dict = {'a':1, 'b':2, 'c':3, 'd':2}
print("initial_dictionary", str(ini_dict))
rev_dict = {}
for key, value in ini_dict.items():
    rev_dict.setdefault(value, set()).add(key)
    result = [key for key, values in rev_dict.items()
                              if len(values) > 1]
print("duplicate values", str(result))
