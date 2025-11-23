num = int(input())

# Method 1
for i in range(1,num+1):
    print("  " * (num - i),end = " ")
    print("* " * ((i*2)-1),end = " ")
    print()

# Method 2
for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end = " ")

    for j in range((i*2)-1):
        print("*", end = " ")

    print()    
        