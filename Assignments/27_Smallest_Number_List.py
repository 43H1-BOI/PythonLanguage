list1 = [34, 12, 56, 7, 89, 3, 45]

# using built-in min function
smallest = min(list1)
print(f"List: {list1}")
print(f"Smallest number: {smallest}")

# using loop
smallest_loop = list1[0]
for num in list1:
    if num < smallest_loop:
        smallest_loop = num
print(f"Using loop: {smallest_loop}")

# using sorted
smallest_sorted = sorted(list1)[0]
print(f"Using sorted: {smallest_sorted}")
