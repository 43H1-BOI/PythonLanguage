#
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

num = int(input())

for i in range(num):
    for j in  range(i+1):
        print("*",end = " ")
    print()    


# 2
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *
'''

num = int(input())

for i in range(num):
    for j in range(num -i-1):
        print(" ",end = " ")

    for j in  range(i+1):
        print("*",end = " ")
    print()


# 3
'''
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''

num = 5

for i in range(num):

    for j in  range(i):
        print(" ",end = " ")
    
    for j in range(num-i):
        print("*",end = " ")

    print()


# 4
'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

num = 5

for i in range(num):
    for j in range(num-i):
        print("*",end=" ")
    print()    


# 5
'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
'''

num = 5

for i in range(num):
    for j in range(num-i-1):
        print(" ",end = " ")

    for j in range(i+1):
        print("*",end=" ")

    for j in range(i):
        print("*",end = " ")

    print()            


# 6
'''
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''

num = 5

for i in range(num):

    for j in  range(i):
        print(" ",end = " ")
    
    for j in range(num-i):
        print("*",end = " ")

    for j in range(num - i - 1):
        print("*",end = " ")    

    print()


# 7
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


# 8
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

num = 5

for i in range(num):
    for j in range(num):
        print("*",end = " ")
    print()    


# 9
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

num2 = num*2

for i in range(num2-1):
    if(i < num):
        for j in range(i+1):
            print("*",end = " ")
    else:
        for j in range(num2 - i - 1):
            print("*",end = " ")
    print()        
      

# 10
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

for i in range(num-1):
    for j in range(num-i-1):
        print(" ",end = " ")

    for j in  range(i+1):
        print("*",end = " ")
    print()

for i in range(num):

    for j in  range(i):
        print(" ",end = " ")
    
    for j in range(num-i):
        print("*",end = " ")

    print()    


# 11
'''
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
'''

num = 5

for i in range(num):
    for j in range(num):
        print(i+1,end=" ")
    print()


# 12
'''
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
'''

num = 5

for i in range(num):
    for j in range(num):
        print(j+1,end=" ")
    print()


# 13
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''

num = 5

for i in range(num):
    for j in  range(i+1):
        print(i+1,end = " ")
    print()


# 14
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''

num = 5

for i in range(num):
    for j in  range(i+1):
        print(j+1,end = " ")
    print()


# 15
'''
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5 
'''

num = 5

for i in range(num):
    for j in range(num -i-1):
        print(" ",end = " ")

    for j in  range(i+1):
        print(i+1,end = " ")
    print()


# 16
'''
1 1 1 1 1 
  2 2 2 2 
    3 3 3 
      4 4 
        5 
'''

num = 5

for i in range(num):

    for j in  range(i):
        print(" ",end = " ")
    
    for j in range(num-i):
        print(i+1,end = " ")

    print()


# 17
'''
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
'''

num = 5

for i in range(num):
    for j in range(num-i):
        print(i+1,end=" ")
    print()


# 18
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
'''

num = 5

for i in range(num):
    for j in range(num-i):
        print(num-i,end=" ")
    print()


# 19
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''

num = 5
count = 1

for i in range(num):
    for j in  range(i+1):
        print(count,end = " ")
        count+=1
    print()


# 20
'''
0 0 0 0 0 
1 1 1 1 
0 0 0 
1 1 
0 
'''

num = 5
temp = 0

for i in range(num):
    if(i%2==0):
        temp = 0
    else:
        temp = 1    

    for j in range(num-i):
        print(temp,end=" ")
    print()


#21
'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''

num = 5

for i in range(num):
    for j in range(num-i):
        print(j+1,end=" ")
    print()


# 22
'''
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 
'''

num = 5

for i in range(num):
    for j in range(num-i):
        print(num-j,end=" ")
    print()


# 23
'''
1 
3 5 
7 9 11 
13 15 17 19 
21 23 25 27 29 
'''

num = 5
count = 1

for i in range(num):
    for j in  range(i+1):
        print(count,end = " ")
        count+=2
    print()


# 24
'''
2 
4 6 
8 10 12 
14 16 18 20 
22 24 26 28 30 
'''

num = 5
count = 2

for i in range(num):
    for j in  range(i+1):
        print(count,end = " ")
        count+=2
    print()


# 25
'''
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E 
'''

num = 5

for i in range(num):
    for j in range(num):
        print(chr(65+i),end = " ")
    print()    


# 26
'''
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E 
'''

num = 5

for i in range(num):
    for j in range(num):
        print(chr(65+j),end = " ")
    print()    


# 27
'''
A 
A B 
A B C 
A B C D 
A B C D E 
'''

num = 5

for i in range(num):
    for j in  range(i+1):
        print(chr(65+j),end = " ")
    print()


# 28
'''
A 
B B 
C C C 
D D D D 
E E E E E 
'''

num = 5

for i in range(num):
    for j in  range(i+1):
        print(chr(65+i),end = " ")
    print()