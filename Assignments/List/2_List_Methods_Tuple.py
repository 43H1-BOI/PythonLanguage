print("TUPLE AND LIST METHODS WITH NESTED STRUCTURES")
print("=" * 50)

# Sample data structures
num = (10, 20, 30, 20, 40, 30, 50)
stringT = ("apple", "banana", "cherry", "apple")
nestedT = ((1, 2), [3, 4], (5, 6))

print(f"Numeric tuple: {num}")
# Output: (10, 20, 30, 20, 40, 30, 50)

# Tuple Methods
print("\n1. Tuple Methods:")
print(f"Count of 20 in tuple: {num.count(20)}")
# Output: Count of 20 in tuple: 2

print(f"Index of 30 in tuple: {num.index(30)}")
# Output: Index of 30 in tuple: 2

print(f"Count of 'apple': {stringT.count('apple')}")
# Output: Count of 'apple': 2

# Built-in Functions
print("\n2. Built-in Functions:")
print(f"Length tuple: {len(num)}")
# Output: Length tuple: 7

print(f"Max tuple: {max(num)}, Min tuple: {min(num)}")
# Output: Max tuple: 50, Min tuple: 10

print(f"Sum tuple: {sum(num)}")
# Output: Sum tuple: 200


# Operations
print("\n3. Operations:")
tuple1 = (1, 2, 3)
list1 = [1, 2, 3]
print(f"Tuple concatenation: {tuple1 + (4, 5)}")
# Output: Tuple concatenation: (1, 2, 3, 4, 5)

print(f"List concatenation: {list1 + [4, 5]}")
# Output: List concatenation: [1, 2, 3, 4, 5]

print(f"Tuple repetition: {tuple1 * 2}")
# Output: Tuple repetition: (1, 2, 3, 1, 2, 3)

print(f"List repetition: {list1 * 2}")
# Output: List repetition: [1, 2, 3, 1, 2, 3]

# Indexing and Slicing
print("\n4. Indexing and Slicing:")
sample_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Tuple slice [2:5]: {sample_tuple[2:5]}")
# Output: Tuple slice [2:5]: (2, 3, 4)

print(f"List slice [2:5]: {sample_list[2:5]}")
# Output: List slice [2:5]: [2, 3, 4]

print(f"Tuple step [::2]: {sample_tuple[::2]}")
# Output: Tuple step [::2]: (0, 2, 4, 6, 8)

print(f"List step [::2]: {sample_list[::2]}")
# Output: List step [::2]: [0, 2, 4, 6, 8]

# Nested Structures
print("\n5. Nested Structures:")
print(f"Access nestedT[0][1]: {nestedT[0][1]}")
# Output: Access nestedT[0][1]: 2

print(f"Access nestedT[1][0]: {nestedT[1][0]}")
# Output: Access nestedT[1][0]: 3

# Conversions
print("\n6. Conversions:")
print(f"List to tuple: {tuple([1, 2, 3])}")
# Output: List to tuple: (1, 2, 3)

print(f"Tuple to list: {list((1, 2, 3))}")
# Output: Tuple to list: [1, 2, 3]

print(f"String to tuple: {tuple('hello')}")
# Output: String to tuple: ('h', 'e', 'l', 'l', 'o')

print(f"String to list: {list('hello')}")
# Output: String to list: ['h', 'e', 'l', 'l', 'o']

print(f"List to String : {"".join(list('hello'))}")


# Unpacking
print("\n7. Unpacking:")
x, y = (10, 20)
print(f"Tuple unpacking: x={x}, y={y}")
# Output: Tuple unpacking: x=10, y=20

a, b = [30, 40]
print(f"List unpacking: a={a}, b={b}")
# Output: List unpacking: a=30, b=40

first, *middle, last = (1, 2, 3, 4, 5)
print(f"Extended unpacking: first={first}, middle={middle}, last={last}")
# Output: Extended unpacking: first=1, middle=[2, 3, 4], last=5

# Generation
print("\n8. Generation:")
squares_tuple = tuple(x**2 for x in range(1, 5))
squares_list = [x**2 for x in range(1, 5)]
print(f"Generated tuple: {squares_tuple}")
# Output: Generated tuple: (1, 4, 9, 16)

print(f"Generated list: {squares_list}")
# Output: Generated list: [1, 4, 9, 16]

combined = tuple(zip(("A", "B"), [1, 2]))
print(f"Zipped tuple-list: {combined}")
# Output: Zipped tuple-list: (('A', 1), ('B', 2))

# Advanced Nested Operations
print("\n9. Advanced Nested:")
complex_nested = [(1, 2), (3, [4, 5]), ([6, 7], (8, 9))]
print(f"Complex nested: {complex_nested}")
# Output: Complex nested: [(1, 2), (3, [4, 5]), ([6, 7], (8, 9))]

print(f"Deep access: {complex_nested[1][1][0]}")
# Output: Deep access: 4

print(f"Deep access: {complex_nested[2][0][1]}")
# Output: Deep access: 7

# Comparison
print("\n10. Comparison:")
print(f"Tuple vs Tuple: (1,2,3) == (1,2,3) = {(1,2,3) == (1,2,3)}")
# Output: Tuple vs Tuple: (1,2,3) == (1,2,3) = True

print(f"List vs List: [1,2,3] == [1,2,3] = {[1,2,3] == [1,2,3]}")
# Output: List vs List: [1,2,3] == [1,2,3] = True

print(f"Tuple vs List: (1,2,3) == [1,2,3] = {(1,2,3) == [1,2,3]}")
# Output: Tuple vs List: (1,2,3) == [1,2,3] = False

print("\nAll methods demonstrated!")
# Output: All methods demonstrated!
