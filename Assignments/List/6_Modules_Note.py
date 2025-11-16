print("Short Note on Modules")
print("=" * 70)

print("\nWHAT ARE MODULES?")
print("-" * 70)
print("Modules are Python files containing functions, classes, and variables.")
print("They help organize code and promote reusability.")
print("Modules can be imported using the 'import' statement.")

print("\n" + "=" * 70)
print("\n1. MATH MODULE")
print("-" * 70)

import math

# sqrt() - returns square root
print(f"math.sqrt(16) = {math.sqrt(16)}")

# pow() - returns power
print(f"math.pow(2, 3) = {math.pow(2, 3)}")

# ceil() - rounds up to nearest integer
print(f"math.ceil(4.3) = {math.ceil(4.3)}")

# floor() - rounds down to nearest integer
print(f"math.floor(4.7) = {math.floor(4.7)}")

# factorial() - returns factorial
print(f"math.factorial(5) = {math.factorial(5)}")

print("\n" + "=" * 70)
print("\n2. RANDOM MODULE")
print("-" * 70)

import random

# random() - returns random float between 0 and 1
print(f"random.random() = {random.random()}")

# randint() - returns random integer in range
print(f"random.randint(1, 10) = {random.randint(1, 10)}")

# choice() - returns random element from sequence
colors = ["red", "blue", "green"]
print(f"random.choice({colors}) = {random.choice(colors)}")

# shuffle() - shuffles list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"random.shuffle([1,2,3,4,5]) = {numbers}")

# randrange() - returns random number from range
print(f"random.randrange(0, 100, 5) = {random.randrange(0, 100, 5)}")

print("\n" + "=" * 70)
print("\n3. DATETIME MODULE")
print("-" * 70)

import datetime

# datetime.now() - returns current date and time
print(f"datetime.datetime.now() = {datetime.datetime.now()}")

# date.today() - returns current date
print(f"datetime.date.today() = {datetime.date.today()}")

# timedelta() - represents duration
future_date = datetime.date.today() + datetime.timedelta(days=7)
print(f"Date after 7 days = {future_date}")

# strftime() - formats date as string
formatted = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted datetime = {formatted}")

# weekday() - returns day of week (0=Monday)
print(f"Today's weekday = {datetime.date.today().weekday()}")

print("\n" + "=" * 70)
print("\n4. OS MODULE")
print("-" * 70)

import os

# getcwd() - returns current working directory
print(f"os.getcwd() = {os.getcwd()}")

# listdir() - lists files in directory
print(f"os.listdir('.') = {os.listdir('.')[:5]}...")

# path.exists() - checks if path exists
print(f"os.path.exists('test.txt') = {os.path.exists('test.txt')}")

# path.join() - joins path components
joined_path = os.path.join("folder", "subfolder", "file.txt")
print(f"os.path.join('folder', 'subfolder', 'file.txt') = {joined_path}")

# getenv() - gets environment variable
print(f"os.getenv('HOME', 'Not Found') = {os.getenv('HOME', 'Not Found')}")

print("\n" + "=" * 70)
print("\n5. STRING MODULE")
print("-" * 70)

import string

# ascii_lowercase - lowercase letters
print(f"string.ascii_lowercase = {string.ascii_lowercase}")

# ascii_uppercase - uppercase letters
print(f"string.ascii_uppercase = {string.ascii_uppercase}")

# digits - digit characters
print(f"string.digits = {string.digits}")

# punctuation - punctuation characters
print(f"string.punctuation = {string.punctuation}")

# ascii_letters - all letters
print(f"string.ascii_letters = {string.ascii_letters}")

print("\n" + "=" * 70)
print("\nBENEFITS OF MODULES:")
print("-" * 70)
print("1. Code Reusability - Write once, use multiple times")
print("2. Organization - Keep code organized and manageable")
print("3. Namespace - Avoid naming conflicts")
print("4. Maintainability - Easier to maintain and update")
print("5. Collaboration - Team members can work on different modules")
