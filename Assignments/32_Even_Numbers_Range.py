start = 1
end = 20

print(f"Even numbers from {start} to {end}:")

# using loop
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=" ")

print("\n")

# using range with step
even_range = list(range(2, end + 1, 2))
print(f"Using range step: {even_range}")

# using list comprehension
even_comp = [num for num in range(start, end + 1) if num % 2 == 0]
print(f"Using comprehension: {even_comp}")

