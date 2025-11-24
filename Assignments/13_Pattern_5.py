'''
num = 5
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
num = 5

for i in range(1,num+1):
    for j in range(num - i):
        print(" ",end = " ")
    
    for j in range((2*i)-1):
        print("*",end = " ")

    print()    



# num = int(input("Enter Number of Rows : "))

# for i in range(num):
#     for j in range(num-i):
#         print(" ",end = " ")

#     for j in range((i*2)-1):
#         print("*",end = " ")
#     print()
    