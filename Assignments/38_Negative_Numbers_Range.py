start = -10
end = 10

print(f"Negative numbers from {start} to {end}:")

# using loop
for num in range(start, end + 1):
    if num < 0:
        print(num, end=" ")

print("\n")

# using list comprehension
negative_range = [num for num in range(start, end + 1) if num < 0]
print(f"Using comprehension: {negative_range}")

# starting from start if range includes positives
if end >= 0:
    negative_direct = list(range(start, 0))
    print(f"Direct range: {negative_direct}")

