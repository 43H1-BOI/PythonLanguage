"""
Encapsulation - Data Hiding and Access Control
==============================================
Encapsulation: Wrapping data and methods within a class with controlled access
Access Levels: public, protected (_), private (__)
Key Tools: getter/setter methods, @property decorator
"""

# CORE ENCAPSULATION EXAMPLE
class BankAccount:
    """Demonstrates encapsulation with private data and controlled access"""
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder    # Public attribute
        self.__balance = balance                # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount")
    
    def get_balance(self):
        """Getter method for private balance"""
        return self.__balance
    
    def display(self):
        return f"Account: {self.account_holder}, Balance: {self.__balance}"

# PROPERTY DECORATOR EXAMPLE
class Employee:
    """Demonstrates encapsulation using @property decorator"""
    
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    @property
    def name(self):
        """Getter for name"""
        return self.__name
    
    @name.setter
    def name(self, value):
        """Setter for name with validation"""
        if value.strip():
            self.__name = value
        else:
            print("Name cannot be empty")
    
    @property
    def salary(self):
        """Getter for salary"""
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        """Setter for salary with validation"""
        if value > 0:
            self.__salary = value
        else:
            print("Salary must be positive")
    
    def display(self):
        return f"Employee: {self.__name}, Salary: ${self.__salary}"

# DEMONSTRATION
def demonstrate_encapsulation():
    """Shows encapsulation concepts with expected outputs"""
    
    print("Encapsulation Demo")
    print("=" * 40)
    
    # Bank Account Example
    print("Bank Account Operations:")
    account = BankAccount("John", 5000)
    print(account.display())                                # Output: Account: John, Balance: 5000
    
    account.deposit(2000)                                   # Output: Deposited: 2000
    print(f"Balance: ${account.get_balance()}")             # Output: Balance: $7000
    
    account.withdraw(1500)                                  # Output: Withdrawn: 1500
    print(f"Balance: ${account.get_balance()}")             # Output: Balance: $5500
    
    account.withdraw(10000)                                 # Output: Insufficient balance or invalid amount
    
    # Try accessing private variable
    try:
        print(account.__balance)                            # Will raise AttributeError
    except AttributeError:
        print("✓ Private variable protected")               # Output: ✓ Private variable protected
    
    # Employee Property Example
    print(f"\nEmployee Property Operations:")
    emp = Employee("Bob", 50000)
    print(emp.display())                                    # Output: Employee: Bob, Salary: $50000
    
    # Using property accessors
    emp.name = "Robert"                                     # Uses setter validation
    emp.salary = 60000                                      # Uses setter validation
    print(emp.display())                                    # Output: Employee: Robert, Salary: $60000
    
    # Invalid operations
    emp.salary = -1000                                      # Output: Salary must be positive
    print(emp.display())                                    # Output: Employee: Robert, Salary: $60000 (unchanged)

# Run demonstration
if __name__ == "__main__":
    demonstrate_encapsulation()

"""
COMMENTED OUT SECTIONS - Additional examples for learning:

# Access Modifier Examples
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name        # Public - accessible everywhere
        self._roll_no = roll_no # Protected - accessible but shouldn't be used outside class
        self.__marks = marks    # Private - only accessible within class
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully")            # Output: Marks updated successfully
        else:
            print("Invalid marks. Must be between 0 and 100")  # Output: Invalid marks...
    
    def display(self):
        return f"Name: {self.name}, Roll: {self._roll_no}, Marks: {self.__marks}"

# Usage:
# student = Student("Alice", "S001", 85)
# print(student.name)          # Output: Alice (public access)
# print(student._roll_no)      # Output: S001 (protected - not recommended)
# print(student.get_marks())   # Output: 85 (proper private access)
# student.set_marks(90)        # Output: Marks updated successfully
# student.set_marks(150)       # Output: Invalid marks. Must be between 0 and 100

# Encapsulation Benefits:
# 1. Data Hiding: Prevents unauthorized access to internal data
# 2. Validation: Control how data is modified (business rules)
# 3. Flexibility: Change internal implementation without breaking external code
# 4. Maintainability: Easier to debug and maintain
# 5. Security: Protect sensitive data from direct manipulation

# Name Mangling in Python:
# Python doesn't have true private members, but uses name mangling
# __attribute becomes _ClassName__attribute
# This prevents accidental access but doesn't provide true security

# Best Practices:
# - Use _ for protected (internal use but accessible)
# - Use __ for private (internal implementation details)
# - Prefer @property over getter/setter methods for Pythonic code
# - Validate data in setters to maintain data integrity
"""
