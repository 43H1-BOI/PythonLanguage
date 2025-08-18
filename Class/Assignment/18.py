# 18. Write a python program to calculate the sum of first 50 odd and even numbers.

sumOdd = 1
sumEven = 0

for i in range(50):
    sumOdd += 2
    sumEven += 2

print("Sum Odd =",sumOdd)
print("Sum Even =",sumEven)