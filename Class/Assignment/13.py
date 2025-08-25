# 13. Write a python program to calculate simple interest.

principal = int(input("Enter Principal Amount : "))
rate = float(input("Enter Rate of Interest PA (in %) : "))
time = int(input("Enter Time of Loan (in Yrs.): "))

simple_interest = ((principal*rate*time)/100)

print("Simple Interest :",simple_interest)