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