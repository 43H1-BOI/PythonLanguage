"""
Multilevel Inheritance - Chain of Inheritance
===========================================
Multilevel Inheritance: Child class inherits from parent, which inherits from grandparent
Structure: Grandparent -> Parent -> Child
"""

# CORE MULTILEVEL INHERITANCE EXAMPLE
class Vehicle:
    """Grandparent class - Base of inheritance chain"""
    def __init__(self, brand):
        self.brand = brand
    
    def show_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    """Parent class - Inherits from Vehicle"""
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model
    
    def show_model(self):
        print(f"Model: {self.model}")

class ElectricCar(Car):
    """Child class - Inherits from Car (which inherits from Vehicle)"""
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Call parent constructor
        self.battery_capacity = battery_capacity
    
    def show_battery(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")
    
    def display_all(self):
        """Method accessing all inherited attributes"""
        return f"Brand: {self.brand}, Model: {self.model}, Battery: {self.battery_capacity} kWh"

# DEMONSTRATION
def demonstrate_multilevel_inheritance():
    """Shows multilevel inheritance in action with expected outputs"""
    
    print("Multilevel Inheritance Demo")
    print("=" * 40)
    
    # Create object from deepest level
    tesla = ElectricCar("Tesla", "Model S", 100)
    
    # Access methods from all inheritance levels
    tesla.show_brand()                                      # Output: Brand: Tesla
    tesla.show_model()                                      # Output: Model: Model S  
    tesla.show_battery()                                    # Output: Battery Capacity: 100 kWh
    print(tesla.display_all())                              # Output: Brand: Tesla, Model: Model S, Battery: 100 kWh
    
    # Show inheritance chain
    print(f"\nInheritance Chain:")
    print(f"ElectricCar -> Car -> Vehicle")                 # Output: ElectricCar -> Car -> Vehicle
    print(f"isinstance(tesla, Vehicle): {isinstance(tesla, Vehicle)}")  # Output: True
    print(f"isinstance(tesla, Car): {isinstance(tesla, Car)}")          # Output: True

# Run demonstration
if __name__ == "__main__":
    demonstrate_multilevel_inheritance()

"""
COMMENTED OUT SECTIONS - Additional examples for learning:

# Alternative Example: Person -> Student -> CollegeStudent
class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(f"Name: {self.name}")                         # Output: Name: [name]

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    def show_id(self):
        print(f"Student ID: {self.student_id}")             # Output: Student ID: [id]

class CollegeStudent(Student):
    def __init__(self, name, student_id, college):
        super().__init__(name, student_id)
        self.college = college
    def show_college(self):
        print(f"College: {self.college}")                   # Output: College: [college]
    def display_info(self):
        return f"Name: {self.name}, ID: {self.student_id}, College: {self.college}"

# Usage:
# student = CollegeStudent("John", "S12345", "MIT")
# student.show_name()        # Output: Name: John
# student.show_id()          # Output: Student ID: S12345  
# student.show_college()     # Output: College: MIT
# print(student.display_info())  # Output: Name: John, ID: S12345, College: MIT

# Method Resolution Order (MRO) demonstration:
# print(ElectricCar.__mro__)  # Shows inheritance chain order
# print(ElectricCar.mro())    # Alternative way to see MRO
"""
