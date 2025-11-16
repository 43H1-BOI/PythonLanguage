print("Encapsulation")
print("=" * 70)

# Encapsulation: Wrapping data and methods within a class
# Access modifiers: public, protected (_), private (__)

# Example 1: Basic Encapsulation
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
    
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
        return self.__balance
    
    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.__balance}")

print("\nCreating Bank Account:")
account = BankAccount("John", 5000)
account.display()

print("\nDepositing money:")
account.deposit(2000)
print(f"Current Balance: {account.get_balance()}")

print("\nWithdrawing money:")
account.withdraw(1500)
print(f"Current Balance: {account.get_balance()}")

print("\nTrying to withdraw more than balance:")
account.withdraw(10000)

print("\nTrying to access private variable directly:")
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Error: Cannot access private variable directly")

print("\n" + "=" * 70)
print("\nExample 2: Public, Protected, Private Members")
print("-" * 70)

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self._roll_no = roll_no
        self.__marks = marks
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully")
        else:
            print("Invalid marks. Must be between 0 and 100")
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self._roll_no}")
        print(f"Marks: {self.__marks}")

print("\nCreating Student:")
student = Student("Alice", "S001", 85)

# Accessing public member
print(f"Public member (name): {student.name}")

# Accessing protected member (can be accessed but shouldn't be)
print(f"Protected member (roll_no): {student._roll_no}")

# Accessing private member using getter
print(f"Private member (marks) using getter: {student.get_marks()}")

print("\nUpdating marks using setter:")
student.set_marks(90)
student.display()

print("\nTrying to set invalid marks:")
student.set_marks(150)

print("\n" + "=" * 70)
print("\nExample 3: Encapsulation with Property Decorator")
print("-" * 70)

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value:
            self.__name = value
        else:
            print("Name cannot be empty")
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            print("Salary must be positive")
    
    def display(self):
        print(f"Name: {self.__name}, Salary: {self.__salary}")

print("\nCreating Employee:")
emp = Employee("Bob", 50000)
emp.display()

print("\nAccessing properties:")
print(f"Name: {emp.name}")
print(f"Salary: {emp.salary}")

print("\nModifying properties:")
emp.name = "Robert"
emp.salary = 60000
emp.display()

print("\nTrying to set invalid salary:")
emp.salary = -1000
emp.display()

print("\n" + "=" * 70)
print("\nBenefits of Encapsulation:")
print("-" * 70)
print("1. Data hiding - Prevents direct access to internal data")
print("2. Flexibility - Internal implementation can change without affecting code")
print("3. Validation - Control how data is accessed and modified")
print("4. Maintainability - Easier to maintain and debug")
print("5. Security - Protects data from unauthorized access")
