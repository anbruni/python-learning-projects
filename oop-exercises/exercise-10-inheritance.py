# OOP Exercise 10: Inheritance
# Difficulty: Intermediate

# CONCEPTS:
# - Inheritance: Creating a new class based on an existing class
# - Parent/Base class: The class being inherited from
# - Child/Derived class: The class that inherits
# - super(): Call the parent class's methods
# - Method overriding: Child class replaces parent's method
# - isinstance() and issubclass(): Check inheritance relationships

# WHY THIS MATTERS:
# Inheritance allows code reuse and creates hierarchical relationships.
# It's fundamental in OOP and used everywhere: frameworks, libraries, etc.

# ============================================================================
# 📚 KNOWLEDGE: Inheritance Basics
# ============================================================================

"""
WHAT IS INHERITANCE?

Inheritance allows a class (child) to inherit attributes and methods from
another class (parent). The child gets everything from the parent and can:
1. Use parent's methods as-is
2. Override parent's methods (replace them)
3. Add new methods and attributes

SYNTAX:

class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):  # ← Inherits from Parent
    pass

child = Child()
child.method()  # Works! Inherited from Parent

WHY USE INHERITANCE?

✅ Code reuse (don't repeat yourself)
✅ Hierarchical relationships (Employee → Manager, Developer)
✅ Polymorphism (treat different types uniformly)
✅ Extend existing classes without modifying them

COMPARISON WITH JAVASCRIPT:

// JavaScript (ES6 classes)
class Parent {
    constructor(name) {
        this.name = name;
    }
    greet() {
        console.log(`Hello, I'm ${this.name}`);
    }
}

class Child extends Parent {  // 'extends' keyword
    constructor(name, age) {
        super(name);  // Call parent constructor
        this.age = age;
    }
}

# Python
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")

class Child(Parent):  # Parent in parentheses
    def __init__(self, name, age):
        super().__init__(name)  # Call parent __init__
        self.age = age
"""

# ============================================================================
# 📚 KNOWLEDGE: super() Function
# ============================================================================

"""
WHAT IS super()?

super() gives you access to the parent class's methods.
Most commonly used in __init__ to initialize parent attributes.

EXAMPLE:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_annual_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # ← Initialize parent attributes
        self.department = department    # ← Add child-specific attribute

# Without super(), you'd have to manually set name and salary:
class Manager(Employee):
    def __init__(self, name, salary, department):
        self.name = name        # Duplicate code
        self.salary = salary    # Duplicate code
        self.department = department

WHEN TO USE super():

✅ In __init__ to call parent's constructor
✅ When overriding a method but want to keep parent's behavior
✅ In multiple inheritance (advanced)

COMPARISON WITH JAVASCRIPT:

// JavaScript
class Manager extends Employee {
    constructor(name, salary, department) {
        super(name, salary);  // Call parent constructor
        this.department = department;
    }
}

# Python
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Call parent constructor
        self.department = department
"""

# ============================================================================
# 📚 KNOWLEDGE: Method Overriding
# ============================================================================

"""
METHOD OVERRIDING:

Child class can replace (override) a parent's method with its own version.

EXAMPLE:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"{self.name}: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    # Override display_info
    def display_info(self):
        # Can call parent's version with super()
        parent_info = super().display_info()
        return f"{parent_info}, Department: {self.department}"

emp = Employee("John", 50000)
print(emp.display_info())  # "John: $50000"

mgr = Manager("Jane", 80000, "Sales")
print(mgr.display_info())  # "Jane: $80000, Department: Sales"

WHEN TO OVERRIDE:

✅ Child needs different behavior
✅ Want to extend parent's behavior (call super() + add more)
✅ Parent method doesn't fit child's needs
"""

# ============================================================================
# 📚 KNOWLEDGE: isinstance() and issubclass()
# ============================================================================

"""
isinstance(obj, Class):
Check if object is an instance of a class (or its subclasses)

issubclass(ChildClass, ParentClass):
Check if a class inherits from another class

EXAMPLES:

class Employee:
    pass

class Manager(Employee):
    pass

emp = Employee()
mgr = Manager()

# isinstance
print(isinstance(emp, Employee))  # True
print(isinstance(mgr, Employee))  # True (Manager IS-A Employee)
print(isinstance(mgr, Manager))   # True
print(isinstance(emp, Manager))   # False

# issubclass
print(issubclass(Manager, Employee))  # True
print(issubclass(Employee, Manager))  # False
print(issubclass(Manager, Manager))   # True (class is subclass of itself)

# Check type
print(type(emp))  # <class '__main__.Employee'>
print(type(mgr))  # <class '__main__.Manager'>
"""

