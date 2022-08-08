# Q33.Python: Print a dictionary line by line
# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# Sample Output:
# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3 

cars={'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
for x in cars:
    print (x)
    for y in cars[x]:
        print (y,':',cars[x][y])
        