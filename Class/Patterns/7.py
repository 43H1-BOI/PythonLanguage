'''
    * 
  * * * 
* * * * *  
  * * * 
    * 
'''


num = 3

for i in range(num-1):
    for j in range(num-i-1):
        print(" ",end = " ")

    for j in range(i+1):
        print("*",end=" ")

    for j in range(i):
        print("*",end = " ")

    print()         


for i in range(num):

    for j in range(i):
        print(" ",end = " ")
    
    for j in range(num-i):
        print("*",end = " ")

    for j in range(num - i - 1):
        print("*",end = " ")    

    print()       

# num = 3
# num2 = 2 * num - 1

# for i in range(num2):
#     if i < num:
#         for j in range(num - i - 1):
#             print(" ", end=" ")
#         for j in range(2 * i + 1):
#             print("*", end=" ")
#     else:
#         for j in range(i - num + 1):
#             print(" ", end=" ")
#         for j in range(2 * (num2 - i - 1) + 1):
#             print("*", end=" ")
#     print()