list1 = [2, 3, 4, 5]

# using loop
product = 1
for num in list1:
    product *= num

print(f"List: {list1}")
print(f"Product of all numbers: {product}")

# using reduce
from functools import reduce
product_reduce = reduce(lambda x, y: x * y, list1)
print(f"Using reduce: {product_reduce}")
