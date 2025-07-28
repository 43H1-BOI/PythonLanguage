num1 = int(input("Enter 1st Value : "))
num2 = int(input("Enter 2nd Value : "))
operator = input("Enter Operator (+,-,*,/,%) : ")

''' Using If Else :-
if(operator == "+") :
    res = num1 + num2 
elif(operator == "-") :
    res = num1 - num2
elif(operator == "*") :
    res = num1 * num2
elif(operator == "/") :
    res = num1 / num2
elif(operator == "%") :
    res = num1 % num2    
else :
    res = operator + " is an Invalid Operator"    
'''

match operator :
    case '+':
        res = num1 + num2 
    case "-":
        res = num1 - num2
    case "*" :
        res = num1 * num2
    case "/" :
        res = num1 / num2
    case "%" :
        res = num1 % num2 
    case any :
        print(operator + " is an Invalid Operator")
        res = "Not a Valid Operation" 

print("{num1} {operator} {num2} = {res}".format(num1 = num1 ,operator = operator,num2 = num2,res = res))