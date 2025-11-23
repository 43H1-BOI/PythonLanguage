# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# Normal
def fibbMain(num):
    fibb1 = 0
    fibb2 = 1
    
    if num < 1 :
        print("InValid Input")
    else :
        for i in range(num):
            print(fibb1,end = " ")
            fibb1 , fibb2 = fibb2 , fibb1 + fibb2

# fibbMain(5)


# Recurssion
def fibbRec(num):
    if num <= 1 :
        return num
    else :
        return (fibbRec(num - 1) + fibbRec(num - 2))
    

count = int(input())

for i in range(count):
    print(fibbRec(i),end = " ")
