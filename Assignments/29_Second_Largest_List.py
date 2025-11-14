list1 = [34, 12, 56, 7, 89, 3, 45]

# using sorted
sorted_list = sorted(list1, reverse=True)
second_largest = sorted_list[1]
print(f"List: {list1}")
print(f"Second largest number: {second_largest}")

# using loop
largest = max(list1)
second = float('-inf')
for num in list1:
    if num > second and num < largest:
        second = num
print(f"Using loop: {second}")

# removing duplicates
list2 = [10, 20, 30, 20, 10, 30, 40]
unique_sorted = sorted(set(list2), reverse=True)
if len(unique_sorted) >= 2:
    print(f"\nList with duplicates: {list2}")
    print(f"Second largest (unique): {unique_sorted[1]}")
