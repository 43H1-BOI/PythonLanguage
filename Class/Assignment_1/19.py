# 19. Write a python program to find a factorial of a number.

num = int(input())
fact = num

for i in range(2,num):
    fact *= i

print("Factorial =",fact)    