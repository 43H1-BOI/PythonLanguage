'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''


num = 5
num2 = num * 2

for i in range(num2 - 1):
    if i < num:
        stars = i + 1
    else:
        stars = num2 - i - 1
    spaces = num - stars
    print("  " * spaces + "* " * stars)



# num = 5
# num2 = num * 2 - 1

# for i in range(num2):
#     spaces = abs(num - i - 1)
#     stars = num - spaces
#     print("  " * spaces + "* " * stars)



# num = 5
# num2 = num*2

# for i in range(num2):
#     if i < num :
#       for j in range(num-i-1):
#         print(" ",end = " ")

#       for j in  range(i+1):
#         print("*",end = " ")

#     else :
#        for j in range(num-i):
#           pass

#        for j in range(num2 - i - 1):
#             print("*",end = " ")
#     print()

# for i in range(num):
#     for j in  range(i):
#         print(" ",end = " ")
    
#     for j in range(num-i):
#         print("*",end = " ")

#     print()    