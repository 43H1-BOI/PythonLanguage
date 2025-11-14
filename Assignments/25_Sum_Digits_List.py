list1 = [123, 456, 789]

total = 0
for num in list1:
    # convert number to string and iterate through digits
    for digit in str(num):
        total += int(digit)

print(f"List: {list1}")
print(f"Sum of all digits: {total}")

# alternative approach
total_alt = sum(int(digit) for num in list1 for digit in str(num))
print(f"Using comprehension: {total_alt}")
