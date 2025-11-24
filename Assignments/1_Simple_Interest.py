print("Simple Interest")

def fun(principal, time, rate):
    return (principal * time * rate) / 100

principal = int(input("Enter Principal Amount (in 1000's): ")) 
time = int(input("Enter Time Period (in Years): ")) 
rate = float(input("Enter Rate of Interest (in %): ")) 

res = fun(principal, time, rate)
print(res)