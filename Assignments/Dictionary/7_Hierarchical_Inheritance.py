"""
Hierarchical Inheritance - One Parent, Multiple Children
========================================================
Hierarchical Inheritance: Multiple child classes inherit from one parent class
Structure: Parent -> Child1, Child2, Child3...
"""

# CORE HIERARCHICAL INHERITANCE EXAMPLE
class Animal:
    """Parent class - Common base for all animals"""
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    """Child class 1 - Inherits from Animal"""
    def bark(self):
        print(f"{self.name} is barking")
    
    def play(self):
        print(f"{self.name} is playing fetch")

class Cat(Animal):
    """Child class 2 - Inherits from Animal"""
    def meow(self):
        print(f"{self.name} is meowing")
    
    def climb(self):
        print(f"{self.name} is climbing tree")

class Bird(Animal):
    """Child class 3 - Inherits from Animal"""
    def chirp(self):
        print(f"{self.name} is chirping")
    
    def fly(self):
        print(f"{self.name} is flying")

# DEMONSTRATION
def demonstrate_hierarchical_inheritance():
    """Shows hierarchical inheritance with expected outputs"""
    
    print("Hierarchical Inheritance Demo")
    print("=" * 40)
    
    # Create objects from different child classes
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    bird = Bird("Tweety")
    
    print("Dog actions:")
    dog.eat()                                               # Output: Buddy is eating
    dog.bark()                                              # Output: Buddy is barking
    dog.play()                                              # Output: Buddy is playing fetch
    
    print("\nCat actions:")
    cat.eat()                                               # Output: Whiskers is eating
    cat.meow()                                              # Output: Whiskers is meowing
    cat.climb()                                             # Output: Whiskers is climbing tree
    
    print("\nBird actions:")
    bird.eat()                                              # Output: Tweety is eating
    bird.chirp()                                            # Output: Tweety is chirping
    bird.fly()                                              # Output: Tweety is flying
    
    # Show inheritance verification
    print(f"\nInheritance verification:")
    print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")      # Output: True
    print(f"isinstance(cat, Animal): {isinstance(cat, Animal)}")      # Output: True
    print(f"isinstance(bird, Animal): {isinstance(bird, Animal)}")    # Output: True

# Run demonstration
if __name__ == "__main__":
    demonstrate_hierarchical_inheritance()

"""
COMMENTED OUT SECTIONS - Additional examples for learning:

# Alternative Example: Shape -> Circle, Rectangle, Triangle
class Shape:
    def __init__(self, color):
        self.color = color
    def show_color(self):
        print(f"Color: {self.color}")                      # Output: Color: [color]

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        area = 3.14 * self.radius * self.radius
        print(f"Circle area: {area}")                      # Output: Circle area: [calculated area]

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        print(f"Rectangle area: {area}")                   # Output: Rectangle area: [calculated area]

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
    def area(self):
        area = 0.5 * self.base * self.height
        print(f"Triangle area: {area}")                    # Output: Triangle area: [calculated area]

# Usage:
# circle = Circle("Red", 5)
# circle.show_color()    # Output: Color: Red
# circle.area()          # Output: Circle area: 78.5

# rectangle = Rectangle("Blue", 10, 5)
# rectangle.show_color() # Output: Color: Blue
# rectangle.area()       # Output: Rectangle area: 50

# triangle = Triangle("Green", 8, 6)
# triangle.show_color()  # Output: Color: Green
# triangle.area()        # Output: Triangle area: 24.0

# Hierarchical vs Other Inheritance Types:
# Single: Parent -> Child
# Multilevel: GrandParent -> Parent -> Child
# Multiple: Parent1, Parent2 -> Child
# Hierarchical: Parent -> Child1, Child2, Child3
# Hybrid: Combination of above types
"""
