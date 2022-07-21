# Q1. Difference between dict.items() and dict.iteritems() in Python?

# dict.items(): returns a copy of the dictionary’s list in the form of
# (key, value) tuple pairs, which is a (Python v3.x) version, and exists in 
# (Python v2.x) version.

# dict.iteritems(): returns an iterator of the dictionary’s list in the form of 
# (key, value) tuple pairs. which is a (Python v2.x) version and got omitted in 
# (Python v3.x) version.
d={
  "fantasy": "harrypotter",
  "romance": "me before you",
  "fiction": "divergent"
  }
print(d.items())

# d={
#   "fantasy": "harrypotter",
#   "romance": "me before you",
#   "fiction": "divergent"
#   }
# print(d.iteritems())