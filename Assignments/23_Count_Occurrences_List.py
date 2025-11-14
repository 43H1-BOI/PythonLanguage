list1 = [1, 2, 3, 4, 2, 5, 2, 6, 7, 2]

element = 2

# using count method
count = list1.count(element)
print(f"Element {element} occurs {count} times")

# using loop
count_loop = 0
for item in list1:
    if item == element:
        count_loop += 1
print(f"Using loop: Element {element} occurs {count_loop} times")
