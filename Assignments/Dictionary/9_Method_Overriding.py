print("Method Overriding")
print("=" * 70)

# Method Overriding: Child class provides specific implementation of parent class method

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print(f"{self.name} makes a sound")
    
    def move(self):
        print(f"{self.name} is moving")

# Child class 1 - overrides sound method
class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks: Woof Woof!")

# Child class 2 - overrides sound method
class Cat(Animal):
    def sound(self):
        print(f"{self.name} meows: Meow Meow!")

# Child class 3 - overrides both methods
class Bird(Animal):
    def sound(self):
        print(f"{self.name} chirps: Chirp Chirp!")
    
    def move(self):
        print(f"{self.name} is flying")

print("\nUsing Animal class:")
animal = Animal("Generic Animal")
animal.sound()
animal.move()

print("\nUsing Dog class:")
dog = Dog("Buddy")
dog.sound()
dog.move()

print("\nUsing Cat class:")
cat = Cat("Whiskers")
cat.sound()
cat.move()

print("\nUsing Bird class:")
bird = Bird("Tweety")
bird.sound()
bird.move()

print("\n" + "=" * 70)
print("\nAnother Example:")
print("-" * 70)

# Parent class
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        print("Area calculation not defined")
    
    def perimeter(self):
        print("Perimeter calculation not defined")

# Child class 1
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        area = 3.14 * self.radius * self.radius
        print(f"{self.name} area: {area}")
    
    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        print(f"{self.name} perimeter: {perimeter}")

# Child class 2
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
    
    def area(self):
        area = self.length * self.width
        print(f"{self.name} area: {area}")
    
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print(f"{self.name} perimeter: {perimeter}")

print("\nUsing Circle class:")
circle = Circle("Circle", 5)
circle.area()
circle.perimeter()

print("\nUsing Rectangle class:")
rectangle = Rectangle("Rectangle", 10, 5)
rectangle.area()
rectangle.perimeter()

print("\n" + "=" * 70)
print("\nMethod Overriding with super():")
print("-" * 70)

# Parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Child class - extends parent method
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display(self):
        super().display()
        print(f"Department: {self.department}")

print("\nUsing Employee class:")
emp = Employee("John", 50000)
emp.display()

print("\nUsing Manager class:")
mgr = Manager("Sarah", 80000, "IT")
mgr.display()
