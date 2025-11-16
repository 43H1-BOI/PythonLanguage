print("Basics of OOPS in Python")
print("=" * 70)

print("\nOBJECT-ORIENTED PROGRAMMING (OOP)")
print("-" * 70)
print("OOP is a programming paradigm based on the concept of objects.")
print("Objects contain data (attributes) and code (methods).")

print("\n" + "=" * 70)
print("\n1. CLASS AND OBJECT")
print("-" * 70)

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
student1.display()

print("\nStudent 2:")
student2.display()

print("\n" + "=" * 70)
print("\n2. FOUR PILLARS OF OOP")
print("-" * 70)

print("\nA. ENCAPSULATION")
print("Wrapping data and methods together in a class")
print("Data hiding using private members")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

account = BankAccount(1000)
print(f"Balance: {account.get_balance()}")
account.deposit(500)
print(f"After deposit: {account.get_balance()}")

print("\nB. INHERITANCE")
print("Creating new class from existing class")

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

print("\nC. POLYMORPHISM")
print("Same method name, different implementations")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

class Bird(Animal):
    def speak(self):
        print(f"{self.name} chirps")

animals = [Dog("Max"), Cat("Whiskers"), Bird("Tweety")]
for animal in animals:
    animal.speak()

print("\nD. ABSTRACTION")
print("Hiding complex implementation details")
print("Showing only essential features")

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

print("\n" + "=" * 70)
print("\n3. CONSTRUCTOR")
print("-" * 70)
print("Special method __init__() called when object is created")

class Person:
    def __init__(self, name, age):
        print("Constructor called")
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("John", 25)
person.display()

print("\n" + "=" * 70)
print("\n4. TYPES OF VARIABLES")
print("-" * 70)

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
emp1.display()
emp2.display()

print("\nClass variable (shared by all objects):")
print(f"Company: {Employee.company}")

print("\n" + "=" * 70)
print("\n5. TYPES OF METHODS")
print("-" * 70)

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
print(f"Square of 5: {calc.square()}")

print("\nClass method:")
print(f"Circle area (radius=3): {Calculator.circle_area(3)}")

print("\nStatic method:")
print(f"Add 10 + 20: {Calculator.add(10, 20)}")

print("\n" + "=" * 70)
print("\n6. ACCESS MODIFIERS")
print("-" * 70)

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
obj.display()

print("\nOutside class:")
print(f"Public: {obj.public}")
print(f"Protected: {obj._protected}")

print("\n" + "=" * 70)
print("\nBENEFITS OF OOP")
print("-" * 70)
print("1. Code Reusability - Use existing code through inheritance")
print("2. Modularity - Divide program into independent objects")
print("3. Data Security - Encapsulation protects data")
print("4. Flexibility - Polymorphism allows flexibility")
print("5. Maintainability - Easier to maintain and modify")
print("6. Real-world modeling - Objects represent real entities")

print("\n" + "=" * 70)
print("\nKEY CONCEPTS SUMMARY")
print("-" * 70)
print("• Class: Blueprint for creating objects")
print("• Object: Instance of a class")
print("• Attributes: Variables that belong to a class/object")
print("• Methods: Functions that belong to a class")
print("• Constructor: __init__() method")
print("• self: Reference to current instance")
print("• Inheritance: Child class inherits from parent")
print("• Encapsulation: Data hiding using private members")
print("• Polymorphism: Same interface, different implementations")
print("• Abstraction: Hiding complex details")
