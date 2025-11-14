list1 = [-10, 5, -3, 8, 0, -7, 15, -2, 20]

print(f"List: {list1}")
print("Positive numbers:")

# using loop
for num in list1:
    if num > 0:
        print(num, end=" ")

print("\n")

# using list comprehension
positive_numbers = [num for num in list1 if num > 0]
print(f"Using comprehension: {positive_numbers}")

# using filter
positive_filter = list(filter(lambda x: x > 0, list1))
print(f"Using filter: {positive_filter}")
