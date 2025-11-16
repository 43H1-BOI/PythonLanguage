print("Set Methods and Operations on Four Different Sets")

# Creating four different sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {1, 3, 5, 7, 9}
set4 = {2, 4, 6, 8, 10}

print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Set3: {set3}")
print(f"Set4: {set4}")

print("\n--- Set Methods ---")

# add() - adds single element
set1.add(6)
print(f"Set1 after add(6): {set1}")

# update() - adds multiple elements
set1.update([7, 8, 9])
print(f"Set1 after update([7, 8, 9]): {set1}")

# remove() - removes element (raises error if not found)
set1.remove(9)
print(f"Set1 after remove(9): {set1}")

# discard() - removes element (no error if not found)
set1.discard(10)
print(f"Set1 after discard(10): {set1}")

# pop() - removes and returns random element
removed = set2.pop()
print(f"Set2 after pop(): {set2}, Removed: {removed}")

# clear() - removes all elements
temp_set = {1, 2, 3}
temp_set.clear()
print(f"Temp set after clear(): {temp_set}")

# copy() - creates shallow copy
copied_set = set3.copy()
print(f"Copied Set3: {copied_set}")

print("\n--- Set Operations ---")

# Union - combines all elements from both sets
union_result = set1.union(set2)
print(f"Union of Set1 and Set2: {union_result}")

# Using | operator
union_operator = set1 | set2
print(f"Union using | operator: {union_operator}")

# Intersection - common elements in both sets
intersection_result = set1.intersection(set2)
print(f"Intersection of Set1 and Set2: {intersection_result}")

# Using & operator
intersection_operator = set1 & set2
print(f"Intersection using & operator: {intersection_operator}")

# Difference - elements in first set but not in second
difference_result = set1.difference(set2)
print(f"Difference Set1 - Set2: {difference_result}")

# Using - operator
difference_operator = set1 - set2
print(f"Difference using - operator: {difference_operator}")

# Symmetric Difference - elements in either set but not in both
sym_diff_result = set1.symmetric_difference(set2)
print(f"Symmetric Difference Set1 and Set2: {sym_diff_result}")

# Using ^ operator
sym_diff_operator = set1 ^ set2
print(f"Symmetric Difference using ^ operator: {sym_diff_operator}")

print("\n--- Set Comparisons ---")

# issubset() - checks if all elements of one set are in another
subset_test = {1, 2}
print(f"Is {subset_test} subset of Set1? {subset_test.issubset(set1)}")

# issuperset() - checks if set contains all elements of another
print(f"Is Set1 superset of {subset_test}? {set1.issuperset(subset_test)}")

# isdisjoint() - checks if two sets have no common elements
print(f"Are Set1 and Set4 disjoint? {set1.isdisjoint(set4)}")

print("\n--- Operations on All Four Sets ---")

# Union of all four sets
all_union = set1.union(set2, set3, set4)
print(f"Union of all four sets: {all_union}")

# Intersection of all four sets
all_intersection = set1.intersection(set2, set3, set4)
print(f"Intersection of all four sets: {all_intersection}")

# Multiple operations
result1 = (set1 | set2) & (set3 | set4)
print(f"(Set1 | Set2) & (Set3 | Set4): {result1}")

result2 = set1 - set2 - set3
print(f"Set1 - Set2 - Set3: {result2}")

# Membership test
print(f"Is 5 in Set1? {5 in set1}")
print(f"Is 15 in Set2? {15 in set2}")

# Length of sets
print(f"Length of Set1: {len(set1)}")
print(f"Length of Set2: {len(set2)}")
print(f"Length of Set3: {len(set3)}")
print(f"Length of Set4: {len(set4)}")
