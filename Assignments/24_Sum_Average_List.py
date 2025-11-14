list1 = [10, 20, 30, 40, 50]

# using built-in functions
total = sum(list1)
average = sum(list1) / len(list1)

print(f"List: {list1}")
print(f"Sum: {total}")
print(f"Average: {average}")

# using loop
total_loop = 0
for num in list1:
    total_loop += num
average_loop = total_loop / len(list1)

print(f"\nUsing loop:")
print(f"Sum: {total_loop}")
print(f"Average: {average_loop}")
