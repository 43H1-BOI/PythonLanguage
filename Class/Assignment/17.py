# 17. Write a python program to check whether a number is prime or not. 

num = int(input())
flag = False

for i in range(2,num):
    if(num % i == 0):
        flag = True
        break
    
if flag :
    print("Not Prime")
else :
    print("Prime")