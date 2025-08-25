# 16. Write a python program to print the Fibonacci sequence.

num = int(input())

fibb1 = 0
fibb2 = 1
for i in range(num):
    print(fibb1,end=" ")
    fibb1 , fibb2 = fibb2 , fibb1 + fibb2
