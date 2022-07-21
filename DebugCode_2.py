# You have been given a dictionary in which you have to find the sum of all the keys.
# You have to debug this code and find out how you can get the output as 14.

# dict={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict:
#     sum=sum+dict[i]
# print(sum)


dict={1:2,2:3,3:4,4:5}
for i in dict.iitems:
    sum=sum+dict[i]
print(sum)
