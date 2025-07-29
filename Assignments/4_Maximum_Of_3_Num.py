num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
num3 = int(input("Enter 3rd Number : "))

max = num1

if(num1 > num2):
    if(num1 >= num3):
        max = num1
    else :
        max = num3
else : # num 2 >= num1
    if(num2 >= num3) :
        max = num2
    else :
        max = num3    


print("Maximum = ",max)