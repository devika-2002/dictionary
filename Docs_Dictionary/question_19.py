# Q19.Write a Python program to remove duplicates from Dictionary.

student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
 'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
 'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
 'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']},
}
# # Sample output:
# {'id2': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['David']}, 'id4': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['Surya']}, 'id1': {'subject_integration'
# : ['english, math, science'], 'class': ['V'], 'name': ['Sara']}} 

temp = []
res = dict()
for key, val in student_data.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
  
# printing result 
print("The dictionary after values removal : " + str(res)) 