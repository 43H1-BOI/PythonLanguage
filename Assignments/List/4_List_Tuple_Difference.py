print("Difference Between List and Tuple")
print("=" * 50)

print("\n1. MUTABILITY")
print("-" * 50)
print("List: Mutable (can be modified)")
my_list = [1, 2, 3, 4, 5]
print(f"Original List: {my_list}")
my_list[0] = 10
my_list.append(6)
print(f"Modified List: {my_list}")

print("\nTuple: Immutable (cannot be modified)")
my_tuple = (1, 2, 3, 4, 5)
print(f"Original Tuple: {my_tuple}")
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error when trying to modify: {e}")

print("\n2. SYNTAX")
print("-" * 50)
print("List: Uses square brackets []")
list_example = [1, 2, 3]
print(f"List: {list_example}, Type: {type(list_example)}")

print("\nTuple: Uses parentheses ()")
tuple_example = (1, 2, 3)
print(f"Tuple: {tuple_example}, Type: {type(tuple_example)}")

print("\n3. METHODS")
print("-" * 50)
print("List: Has many methods (append, insert, remove, etc.)")
list_methods = [method for method in dir(list) if not method.startswith('_')]
print(f"List methods: {list_methods}")

print("\nTuple: Has only 2 methods (count, index)")
tuple_methods = [method for method in dir(tuple) if not method.startswith('_')]
print(f"Tuple methods: {tuple_methods}")

print("\n4. PERFORMANCE")
print("-" * 50)
print("List: Slower due to mutability")
print("Tuple: Faster due to immutability")

import sys
list_size = sys.getsizeof([1, 2, 3, 4, 5])
tuple_size = sys.getsizeof((1, 2, 3, 4, 5))
print(f"Size of list [1,2,3,4,5]: {list_size} bytes")
print(f"Size of tuple (1,2,3,4,5): {tuple_size} bytes")

print("\n5. USE CASES")
print("-" * 50)
print("List: Used when data needs to be modified")
print("Example: Shopping cart items")
shopping_cart = ["apple", "banana"]
shopping_cart.append("orange")
print(f"Shopping cart: {shopping_cart}")

print("\nTuple: Used for fixed data that shouldn't change")
print("Example: Coordinates, RGB colors")
coordinates = (10, 20)
rgb_color = (255, 0, 0)
print(f"Coordinates: {coordinates}")
print(f"RGB Color: {rgb_color}")

print("\n6. ITERATION")
print("-" * 50)
print("Both support iteration:")
print("List iteration:")
for item in [1, 2, 3]:
    print(item, end=" ")

print("\n\nTuple iteration:")
for item in (4, 5, 6):
    print(item, end=" ")

print("\n\n7. NESTING")
print("-" * 50)
print("Both support nesting:")
nested_list = [[1, 2], [3, 4]]
nested_tuple = ((1, 2), (3, 4))
print(f"Nested List: {nested_list}")
print(f"Nested Tuple: {nested_tuple}")

print("\n8. KEY DIFFERENCES SUMMARY")
print("=" * 50)
print("| Feature      | List          | Tuple         |")
print("|--------------|---------------|---------------|")
print("| Mutable      | Yes           | No            |")
print("| Syntax       | []            | ()            |")
print("| Performance  | Slower        | Faster        |")
print("| Memory       | More          | Less          |")
print("| Methods      | Many          | 2 (count,index)|")
print("| Use Case     | Dynamic data  | Fixed data    |")