# ============================================================================
# PART 1: Basic Inheritance
# ============================================================================


class Employee:
    """
    Base class for all employees.
    Attributes: name, salary
    Methods: get_annual_salary(), display_info()
    """

    def __init__(self, name, salary):
        """
        Initialize Employee with name and salary.

        Args:
            name (str): Employee's name
            salary (int): Monthly salary
        """
        # Your code here
        pass

    def get_annual_salary(self):
        """
        Calculate and return annual salary (salary * 12).

        Returns:
            int: Annual salary

        Example:
            emp = Employee("John", 5000)
            emp.get_annual_salary() → 60000
        """
        # Your code here
        pass

    def display_info(self):
        """
        Display employee information.

        Returns:
            str: "Name: {name}, Salary: ${salary}"

        Example:
            emp = Employee("John", 5000)
            emp.display_info() → "Name: John, Salary: $5000"
        """
        # Your code here
        pass


class Manager(Employee):
    """
    Manager class inherits from Employee.
    Adds: department attribute
    Overrides: display_info() to show department
    """

    def __init__(self, name, salary, department):
        """
        Initialize Manager.

        Args:
            name (str): Manager's name
            salary (int): Monthly salary
            department (str): Department name

        Hint: Use super().__init__(name, salary) to initialize parent
        """
        # Your code here
        pass

    def display_info(self):
        """
        Override display_info to include department.

        Returns:
            str: "Name: {name}, Salary: ${salary}, Department: {department}"

        Example:
            mgr = Manager("Jane", 8000, "Sales")
            mgr.display_info() → "Name: Jane, Salary: $8000, Department: Sales"

        Hint: You can call parent's display_info() with super().display_info()
        """
        # Your code here
        pass


class Developer(Employee):
    """
    Developer class inherits from Employee.
    Adds: programming_language attribute and code() method
    """

    def __init__(self, name, salary, programming_language):
        """
        Initialize Developer.

        Args:
            name (str): Developer's name
            salary (int): Monthly salary
            programming_language (str): Primary programming language

        Hint: Use super().__init__(name, salary)
        """
        # Your code here
        pass

    def code(self):
        """
        Print a message about coding.

        Returns:
            str: "{name} is coding in {programming_language}"

        Example:
            dev = Developer("Alice", 7000, "Python")
            dev.code() → "Alice is coding in Python"
        """
        # Your code here
        pass


# ============================================================================
# PART 2: Advanced Inheritance - Animal Hierarchy
# ============================================================================


class Animal:
    """
    Base class for all animals.
    Every animal has a name and can make a sound.
    """

    def __init__(self, name):
        """
        Initialize Animal with name.

        Args:
            name (str): Animal's name
        """
        # Your code here
        pass

    def speak(self):
        """
        Generic speak method. Should be overridden by child classes.

        Returns:
            str: "{name} makes a sound"
        """
        # Your code here
        pass


class Dog(Animal):
    """
    Dog class inherits from Animal.
    Dogs can bark and have a breed.
    """

    def __init__(self, name, breed):
        """
        Initialize Dog.

        Args:
            name (str): Dog's name
            breed (str): Dog's breed

        Hint: Use super().__init__(name)
        """
        # Your code here
        pass

    def speak(self):
        """
        Override speak method for dogs.

        Returns:
            str: "{name} says Woof!"

        Example:
            dog = Dog("Buddy", "Golden Retriever")
            dog.speak() → "Buddy says Woof!"
        """
        # Your code here
        pass

    def get_breed(self):
        """
        Return the dog's breed.

        Returns:
            str: The breed
        """
        # Your code here
        pass


class Cat(Animal):
    """
    Cat class inherits from Animal.
    Cats can meow and have indoor/outdoor status.
    """

    def __init__(self, name, is_indoor):
        """
        Initialize Cat.

        Args:
            name (str): Cat's name
            is_indoor (bool): True if indoor cat, False if outdoor
        """
        # Your code here
        pass

    def speak(self):
        """
        Override speak method for cats.

        Returns:
            str: "{name} says Meow!"
        """
        # Your code here
        pass

    def get_location(self):
        """
        Return if cat is indoor or outdoor.

        Returns:
            str: "{name} is an indoor cat" or "{name} is an outdoor cat"
        """
        # Your code here
        pass


