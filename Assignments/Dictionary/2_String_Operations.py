print("String Operations")
print("=" * 70)

# A. SLICING
print("\nA. SLICING")
print("-" * 70)

text = "Hello World Python"
print(f"Original String: {text}")

# Basic slicing
print(f"text[0:5]: {text[0:5]}")
print(f"text[6:11]: {text[6:11]}")
print(f"text[12:]: {text[12:]}")
print(f"text[:5]: {text[:5]}")

# Negative indexing
print(f"text[-6:]: {text[-6:]}")
print(f"text[:-7]: {text[:-7]}")

# Step slicing
print(f"text[::2]: {text[::2]}")
print(f"text[::3]: {text[::3]}")

# Reverse string
print(f"text[::-1]: {text[::-1]}")

# Slicing with step and negative index
print(f"text[0:10:2]: {text[0:10:2]}")

# B. MEMBERSHIP OPERATOR
print("\n\nB. MEMBERSHIP OPERATOR")
print("-" * 70)

sentence = "Python is a powerful programming language"
print(f"String: {sentence}")

# in operator
print(f"'Python' in sentence: {'Python' in sentence}")
print(f"'Java' in sentence: {'Java' in sentence}")
print(f"'powerful' in sentence: {'powerful' in sentence}")

# not in operator
print(f"'Java' not in sentence: {'Java' not in sentence}")
print(f"'Python' not in sentence: {'Python' not in sentence}")

# Case sensitive check
print(f"'python' in sentence: {'python' in sentence}")
print(f"'PYTHON' in sentence: {'PYTHON' in sentence}")

# C. CONCATENATION
print("\n\nC. CONCATENATION")
print("-" * 70)

str1 = "Hello"
str2 = "World"
str3 = "Python"

# Using + operator
concatenated = str1 + " " + str2
print(f"str1 + ' ' + str2: {concatenated}")

# Multiple concatenation
result = str1 + " " + str2 + " " + str3
print(f"str1 + ' ' + str2 + ' ' + str3: {result}")

# Using += operator
message = "Python"
message += " is"
message += " awesome"
print(f"Using +=: {message}")

# Concatenation with repetition
repeated = str1 * 3
print(f"str1 * 3: {repeated}")

# Using join()
words = ["Python", "is", "fun"]
joined = " ".join(words)
print(f"' '.join({words}): {joined}")

# Concatenating with numbers (need conversion)
name = "Age"
age = 25
result = name + " is " + str(age)
print(f"String + number: {result}")

# D. MULTILINE STRING
print("\n\nD. MULTILINE STRING")
print("-" * 70)

# Using triple quotes
multiline1 = """This is a multiline string.
It spans multiple lines.
Python makes it easy!"""
print("Using triple double quotes:")
print(multiline1)

# Using triple single quotes
multiline2 = '''Another way to create
multiline strings is using
triple single quotes.'''
print("\nUsing triple single quotes:")
print(multiline2)

# Multiline with indentation
multiline3 = """
Line 1
    Line 2 (indented)
        Line 3 (more indented)
Line 4
"""
print("\nWith indentation:")
print(multiline3)

# Multiline string with escape sequences
multiline4 = "Line 1\nLine 2\nLine 3"
print("\nUsing \\n:")
print(multiline4)

# Formatted multiline string
name = "John"
age = 25
multiline5 = f"""
Name: {name}
Age: {age}
Description: This is a formatted
             multiline string.
"""
print("\nFormatted multiline:")
print(multiline5)

# Preserving quotes in multiline
multiline6 = """He said, "Hello World!"
She replied, 'Hi there!'"""
print("\nWith quotes:")
print(multiline6)

print("\n" + "=" * 70)
print("\nALL OPERATIONS COMBINED")
print("-" * 70)

# Example combining all operations
original = "Python Programming"
sliced = original[0:6]
check = "Python" in original
concatenated = sliced + " is awesome"
multiline_result = f"""
Original: {original}
Sliced: {sliced}
Contains 'Python': {check}
Concatenated: {concatenated}
"""
print(multiline_result)
