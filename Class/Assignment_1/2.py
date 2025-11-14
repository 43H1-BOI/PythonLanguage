# Write a python program whether a number is positive negative or zero.

print("Program to Check +ve , -ve , zero")

num = int(input("Enter Number : "))
answer = ""

if num < 0 :
    answer = "-ve"
elif num > 0 :
    answer = "+ve"
else : # num == 0
    answer = "zero" 

print(num , "is", answer)       