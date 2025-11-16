print("Multilevel Inheritance")
print("=" * 70)

# Multilevel Inheritance: A child class inherits from another child class

# Grandparent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def show_brand(self):
        print(f"Brand: {self.brand}")

# Parent class (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def show_model(self):
        print(f"Model: {self.model}")

# Child class (inherits from Car)
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def show_battery(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")
    
    def display_all(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Battery: {self.battery_capacity} kWh")

print("\nCreating ElectricCar object:")
tesla = ElectricCar("Tesla", "Model S", 100)

# Accessing methods from all levels
tesla.show_brand()
tesla.show_model()
tesla.show_battery()
tesla.display_all()

print("\n" + "=" * 70)
print("\nAnother Example:")
print("-" * 70)

# Grandparent class
class Person:
    def __init__(self, name):
        self.name = name
    
    def show_name(self):
        print(f"Name: {self.name}")

# Parent class
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    
    def show_id(self):
        print(f"Student ID: {self.student_id}")

# Child class
class CollegeStudent(Student):
    def __init__(self, name, student_id, college):
        super().__init__(name, student_id)
        self.college = college
    
    def show_college(self):
        print(f"College: {self.college}")
    
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.student_id}, College: {self.college}")

print("\nCreating CollegeStudent object:")
student = CollegeStudent("John", "S12345", "MIT")

student.show_name()
student.show_id()
student.show_college()
student.display_info()