# ============================================================================
# PART 3: Method Overriding with super()
# ============================================================================


class Vehicle:
    """
    Base class for vehicles.
    All vehicles have make, model, year.
    """

    def __init__(self, make, model, year):
        """Initialize Vehicle."""
        # Your code here
        pass

    def start(self):
        """
        Start the vehicle.

        Returns:
            str: "{year} {make} {model} is starting..."
        """
        # Your code here
        pass

    def get_info(self):
        """
        Get vehicle information.

        Returns:
            str: "{year} {make} {model}"
        """
        # Your code here
        pass


class ElectricCar(Vehicle):
    """
    Electric car with battery capacity.
    Overrides start() to include battery check.
    """

    def __init__(self, make, model, year, battery_capacity):
        """
        Initialize ElectricCar.

        Args:
            make (str): Car make
            model (str): Car model
            year (int): Manufacturing year
            battery_capacity (int): Battery capacity in kWh
        """
        # Your code here
        pass

    def start(self):
        """
        Override start to include battery check.
        Should call parent's start() and add battery info.

        Returns:
            str: Parent start message + "\nBattery: {battery_capacity} kWh"

        Example:
            car = ElectricCar("Tesla", "Model 3", 2023, 75)
            car.start() → "2023 Tesla Model 3 is starting...\nBattery: 75 kWh"

        Hint: Use super().start() to get parent's message
        """
        # Your code here
        pass

    def charge(self):
        """
        Charge the electric car.

        Returns:
            str: "Charging {make} {model}..."
        """
        # Your code here
        pass


# ============================================================================
# PART 4: Testing Inheritance with isinstance()
# ============================================================================


def describe_employee(employee):
    """
    Describe an employee using isinstance() to check type.

    Args:
        employee: An Employee, Manager, or Developer instance

    Returns:
        str: Description based on type

    Rules:
    - If Manager: "Manager in {department}"
    - If Developer: "Developer coding in {language}"
    - If Employee (base): "Employee"

    Example:
        emp = Employee("John", 5000)
        describe_employee(emp) → "Employee"

        mgr = Manager("Jane", 8000, "Sales")
        describe_employee(mgr) → "Manager in Sales"

        dev = Developer("Alice", 7000, "Python")
        describe_employee(dev) → "Developer coding in Python"

    Hint: Check isinstance() in order: Manager first, then Developer, then Employee
          (because Manager and Developer ARE ALSO Employee)
    """
    # Your code here
    pass


# ============================================================================
# TESTS
# ============================================================================

print("=== PART 1: Basic Inheritance ===")
emp = Employee("John", 5000)
print(emp.display_info())
# Expected: "Name: John, Salary: $5000"

print(emp.get_annual_salary())
# Expected: 60000

mgr = Manager("Jane", 8000, "Sales")
print(mgr.display_info())
# Expected: "Name: Jane, Salary: $8000, Department: Sales"

print(mgr.get_annual_salary())
# Expected: 96000

dev = Developer("Alice", 7000, "Python")
print(dev.display_info())
# Expected: "Name: Alice, Salary: $7000"

print(dev.code())
# Expected: "Alice is coding in Python"
print()

print("=== PART 2: Animal Hierarchy ===")
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())
# Expected: "Buddy says Woof!"

print(dog.get_breed())
# Expected: "Golden Retriever"

cat = Cat("Whiskers", True)
print(cat.speak())
# Expected: "Whiskers says Meow!"

print(cat.get_location())
# Expected: "Whiskers is an indoor cat"
print()

print("=== PART 3: Method Overriding ===")
car = ElectricCar("Tesla", "Model 3", 2023, 75)
print(car.start())
# Expected:
# "2023 Tesla Model 3 is starting...
# Battery: 75 kWh"

print(car.charge())
# Expected: "Charging Tesla Model 3..."

print(car.get_info())
# Expected: "2023 Tesla Model 3"
print()

print("=== PART 4: isinstance() Tests ===")
print(describe_employee(emp))
# Expected: "Employee"

print(describe_employee(mgr))
# Expected: "Manager in Sales"

print(describe_employee(dev))
# Expected: "Developer coding in Python"

# isinstance checks
print(isinstance(mgr, Manager))   # True
print(isinstance(mgr, Employee))  # True (Manager IS-A Employee)
print(isinstance(emp, Manager))   # False
