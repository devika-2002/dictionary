# Q7. Convert a set into a dictionary?
# O/P:=initial string {1, 2, 3, 4, 5}
# final list {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

ini_set = {1, 2, 3, 4, 5}
print ("initial string", ini_set)
res = dict.fromkeys(ini_set, 0)
print ("final list", res)