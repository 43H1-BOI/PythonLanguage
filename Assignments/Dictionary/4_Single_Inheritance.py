print("Single Inheritance")
print("=" * 70)

# Single Inheritance: One child class inherits from one parent class

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking")
    
    def show_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

print("\nCreating Dog object:")
dog = Dog("Buddy", "Golden Retriever")

# Accessing parent class methods
dog.eat()  # Output: Buddy is eating
dog.sleep()  # Output: Buddy is sleeping

# Accessing child class methods
dog.bark()  # Output: Buddy is barking
dog.show_info()  # Output: Name: Buddy, Breed: Golden Retriever

# unnecessary: Alternative example with Vehicle and Car - similar concept already demonstrated
# print("\n" + "=" * 70)
# print("\nAnother Example:")
# print("-" * 70)

# # Parent class
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     
#     def start(self):
#         print(f"{self.brand} {self.model} is starting")
#     
#     def stop(self):
#         print(f"{self.brand} {self.model} is stopping")

# # Child class
# class Car(Vehicle):
#     def __init__(self, brand, model, doors):
#         super().__init__(brand, model)
#         self.doors = doors
#     
#     def open_trunk(self):
#         print(f"Opening trunk of {self.brand} {self.model}")
#     
#     def display(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Doors: {self.doors}")

# print("\nCreating Car object:")
# car = Car("Toyota", "Camry", 4)

# car.start()
# car.stop()
# car.open_trunk()
# car.display()
