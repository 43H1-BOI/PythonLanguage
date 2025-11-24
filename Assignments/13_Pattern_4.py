'''
num = 5
        * 
      * *
    * * *
  * * * *
* * * * *
'''

num = int(input("Enter Number of Rows : "))

# for i in range(num):
#     print("  " * (num-i-1) + "* " * (i+1))


for i in range(num):
    for j in range(num-i):
        print(" ",end = " ")

    for j in range(i+1):
        print("*",end = " ")
    print()
    