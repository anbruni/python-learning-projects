# Python OOP Learning Plan
## From Beginner to Advanced

---

## Exercise 7: Introduction to Classes and Objects
**Difficulty:** Beginner

### Concepts:
- **Class**: A blueprint for creating objects (like a template)
- **Object/Instance**: A specific example created from a class
- **Attributes**: Variables that belong to an object
- **Methods**: Functions that belong to a class
- **`__init__`**: Special method (constructor) that runs when you create an object
- **`self`**: Reference to the current instance (like `this` in JavaScript)

### Exercise Description:
Create a `BankAccount` class that models a simple bank account. Each account should have:
- Owner name (attribute)
- Balance (attribute, starts at 0)
- Methods to deposit, withdraw, and check balance
- A method to display account info

**Example usage:**
```python
account = BankAccount("Alice")
account.deposit(100)
account.withdraw(30)
print(account.get_balance())  # 70
account.display_info()  # "Account owner: Alice, Balance: $70"
```

---

## Exercise 8: Instance vs Class Attributes
**Difficulty:** Beginner+

### Concepts:
- **Instance attributes**: Belong to each individual object (defined in `__init__`)
- **Class attributes**: Shared by ALL instances of the class (defined at class level)
- **Class methods**: Methods that work with class-level data (use `@classmethod`)
- **Static methods**: Utility functions that don't need instance or class data (use `@staticmethod`)

### Exercise Description:
Create a `Student` class for a school system:
- Instance attributes: name, grade
- Class attribute: `total_students` (tracks how many students exist)
- Class method: `get_total_students()` returns the count
- Static method: `is_passing_grade(grade)` returns True if grade >= 60
- Instance method: `display_info()`

Every time you create a student, increment `total_students`.

**Example usage:**
```python
s1 = Student("Bob", 85)
s2 = Student("Carol", 55)
print(Student.get_total_students())  # 2
print(Student.is_passing_grade(85))  # True
print(s2.is_passing_grade(s2.grade))  # False
```

---

## Exercise 9: Encapsulation and Properties
**Difficulty:** Intermediate

### Concepts:
- **Encapsulation**: Hiding internal data from direct access
- **Private attributes**: Use `_` prefix (convention) or `__` prefix (name mangling)
- **Getter/Setter**: Methods to control access to private attributes
- **`@property`**: Decorator to make a method look like an attribute
- **`@attribute.setter`**: Decorator to control how an attribute is set

### Exercise Description:
Create a `Temperature` class that stores temperature in Celsius but allows getting/setting in both Celsius and Fahrenheit:
- Private attribute: `_celsius`
- Property: `celsius` (get and set)
- Property: `fahrenheit` (get and set, converts to/from Celsius)
- Validation: Temperature cannot go below absolute zero (-273.15°C)

**Example usage:**
```python
temp = Temperature(25)
print(temp.celsius)  # 25
print(temp.fahrenheit)  # 77.0
temp.fahrenheit = 86
print(temp.celsius)  # 30
temp.celsius = -300  # Should raise ValueError
```

---

## Exercise 10: Inheritance
**Difficulty:** Intermediate

### Concepts:
- **Inheritance**: Creating a new class based on an existing class
- **Parent/Base class**: The class being inherited from
- **Child/Derived class**: The class that inherits
- **`super()`**: Call the parent class's methods
- **Method overriding**: Child class replaces parent's method

### Exercise Description:
Create an `Employee` hierarchy:
- Base class `Employee`: name, salary, `get_annual_salary()`, `display_info()`
- Child class `Manager` (inherits Employee): adds `department` attribute, overrides `display_info()`
- Child class `Developer` (inherits Employee): adds `programming_language`, adds `code()` method

**Example usage:**
```python
emp = Employee("John", 50000)
mgr = Manager("Jane", 80000, "Sales")
dev = Developer("Alice", 70000, "Python")

print(emp.get_annual_salary())  # 50000
mgr.display_info()  # Shows name, salary, AND department
dev.code()  # "Alice is coding in Python"
```

---

## Exercise 11: Polymorphism
**Difficulty:** Intermediate+

### Concepts:
- **Polymorphism**: Different classes respond to the same method in their own way
- **Duck typing**: "If it walks like a duck and quacks like a duck, it's a duck"
- **Method overriding**: Each child implements the same method differently

### Exercise Description:
Create a payment system with different payment methods:
- Base class `Payment`: has method `process_payment(amount)`
- Child `CreditCard`: overrides `process_payment()` to show "Charged $X to credit card"
- Child `PayPal`: overrides to show "Sent $X via PayPal"
- Child `Bitcoin`: overrides to show "Transferred X BTC"
- Function `checkout(payment_method, amount)` that works with ANY payment type

