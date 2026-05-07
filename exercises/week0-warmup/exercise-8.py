# Exercise 8: Instance vs Class Attributes
# Difficulty: Beginner+

# CONCEPTS EXPLANATION:
#
# 1. INSTANCE ATTRIBUTES: Belong to each individual object
#    - Defined in __init__ with self.attribute
#    - Each object has its own copy
#    - Example: dog1.name = "Buddy", dog2.name = "Max" (different values)
#
# 2. CLASS ATTRIBUTES: Shared by ALL instances of the class
#    - Defined at class level (not in __init__)
#    - All objects share the same value
#    - Example: Dog.species = "Canis familiaris" (same for all dogs)
#
# 3. CLASS METHODS: Methods that work with class-level data
#    - Use @classmethod decorator
#    - First parameter is 'cls' (the class itself, not an instance)
#    - Can access/modify class attributes
#
# 4. STATIC METHODS: Utility functions that don't need instance or class data
#    - Use @staticmethod decorator
#    - No self or cls parameter
#    - Just regular functions organized inside the class

# EXAMPLE - Understanding the difference:
#
# class Dog:
#     species = "Canis familiaris"  # Class attribute (shared by all)
#     total_dogs = 0                # Class attribute (counter)
#
#     def __init__(self, name, age):
#         self.name = name          # Instance attribute (unique per dog)
#         self.age = age            # Instance attribute (unique per dog)
#         Dog.total_dogs += 1       # Increment class attribute
#
#     def bark(self):               # Instance method
#         return f"{self.name} says woof!"
#
#     @classmethod
#     def get_total_dogs(cls):      # Class method
#         return cls.total_dogs
#
#     @staticmethod
#     def is_adult(age):            # Static method
#         return age >= 2
#
# # Usage:
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Max", 1)
#
# print(dog1.name)               # "Buddy" (instance attribute)
# print(dog1.species)            # "Canis familiaris" (class attribute)
# print(Dog.species)             # "Canis familiaris" (accessed via class)
# print(Dog.get_total_dogs())    # 2 (class method)
# print(Dog.is_adult(3))         # True (static method)
# print(dog1.is_adult(dog1.age)) # True (can call via instance too)

# YOUR TASK:
# Create a Student class for a school system.
#
# Requirements:
# - Instance attributes: name, grade (set in __init__)
# - Class attribute: total_students (starts at 0, tracks how many students exist)
# - Every time you create a student, increment total_students
# - Class method: get_total_students() returns the count
# - Static method: is_passing_grade(grade) returns True if grade >= 60
# - Instance method: display_info() prints "Student: X, Grade: Y"

class Student:
    total_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        Student.total_students += 1
        
    def display_info(self):
        print(f"Student: {self.name}, Grade: {self.grade}")
    
    @classmethod
    def get_total_students(cls):
        return cls.total_students

    @staticmethod
    def is_passing_grade(grade):
        return grade >= 60



# --- Tests ---
# Check initial count
print(f"Total students: {Student.get_total_students()}")  # Expected: 0

# # Create students
s1 = Student("Alice", 85)
s2 = Student("Bob", 55)
s3 = Student("Carol", 92)

# # Check count after creating students
print(f"Total students: {Student.get_total_students()}")  # Expected: 3

# # Test instance method
s1.display_info()  # Expected: "Student: Alice, Grade: 85"

# # Test static method via class
print(Student.is_passing_grade(85))  # Expected: True
print(Student.is_passing_grade(55))  # Expected: False
print(Student.is_passing_grade(60))  # Expected: True (exactly 60)

# # Test static method via instance
print(s2.is_passing_grade(s2.grade))  # Expected: False (Bob has 55)

# # Check that each student is independent
s1.grade = 90  # Change Alice's grade
print(s1.grade)  # Expected: 90
print(s2.grade)  # Expected: 55 (Bob's grade unchanged)

# # But total_students is shared
print(f"Total from class: {Student.get_total_students()}")  # Expected: 3
print(f"Total from s1: {s1.get_total_students()}")  # Expected: 3 (same)
