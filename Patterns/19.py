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