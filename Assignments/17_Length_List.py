list = [0,1,2,3,4,5,6,7,8,9]

# using built-in
print("len:", len(list))

# direct dunder
print("__len__:", list.__len__())

# loop counter
count = 0
for _ in list:
    count += 1
print("loop count:", count)

# generator + sum
print("sum(1 for _ in list):", sum(1 for _ in list))