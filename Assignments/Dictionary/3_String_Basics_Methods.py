print("String Basics and Methods")
print("=" * 70)

# STRING BASICS
print("\nSTRING BASICS")
print("-" * 70)

# Creating strings
str1 = "Hello"
str2 = 'World'
str3 = """Multiline
String"""

print(f"String 1: {str1}")
print(f"String 2: {str2}")
print(f"String 3: {str3}")

# String indexing
text = "Python"
print(f"\nString: {text}")
print(f"text[0]: {text[0]}")
print(f"text[-1]: {text[-1]}")

# String is immutable
print(f"\nStrings are immutable")

print("\n" + "=" * 70)
print("\nSTRING METHODS")
print("-" * 70)

sample = "  Hello World Python  "
print(f"Original: '{sample}'")

# upper() - converts to uppercase
print(f"\nupper(): {sample.upper()}")

# lower() - converts to lowercase
print(f"lower(): {sample.lower()}")

# capitalize() - capitalizes first character
print(f"capitalize(): {sample.capitalize()}")

# title() - capitalizes first letter of each word
print(f"title(): {sample.title()}")

# strip() - removes leading and trailing whitespace
print(f"strip(): '{sample.strip()}'")

# lstrip() - removes leading whitespace
print(f"lstrip(): '{sample.lstrip()}'")

# rstrip() - removes trailing whitespace
print(f"rstrip(): '{sample.rstrip()}'")

# replace() - replaces substring
print(f"replace('World', 'Universe'): {sample.replace('World', 'Universe')}")

# split() - splits string into list
print(f"split(): {sample.split()}")

# join() - joins list into string
words = ["Python", "is", "awesome"]
print(f"' '.join({words}): {' '.join(words)}")

# find() - returns index of first occurrence
text2 = "Hello World"
print(f"\nString: {text2}")
print(f"find('World'): {text2.find('World')}")
print(f"find('Python'): {text2.find('Python')}")

# index() - returns index of first occurrence (raises error if not found)
print(f"index('World'): {text2.index('World')}")

# count() - counts occurrences
text3 = "hello hello world"
print(f"\nString: {text3}")
print(f"count('hello'): {text3.count('hello')}")

# startswith() - checks if string starts with substring
print(f"\nstartswith('hello'): {text3.startswith('hello')}")
print(f"startswith('world'): {text3.startswith('world')}")

# endswith() - checks if string ends with substring
print(f"endswith('world'): {text3.endswith('world')}")
print(f"endswith('hello'): {text3.endswith('hello')}")

# isalpha() - checks if all characters are alphabetic
print(f"\n'Hello'.isalpha(): {'Hello'.isalpha()}")
print(f"'Hello123'.isalpha(): {'Hello123'.isalpha()}")

# isdigit() - checks if all characters are digits
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'123abc'.isdigit(): {'123abc'.isdigit()}")

# isalnum() - checks if all characters are alphanumeric
print(f"'Hello123'.isalnum(): {'Hello123'.isalnum()}")
print(f"'Hello 123'.isalnum(): {'Hello 123'.isalnum()}")

# isspace() - checks if all characters are whitespace
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'Hello'.isspace(): {'Hello'.isspace()}")

# islower() - checks if all characters are lowercase
print(f"'hello'.islower(): {'hello'.islower()}")
print(f"'Hello'.islower(): {'Hello'.islower()}")

# isupper() - checks if all characters are uppercase
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")
print(f"'Hello'.isupper(): {'Hello'.isupper()}")

# swapcase() - swaps case of characters
text4 = "Hello World"
print(f"\n'{text4}'.swapcase(): {text4.swapcase()}")

# center() - centers string with padding
text5 = "Python"
print(f"\n'{text5}'.center(20, '*'): {text5.center(20, '*')}")

# ljust() - left justifies string
print(f"'{text5}'.ljust(20, '*'): {text5.ljust(20, '*')}")

# rjust() - right justifies string
print(f"'{text5}'.rjust(20, '*'): {text5.rjust(20, '*')}")

# zfill() - pads string with zeros
number = "42"
print(f"\n'{number}'.zfill(5): {number.zfill(5)}")

# partition() - splits string at first occurrence
text6 = "Hello-World-Python"
print(f"\n'{text6}'.partition('-'): {text6.partition('-')}")

# splitlines() - splits at line breaks
text7 = "Line1\nLine2\nLine3"
print(f"\n'Line1\\nLine2\\nLine3'.splitlines(): {text7.splitlines()}")

# format() - formats string
template = "Name: {}, Age: {}"
print(f"\ntemplate.format('John', 25): {template.format('John', 25)}")

# f-strings (formatted string literals)
name = "Alice"
age = 30
print(f"\nf-string: Name is {name} and age is {age}")

# String concatenation
str_a = "Hello"
str_b = "World"
print(f"\n'{str_a}' + ' ' + '{str_b}': {str_a + ' ' + str_b}")

# String repetition
print(f"'*' * 10: {'*' * 10}")

# String length
print(f"\nlen('Python'): {len('Python')}")

# Checking membership
print(f"'Py' in 'Python': {'Py' in 'Python'}")
print(f"'Java' in 'Python': {'Java' in 'Python'}")
