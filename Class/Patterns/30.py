'''
A * * * * 
B B * * * 
C C C * * 
D D D D * 
E E E E E 
'''


# num = int(input())

num = 5

for i in range(num):
    for j in range(i+1):
        print(chr(i+65),end=" ")

    for j in range(num-i-1):
        print("*",end = " ")

    print()
