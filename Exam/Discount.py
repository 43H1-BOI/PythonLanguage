amount = int(input())

if amount < 1000 :
    newAmt = amount - (amount * 0.05)
else :   
    newAmt = amount - (amount * 0.10)


print("Discount Amount =",(amount - newAmt))
print("Final Amount =",newAmt)