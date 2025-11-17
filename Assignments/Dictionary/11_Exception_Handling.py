"""
Exception Handling - Managing Runtime Errors Gracefully
======================================================
Exception Handling: Mechanism to handle runtime errors without crashing the program
Key Components: try, except, else, finally blocks
Common Exceptions: ZeroDivisionError, ValueError, IndexError, KeyError, FileNotFoundError
"""

# CORE EXCEPTION HANDLING EXAMPLES
def demonstrate_basic_exceptions():
    """Shows common exceptions with expected outputs"""
    
    print("Exception Handling Demo")
    print("=" * 40)
    
    # 1. ZeroDivisionError
    print("1. ZeroDivisionError Example:")
    try:
        result = 10 / 0
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")                 # Output: Error: Cannot divide by zero!
    finally:
        print("Division operation completed")                   # Output: Division operation completed
    
    # 2. ValueError 
    print("\n2. ValueError Example:")
    try:
        age = int("not_a_number")
        print(f"Age: {age}")
    except ValueError:
        print("Error: Invalid input! Not a number")            # Output: Error: Invalid input! Not a number
    finally:
        print("Input operation completed")                      # Output: Input operation completed
    
    # 3. IndexError
    print("\n3. IndexError Example:")
    try:
        my_list = [1, 2, 3]
        print(f"Element at index 5: {my_list[5]}")
    except IndexError:
        print("Error: Index out of range!")                    # Output: Error: Index out of range!
    finally:
        print("List access completed")                          # Output: List access completed

# MULTIPLE EXCEPTION HANDLING
def demonstrate_multiple_exceptions():
    """Shows handling multiple exceptions in one try block"""
    
    print("\nMultiple Exception Handling:")
    
    def safe_operation(numbers, index, divisor):
        try:
            result = numbers[index] / divisor
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero!"             # When divisor is 0
        except IndexError:
            return "Error: Index out of range!"                # When index >= len(numbers)
        except TypeError:
            return "Error: Invalid data type!"                 # When wrong type passed
        except Exception as e:
            return f"Unexpected error: {e}"                    # Any other exception
    
    # Test different scenarios
    numbers = [10, 20, 30]
    print(f"Numbers: {numbers}")
    
    print(safe_operation(numbers, 1, 2))                       # Output: Result: 10.0
    print(safe_operation(numbers, 1, 0))                       # Output: Error: Cannot divide by zero!
    print(safe_operation(numbers, 5, 2))                       # Output: Error: Index out of range!

# CUSTOM EXCEPTION EXAMPLE
class AgeException(Exception):
    """Custom exception for age validation"""
    pass

def validate_age(age):
    """Validates age with custom exception"""
    try:
        if age < 0:
            raise AgeException("Age cannot be negative")
        elif age < 18:
            raise AgeException("Age must be 18 or above")
        else:
            return f"Valid age: {age}"
    except AgeException as e:
        return f"Error: {e}"

def demonstrate_custom_exceptions():
    """Shows custom exception handling"""
    
    print("\nCustom Exception Handling:")
    
    test_ages = [-5, 15, 25]
    for age in test_ages:
        print(validate_age(age))
        # Output: Error: Age cannot be negative
        # Output: Error: Age must be 18 or above  
        # Output: Valid age: 25

# COMMON EXCEPTIONS SHOWCASE
def demonstrate_common_exceptions():
    """Shows other common exception types"""
    
    print("\nCommon Exception Types:")
    
    # KeyError
    try:
        my_dict = {"name": "John", "age": 25}
        print(my_dict["city"])
    except KeyError:
        print("KeyError: Key not found in dictionary")         # Output: KeyError: Key not found in dictionary
    
    # TypeError
    try:
        result = "Hello" + 5
    except TypeError:
        print("TypeError: Cannot concatenate string with int")  # Output: TypeError: Cannot concatenate string with int
    
    # FileNotFoundError (simulated)
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("FileNotFoundError: File not found")             # Output: FileNotFoundError: File not found

# Run demonstrations
if __name__ == "__main__":
    demonstrate_basic_exceptions()
    demonstrate_multiple_exceptions()
    demonstrate_custom_exceptions()
    demonstrate_common_exceptions()

"""
COMMENTED OUT SECTIONS - Additional concepts for learning:

# Exception Hierarchy in Python:
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt  
#  +-- Exception
#       +-- ArithmeticError
#       |    +-- ZeroDivisionError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- ValueError
#       +-- TypeError
#       +-- FileNotFoundError

# Interactive Input Handling (commented for automated testing):
# def get_user_input():
#     try:
#         age = int(input("Enter your age: "))
#         print(f"Your age is: {age}")                       # Output: Your age is: [entered_value]
#     except ValueError:
#         print("Error: Invalid input! Please enter a number")  # Output when non-number entered
#     else:
#         print("Input is valid")                            # Output: Input is valid (if no exception)
#     finally:
#         print("Input operation completed")                 # Always executes

# Advanced Exception Handling:
# try:
#     # Code that might raise exceptions
#     pass
# except (ValueError, TypeError) as e:  # Multiple exceptions in one except
#     print(f"Input error: {e}")
# except Exception as e:                # Catch-all for unexpected exceptions
#     print(f"Unexpected error: {e}")
# else:                                # Executes only if no exception occurred
#     print("Success!")
# finally:                             # Always executes (cleanup code)
#     print("Cleanup completed")

# Best Practices:
# 1. Be specific with exception types (avoid bare except:)
# 2. Use finally for cleanup (close files, database connections)
# 3. Log exceptions for debugging
# 4. Don't suppress exceptions unnecessarily
# 5. Create custom exceptions for domain-specific errors
# 6. Use else block for code that should run only if no exceptions occurred
"""