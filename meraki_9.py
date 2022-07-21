# Store the unique letters and their frequency of the letters from the word 
# "MISSISSIPPI" to a dictionary, were the letters are the keys and their frequencies
# are the values.
# O/P:-{'M':1,'I':4,'S':4,'P':2}
a= "MISSISSIPPI"
dict = {}
for letter in a:
    dict[letter] = a.count(letter)
    continue
print (dict)      


# # # # input Enter the string:-aabcdc
# # # # O/P:={'a':2,'b':1,'c':2,'d':1}
# text= input("input Enter the string:- ")
# dict = {}
# for letter in text:
#     dict[letter] = text.count(letter)
#     continue
# print (dict)      


# # o/p:-{'M':1,'I':1,'S':1,'P':1}
# a= "MISSISSIPPI"
# count={}
# for i in a:
#     if  i  in count:
#         count[i]=1
#     else:
#         count[i]=1
# print(count)
        
