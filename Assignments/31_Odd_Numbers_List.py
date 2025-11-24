list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"List: {list1}")
print("Odd numbers:")

# using loop
for num in list1:
    if num % 2 != 0:
        print(num, end=" ")

print("\n")

# using list comprehension
odd_numbers = [num for num in list1 if num % 2 != 0]
print(f"Using comprehension: {odd_numbers}")

# using filter
odd_filter = list(filter(lambda x: x % 2 != 0, list1))
print(f"Using filter: {odd_filter}")

