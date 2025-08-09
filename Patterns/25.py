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