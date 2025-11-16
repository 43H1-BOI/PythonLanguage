print("Multiple Inheritance")
print("=" * 70)

# Multiple Inheritance: A child class inherits from multiple parent classes

# Parent class 1
class Father:
    def __init__(self):
        self.father_name = "Rajesh"
    
    def show_father(self):
        print(f"Father's name: {self.father_name}")
    
    def gardening(self):
        print(f"{self.father_name} likes gardening")

# Parent class 2
class Mother:
    def __init__(self):
        self.mother_name = "Priya"
    
    def show_mother(self):
        print(f"Mother's name: {self.mother_name}")
    
    def cooking(self):
        print(f"{self.mother_name} likes cooking")

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def __init__(self, name):
        Father.__init__(self)
        Mother.__init__(self)
        self.name = name
    
    def show_child(self):
        print(f"Child's name: {self.name}")
    
    def show_parents(self):
        print(f"{self.name}'s parents are {self.father_name} and {self.mother_name}")

print("\nCreating Child object:")
child = Child("Amit")

# Accessing methods from both parent classes
child.show_father()
child.show_mother()
child.show_child()
child.show_parents()
child.gardening()
child.cooking()

print("\n" + "=" * 70)
print("\nAnother Example:")
print("-" * 70)

# Parent class 1
class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id
    
    def show_emp_id(self):
        print(f"Employee ID: {self.emp_id}")
    
    def work(self):
        print("Employee is working")

# Parent class 2
class Person:
    def __init__(self, name):
        self.name = name
    
    def show_name(self):
        print(f"Name: {self.name}")
    
    def eat(self):
        print(f"{self.name} is eating")

# Child class
class Manager(Employee, Person):
    def __init__(self, emp_id, name, department):
        Employee.__init__(self, emp_id)
        Person.__init__(self, name)
        self.department = department
    
    def show_department(self):
        print(f"Department: {self.department}")
    
    def manage_team(self):
        print(f"{self.name} is managing the {self.department} team")
    
    def display_all(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}")

print("\nCreating Manager object:")
manager = Manager("E001", "Sarah", "IT")

manager.show_emp_id()
manager.show_name()
manager.show_department()
manager.work()
manager.eat()
manager.manage_team()
manager.display_all()