**Example usage:**
```python
def checkout(payment_method, amount):
    payment_method.process_payment(amount)

cc = CreditCard("1234-5678")
pp = PayPal("user@email.com")

checkout(cc, 100)  # "Charged $100 to credit card 1234-5678"
checkout(pp, 50)   # "Sent $50 via PayPal to user@email.com"
```

---

## Exercise 12: Magic/Dunder Methods
**Difficulty:** Intermediate+

### Concepts:
- **Magic methods**: Special methods with double underscores (dunder)
- **`__str__`**: String representation for users (used by `print()`)
- **`__repr__`**: String representation for developers (used by debugger)
- **`__len__`**: Makes `len(obj)` work
- **`__eq__`**: Defines equality (`==`)
- **`__lt__`, `__gt__`**: Comparison operators (`<`, `>`)
- **`__add__`**: Addition operator (`+`)

### Exercise Description:
Create a `Vector2D` class for 2D math:
- Attributes: x, y
- `__str__`: Returns "(x, y)"
- `__repr__`: Returns "Vector2D(x, y)"
- `__eq__`: Two vectors equal if x and y match
- `__add__`: Add two vectors component-wise
- `__mul__`: Multiply vector by a scalar
- `magnitude()`: Calculate length of vector

**Example usage:**
```python
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
print(v1)  # "(3, 4)"
print(v1 + v2)  # "(4, 6)"
print(v1 * 2)  # "(6, 8)"
print(v1.magnitude())  # 5.0
```

---

## Exercise 13: Composition Over Inheritance
**Difficulty:** Advanced

### Concepts:
- **Composition**: Building complex objects by combining simpler ones
- **"Has-a" relationship**: vs "Is-a" (inheritance)
- **Delegation**: Forwarding method calls to contained objects

### Exercise Description:
Create a `Car` class that uses composition (not inheritance):
- `Engine` class: horsepower, `start()`, `stop()`
- `Wheel` class: size, `rotate()`
- `Car` class: has ONE engine and FOUR wheels
- Car methods: `start()` (starts engine), `drive()` (rotates wheels), `get_specs()`

**Example usage:**
```python
car = Car(engine_hp=200, wheel_size=18)
car.start()  # Starts the engine
car.drive()  # Rotates all 4 wheels
car.get_specs()  # Shows engine and wheel info
```

---

## Exercise 14: Abstract Base Classes
**Difficulty:** Advanced

### Concepts:
- **Abstract class**: Cannot be instantiated, serves as template
- **Abstract method**: Must be implemented by child classes
- **`abc` module**: Python's built-in abstraction support
- **`@abstractmethod`**: Decorator to mark methods as required

### Exercise Description:
Create a shape hierarchy with enforced structure:
- Abstract base class `Shape`: abstract methods `area()`, `perimeter()`
- `Circle`: implements area and perimeter
- `Rectangle`: implements area and perimeter
- `Triangle`: implements area and perimeter
- Function `print_shape_info(shape)` that works with any shape

Trying to create a `Shape()` directly should raise an error.

**Example usage:**
```python
# shape = Shape()  # ERROR: Can't instantiate abstract class

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(circle.area())  # 78.54
print(rectangle.perimeter())  # 20
```

---

## Exercise 15: Putting It All Together - Library System
**Difficulty:** Advanced

### Concepts:
All previous concepts combined in a real-world scenario.

### Exercise Description:
Build a library management system:
- Abstract base class `LibraryItem`: title, item_id, `checkout()`, `return_item()`, `display_info()`
- `Book` (inherits LibraryItem): author, pages, genre
- `Magazine` (inherits LibraryItem): issue_number, publisher
- `DVD` (inherits LibraryItem): director, duration
- `Library` class: contains list of items, methods: `add_item()`, `remove_item()`, `find_by_title()`, `list_available()`
- `Member` class: name, member_id, checked_out_items (list)

Use:
- Inheritance for different item types
- Polymorphism (all items can be checked out the same way)
- Encapsulation (private member ID)
- Magic methods (`__str__` for nice display)
- Composition (Library HAS items)

**Example usage:**
```python
library = Library("City Library")
book = Book("1984", "B001", "George Orwell", 328, "Dystopian")
dvd = DVD("Inception", "D001", "Nolan", 148)

library.add_item(book)
library.add_item(dvd)

member = Member("Alice", "M001")
library.checkout_item("B001", member)
library.list_available()
```

---

## Learning Path Summary:
1. **Ex 7**: Basic classes, objects, methods
2. **Ex 8**: Class vs instance, different method types
3. **Ex 9**: Encapsulation, getters/setters, properties
4. **Ex 10**: Inheritance, super(), overriding
5. **Ex 11**: Polymorphism, duck typing
6. **Ex 12**: Magic methods, operator overloading
7. **Ex 13**: Composition pattern
8. **Ex 14**: Abstract classes, interfaces
9. **Ex 15**: Full integration project

Each exercise builds on previous concepts while introducing new ones!
