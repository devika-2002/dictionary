##1..Print all key names in the dictionary, one by one:???????????
# a=	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in a:
#   print(x)

##2.. Print all values in the dictionary, one by one:?????????/
# a=	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in a:
#   print(a[x])

##3..You can also use the values() method to return values of a dictionary:????????
# a={
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in a.values():
#   print(x)

##4..You can use the keys() method to return the keys of a dictionary:????
# a={
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in a.keys():
#   print(x)


##5..Loop through both keys and values, by using the items() method:
a={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in a.items():
  print(x, y)



