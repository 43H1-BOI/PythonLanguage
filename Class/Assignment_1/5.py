# 5. Write a python program to check whether a year is a leap year or not.

num = int(input())

if((num % 4 == 0 and num % 100 != 0) or (num % 400 == 0)):
    print("Leap Year")
else :
    print("Not a Leap Year")