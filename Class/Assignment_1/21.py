# 21. Write a python program to find the sum of digits of a given number. 

num = input("Enter a Number : ")
sum = 0

for i in num:
    sum += int(i)

print("Sum =",sum)    