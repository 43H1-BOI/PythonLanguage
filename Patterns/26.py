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