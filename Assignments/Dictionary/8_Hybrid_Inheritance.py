print("Hybrid Inheritance")
print("=" * 70)

# Hybrid Inheritance: Combination of multiple types of inheritance

# Base class
class University:
    def __init__(self, uni_name):
        self.uni_name = uni_name
    
    def show_university(self):
        print(f"University: {self.uni_name}")

# Derived class 1 (Single Inheritance from University)
class Department(University):
    def __init__(self, uni_name, dept_name):
        super().__init__(uni_name)
        self.dept_name = dept_name
    
    def show_department(self):
        print(f"Department: {self.dept_name}")

# Independent class 1
class Person:
    def __init__(self, name):
        self.name = name
    
    def show_person(self):
        print(f"Person: {self.name}")

# Derived class 2 (Multiple Inheritance from Department and Person)
class Student(Department, Person):
    def __init__(self, uni_name, dept_name, name, student_id):
        Department.__init__(self, uni_name, dept_name)
        Person.__init__(self, name)
        self.student_id = student_id
    
    def show_student(self):
        print(f"Student ID: {self.student_id}")
    
    def display_all(self):
        print(f"University: {self.uni_name}")
        print(f"Department: {self.dept_name}")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")

# Another Derived class (Hierarchical - shares Person)
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    def show_teacher(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

print("\nCreating Student object:")
student = Student("MIT", "Computer Science", "Alice", "S12345")
student.show_university()
student.show_department()
student.show_person()
student.show_student()
print("\nComplete Info:")
student.display_all()

print("\n" + "=" * 70)
print("\nCreating Teacher object:")
teacher = Teacher("Bob", "Mathematics")
teacher.show_person()
teacher.show_teacher()

print("\n" + "=" * 70)
print("\nAnother Example:")
print("-" * 70)

# Base class
class Device:
    def __init__(self, brand):
        self.brand = brand
    
    def show_brand(self):
        print(f"Brand: {self.brand}")

# Derived class 1
class Mobile(Device):
    def __init__(self, brand, os):
        super().__init__(brand)
        self.os = os
    
    def show_os(self):
        print(f"Operating System: {self.os}")

# Independent class
class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels
    
    def show_camera(self):
        print(f"Camera: {self.megapixels} MP")

# Multiple inheritance
class Smartphone(Mobile, Camera):
    def __init__(self, brand, os, megapixels, model):
        Mobile.__init__(self, brand, os)
        Camera.__init__(self, megapixels)
        self.model = model
    
    def show_model(self):
        print(f"Model: {self.model}")
    
    def display_specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, OS: {self.os}, Camera: {self.megapixels} MP")

# Hierarchical inheritance
class Tablet(Mobile):
    def __init__(self, brand, os, screen_size):
        super().__init__(brand, os)
        self.screen_size = screen_size
    
    def show_screen(self):
        print(f"Screen Size: {self.screen_size} inches")

print("\nCreating Smartphone object:")
phone = Smartphone("Apple", "iOS", 12, "iPhone 13")
phone.show_brand()
phone.show_os()
phone.show_camera()
phone.show_model()
print("\nComplete Specs:")
phone.display_specs()

print("\nCreating Tablet object:")
tablet = Tablet("Samsung", "Android", 10.5)
tablet.show_brand()
tablet.show_os()
tablet.show_screen()
