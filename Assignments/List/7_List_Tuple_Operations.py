print("Operations on List and Tuple")
print("=" * 70)

# a. Repetition Operator
print("\na. REPETITION OPERATOR")
print("-" * 70)

list1 = [1, 2, 3]
print(f"Original List: {list1}")
repeated_list = list1 * 3
print(f"List * 3 = {repeated_list}")

tuple1 = (4, 5, 6)
print(f"\nOriginal Tuple: {tuple1}")
repeated_tuple = tuple1 * 4
print(f"Tuple * 4 = {repeated_tuple}")

# b. Iteration
print("\n\nb. ITERATION")
print("-" * 70)

print("Iterating through list:")
for item in [10, 20, 30, 40]:
    print(f"Item: {item}")

print("\nIterating through tuple:")
for item in (50, 60, 70, 80):
    print(f"Item: {item}")

print("\nIterating with index (enumerate):")
my_list = ["apple", "banana", "cherry"]
for index, item in enumerate(my_list):
    print(f"Index {index}: {item}")

print("\nIterating through tuple with index:")
my_tuple = ("red", "green", "blue")
for index, item in enumerate(my_tuple):
    print(f"Index {index}: {item}")

# c. Concatenation
print("\n\nc. CONCATENATION")
print("-" * 70)

list_a = [1, 2, 3]
list_b = [4, 5, 6]
concatenated_list = list_a + list_b
print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"Concatenated: {concatenated_list}")

tuple_a = (7, 8, 9)
tuple_b = (10, 11, 12)
concatenated_tuple = tuple_a + tuple_b
print(f"\nTuple A: {tuple_a}")
print(f"Tuple B: {tuple_b}")
print(f"Concatenated: {concatenated_tuple}")

# d. Copy Method
print("\n\nd. COPY METHOD")
print("-" * 70)

original_list = [1, 2, 3, 4, 5]
print(f"Original List: {original_list}")

# Shallow copy using copy()
copied_list = original_list.copy()
print(f"Copied List: {copied_list}")

# Modify copied list
copied_list[0] = 100
print(f"Modified Copied List: {copied_list}")
print(f"Original List unchanged: {original_list}")

# Copy using slicing
slice_copy = original_list[:]
print(f"Copy using slicing: {slice_copy}")

# Copy using list()
list_copy = list(original_list)
print(f"Copy using list(): {list_copy}")

print("\nTuple doesn't have copy() method:")
original_tuple = (1, 2, 3, 4, 5)
print(f"Original Tuple: {original_tuple}")

# Copy tuple using slicing
tuple_copy = original_tuple[:]
print(f"Tuple copy using slicing: {tuple_copy}")

# Copy using tuple()
tuple_copy2 = tuple(original_tuple)
print(f"Tuple copy using tuple(): {tuple_copy2}")

# e. Arrange in Ascending and Descending Order
print("\n\ne. SORTING (ASCENDING AND DESCENDING)")
print("-" * 70)

unsorted_list = [5, 2, 8, 1, 9, 3]
print(f"Unsorted List: {unsorted_list}")

# Sort in ascending order (modifies original)
sorted_list_asc = unsorted_list.copy()
sorted_list_asc.sort()
print(f"Ascending order (using sort()): {sorted_list_asc}")

# Sort in descending order
sorted_list_desc = unsorted_list.copy()
sorted_list_desc.sort(reverse=True)
print(f"Descending order (using sort(reverse=True)): {sorted_list_desc}")

# Using sorted() - returns new list
sorted_new = sorted(unsorted_list)
print(f"Ascending (using sorted()): {sorted_new}")
print(f"Original list unchanged: {unsorted_list}")

print("\nSorting Tuple:")
unsorted_tuple = (7, 3, 9, 1, 5, 2)
print(f"Unsorted Tuple: {unsorted_tuple}")

# Tuple doesn't have sort(), use sorted()
sorted_tuple_asc = tuple(sorted(unsorted_tuple))
print(f"Ascending order: {sorted_tuple_asc}")

sorted_tuple_desc = tuple(sorted(unsorted_tuple, reverse=True))
print(f"Descending order: {sorted_tuple_desc}")

print(f"Original tuple unchanged: {unsorted_tuple}")

print("\n\nSORTING STRING LISTS/TUPLES")
print("-" * 70)

string_list = ["banana", "apple", "cherry", "date"]
print(f"Unsorted: {string_list}")

string_list.sort()
print(f"Ascending: {string_list}")

string_list.sort(reverse=True)
print(f"Descending: {string_list}")

string_tuple = ("zebra", "ant", "cat", "dog")
print(f"\nUnsorted Tuple: {string_tuple}")
print(f"Ascending: {tuple(sorted(string_tuple))}")
print(f"Descending: {tuple(sorted(string_tuple, reverse=True))}")
