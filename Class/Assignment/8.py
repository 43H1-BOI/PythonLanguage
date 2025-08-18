# 8. Write a python program to check whether a person is eligible for loan or not if he is 
#    having salary more than 50k and 3 years of experience. 

sal = int(input("Enter Your Salary : "))
exp = int(input("Enter Your Exp. ( in Years ) : "))

if(sal >= 50000 and exp <= 3):
    print("You are Eligible for Loan")
else :
    print("You are Not Eligible for Loan")