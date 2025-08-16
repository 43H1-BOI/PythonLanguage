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