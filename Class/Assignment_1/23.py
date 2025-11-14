# 23. Write a python program to implement continue, break and pass statement 

num = 10

for i in range(num):
    if(i < 2):
        # at i < 2 loop will continue
        continue
    elif(i == 5):
        # at i == 4 loop will break
        break
    else:
        print("Value of",i)

if num > 10 :
    pass        