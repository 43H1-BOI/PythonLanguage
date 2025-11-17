print("Basics of OOPS in Python")
# Output: Basics of OOPS in Python

print("=" * 70)
# Output: ======================================================================

print("\nOBJECT-ORIENTED PROGRAMMING (OOP)")
# Output: OBJECT-ORIENTED PROGRAMMING (OOP)

print("-" * 70)
# Output: ----------------------------------------------------------------------

print("OOP is a programming paradigm based on the concept of objects.")
# Output: OOP is a programming paradigm based on the concept of objects.

print("Objects contain data (attributes) and code (methods).")
# Output: Objects contain data (attributes) and code (methods).

print("\n" + "=" * 70)
# Output: ======================================================================

print("\n1. CLASS AND OBJECT")
# Output: 1. CLASS AND OBJECT

print("-" * 70)
# Output: ----------------------------------------------------------------------

# Class definition
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

# Creating objects
student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

print("\nStudent 1:")
# Output: Student 1:

student1.display()
# Output: Name: Alice, Roll No: 101

print("\nStudent 2:")
# Output: Student 2:

student2.display()
# Output: Name: Bob, Roll No: 102

print("\n" + "=" * 70)
# Output: ======================================================================

print("\n2. FOUR PILLARS OF OOP")
# Output: 2. FOUR PILLARS OF OOP

print("-" * 70)
# Output: ----------------------------------------------------------------------

print("\nA. ENCAPSULATION")
# Output: A. ENCAPSULATION

# print("Wrapping data and methods together in a class")
# print("Data hiding using private members")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

account = BankAccount(1000)
print(f"Balance: {account.get_balance()}")
# Output: Balance: 1000

account.deposit(500)
print(f"After deposit: {account.get_balance()}")
# Output: After deposit: 1500

print("\nB. INHERITANCE")
# Output: B. INHERITANCE

# print("Creating new class from existing class")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

dog = Dog("Buddy")
dog.speak()
# Output: Buddy barks

print("\nC. POLYMORPHISM")
# Output: C. POLYMORPHISM

# print("Same method name, different implementations")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

class Bird(Animal):
    def speak(self):
        print(f"{self.name} chirps")

animals = [Dog("Max"), Cat("Whiskers"), Bird("Tweety")]
for animal in animals:
    animal.speak()
# Output: Max barks
# Output: Whiskers meows
# Output: Tweety chirps

print("\nD. ABSTRACTION")
# Output: D. ABSTRACTION

# print("Hiding complex implementation details")
# print("Showing only essential features")

class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        self.__ignition()
        self.__fuel_pump()
        print(f"{self.brand} started")
    
    def __ignition(self):
        print("Ignition on")
    
    def __fuel_pump(self):
        print("Fuel pump activated")

car = Car("Toyota")
car.start()
# Output: Ignition on
# Output: Fuel pump activated
# Output: Toyota started

print("\n" + "=" * 70)
# Output: ======================================================================

print("\n3. CONSTRUCTOR")
# Output: 3. CONSTRUCTOR

print("-" * 70)
# Output: ----------------------------------------------------------------------

# print("Special method __init__() called when object is created")

class Person:
    def __init__(self, name, age):
        print("Constructor called")
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("John", 25)
# Output: Constructor called

person.display()
# Output: Name: John, Age: 25

print("\n" + "=" * 70)
# Output: ======================================================================

print("\n4. TYPES OF VARIABLES")
# Output: 4. TYPES OF VARIABLES

print("-" * 70)
# Output: ----------------------------------------------------------------------

class Employee:
    company = "ABC Corp"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"Company: {Employee.company}, Name: {self.name}, Salary: {self.salary}")

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print("\nInstance variables (unique to each object):")
# Output: Instance variables (unique to each object):

emp1.display()
# Output: Company: ABC Corp, Name: Alice, Salary: 50000

emp2.display()
# Output: Company: ABC Corp, Name: Bob, Salary: 60000

print("\nClass variable (shared by all objects):")
# Output: Class variable (shared by all objects):

print(f"Company: {Employee.company}")
# Output: Company: ABC Corp

print("\n" + "=" * 70)
# Output: ======================================================================

print("\n5. TYPES OF METHODS")
# Output: 5. TYPES OF METHODS

print("-" * 70)
# Output: ----------------------------------------------------------------------

class Calculator:
    pi = 3.14
    
    def __init__(self, num):
        self.num = num
    
    # Instance method
    def square(self):
        return self.num * self.num
    
    # Class method
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius * radius
    
    # Static method
    @staticmethod
    def add(a, b):
        return a + b

calc = Calculator(5)

print("\nInstance method:")
# Output: Instance method:

print(f"Square of 5: {calc.square()}")
# Output: Square of 5: 25

print("\nClass method:")
# Output: Class method:

print(f"Circle area (radius=3): {Calculator.circle_area(3)}")
# Output: Circle area (radius=3): 28.26

print("\nStatic method:")
# Output: Static method:

print(f"Add 10 + 20: {Calculator.add(10, 20)}")
# Output: Add 10 + 20: 30

print("\n" + "=" * 70)
# Output: ======================================================================

print("\n6. ACCESS MODIFIERS")
# Output: 6. ACCESS MODIFIERS

print("-" * 70)
# Output: ----------------------------------------------------------------------

class AccessDemo:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"
    
    def display(self):
        print(f"Public: {self.public}")
        print(f"Protected: {self._protected}")
        print(f"Private: {self.__private}")

obj = AccessDemo()
print("\nInside class:")
# Output: Inside class:

obj.display()
# Output: Public: Public
# Output: Protected: Protected
# Output: Private: Private

print("\nOutside class:")
# Output: Outside class:

print(f"Public: {obj.public}")
# Output: Public: Public

print(f"Protected: {obj._protected}")
# Output: Protected: Protected

# print("\n" + "=" * 70)
# print("\nBENEFITS OF OOP")
# print("-" * 70)
# print("1. Code Reusability - Use existing code through inheritance")
# print("2. Modularity - Divide program into independent objects")
# print("3. Data Security - Encapsulation protects data")
# print("4. Flexibility - Polymorphism allows flexibility")
# print("5. Maintainability - Easier to maintain and modify")
# print("6. Real-world modeling - Objects represent real entities")

# print("\n" + "=" * 70)
# print("\nKEY CONCEPTS SUMMARY")
# print("-" * 70)
# print("• Class: Blueprint for creating objects")
# print("• Object: Instance of a class")
# print("• Attributes: Variables that belong to a class/object")
# print("• Methods: Functions that belong to a class")
# print("• Constructor: __init__() method")
# print("• self: Reference to current instance")
# print("• Inheritance: Child class inherits from parent")
# print("• Encapsulation: Data hiding using private members")
# print("• Polymorphism: Same interface, different implementations")
# print("• Abstraction: Hiding complex details")
