# Exercise 9: Encapsulation and Properties
# Difficulty: Intermediate

# CONCEPTS EXPLANATION:
#
# 1. ENCAPSULATION: Hiding internal data from direct access
#    - Protects data from invalid modifications
#    - Allows validation before setting values
#
# 2. PRIVATE ATTRIBUTES: Convention to indicate "don't touch this directly"
#    - Single underscore: _attribute (convention, not enforced)
#    - Double underscore: __attribute (name mangling, harder to access)
#    - Python doesn't have true private attributes like Java/C++
#
# 3. GETTER/SETTER: Methods to control access to attributes
#    - get_attribute(): returns the value
#    - set_attribute(value): sets the value with validation
#
# 4. @property: Decorator that makes a method look like an attribute
#    - Lets you call obj.attribute instead of obj.get_attribute()
#    - More Pythonic and cleaner syntax
#
# 5. @attribute.setter: Decorator to control how an attribute is set
#    - Lets you use obj.attribute = value with validation
#    - Works together with @property

# EXAMPLE - Understanding properties:
#
# class Person:
#     def __init__(self, name, age):
#         self._name = name    # Private by convention
#         self._age = age      # Private by convention
#
#     # Getter using @property
#     @property
#     def age(self):
#         return self._age
#
#     # Setter using @age.setter
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             raise ValueError("Age cannot be negative")
#         self._age = value
#
#     @property
#     def name(self):
#         return self._name
#
#     # name has no setter, so it's read-only
#
# # Usage:
# person = Person("Alice", 30)
# print(person.age)      # 30 (looks like attribute, but calls getter)
# person.age = 31        # Calls setter with validation
# print(person.age)      # 31
# person.age = -5        # Raises ValueError
# print(person.name)     # "Alice"
# person.name = "Bob"    # AttributeError (no setter defined)

# YOUR TASK:
# Create a Temperature class that stores temperature in Celsius
# but allows getting/setting in both Celsius and Fahrenheit.
#
# Requirements:
# - Private attribute: _celsius (the internal storage)
# - Property: celsius (get and set with validation)
# - Property: fahrenheit (get and set, converts to/from Celsius)
# - Validation: Temperature cannot go below absolute zero (-273.15°C)
# - Formulas:
#   - Fahrenheit to Celsius: (F - 32) * 5/9
#   - Celsius to Fahrenheit: (C * 9/5) + 32

class Temperature:

    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot go below absolute zero (-273.15°C)")
        self._celsius = value

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9


# --- Tests ---
# Create temperature object
temp = Temperature(25)
# print(f"Celsius: {temp.celsius}")      # Expected: 25
# print(f"Fahrenheit: {temp.fahrenheit}")  # Expected: 77.0

# # Set via Celsius
temp.celsius = 0
print(f"Celsius: {temp.celsius}")      # Expected: 0
# print(f"Fahrenheit: {temp.fahrenheit}")  # Expected: 32.0

# # Set via Fahrenheit
# temp.fahrenheit = 212
# print(f"Celsius: {temp.celsius}")      # Expected: 100.0
# print(f"Fahrenheit: {temp.fahrenheit}")  # Expected: 212.0

# # Set via Fahrenheit again
# temp.fahrenheit = 86
# print(f"Celsius: {temp.celsius}")      # Expected: 30.0
# print(f"Fahrenheit: {temp.fahrenheit}")  # Expected: 86.0

# # Test validation - try to set below absolute zero
# try:
#     temp.celsius = -300
#     print("ERROR: Should have raised ValueError!")
# except ValueError as e:
#     print(f"Correctly raised error: {e}")  # Expected: Error message

# # Test validation via Fahrenheit (below absolute zero)
# try:
#     temp.fahrenheit = -500
#     print("ERROR: Should have raised ValueError!")
# except ValueError as e:
#     print(f"Correctly raised error: {e}")  # Expected: Error message

# Verify temp still has valid value after failed attempts
print(f"Final temp: {temp.celsius}°C")  # Expected: 30.0 (unchanged from failed sets)
