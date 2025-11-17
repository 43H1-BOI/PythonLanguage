print("String Operations")
# Output: String Operations

print("=" * 70)
# Output: ======================================================================

# A. SLICING
print("\nA. SLICING")
# Output: A. SLICING

print("-" * 70)
# Output: ----------------------------------------------------------------------

text = "Hello World Python"
print(f"Original String: {text}")
# Output: Original String: Hello World Python

# Basic slicing
print(f"text[0:5]: {text[0:5]}")
# Output: text[0:5]: Hello

print(f"text[6:11]: {text[6:11]}")
# Output: text[6:11]: World

print(f"text[-6:]: {text[-6:]}")
# Output: text[-6:]: Python

# Step slicing
print(f"text[::2]: {text[::2]}")
# Output: text[::2]: HloWrdPto

# Reverse string
print(f"text[::-1]: {text[::-1]}")
# Output: text[::-1]: nohtyP dlroW olleH

# B. MEMBERSHIP OPERATOR
print("\n\nB. MEMBERSHIP OPERATOR")
# Output: B. MEMBERSHIP OPERATOR

print("-" * 70)
# Output: ----------------------------------------------------------------------

sentence = "Python is a powerful programming language"
print(f"String: {sentence}")
# Output: String: Python is a powerful programming language

# in and not in operators
print(f"'Python' in sentence: {'Python' in sentence}")
# Output: 'Python' in sentence: True

print(f"'Java' not in sentence: {'Java' not in sentence}")
# Output: 'Java' not in sentence: True

# Case sensitive check
print(f"'python' in sentence: {'python' in sentence}")
# Output: 'python' in sentence: False

# C. CONCATENATION
print("\n\nC. CONCATENATION")
# Output: C. CONCATENATION

print("-" * 70)
# Output: ----------------------------------------------------------------------

str1 = "Hello"
str2 = "World"

# Using + operator
print(f"str1 + ' ' + str2: {str1 + ' ' + str2}")
# Output: str1 + ' ' + str2: Hello World

# Using += operator
message = "Python"
message += " is awesome"
print(f"Using +=: {message}")
# Output: Using +=: Python is awesome

# Repetition and join
print(f"str1 * 3: {str1 * 3}")
# Output: str1 * 3: HelloHelloHello

words = ["Python", "is", "fun"]
print(f"' '.join({words}): {' '.join(words)}")
# Output: ' '.join(['Python', 'is', 'fun']): Python is fun

# D. MULTILINE STRING
print("\n\nD. MULTILINE STRING")
# Output: D. MULTILINE STRING

print("-" * 70)
# Output: ----------------------------------------------------------------------

# Using triple quotes
multiline1 = """This is a multiline string.
It spans multiple lines.
Python makes it easy!"""
print("Triple quotes:")
# Output: Triple quotes:

print(multiline1)
# Output: This is a multiline string.
# Output: It spans multiple lines.
# Output: Python makes it easy!

# Escape sequences
multiline2 = "Line 1\nLine 2\nLine 3"
print("\nUsing \\n:")
# Output: Using \n:

print(multiline2)
# Output: Line 1
# Output: Line 2
# Output: Line 3

# Formatted multiline
name = "John"
age = 25
multiline3 = f"""Name: {name}
Age: {age}
Status: Active"""
print("\nFormatted multiline:")
# Output: Formatted multiline:

print(multiline3)
# Output: Name: John
# Output: Age: 25
# Output: Status: Active

print("\n" + "=" * 50)
# Output: ==================================================

print("\nCOMBINED OPERATIONS")
# Output: COMBINED OPERATIONS

# Example combining operations
original = "Python Programming"
sliced = original[0:6]
concatenated = sliced + " is awesome"
print(f"Original: {original}")
# Output: Original: Python Programming

print(f"Sliced: {sliced}")
# Output: Sliced: Python

print(f"Concatenated: {concatenated}")
# Output: Concatenated: Python is awesome
