list1 = [34, 12, 56, 7, 89, 3, 45]

# using built-in max function
largest = max(list1)
print(f"List: {list1}")
print(f"Largest number: {largest}")

# using loop
largest_loop = list1[0]
for num in list1:
    if num > largest_loop:
        largest_loop = num
print(f"Using loop: {largest_loop}")

# using sorted
largest_sorted = sorted(list1)[-1]
print(f"Using sorted: {largest_sorted}")

