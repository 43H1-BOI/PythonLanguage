'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''


num = 5

num2 = num*2

for i in range(num2-1):
    if(i < num):
        for j in range(i+1):
            print("*",end = " ")
    else:
        for j in range(num2 - i - 1):
            print("*",end = " ")
    print()        
      