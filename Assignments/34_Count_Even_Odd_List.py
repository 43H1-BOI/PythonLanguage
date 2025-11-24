list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0

# using loop
for num in list1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"List: {list1}")
print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}")

# using comprehension
even_count_comp = len([num for num in list1 if num % 2 == 0])

# evem = sum(1 for i in list1 if i % 2 == 0)

odd_count_comp = len([num for num in list1 if num % 2 != 0])
print(f"\nUsing comprehension:")
print(f"Even count: {even_count_comp}")
print(f"Odd count: {odd_count_comp}")
