# 22. Write a python program to print a table of a number using for and while loop.

num = int(input())

print("Using For Loop : ")
for i in range(1,11):
    print(num,"x",i,"=",(num*i))

print("Using While Loop : ")
i = 1
while i <= 10 :
    print(num,"x",i,"=",(num*i))
    i+=1