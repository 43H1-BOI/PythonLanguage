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
# Output: Set1 after add(6): {1, 2, 3, 4, 5, 6}

# update() - adds multiple elements
set1.update([7, 8, 9])
print(f"Set1 after update([7, 8, 9]): {set1}")
# Output: Set1 after update([7, 8, 9]): {1, 2, 3, 4, 5, 6, 7, 8, 9}

# remove() - removes element (raises error if not found)
set1.remove(9)
print(f"Set1 after remove(9): {set1}")
# Output: Set1 after remove(9): {1, 2, 3, 4, 5, 6, 7, 8}

# discard() - removes element (no error if not found)
set1.discard(10)
print(f"Set1 after discard(10): {set1}")
# Output: Set1 after discard(10): {1, 2, 3, 4, 5, 6, 7, 8}

# pop() - removes and returns random element
removed = set2.pop()
print(f"Set2 after pop(): {set2}, Removed: {removed}")
# Output: Set2 after pop(): {4, 5, 6, 7}, Removed: 8 (or any random element)

print("\n--- Set Operations ---")

# Union - combines all elements from both sets
print(f"Union using | operator: {set1 | set2}")
# Output: Union using | operator: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection - common elements in both sets
print(f"Intersection using & operator: {set1 & set2}")
# Output: Intersection using & operator: {4, 5, 6, 7, 8}

# Difference - elements in first set but not in second
print(f"Difference using - operator: {set1 - set2}")
# Output: Difference using - operator: {1, 2, 3}

# Symmetric Difference - elements in either set but not in both
print(f"Symmetric Difference using ^ operator: {set1 ^ set2}")
# Output: Symmetric Difference using ^ operator: {1, 2, 3, 8}

print("\n--- Set Comparisons ---")

# issubset() - checks if all elements of one set are in another
subset_test = {1, 2}
print(f"Is {subset_test} subset of Set1? {subset_test.issubset(set1)}")
# Output: Is {1, 2} subset of Set1? True

# issuperset() - checks if set contains all elements of another
print(f"Is Set1 superset of {subset_test}? {set1.issuperset(subset_test)}")
# Output: Is Set1 superset of {1, 2}? True

# isdisjoint() - checks if two sets have no common elements
print(f"Are Set1 and Set4 disjoint? {set1.isdisjoint(set4)}")
# Output: Are Set1 and Set4 disjoint? False

print("\n--- Operations on All Four Sets ---")

# Union of all four sets
print(f"Union of all four sets: {set1.union(set2, set3, set4)}")
# Output: Union of all four sets: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} (based on modified sets)

# Intersection of all four sets
print(f"Intersection of all four sets: {set1.intersection(set2, set3, set4)}")
# Output: Intersection of all four sets: set() or small intersection (depends on set2 after pop)

# Multiple operations
print(f"(Set1 | Set2) & (Set3 | Set4): {(set1 | set2) & (set3 ^ set4)}")
# Output: (Set1 | Set2) & (Set3 ^ Set4): varies based on modified set1 and set2

print(f"Set1 - Set2 - Set3: {set1 - set2 - set3}")
# Output: Set1 - Set2 - Set3: varies based on modified set1 (likely {2, 8} or similar)

# Membership test
print(f"Is 5 in Set1? {5 in set1}")
# Output: Is 5 in Set1? True

print(f"Is 15 in Set2? {15 in set2}")
# Output: Is 15 in Set2? False

# Length of sets
print(f"Lengths - Set1: {len(set1)}, Set2: {len(set2)}, Set3: {len(set3)}, Set4: {len(set4)}")
# Output: Lengths - Set1: 8 (modified), Set2: 4 (after pop), Set3: 5, Set4: 5