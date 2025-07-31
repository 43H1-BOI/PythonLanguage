'''
num = 5
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

Having Problem like not printing last row
'''


num = int(input("Enter Number of Rows : "))

for i in range(num):
    for j in range(num-i):
        print(" ",end = " ")

    for j in range((i*2)-1):
        print("*",end = " ")
    print()
    