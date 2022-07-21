# # Enter the  string:-aaabcddeff
# # O/P:-{"a"3:"b":1,"c":1,"d":2,"e":1,"f":2}
text= input("Enter the  string: ")
dict = {}
for letter in text:
    dict[letter] = text.count(letter)
    continue
print (dict)