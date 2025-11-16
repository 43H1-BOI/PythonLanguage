print("List Methods on Tuple and Nested Tuple")

# Single Tuple
single_tuple = (1, 2, 3, 4, 5, 3, 2)
print(f"Original Tuple: {single_tuple}")

# count() - returns number of occurrences
count = single_tuple.count(3)
print(f"Count of 3: {count}")

# index() - returns index of first occurrence
idx = single_tuple.index(4)
print(f"Index of 4: {idx}")

# len() - returns length of tuple
length = len(single_tuple)
print(f"Length of tuple: {length}")

# max() - returns maximum element
maximum = max(single_tuple)
print(f"Maximum element: {maximum}")

# min() - returns minimum element
minimum = min(single_tuple)
print(f"Minimum element: {minimum}")

# sum() - returns sum of elements
total = sum(single_tuple)
print(f"Sum of elements: {total}")

# sorted() - returns sorted list (tuple remains unchanged)
sorted_list = sorted(single_tuple)
print(f"Sorted (as list): {sorted_list}")
print(f"Original tuple unchanged: {single_tuple}")

# sorted(reverse=True) - returns sorted list in descending order
sorted_desc = sorted(single_tuple, reverse=True)
print(f"Sorted descending: {sorted_desc}")

# tuple() - converts list to tuple
list_data = [10, 20, 30]
new_tuple = tuple(list_data)
print(f"List converted to tuple: {new_tuple}")

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2
print(f"Concatenated tuples: {concatenated}")

# Repetition
repeated = tuple1 * 3
print(f"Repeated tuple: {repeated}")

# Membership
print(f"Is 2 in tuple1? {2 in tuple1}")
print(f"Is 10 in tuple1? {10 in tuple1}")

print("\n--- Nested Tuple ---")

# Nested Tuple
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (4, 5, 6))
print(f"Original Nested Tuple: {nested_tuple}")

# count() - counts occurrences of tuple
count = nested_tuple.count((4, 5, 6))
print(f"Count of (4, 5, 6): {count}")

# index() - returns index of tuple
idx = nested_tuple.index((7, 8, 9))
print(f"Index of (7, 8, 9): {idx}")

# len() - returns length
length = len(nested_tuple)
print(f"Length of nested tuple: {length}")

# Accessing elements
print(f"First tuple: {nested_tuple[0]}")
print(f"First element of first tuple: {nested_tuple[0][0]}")
print(f"Second element of third tuple: {nested_tuple[2][1]}")

# Slicing nested tuple
sliced = nested_tuple[1:3]
print(f"Sliced nested tuple [1:3]: {sliced}")

# sorted() - sorts nested tuples
sorted_nested = sorted(nested_tuple)
print(f"Sorted nested tuple: {sorted_nested}")

# Concatenation with nested tuples
nested1 = ((1, 2), (3, 4))
nested2 = ((5, 6), (7, 8))
concat_nested = nested1 + nested2
print(f"Concatenated nested tuples: {concat_nested}")

# Repetition with nested tuples
repeated_nested = nested1 * 2
print(f"Repeated nested tuple: {repeated_nested}")

# Converting nested tuple to list
nested_list = list(nested_tuple)
print(f"Nested tuple as list: {nested_list}")
