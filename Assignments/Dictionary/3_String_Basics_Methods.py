"""
String Basics and Methods - Comprehensive Guide
===============================================
"""

# CORE STRING METHODS DEMONSTRATION
def demonstrate_string_methods():
    """Demonstrates essential string methods with expected outputs"""
    
    # 1. Basic String Operations
    sample = "  Hello World Python  "
    print(f"Original: '{sample}'")
    print(f"upper(): {sample.upper()}")                    # Output:   HELLO WORLD PYTHON  
    print(f"lower(): {sample.lower()}")                    # Output:   hello world python  
    print(f"strip(): '{sample.strip()}'")                  # Output: 'Hello World Python'
    print(f"replace('World', 'Universe'): {sample.replace('World', 'Universe')}")  # Output:   Hello Universe Python  
    
    # 2. String Analysis Methods
    text = "Hello World"
    print(f"\nString: {text}")
    print(f"find('World'): {text.find('World')}")          # Output: 6
    print(f"count('l'): {text.count('l')}")                # Output: 3
    print(f"startswith('Hello'): {text.startswith('Hello')}")  # Output: True
    print(f"endswith('World'): {text.endswith('World')}")     # Output: True
    
    # 3. Character Type Checking
    print(f"\n'Hello'.isalpha(): {'Hello'.isalpha()}")     # Output: True
    print(f"'123'.isdigit(): {'123'.isdigit()}")           # Output: True
    print(f"'Hello123'.isalnum(): {'Hello123'.isalnum()}")  # Output: True
    
    # 4. String Formatting
    name, age = "Alice", 30
    print(f"\nf-string: Name is {name} and age is {age}")   # Output: Name is Alice and age is 30
    
    # 5. String Splitting and Joining
    words = ["Python", "is", "awesome"]
    print(f"join(): {' '.join(words)}")                     # Output: Python is awesome
    print(f"split(): {'Hello World Python'.split()}")       # Output: ['Hello', 'World', 'Python']

# Run demonstration
if __name__ == "__main__":
    print("String Methods Quick Reference")
    print("=" * 40)
    demonstrate_string_methods()

"""
COMMENTED OUT SECTIONS - Uncomment if needed for detailed learning:

# Extended String Methods (Less commonly used)
# text5 = "Python"
# print(f"center(20, '*'): {text5.center(20, '*')}")      # Output: *******Python*******
# print(f"ljust(20, '*'): {text5.ljust(20, '*')}")        # Output: Python**************
# print(f"rjust(20, '*'): {text5.rjust(20, '*')}")        # Output: **************Python
# print(f"swapcase(): {'Hello World'.swapcase()}")        # Output: hELLO wORLD

# String Validation Methods
# print(f"islower(): {'hello'.islower()}")                 # Output: True
# print(f"isupper(): {'HELLO'.isupper()}")                # Output: True
# print(f"isspace(): {'   '.isspace()}")                  # Output: True

# Advanced String Operations
# print(f"partition('-'): {'Hello-World-Python'.partition('-')}")  # Output: ('Hello', '-', 'World-Python')
# print(f"splitlines(): {'Line1\\nLine2\\nLine3'.splitlines()}")   # Output: ['Line1', 'Line2', 'Line3']
# print(f"zfill(5): {'42'.zfill(5)}")                     # Output: 00042

# String Indexing and Slicing
# text = "Python"
# print(f"text[0]: {text[0]}")                            # Output: P
# print(f"text[-1]: {text[-1]}")                          # Output: n
# print(f"len('Python'): {len('Python')}")                # Output: 6
# print(f"'Py' in 'Python': {'Py' in 'Python'}")         # Output: True
"""
