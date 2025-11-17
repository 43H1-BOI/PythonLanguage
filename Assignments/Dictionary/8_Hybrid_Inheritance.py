"""
Hybrid Inheritance - Combination of Multiple Inheritance Types
=============================================================
Hybrid Inheritance: Combines multiple inheritance types (single, multiple, hierarchical)
Structure: Mix of different inheritance patterns in one hierarchy
"""

# CORE HYBRID INHERITANCE EXAMPLE
class University:
    """Base class - Root of inheritance tree"""
    def __init__(self, uni_name):
        self.uni_name = uni_name
    
    def show_university(self):
        print(f"University: {self.uni_name}")

class Department(University):
    """Single inheritance from University"""
    def __init__(self, uni_name, dept_name):
        super().__init__(uni_name)
        self.dept_name = dept_name
    
    def show_department(self):
        print(f"Department: {self.dept_name}")

class Person:
    """Independent class for multiple inheritance"""
    def __init__(self, name):
        self.name = name
    
    def show_person(self):
        print(f"Person: {self.name}")

class Student(Department, Person):
    """Multiple inheritance: Department + Person"""
    def __init__(self, uni_name, dept_name, name, student_id):
        Department.__init__(self, uni_name, dept_name)
        Person.__init__(self, name)
        self.student_id = student_id
    
    def show_student(self):
        print(f"Student ID: {self.student_id}")
    
    def display_all(self):
        return f"University: {self.uni_name}, Department: {self.dept_name}, Name: {self.name}, ID: {self.student_id}"

class Teacher(Person):
    """Hierarchical inheritance from Person"""
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    def show_teacher(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

# DEMONSTRATION
def demonstrate_hybrid_inheritance():
    """Shows hybrid inheritance with expected outputs"""
    
    print("Hybrid Inheritance Demo")
    print("=" * 40)
    
    # Create Student object (uses multiple inheritance)
    student = Student("MIT", "Computer Science", "Alice", "S12345")
    
    print("Student Information:")
    student.show_university()                               # Output: University: MIT
    student.show_department()                               # Output: Department: Computer Science
    student.show_person()                                   # Output: Person: Alice
    student.show_student()                                  # Output: Student ID: S12345
    print(student.display_all())                            # Output: University: MIT, Department: Computer Science, Name: Alice, ID: S12345
    
    # Create Teacher object (uses hierarchical inheritance)
    teacher = Teacher("Bob", "Mathematics")
    
    print("\nTeacher Information:")
    teacher.show_person()                                   # Output: Person: Bob
    teacher.show_teacher()                                  # Output: Teacher: Bob, Subject: Mathematics
    
    # Show inheritance verification
    print(f"\nInheritance Structure:")
    print(f"Student MRO: {[cls.__name__ for cls in Student.mro()]}")  # Output: ['Student', 'Department', 'University', 'Person', 'object']
    print(f"isinstance(student, University): {isinstance(student, University)}")  # Output: True
    print(f"isinstance(student, Person): {isinstance(student, Person)}")          # Output: True

# Run demonstration
if __name__ == "__main__":
    demonstrate_hybrid_inheritance()

"""
COMMENTED OUT SECTIONS - Additional examples for learning:

# Alternative Example: Device -> Mobile/Tablet + Camera -> Smartphone
class Device:
    def __init__(self, brand):
        self.brand = brand
    def show_brand(self):
        print(f"Brand: {self.brand}")                      # Output: Brand: [brand]

class Mobile(Device):
    def __init__(self, brand, os):
        super().__init__(brand)
        self.os = os
    def show_os(self):
        print(f"Operating System: {self.os}")              # Output: Operating System: [os]

class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels
    def show_camera(self):
        print(f"Camera: {self.megapixels} MP")             # Output: Camera: [mp] MP

class Smartphone(Mobile, Camera):  # Multiple inheritance
    def __init__(self, brand, os, megapixels, model):
        Mobile.__init__(self, brand, os)
        Camera.__init__(self, megapixels)
        self.model = model
    def show_model(self):
        print(f"Model: {self.model}")                      # Output: Model: [model]
    def display_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, OS: {self.os}, Camera: {self.megapixels} MP"

class Tablet(Mobile):  # Hierarchical inheritance
    def __init__(self, brand, os, screen_size):
        super().__init__(brand, os)
        self.screen_size = screen_size
    def show_screen(self):
        print(f"Screen Size: {self.screen_size} inches")   # Output: Screen Size: [size] inches

# Usage:
# phone = Smartphone("Apple", "iOS", 12, "iPhone 13")
# phone.show_brand()     # Output: Brand: Apple
# phone.show_os()        # Output: Operating System: iOS
# phone.show_camera()    # Output: Camera: 12 MP
# phone.show_model()     # Output: Model: iPhone 13
# print(phone.display_specs())  # Output: Brand: Apple, Model: iPhone 13, OS: iOS, Camera: 12 MP

# tablet = Tablet("Samsung", "Android", 10.5)
# tablet.show_brand()    # Output: Brand: Samsung
# tablet.show_os()       # Output: Operating System: Android
# tablet.show_screen()   # Output: Screen Size: 10.5 inches

# Hybrid Inheritance Characteristics:
# 1. Combines single, multiple, and hierarchical inheritance
# 2. Creates complex inheritance hierarchies
# 3. Requires careful design to avoid diamond problem
# 4. Uses MRO (Method Resolution Order) for method lookup
# 5. Enables maximum code reuse and flexibility
"""
