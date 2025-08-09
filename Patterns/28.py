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