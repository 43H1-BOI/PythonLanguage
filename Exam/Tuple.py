# Write a function that accept a tuple of numbers and returns the sum and average of the numbers.

def sum_avg(tup):
    sum = 0
    for i in tup:
        sum += i

    avg = sum/len(tup)
    
    return sum , avg

tuple = (1,3,5,7,9,11)

sum , avg = sum_avg(tuple)

print(sum , avg)