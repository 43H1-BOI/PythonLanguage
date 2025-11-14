# 6. Write a python program to calculate profit or loss.

cp = int(input("Enter Cost Price : "))
sp = int(input("Enter Selling Price : "))

if sp > cp :
    print("Profit =",str(sp-cp))
else :
    print("Loss =",str(cp-sp))