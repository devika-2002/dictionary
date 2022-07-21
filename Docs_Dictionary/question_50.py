# Q50.Write a Python program to convert a given dictionary into a list of lists. 
# Original Dictionary:
# Convert the said dictionary into a list of lists:
#O/P:- [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
devika=[]
for i in a.items():
    devika.append(list(i))
print(devika)





color_dict = {'1' : 'Austin Little', '2' : 'Natasha Howard', '3' : 'Alfred Mullins', '4' : 'Jamie Rowe'}
devika=[]
for i in color_dict.items():
    devika.append(list(i))
print(devika)