start = -10
end = 10

print(f"Positive numbers from {start} to {end}:")

# using loop
for num in range(start, end + 1):
    if num > 0:
        print(num, end=" ")

print("\n")

# using list comprehension
positive_range = [num for num in range(start, end + 1) if num > 0]
print(f"Using comprehension: {positive_range}")

# starting from 1 if range includes negatives
if start <= 0:
    positive_direct = list(range(1, end + 1))
    print(f"Direct range: {positive_direct}")

