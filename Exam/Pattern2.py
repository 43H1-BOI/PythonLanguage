num = int(input("Enter number of rows: "))

for i in range(num):
    for j in range(i):
        print(" ", end=" ")
    
    for j in range(num - i):
        print("*", end=" ")
    
    count = i + 1
    for j in range(num - i - 1):
        print(count, end=" ")
        count += 1
    
    print() 

# * * * * * 1 2 3 4 
#   * * * * 2 3 4
#     * * * 3 4
#       * * 4
#         *    