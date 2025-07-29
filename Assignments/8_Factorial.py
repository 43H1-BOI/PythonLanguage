num = int(input("Enter a Number : "))

res = num

for i in range(1,num):
    res *= i

print("Factorial of",num,"=",res)