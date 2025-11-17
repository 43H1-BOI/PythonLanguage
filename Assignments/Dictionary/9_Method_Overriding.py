"""
Method Overriding - Child Class Redefines Parent Methods
========================================================
Method Overriding: Child class provides specific implementation of parent class method
Key Concepts: Polymorphism, Runtime method resolution, super() usage
"""

# CORE METHOD OVERRIDING EXAMPLE
class Animal:
    """Parent class with generic methods"""
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print(f"{self.name} makes a sound")
    
    def move(self):
        print(f"{self.name} is moving")

class Dog(Animal):
    """Child class - overrides sound method"""
    def sound(self):
        print(f"{self.name} barks: Woof Woof!")

class Cat(Animal):
    """Child class - overrides sound method"""
    def sound(self):
        print(f"{self.name} meows: Meow Meow!")

class Bird(Animal):
    """Child class - overrides both methods"""
    def sound(self):
        print(f"{self.name} chirps: Chirp Chirp!")
    
    def move(self):
        print(f"{self.name} is flying")

# DEMONSTRATION
def demonstrate_method_overriding():
    """Shows method overriding with expected outputs"""
    
    print("Method Overriding Demo")
    print("=" * 40)
    
    # Create objects and show overriding behavior
    animals = [
        Animal("Generic Animal"),
        Dog("Buddy"),
        Cat("Whiskers"),
        Bird("Tweety")
    ]
    
    for animal in animals:
        print(f"\n{animal.__class__.__name__} actions:")
        animal.sound()                                      # Output varies by class
        animal.move()                                       # Output varies by class
        
    # Specific expected outputs:
    # Animal: Generic Animal makes a sound | Generic Animal is moving
    # Dog: Buddy barks: Woof Woof! | Buddy is moving
    # Cat: Whiskers meows: Meow Meow! | Whiskers is moving  
    # Bird: Tweety chirps: Chirp Chirp! | Tweety is flying
    
    # Show polymorphism in action
    print(f"\nPolymorphism demonstration:")
    dog = Dog("Rex")
    cat = Cat("Fluffy")
    
    for pet in [dog, cat]:
        pet.sound()                                         # Different output based on actual object type

# METHOD OVERRIDING WITH SUPER()
class Employee:
    """Parent class for employee hierarchy"""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    """Child class - extends parent method using super()"""
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display(self):
        super().display()                                   # Call parent method first
        print(f"Department: {self.department}")             # Add additional functionality

def demonstrate_super_usage():
    """Shows method overriding with super() extension"""
    
    print("\nMethod Overriding with super()")
    print("=" * 40)
    
    emp = Employee("John", 50000)
    mgr = Manager("Sarah", 80000, "IT")
    
    print("Employee display:")
    emp.display()                                           # Output: Name: John, Salary: 50000
    
    print("\nManager display (extends parent):")
    mgr.display()                                           # Output: Name: Sarah, Salary: 80000
                                                           # Output: Department: IT

# Run demonstrations
if __name__ == "__main__":
    demonstrate_method_overriding()
    demonstrate_super_usage()

"""
COMMENTED OUT SECTIONS - Additional examples for learning:

# Shape Example with Method Overriding
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        print("Area calculation not defined")              # Default implementation
    def perimeter(self):
        print("Perimeter calculation not defined")         # Default implementation

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def area(self):
        area = 3.14 * self.radius * self.radius
        print(f"{self.name} area: {area}")                 # Specific implementation
    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        print(f"{self.name} perimeter: {perimeter}")       # Specific implementation

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        print(f"{self.name} area: {area}")                 # Different implementation
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print(f"{self.name} perimeter: {perimeter}")       # Different implementation

# Usage:
# circle = Circle("Circle", 5)
# circle.area()          # Output: Circle area: 78.5
# circle.perimeter()     # Output: Circle perimeter: 31.400000000000002

# rectangle = Rectangle("Rectangle", 10, 5)
# rectangle.area()       # Output: Rectangle area: 50
# rectangle.perimeter()  # Output: Rectangle perimeter: 30

# Method Overriding Key Points:
# 1. Child class method has same name as parent class method
# 2. Python uses dynamic method dispatch (runtime method resolution)
# 3. super() allows calling parent class method from child
# 4. Enables polymorphism - same interface, different behavior
# 5. @override decorator (Python 3.12+) can be used for clarity
"""
