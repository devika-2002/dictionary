# Python has a set of built-in methods that you can use on dictionaries.
                # Method	Description
##1.. clear()	Removes all the elements from the dictionary???
# a={'a':2,'b':9,'c':5}
# b=a.clear()
# print(b)

##2.. copy()	Returns a copy of the dictionary?????????
# a={'a':2,'b':9,'c':5}
# b=a.copy()
# print(b)

##3..fromkeys()	Returns a dictionary with the specified keys and value????
# x = ('key1', 'key2', 'key3')
# y = 9
# thisdict = dict.fromkeys(x, y)
# print(thisdict)

##4..get()	Returns the value of the specified key?????????/
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.get("model")
# print(x)

##5..items()	Returns a list containing a tuple for each key value pair???
# a={'a':2,'b':9,'c':5}
# for i in a.items():
#     print(i)

##6..keys()	Returns a list containing the dictionary's keys??
# a={'a':2,'b':9,'c':5}
# b=a.keys()
# print(b)

##7..pop()	Removes the element with the specified key??
# a={'a':2,'b':9,'c':5}
# a.pop('a')
# print(a)

##8..popitem()	Removes the last inserted key-value pair??
# a={'a':2,'b':9,'c':5}
# a.popitem()
# print(a)

##9..setdefault()	Returns the value of the specified key. If the key does
## not exist: insert the key, with the specified value??
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.setdefault("brand", "model")
# print(x)

##10..update()	Updates the dictionary with the specified key-value pairs???
# a={'a':2,'b':9,'c':5}
# a.update({'d':10})
# print(a)


#11..values()	Returns a list of all the values in the dictionary??
#  a={'a':2,'b':9,'c':5}
# print(a.values())

