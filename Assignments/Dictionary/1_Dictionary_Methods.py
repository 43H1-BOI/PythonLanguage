print("All Dictionary Methods")
print("=" * 70)

# Creating a dictionary
my_dict = {"name": "Abhi", "age": 25, "city": "Indore"}
print(f"Original Dictionary: {my_dict}")

# get() - returns value for key
print(f"\nget('name'): {my_dict.get('name')}")  # Output: Abhi
print(f"get('country', 'India'): {my_dict.get('country', 'India')}")  # Output: India

# keys() - returns all keys
print(f"\nkeys(): {my_dict.keys()}")  # Output: dict_keys(['name', 'age', 'city'])

# values() - returns all values
print(f"values(): {my_dict.values()}")  # Output: dict_values(['Abhi', 25, 'Indore'])

# items() - returns all key-value pairs
print(f"items(): {my_dict.items()}")  # Output: dict_items([('name', 'Abhi'), ('age', 25), ('city', 'Indore')])

# update() - updates dictionary with key-value pairs
my_dict.update({"country": "India", "age": 26})
print(f"\nAfter update(): {my_dict}")  # Output: {'name': 'Abhi', 'age': 26, 'city': 'Indore', 'country': 'India'}

# pop() - removes and returns value for key
removed = my_dict.pop("country")
print(f"\nAfter pop('country'): {my_dict}")  # Output: {'name': 'Abhi', 'age': 26, 'city': 'Indore'}
print(f"Removed value: {removed}")  # Output: India

# popitem() - removes and returns last key-value pair
last_item = my_dict.popitem()
print(f"\nAfter popitem(): {my_dict}")  # Output: {'name': 'Abhi', 'age': 26}
print(f"Removed item: {last_item}")  # Output: ('city', 'Indore')

# setdefault() - returns value if key exists, else sets default
value = my_dict.setdefault("gender", "Male")
print(f"\nAfter setdefault('gender', 'Male'): {my_dict}")  # Output: {'name': 'Abhi', 'age': 26, 'gender': 'Male'}
print(f"Returned value: {value}")  # Output: Male

# copy() - creates shallow copy
copied_dict = my_dict.copy()
print(f"\nCopied dictionary: {copied_dict}")  # Output: {'name': 'Abhi', 'age': 26, 'gender': 'Male'}

# clear() - removes all items
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print(f"\nAfter clear(): {temp_dict}")  # Output: {}

# fromkeys() - creates dictionary from sequence
keys = ["x", "y", "z"]
new_dict = dict.fromkeys(keys, 0)
print(f"\nfromkeys({keys}, 0): {new_dict}")  # Output: {'x': 0, 'y': 0, 'z': 0}

print("\n" + "=" * 70)
print("\nADDITIONAL DICTIONARY OPERATIONS")

# Adding new key-value pair
my_dict["email"] = "Abhi@example.com"
print(f"After adding email: {my_dict}")  # Output: {'name': 'Abhi', 'age': 26, 'gender': 'Male', 'email': 'Abhi@example.com'}

# Updating existing value
my_dict["age"] = 27
print(f"After updating age: {my_dict}")  # Output: {'name': 'Abhi', 'age': 27, 'gender': 'Male', 'email': 'Abhi@example.com'}

# Deleting key using del
del my_dict["gender"]
print(f"After del my_dict['gender']: {my_dict}")  # Output: {'name': 'Abhi', 'age': 27, 'email': 'Abhi@example.com'}

# Checking if key exists
print(f"\n'name' in my_dict: {'name' in my_dict}")  # Output: True
print(f"'country' in my_dict: {'country' in my_dict}")  # Output: False

# Length of dictionary
print(f"\nlen(my_dict): {len(my_dict)}")  # Output: 3

# Iterating through dictionary
print("\nIterating through keys:")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")  # Output: name: Abhi, age: 27, email: Abhi@example.com

print("\nIterating through items:")
for key, value in my_dict.items():
    print(f"{key} = {value}")  # Output: name = Abhi, age = 27, email = Abhi@example.com

print("\n" + "=" * 70)
print("\nNESTED DICTIONARY")

nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25},
    "person3": {"name": "Charlie", "age": 35}
}

print(f"Nested Dictionary: {nested_dict}")

# Accessing nested values
print(f"\nperson1 name: {nested_dict['person1']['name']}")  # Output: Alice
print(f"person2 age: {nested_dict['person2']['age']}")  # Output: 25

# Updating nested value
nested_dict["person1"]["age"] = 31
print(f"\nAfter updating person1 age: {nested_dict}")

# Adding new nested dictionary
nested_dict["person4"] = {"name": "David", "age": 28}
print(f"\nAfter adding person4: {nested_dict}")

# Iterating through nested dictionary
print("\nIterating through nested dictionary:")
for person, details in nested_dict.items():
    print(f"{person}:")
    for key, value in details.items():
        print(f"  {key}: {value}")