print("Hierarchical Inheritance")
print("=" * 70)

# Hierarchical Inheritance: Multiple child classes inherit from one parent class

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

# Child class 1
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")
    
    def play(self):
        print(f"{self.name} is playing fetch")

# Child class 2
class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")
    
    def climb(self):
        print(f"{self.name} is climbing tree")

# Child class 3
class Bird(Animal):
    def chirp(self):
        print(f"{self.name} is chirping")
    
    def fly(self):
        print(f"{self.name} is flying")

print("\nCreating Dog object:")
dog = Dog("Buddy")
dog.eat()
dog.sleep()
dog.bark()
dog.play()

print("\nCreating Cat object:")
cat = Cat("Whiskers")
cat.eat()
cat.sleep()
cat.meow()
cat.climb()

print("\nCreating Bird object:")
bird = Bird("Tweety")
bird.eat()
bird.sleep()
bird.chirp()
bird.fly()

print("\n" + "=" * 70)
print("\nAnother Example:")
print("-" * 70)

# Parent class
class Shape:
    def __init__(self, color):
        self.color = color
    
    def show_color(self):
        print(f"Color: {self.color}")

# Child class 1
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        area = 3.14 * self.radius * self.radius
        print(f"Circle area: {area}")

# Child class 2
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width
    
    def area(self):
        area = self.length * self.width
        print(f"Rectangle area: {area}")

# Child class 3
class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
    
    def area(self):
        area = 0.5 * self.base * self.height
        print(f"Triangle area: {area}")

print("\nCreating Circle object:")
circle = Circle("Red", 5)
circle.show_color()
circle.area()

print("\nCreating Rectangle object:")
rectangle = Rectangle("Blue", 10, 5)
rectangle.show_color()
rectangle.area()

print("\nCreating Triangle object:")
triangle = Triangle("Green", 8, 6)
triangle.show_color()
triangle.area()
