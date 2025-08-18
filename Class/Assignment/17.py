# 17. Write a python program to check whether a number is prime or not. 

num = int(input())

for i in range(2,num):
    if(num % i == 0):
        print("Not Prime")
        break

print("Prime")