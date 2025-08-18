# 15. Write a python program to calculate the sum of n natural numbers.

num = int(input())
sum = 1

for i in range(2,num+1):
    sum += i

print("Sum of",num,"=",sum)    