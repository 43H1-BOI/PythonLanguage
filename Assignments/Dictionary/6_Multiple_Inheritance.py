"""
Multiple Inheritance - Inheriting from Multiple Parents
======================================================
Multiple Inheritance: Child class inherits from multiple parent classes
Structure: Parent1, Parent2 -> Child
"""

# CORE MULTIPLE INHERITANCE EXAMPLE
class Father:
    """First parent class"""
    def __init__(self):
        self.father_name = "Rajesh"
    
    def show_father(self):
        print(f"Father's name: {self.father_name}")
    
    def gardening(self):
        print(f"{self.father_name} likes gardening")

class Mother:
    """Second parent class"""
    def __init__(self):
        self.mother_name = "Priya"
    
    def show_mother(self):
        print(f"Mother's name: {self.mother_name}")
    
    def cooking(self):
        print(f"{self.mother_name} likes cooking")

class Child(Father, Mother):
    """Child class inheriting from both Father and Mother"""
    def __init__(self, name):
        Father.__init__(self)   # Initialize first parent
        Mother.__init__(self)   # Initialize second parent
        self.name = name
    
    def show_child(self):
        print(f"Child's name: {self.name}")
    
    def show_parents(self):
        return f"{self.name}'s parents are {self.father_name} and {self.mother_name}"

# DEMONSTRATION
def demonstrate_multiple_inheritance():
    """Shows multiple inheritance in action with expected outputs"""
    
    print("Multiple Inheritance Demo")
    print("=" * 40)
    
    # Create object inheriting from multiple parents
    child = Child("Amit")
    
    # Access methods from both parent classes
    child.show_father()                                     # Output: Father's name: Rajesh
    child.show_mother()                                     # Output: Mother's name: Priya
    child.show_child()                                      # Output: Child's name: Amit
    print(child.show_parents())                             # Output: Amit's parents are Rajesh and Priya
    child.gardening()                                       # Output: Rajesh likes gardening
    child.cooking()                                         # Output: Priya likes cooking
    
    # Show inheritance structure
    print(f"\nInheritance Structure:")
    print(f"Child inherits from: {Child.__bases__}")        # Output: (<class '__main__.Father'>, <class '__main__.Mother'>)
    print(f"MRO: {[cls.__name__ for cls in Child.mro()]}")  # Output: ['Child', 'Father', 'Mother', 'object']

# Run demonstration
if __name__ == "__main__":
    demonstrate_multiple_inheritance()

"""
COMMENTED OUT SECTIONS - Additional examples for learning:

# Alternative Example: Employee + Person -> Manager
class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id
    def show_emp_id(self):
        print(f"Employee ID: {self.emp_id}")               # Output: Employee ID: [id]
    def work(self):
        print("Employee is working")                       # Output: Employee is working

class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(f"Name: {self.name}")                        # Output: Name: [name]
    def eat(self):
        print(f"{self.name} is eating")                    # Output: [name] is eating

class Manager(Employee, Person):
    def __init__(self, emp_id, name, department):
        Employee.__init__(self, emp_id)
        Person.__init__(self, name)
        self.department = department
    def show_department(self):
        print(f"Department: {self.department}")            # Output: Department: [dept]
    def manage_team(self):
        print(f"{self.name} is managing the {self.department} team")  # Output: [name] is managing the [dept] team
    def display_all(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}"

# Usage:
# manager = Manager("E001", "Sarah", "IT")
# manager.show_emp_id()      # Output: Employee ID: E001
# manager.show_name()        # Output: Name: Sarah
# manager.show_department()  # Output: Department: IT
# manager.work()             # Output: Employee is working
# manager.eat()              # Output: Sarah is eating
# manager.manage_team()      # Output: Sarah is managing the IT team
# print(manager.display_all())  # Output: ID: E001, Name: Sarah, Department: IT

# Diamond Problem and Method Resolution Order (MRO):
# When multiple inheritance creates diamond patterns, Python uses C3 linearization
# Use super() for better handling in complex inheritance hierarchies
"""
