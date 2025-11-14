# 20. Write a python program to count number of digits in given number.

# num = input("Enter a Number : ")
# flag = 0

# for i in num :
#     flag+=1

# print("Count =",flag)


# Check This :
num = int(input("Enter a Number : "))
flag = 0

while num > 0:
    flag += 1
    num = num >> 1

print("Count =",flag)