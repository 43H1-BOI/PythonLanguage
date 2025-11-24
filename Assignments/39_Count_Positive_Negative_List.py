list1 = [-10, 5, -3, 8, 0, -7, 15, -2, 20]

positive_count = 0
negative_count = 0

# using loop
for num in list1:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print(f"List: {list1}")
print(f"Positive count: {positive_count}")
print(f"Negative count: {negative_count}")

# using comprehension
positive_count_comp = len([num for num in list1 if num >= 0])
negative_count_comp = len([num for num in list1 if num < 0])
print(f"\nUsing comprehension:")
print(f"Positive count: {positive_count_comp}")
print(f"Negative count: {negative_count_comp}")

