# 7. Write a python program to calculate grades of a student. 

marks = int(input("Enter Marks of Student (Out of 100) : "))

if marks <= 100 :
    if marks >= 100 :
        print("O")
    elif marks >= 90 :
        print("A+")
    elif marks >= 80 :        
        print("A")    
    elif marks >= 70 :        
        print("B+")    
    elif marks >= 60 :        
        print("B")   
    elif marks >= 50 :        
        print("C")    
    elif marks >= 35 :        
        print("Pass")
    else :
        print("Fail")        
else :
    print("Invalid Marks")