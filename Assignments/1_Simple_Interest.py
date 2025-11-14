print("Simple Interest")

def fun(p, t, r):
    return (p * t * r) / 100

principal = int(input("Enter Principal Amount (in 1000's): ")) 
time = int(input("Enter Time Period (in Years): ")) 
rate = float(input("Enter Rate of Interest (in %): ")) 

res = fun(principal, time, rate)
print(res)