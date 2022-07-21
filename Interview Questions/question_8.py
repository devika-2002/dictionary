# Q8. Get key with maximum value in dictionary?\
# Output:= Jaguar

import operator
 
Car = {'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}
keyMax = max(Car.items(), key = operator.itemgetter(1))[0]
print(keyMax)
