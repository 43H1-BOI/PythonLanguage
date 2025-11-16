print("Exception Handling - Three Different Types of Exceptions")
print("=" * 70)

# Exception 1: ZeroDivisionError
print("\n1. ZeroDivisionError")
print("-" * 70)

try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print("Division successful")
finally:
    print("Division operation completed")

# Exception 2: ValueError
print("\n\n2. ValueError")
print("-" * 70)

try:
    age = int(input("Enter your age: "))
    print(f"Your age is: {age}")
except ValueError:
    print("Error: Invalid input! Please enter a number")
else:
    print("Input is valid")
finally:
    print("Input operation completed")

# Exception 3: IndexError
print("\n\n3. IndexError")
print("-" * 70)

try:
    my_list = [1, 2, 3, 4, 5]
    print(f"List: {my_list}")
    index = int(input("Enter index to access (0-4): "))
    print(f"Element at index {index}: {my_list[index]}")
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Please enter a valid number")
else:
    print("Element accessed successfully")
finally:
    print("List access operation completed")

print("\n" + "=" * 70)
print("\nMultiple Exceptions in Single Try Block")
print("-" * 70)

try:
    numbers = [10, 20, 30]
    print(f"Numbers: {numbers}")
    
    index = int(input("Enter index: "))
    divisor = int(input("Enter divisor: "))
    
    result = numbers[index] / divisor
    print(f"Result: {result}")
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Invalid input! Please enter numbers only")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("Operation successful")
finally:
    print("Operation completed")

print("\n" + "=" * 70)
print("\nMore Examples of Common Exceptions")
print("-" * 70)

# KeyError
print("\nKeyError Example:")
try:
    my_dict = {"name": "John", "age": 25}
    print(my_dict["city"])
except KeyError:
    print("Error: Key not found in dictionary")

# FileNotFoundError
print("\nFileNotFoundError Example:")
try:
    file = open("nonexistent_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found")

# TypeError
print("\nTypeError Example:")
try:
    result = "Hello" + 5
except TypeError:
    print("Error: Cannot concatenate string with integer")

print("\n" + "=" * 70)
print("\nCustom Exception Handling")
print("-" * 70)

class AgeException(Exception):
    pass

def check_age(age):
    if age < 0:
        raise AgeException("Age cannot be negative")
    elif age < 18:
        raise AgeException("Age must be 18 or above")
    else:
        print(f"Valid age: {age}")

try:
    check_age(-5)
except AgeException as e:
    print(f"Error: {e}")

try:
    check_age(15)
except AgeException as e:
    print(f"Error: {e}")

try:
    check_age(25)
except AgeException as e:
    print(f"Error: {e}")

print("\n" + "=" * 70)
print("\nBenefits of Exception Handling:")
print("-" * 70)
print("1. Prevents program crashes")
print("2. Provides meaningful error messages")
print("3. Separates error handling code from normal code")
print("4. Makes code more robust and reliable")
print("5. Allows graceful error recovery")
