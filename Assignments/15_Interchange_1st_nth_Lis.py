list = [8,1,2,3,4,5,6,7,0]

print(list)

print("Enter a Number Between 0 to",len(list)-1,"to Swap : ")
first = int(input("Enter 1st Index : "))
second = int(input("Enter 2nd Index : "))

list[first],list[second] = list[second],list[first] 

print(list)
