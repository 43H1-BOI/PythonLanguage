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