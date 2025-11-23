Z = {1:"a",2:"b","d":4,(1,2,3):["a","b","c"],"abc":"xyz"}

print("Original:", Z)

# 1. ADD
Z['x'] = 'bdE'

# 2. DELETE
del Z['x']

# 3. GET
print(Z.get(2))

# 4. POPITEM
Z.popitem()
print(Z)

# 5. UPDATE
Z.update({3:"assa",22:"'"})

# 6. POP
Z.pop("d")