# Write a python program to find largest number among three and four numbers. 

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
num3 = int(input("Enter 3rd Number : "))
num4 = int(input("Enter 4th Number : "))

greatest = num1

# initialized a list
itemList = [num1,num2,num3,num4]

for i in range(3):
    if itemList[i+1] > greatest:
        greatest = itemList[i+1]

print(greatest)        