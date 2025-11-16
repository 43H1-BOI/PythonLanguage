print("Sum and Average of List and Tuple Without Using Inbuilt Functions")

# List Example
list_data = [10, 20, 30, 40, 50]
print(f"List: {list_data}")

# Calculate sum without using sum()
list_sum = 0
for num in list_data:
    list_sum += num

print(f"Sum of list: {list_sum}")

# Calculate average without using sum() or len()
count = 0
for num in list_data:
    count += 1

list_average = list_sum / count
print(f"Average of list: {list_average}")

print("\n" + "-" * 50)

# Tuple Example
tuple_data = (15, 25, 35, 45, 55, 65)
print(f"Tuple: {tuple_data}")

# Calculate sum without using sum()
tuple_sum = 0
for num in tuple_data:
    tuple_sum += num

print(f"Sum of tuple: {tuple_sum}")

# Calculate average without using sum() or len()
count = 0
for num in tuple_data:
    count += 1

tuple_average = tuple_sum / count
print(f"Average of tuple: {tuple_average}")

print("\n" + "-" * 50)

# Using while loop for list
print("\nUsing while loop for list:")
list2 = [5, 10, 15, 20, 25]
print(f"List: {list2}")

sum_list2 = 0
count_list2 = 0
index = 0

while index < len(list2):
    sum_list2 += list2[index]
    count_list2 += 1
    index += 1

avg_list2 = sum_list2 / count_list2
print(f"Sum: {sum_list2}")
print(f"Average: {avg_list2}")

print("\n" + "-" * 50)

# Using while loop for tuple
print("\nUsing while loop for tuple:")
tuple2 = (100, 200, 300, 400, 500)
print(f"Tuple: {tuple2}")

sum_tuple2 = 0
count_tuple2 = 0
index = 0

while index < len(tuple2):
    sum_tuple2 += tuple2[index]
    count_tuple2 += 1
    index += 1

avg_tuple2 = sum_tuple2 / count_tuple2
print(f"Sum: {sum_tuple2}")
print(f"Average: {avg_tuple2}")

print("\n" + "-" * 50)

# Nested List
print("\nNested List Example:")
nested_list = [[10, 20], [30, 40], [50, 60]]
print(f"Nested List: {nested_list}")

total = 0
element_count = 0

for sublist in nested_list:
    for num in sublist:
        total += num
        element_count += 1

average = total / element_count
print(f"Sum: {total}")
print(f"Average: {average}")

print("\n" + "-" * 50)

# Nested Tuple
print("\nNested Tuple Example:")
nested_tuple = ((5, 10, 15), (20, 25, 30), (35, 40))
print(f"Nested Tuple: {nested_tuple}")

total = 0
element_count = 0

for subtuple in nested_tuple:
    for num in subtuple:
        total += num
        element_count += 1

average = total / element_count
print(f"Sum: {total}")
print(f"Average: {average}")
