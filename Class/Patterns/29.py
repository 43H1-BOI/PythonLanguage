'''
1 * * * * 
2 2 * * * 
3 3 3 * * 
4 4 4 4 * 
5 5 5 5 5
'''


# num = int(input())

num = 5

for i in range(num):
    print((str(i+1)+" ")*(i+1),("* ")*(num-i-1))
    # for j in range(i+1):
    #     print(i+1,end=" ")

    # for j in range(num-i-1):
    #     print("*",end = " ")

    # print()
