# Exercise 7: Introduction to Classes and Objects
# Difficulty: Beginner

# CONCEPTS EXPLANATION:
#
# 1. CLASS: A blueprint/template for creating objects
#    Think of it like a cookie cutter - it defines the shape
#
# 2. OBJECT/INSTANCE: A specific thing created from the class
#    Like actual cookies made from the cookie cutter
#
# 3. __init__: Special method that runs when you CREATE an object
#    It's the constructor - sets up the initial state
#
# 4. self: Refers to the current instance
#    Like "this" in JavaScript - it's how methods access the object's data
#
# 5. INSTANCE ATTRIBUTES: Variables that belong to each object
#    Each object has its own copy
#
# 6. METHODS: Functions that belong to a class
#    They can access and modify the object's attributes

# EXAMPLE - Understanding the basics:
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name    # Instance attribute
#         self.age = age      # Instance attribute
#
#     def bark(self):         # Method
#         return f"{self.name} says woof!"
#
# # Creating instances (objects):
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Max", 5)
#
# print(dog1.name)  # "Buddy"
# print(dog2.bark())  # "Max says woof!"

# YOUR TASK:
# Create a BankAccount class that models a simple bank account.
#
# Requirements:
# - Attribute: owner (string, set in __init__)
# - Attribute: balance (number, starts at 0)
# - Method: deposit(amount) - adds amount to balance
# - Method: withdraw(amount) - subtracts amount from balance
#   (if enough money exists, otherwise print error)
# - Method: get_balance() - returns current balance
# - Method: display_info() - prints "Account owner: X, Balance: $Y"

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("Error")
    def get_balance(self):
        return self.balance
    def display_info(self):
        print(f"Account owner: {self.owner}, Balance: ${self.balance}")
    

# --- Tests ---
# Create an account for Alice
account = BankAccount("Alice")
# print(account.get_balance())  # Expected: 0

# Deposit money
account.deposit(100)
print(account.get_balance())  # Expected: 100

# # Withdraw money
account.withdraw(30)
print(account.get_balance())  # Expected: 70

# # Try to withdraw more than balance
account.withdraw(100)  # Expected: Error message

# # Display account info
account.display_info()  # Expected: "Account owner: Alice, Balance: $70"

# # Create another account (should be independent)
account2 = BankAccount("Bob")
account2.deposit(50)
print(account2.get_balance())  # Expected: 50
print(account.get_balance())  # Expected: 70 (Alice's account unchanged)
