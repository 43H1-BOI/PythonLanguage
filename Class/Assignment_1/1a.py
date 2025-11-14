# Write a python program to find largest number among three and four numbers. 

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
num3 = int(input("Enter 3rd Number : "))
# num4 = int(input("Enter 4th Number : "))

greater = num1

if num1>num2 :
    if num1>num3 :
        greater = num2
    else :
        greater = num3
else:
    if num2>num3:
        greater = num2
    else :
        greater = num3

print(greater)        