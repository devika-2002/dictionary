# Q4. Write a Python script to print a dictionary where the keys are numbers   
# between 1 and 15 (both included) and the values are square of keys.
# Simple Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81,
#                  10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}.
                    # For_loop
# n=int(input("Enteer the numbeer:-"))
# x={}
# for i in range(1,n):
#     x[i]=i*i
# print(x)



                # While_loop
n=int(input("enter the number:-"))
i=1
x={}
while i<=n:
    i=1
    while i<=n:
        x[i]=i*i
        i=i+1
print(x)
i=i+1

