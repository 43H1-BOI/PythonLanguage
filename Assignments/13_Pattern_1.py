'''
num = 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

num = int(input("Enter Number of Rows : "))

for i in range(1,num+1):
    for count in range(1,i+1):
        print(count , end = " ")
    print()