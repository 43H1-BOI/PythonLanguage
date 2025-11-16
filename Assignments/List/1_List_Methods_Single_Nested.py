print("List Methods on Single List and Nested List")

# Single List
single_list = [1, 2, 3, 4, 5]
print(f"Original List: {single_list}")

# append() - adds element at end
single_list.append(6)
print(f"After append(6): {single_list}")

# insert() - adds element at specific position
single_list.insert(0, 0)
print(f"After insert(0, 0): {single_list}")

# extend() - adds multiple elements
single_list.extend([7, 8])
print(f"After extend([7, 8]): {single_list}")

# remove() - removes first occurrence of element
single_list.remove(0)
print(f"After remove(0): {single_list}")

# pop() - removes and returns element at index
removed = single_list.pop()
print(f"After pop(): {single_list}, Removed: {removed}")

# pop(index) - removes element at specific index
removed = single_list.pop(2)
print(f"After pop(2): {single_list}, Removed: {removed}")

# index() - returns index of first occurrence
idx = single_list.index(4)
print(f"Index of 4: {idx}")

# count() - returns number of occurrences
single_list.append(5)
count = single_list.count(5)
print(f"Count of 5: {count}")

# sort() - sorts list in ascending order
single_list.sort()
print(f"After sort(): {single_list}")

# sort(reverse=True) - sorts in descending order
single_list.sort(reverse=True)
print(f"After sort(reverse=True): {single_list}")

# reverse() - reverses list
single_list.reverse()
print(f"After reverse(): {single_list}")

# copy() - creates shallow copy
copied_list = single_list.copy()
print(f"Copied List: {copied_list}")

# clear() - removes all elements
temp_list = [1, 2, 3]
temp_list.clear()
print(f"After clear(): {temp_list}")

print("\n--- Nested List ---")

# Nested List
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Original Nested List: {nested_list}")

# append() - adds list at end
nested_list.append([10, 11, 12])
print(f"After append([10, 11, 12]): {nested_list}")

# insert() - adds list at specific position
nested_list.insert(1, [0, 0, 0])
print(f"After insert(1, [0, 0, 0]): {nested_list}")

# extend() - adds elements from list
nested_list.extend([[13, 14]])
print(f"After extend([[13, 14]]): {nested_list}")

# remove() - removes first occurrence
nested_list.remove([0, 0, 0])
print(f"After remove([0, 0, 0]): {nested_list}")

# pop() - removes and returns last element
removed = nested_list.pop()
print(f"After pop(): {nested_list}")

# index() - returns index of list
idx = nested_list.index([4, 5, 6])
print(f"Index of [4, 5, 6]: {idx}")

# count() - counts occurrences
nested_list.append([1, 2, 3])
count = nested_list.count([1, 2, 3])
print(f"Count of [1, 2, 3]: {count}")

# sort() - sorts nested lists
nested_list.sort()
print(f"After sort(): {nested_list}")

# reverse() - reverses nested list
nested_list.reverse()
print(f"After reverse(): {nested_list}")

# copy() - creates shallow copy
copied_nested = nested_list.copy()
print(f"Copied Nested List: {copied_nested}")

# Accessing nested elements
print(f"First element of first list: {nested_list[0][0]}")
print(f"Second element of second list: {nested_list[1][1]}")
