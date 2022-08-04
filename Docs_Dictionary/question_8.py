# Q8.Write a Python program to check whether a given key already exists in a dictionary.
                  #  For_loop
# def key_in_dict(d, key):
#   return (key in d) 
# students = {
#   'Theodore': 19,
#   'Roxanne': 22,
#   'Mathew': 21,
#   'Betty': 20
# }
    
# print("\nOriginal dictionary elements:")
# print(students)
# print(key_in_dict(students, 'Roxanne'))
# print(key_in_dict(students, 'Gina'))


               # while loop
students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 20
}
x={}
a=list(students)
i=0
while i<len(a):
    x[a[i]]=students[a[i]]
    i=i+1
print(x)