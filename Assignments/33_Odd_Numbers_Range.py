start = 1
end = 20

print(f"Odd numbers from {start} to {end}:")

# using loop
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=" ")

print("\n")

# using range with step
odd_range = list(range(1, end + 1, 2))
print(f"Using range step: {odd_range}")

# using list comprehension
odd_comp = [num for num in range(start, end + 1) if num % 2 != 0]
print(f"Using comprehension: {odd_comp}")

