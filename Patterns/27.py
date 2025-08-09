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