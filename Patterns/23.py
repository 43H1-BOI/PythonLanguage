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