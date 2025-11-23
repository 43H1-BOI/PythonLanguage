print("Program to Check a Number is Prime or Not !")

num = int(input())
flag = False

for i in range(2,num-1):
    if num % i == 0 :
        flag = True
        break

if flag :
    print("Not Prime")
else :    
    print("Prime")