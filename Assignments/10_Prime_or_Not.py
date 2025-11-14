# print("Program to Check Wheather a Number is Prime or Not \n")
# num = int(input("Enter a Number : "))
# flag = False

# for i in range(2,num):
#     if(flag):
#         break

#     if(num % i == 0):
#         flag = True


# if(flag):
#     print("Not Prime")
# else :
#     print("Is Prime")    
print("Program to Check Whether a Number is Prime or Not\n")
num = int(input("Enter a Number : "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Is Prime")
