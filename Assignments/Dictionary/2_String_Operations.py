print("String Operations")
print("=" * 70)

# A. SLICING
print("\nA. SLICING")

text = "Hello World Python"
print(f"Original String: {text}")

# Basic slicing
print(f"text[0:5]: {text[0:5]}")  # Output: Hello
print(f"text[6:11]: {text[6:11]}")  # Output: World
print(f"text[-6:]: {text[-6:]}")  # Output: Python

# Step slicing
print(f"text[::2]: {text[::2]}")  # Output: HloWrdPto

# Reverse string
print(f"text[::-1]: {text[::-1]}")  # Output: nohtyP dlroW olleH

# B. MEMBERSHIP OPERATOR
print("\n\nB. MEMBERSHIP OPERATOR")

sentence = "Python is a powerful programming language"
print(f"String: {sentence}")

# in and not in operators
print(f"'Python' in sentence: {'Python' in sentence}")  # Output: True
print(f"'Java' not in sentence: {'Java' not in sentence}")  # Output: True

# Case sensitive check
print(f"'python' in sentence: {'python' in sentence}")  # Output: False

# C. CONCATENATION
print("\n\nC. CONCATENATION")

str1 = "Hello"
str2 = "World"

# Using + operator
print(f"str1 + ' ' + str2: {str1 + ' ' + str2}")  # Output: Hello World

# Using += operator
message = "Python"
message += " is awesome"
print(f"Using +=: {message}")  # Output: Python is awesome

# Repetition and join
print(f"str1 * 3: {str1 * 3}")  # Output: HelloHelloHello

words = ["Python", "is", "fun"]
print(f"' '.join({words}): {' '.join(words)}")  # Output: Python is fun

# D. MULTILINE STRING
print("\n\nD. MULTILINE STRING")

# Using triple quotes
multiline1 = """This is a multiline string.
It spans multiple lines.
Python makes it easy!"""
print("Triple quotes:")
print(multiline1)

# Escape sequences
multiline2 = "Line 1\nLine 2\nLine 3"
print("\nUsing \\n:")
print(multiline2)

# Formatted multiline
name = "John"
age = 25
multiline3 = f"""Name: {name}
Age: {age}
Status: Active"""
print("\nFormatted multiline:")
print(multiline3)

print("\n" + "=" * 50)
print("\nCOMBINED OPERATIONS")

# Example combining operations
original = "Python Programming"
sliced = original[0:6]
concatenated = sliced + " is awesome"
print(f"Original: {original}")  # Output: Python Programming
print(f"Sliced: {sliced}")  # Output: Python
print(f"Concatenated: {concatenated}")  # Output: Python is awesome
