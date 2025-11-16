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
nList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Original Nested List: {nList}")

# append() - adds list at end
nList.append([10, 11, 12])
print(f"After append([10, 11, 12]): {nList}")

# insert() - adds list at specific position
nList.insert(1, [0, 0, 0])
print(f"After insert(1, [0, 0, 0]): {nList}")

# extend() - adds elements from list
nList.extend([[13, 14]])
print(f"After extend([[13, 14]]): {nList}")

# remove() - removes first occurrence
nList.remove([0, 0, 0])
print(f"After remove([0, 0, 0]): {nList}")

# pop() - removes and returns last element
removed = nList.pop()
print(f"After pop(): {nList}")

# index() - returns index of list
idx = nList.index([4, 5, 6])
print(f"Index of [4, 5, 6]: {idx}")

# count() - counts occurrences
nList.append([1, 2, 3])
count = nList.count([1, 2, 3])
print(f"Count of [1, 2, 3]: {count}")

# sort() - sorts nested lists
nList.sort()
print(f"After sort(): {nList}")

# reverse() - reverses nested list
nList.reverse()
print(f"After reverse(): {nList}")

# copy() - creates shallow copy
copied_nested = nList.copy()
print(f"Copied Nested List: {copied_nested}")

# Accessing nested elements
print(f"First element of first list: {nList[0][0]}")
print(f"Second element of second list: {nList[1][1]}")
