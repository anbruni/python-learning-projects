# Python OOP - Guida Completa

## 🎯 Cos'è OOP (Object-Oriented Programming)?

**Definizione:** Paradigma di programmazione basato su **oggetti** che combinano dati (attributi) e comportamenti (metodi).

**I 4 pilastri di OOP:**
1. **Encapsulation** (Incapsulamento): Nascondere dettagli interni
2. **Inheritance** (Ereditarietà): Riutilizzare codice tramite gerarchie
3. **Polymorphism** (Polimorfismo): Stessi metodi, comportamenti diversi
4. **Abstraction** (Astrazione): Semplificare complessità

---

## 📦 1. Classes & Objects Basics

### Cos'è una Class?

Una **classe** è un **blueprint** (progetto) per creare oggetti.

```python
# Definire una classe
class Dog:
    pass  # Classe vuota

# Creare oggetti (istanze)
dog1 = Dog()
dog2 = Dog()

print(type(dog1))  # <class '__main__.Dog'>
```

### Anatomy di una Class

```python
class Dog:
    # Class attribute (condiviso da tutte le istanze)
    species = "Canis familiaris"
    
    # Constructor (metodo speciale)
    def __init__(self, name, age):
        # Instance attributes (specifici per ogni oggetto)
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # Instance method
    def get_info(self):
        return f"{self.name} is {self.age} years old"

# Creare istanze
buddy = Dog("Buddy", 3)
max_dog = Dog("Max", 5)

# Usare metodi
print(buddy.bark())        # "Buddy says Woof!"
print(max_dog.get_info())  # "Max is 5 years old"

# Accedere attributi
print(buddy.name)          # "Buddy"
print(Dog.species)         # "Canis familiaris"
```

---

## 🔧 2. `__init__` e `self`

### `__init__` (Constructor)

Metodo speciale chiamato **automaticamente** quando crei un'istanza.

```python
class User:
    def __init__(self, username, email):
        print("Constructor called!")
        self.username = username
        self.email = email

user = User("alice", "alice@example.com")
# Output: "Constructor called!"
print(user.username)  # "alice"
```

**IMPORTANTE:** `__init__` **NON è un constructor** (tecnicamente Python usa `__new__`), ma si comporta come tale. È un **initializer**.

### `self` (riferimento all'istanza corrente)

`self` è come `this` in JavaScript, ma **DEVI scriverlo esplicitamente**.

```python
class Counter:
    def __init__(self):
        self.count = 0  # self.count = attributo dell'istanza
    
    def increment(self):
        self.count += 1  # Accesso a self.count
    
    def get_count(self):
        return self.count

counter = Counter()
counter.increment()
print(counter.get_count())  # 1
```

**Confronto con JavaScript:**
```javascript
// JavaScript
class Counter {
    constructor() {
        this.count = 0;  // 'this' implicito
    }
    
    increment() {
        this.count += 1;  // 'this' implicito
    }
}
```

```python
# Python
class Counter:
    def __init__(self):
        self.count = 0  # 'self' ESPLICITO
    
    def increment(self):
        self.count += 1  # 'self' ESPLICITO
```

---

## 📊 3. Instance vs Class Attributes

### Instance Attributes (attributi di istanza)

**Specifici per ogni oggetto.** Definiti in `__init__` con `self.`.

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

alice = Person("Alice", 25)
bob = Person("Bob", 30)

print(alice.name)  # "Alice"
print(bob.name)    # "Bob"  ← Diversi!
```

### Class Attributes (attributi di classe)

**Condivisi da TUTTE le istanze.** Definiti a livello di classe.

```python
class Circle:
    pi = 3.14159  # Class attribute (condiviso)
    
    def __init__(self, radius):
        self.radius = radius  # Instance attribute
    
    def area(self):
        return Circle.pi * self.radius ** 2

c1 = Circle(5)
c2 = Circle(10)

# Class attribute accessibile da classe e istanze
print(Circle.pi)  # 3.14159
print(c1.pi)      # 3.14159
print(c2.pi)      # 3.14159  ← Stesso valore per tutti!

# Instance attribute diverso per ogni istanza
print(c1.radius)  # 5
print(c2.radius)  # 10  ← Diversi!
```

### Quando usare cosa?

| Use Case | Tipo | Esempio |
|----------|------|---------|
| Dati specifici oggetto | Instance | `self.name`, `self.age` |
| Costanti condivise | Class | `Circle.pi`, `MAX_SIZE` |
| Contatori globali | Class | `total_users` |
| Config comune | Class | `default_timeout` |

### Esempio pratico: Counter

```python
class Student:
    total_students = 0  # Class attribute (counter)
    
    def __init__(self, name):
        self.name = name  # Instance attribute
        Student.total_students += 1  # Incrementa counter
    
    @classmethod
    def get_total(cls):
        return cls.total_students

s1 = Student("Alice")
s2 = Student("Bob")
s3 = Student("Charlie")

print(Student.get_total())  # 3
```

---

## 🔨 4. Methods: Instance, Class, Static

### Instance Methods (metodi di istanza)

**Default.** Operano su dati dell'istanza tramite `self`.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    # Instance method
    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount(100)
account.deposit(50)
print(account.balance)  # 150
```

### Class Methods (`@classmethod`)

Operano su **dati della classe**, non dell'istanza. Ricevono `cls` invece di `self`.

```python
class Employee:
    company_name = "TechCorp"
    total_employees = 0
    
    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1
    
    @classmethod
    def get_company_info(cls):
        return f"{cls.company_name} has {cls.total_employees} employees"
    
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

emp1 = Employee("Alice")
emp2 = Employee("Bob")

print(Employee.get_company_info())  # "TechCorp has 2 employees"
Employee.change_company_name("NewCorp")
print(Employee.company_name)  # "NewCorp"
```

**Use case comune: Alternative constructors**

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        # Alternative constructor da string
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        # Alternative constructor con data odierna
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)

# Regular constructor
date1 = Date(2024, 5, 3)

# Alternative constructors
date2 = Date.from_string("2024-05-03")
date3 = Date.today()
```

### Static Methods (`@staticmethod`)

**NON ricevono né `self` né `cls`.** Sono funzioni utility legate alla classe.

```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def is_even(n):
        return n % 2 == 0

# Chiamati dalla classe (no istanza necessaria)
print(Math.add(5, 3))      # 8
print(Math.is_even(4))     # True

# Possono essere chiamati anche da istanza (ma raro)
m = Math()
print(m.add(10, 20))  # 30
```

### Confronto: Quando usare cosa?

```python
class Example:
    class_var = "shared"
    
    def __init__(self, instance_var):
        self.instance_var = instance_var
    
    # Instance method: usa SELF (dati istanza)
    def instance_method(self):
        return f"Instance: {self.instance_var}"
    
    # Class method: usa CLS (dati classe)
    @classmethod
    def class_method(cls):
        return f"Class: {cls.class_var}"
    
    # Static method: NO self, NO cls (utility function)
    @staticmethod
    def static_method(x):
        return f"Static: {x * 2}"

obj = Example("data")
print(obj.instance_method())     # Needs instance
print(Example.class_method())    # Can call from class
print(Example.static_method(5))  # Pure utility function
```

| Metodo | Riceve | Accede a | Quando usare |
|--------|--------|----------|--------------|
| Instance | `self` | Instance attributes | Operazioni su dati oggetto |
| Class | `cls` | Class attributes | Alternative constructors, class-level ops |
| Static | Niente | Niente (solo args) | Utility functions |

---

## 🔐 5. Encapsulation & Properties

### Encapsulation (Nascondere dati interni)

In Python, l'encapsulation è **convenzionale**, non forzata dal linguaggio.

### Convenzioni: `_` e `__`

```python
class BankAccount:
    def __init__(self, balance):
        self.public = "Everyone can see"
        self._protected = "Internal use (convention)"
        self.__private = "Name mangling (rare)"

account = BankAccount(100)

# Tutti accessibili (Python si fida di te!)
print(account.public)      # ✅ OK
print(account._protected)  # ⚠️ Funziona, ma convenzione dice "don't touch"
print(account._BankAccount__private)  # ✅ Name mangling bypass
```

**Convenzione:**
- `attribute` → Public
- `_attribute` → "Internal use" (convenzione, non enforcement)
- `__attribute` → Name mangling (rare, evita collisioni in ereditarietà)

### Properties (`@property`)

**Property** = metodo che si comporta come un attributo.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # "Private" attribute
    
    @property
    def celsius(self):
        """Getter"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Uso (sembra un attributo!)
temp = Temperature(25)
print(temp.celsius)     # 25 (chiama getter)
print(temp.fahrenheit)  # 77.0 (computed)

temp.celsius = 30       # Chiama setter
print(temp.celsius)     # 30

temp.fahrenheit = 86    # Converte automaticamente
print(temp.celsius)     # 30

# temp.celsius = -300   # ValueError!
```

**Vantaggi @property:**
- ✅ Sintassi attributo (no parentesi)
- ✅ Validazione nei setter
- ✅ Computed values (fahrenheit calcolato da celsius)
- ✅ Backward compatibility (puoi aggiungere logic senza cambiare API)

### Confronto con JavaScript

```javascript
// JavaScript (getter/setter)
class Temperature {
    constructor(celsius) {
        this._celsius = celsius;
    }
    
    get celsius() {
        return this._celsius;
    }
    
    set celsius(value) {
        if (value < -273.15) throw new Error("Too cold!");
        this._celsius = value;
    }
}

const temp = new Temperature(25);
console.log(temp.celsius);  // 25
temp.celsius = 30;          // Setter
```

Python properties sono simili a getter/setter JS!

---

## 🧬 6. Inheritance (Ereditarietà)

**Inheritance** = una classe (child) eredita attributi/metodi da un'altra (parent).

### Basic Inheritance

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

# Child class
class Dog(Animal):  # ← Eredita da Animal
    def bark(self):
        return f"{self.name} barks"

dog = Dog("Buddy")
print(dog.speak())  # Ereditato da Animal
print(dog.bark())   # Definito in Dog
```

### `super()` - Chiamare metodi Parent

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_info(self):
        return f"{self.name}: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # ← Chiama __init__ parent
        self.department = department
    
    def get_info(self):
        parent_info = super().get_info()  # ← Chiama get_info parent
        return f"{parent_info}, Dept: {self.department}"

mgr = Manager("Alice", 80000, "Sales")
print(mgr.get_info())  # "Alice: $80000, Dept: Sales"
```

### Method Overriding

Child può **sostituire** metodi parent.

```python
class Animal:
    def speak(self):
        return "Generic sound"

class Dog(Animal):
    def speak(self):  # Override
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Override
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())  # "Woof!"
print(cat.speak())  # "Meow!"
```

### Multiple Inheritance (avanzato)

Python supporta eredità multipla (JavaScript no!).

```python
class Flyable:
    def fly(self):
        return "Flying!"

class Swimmable:
    def swim(self):
        return "Swimming!"

class Duck(Flyable, Swimmable):  # Eredita da entrambe
    pass

duck = Duck()
print(duck.fly())   # "Flying!"
print(duck.swim())  # "Swimming!"
```

**⚠️ Multiple inheritance è potente ma complesso.** Usa con cautela.

---

## 🦆 7. Polymorphism (Polimorfismo)

**Polymorphism** = stessi metodi, comportamenti diversi in base al tipo.

### Duck Typing

"If it walks like a duck and quacks like a duck, it's a duck."

Python non controlla il tipo, controlla solo se il metodo esiste.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Car:
    def drive(self):
        return "Vroom!"

# Funzione polimorfica
def make_speak(animal):
    return animal.speak()  # Chiama speak() su qualsiasi oggetto

dog = Dog()
cat = Cat()
car = Car()

print(make_speak(dog))  # "Woof!"
print(make_speak(cat))  # "Meow!"
# print(make_speak(car))  # AttributeError (no speak method)
```

**No type checking!** Python si fida che l'oggetto abbia il metodo.

### Polymorphism con Inheritance

```python
class Payment:
    def process(self, amount):
        raise NotImplementedError("Subclass must implement")

class CreditCard(Payment):
    def process(self, amount):
        return f"Charged ${amount} to credit card"

class PayPal(Payment):
    def process(self, amount):
        return f"Sent ${amount} via PayPal"

class Bitcoin(Payment):
    def process(self, amount):
        return f"Transferred {amount} BTC"

# Funzione polimorfica
def checkout(payment_method, amount):
    print(payment_method.process(amount))

# Stesso codice, comportamenti diversi!
checkout(CreditCard(), 100)  # Credit card
checkout(PayPal(), 50)       # PayPal
checkout(Bitcoin(), 0.5)     # Bitcoin
```

**Key:** Tutte le classi hanno metodo `process()`, ma implementazioni diverse.

---

## ✨ 8. Magic Methods (Dunder Methods)

**Magic methods** = metodi speciali con `__` che Python chiama automaticamente.

### Metodi comuni

```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # String representation (per utenti)
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # String representation (per developer)
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
    
    # Addition
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    # Multiplication by scalar
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    # Equality
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Length
    def __len__(self):
        import math
        return int(math.sqrt(self.x**2 + self.y**2))

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(v1)           # (3, 4)  ← Chiama __str__
print(repr(v1))     # Vector2D(3, 4)  ← Chiama __repr__
print(v1 + v2)      # (4, 6)  ← Chiama __add__
print(v1 * 2)       # (6, 8)  ← Chiama __mul__
print(v1 == v2)     # False  ← Chiama __eq__
print(len(v1))      # 5  ← Chiama __len__
```

### Magic Methods Reference

| Metodo | Operatore/Funzione | Quando chiamato |
|--------|-------------------|-----------------|
| `__init__` | - | Constructor |
| `__str__` | `print()`, `str()` | String utente |
| `__repr__` | `repr()` | String developer |
| `__len__` | `len()` | Lunghezza |
| `__add__` | `+` | Addizione |
| `__sub__` | `-` | Sottrazione |
| `__mul__` | `*` | Moltiplicazione |
| `__eq__` | `==` | Uguaglianza |
| `__lt__` | `<` | Less than |
| `__gt__` | `>` | Greater than |
| `__getitem__` | `[]` | Accesso indice |
| `__setitem__` | `[] =` | Set indice |
| `__call__` | `()` | Chiamata come funzione |
| `__enter__/__exit__` | `with` | Context manager |

**Esempio pratico:**

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add(self, item, price):
        self.items.append((item, price))
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __str__(self):
        total = sum(price for _, price in self.items)
        return f"Cart with {len(self)} items, total: ${total}"

cart = ShoppingCart()
cart.add("Apple", 1.5)
cart.add("Banana", 0.5)

print(len(cart))     # 2  ← __len__
print(cart[0])       # ('Apple', 1.5)  ← __getitem__
print(cart)          # Cart with 2 items, total: $2.0  ← __str__
```

---

## 🏗️ 9. Composition vs Inheritance

### "Prefer composition over inheritance"

**Inheritance** = "IS-A" relationship  
**Composition** = "HAS-A" relationship

### Inheritance (IS-A)

```python
class Animal:
    def eat(self):
        return "Eating..."

class Dog(Animal):  # Dog IS-A Animal
    def bark(self):
        return "Woof!"

dog = Dog()
dog.eat()   # Inherited
dog.bark()  # Own method
```

### Composition (HAS-A)

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine with {self.horsepower}hp started"

class Car:
    def __init__(self, engine_hp):
        self.engine = Engine(engine_hp)  # Car HAS-A Engine
    
    def start(self):
        return self.engine.start()

car = Car(200)
print(car.start())  # Delegated to engine
```

### Quando usare Composition?

✅ **Composition quando:**
- "HAS-A" relationship (Car HAS Engine)
- Vuoi flessibilità (swap components)
- Multiple unrelated behaviors

❌ **Inheritance quando:**
- "IS-A" relationship (Dog IS Animal)
- Chiara gerarchia
- Vuoi polymorphism

**Esempio: Car con Composition**

```python
class Engine:
    def start(self):
        return "Engine started"

class Wheel:
    def rotate(self):
        return "Wheel rotating"

class Car:
    def __init__(self):
        self.engine = Engine()       # HAS-A Engine
        self.wheels = [Wheel() for _ in range(4)]  # HAS 4 Wheels
    
    def start(self):
        return self.engine.start()
    
    def drive(self):
        results = [wheel.rotate() for wheel in self.wheels]
        return f"Driving: {results}"

car = Car()
print(car.start())  # "Engine started"
print(car.drive())  # "Driving: [...]"
```

---

## 🎭 10. Abstract Base Classes (ABC)

**Abstract class** = classe che non può essere istanziata, serve come template.

```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        """Must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Must be implemented by subclasses"""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()  # ❌ TypeError: Can't instantiate abstract class

circle = Circle(5)
print(circle.area())  # 78.54

rectangle = Rectangle(4, 6)
print(rectangle.perimeter())  # 20

# Polymorphism
def print_shape_info(shape):
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")

print_shape_info(circle)
print_shape_info(rectangle)
```

**Quando usare ABC:**
- ✅ Vuoi forzare child classes a implementare metodi
- ✅ Vuoi creare interfacce/contratti
- ✅ Framework/library design

---

## 🆚 11. Python OOP vs JavaScript OOP

### Syntax Comparison

```javascript
// JavaScript (ES6)
class Animal {
    constructor(name) {
        this.name = name;
    }
    
    speak() {
        console.log(`${this.name} makes a sound`);
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
    
    speak() {
        console.log(`${this.name} barks`);
    }
}

const dog = new Dog("Buddy", "Golden");
dog.speak();
```

```python
# Python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} barks")

dog = Dog("Buddy", "Golden")
dog.speak()
```

### Key Differences

| Feature | Python | JavaScript |
|---------|--------|-----------|
| Constructor | `__init__(self)` | `constructor()` |
| Self reference | `self` (explicit) | `this` (implicit) |
| Inheritance | `class Child(Parent)` | `class Child extends Parent` |
| Super | `super().__init__()` | `super()` |
| Private | `_attr` (convention) | `#attr` (enforced) |
| Static method | `@staticmethod` | `static method()` |
| Class method | `@classmethod` | No equivalent |
| Properties | `@property` | `get/set` |
| Multiple inheritance | ✅ Yes | ❌ No |
| Duck typing | ✅ Yes | ❌ No (TypeScript helps) |

---

## ⚠️ 12. Common Gotchas

### 1. Mutable Default Arguments

```python
# ❌ SBAGLIATO
class MyClass:
    def __init__(self, items=[]):  # ❌ Lista condivisa!
        self.items = items

obj1 = MyClass()
obj2 = MyClass()
obj1.items.append(1)
print(obj2.items)  # [1] ← Condivisa!

# ✅ CORRETTO
class MyClass:
    def __init__(self, items=None):
        self.items = items if items is not None else []

obj1 = MyClass()
obj2 = MyClass()
obj1.items.append(1)
print(obj2.items)  # [] ← Separata!
```

### 2. Forgetting `self`

```python
# ❌ SBAGLIATO
class Counter:
    def __init__(self):
        count = 0  # ❌ Locale, non self.count!
    
    def increment(self):
        self.count += 1  # AttributeError!

# ✅ CORRETTO
class Counter:
    def __init__(self):
        self.count = 0  # ✅ Instance attribute
    
    def increment(self):
        self.count += 1
```

### 3. Shadowing Class Attributes

```python
class MyClass:
    shared = []  # Class attribute
    
    def add(self, item):
        self.shared.append(item)  # Modifica class attribute!

obj1 = MyClass()
obj2 = MyClass()
obj1.add(1)
print(obj2.shared)  # [1] ← Condiviso!

# Soluzione: usa instance attribute
class MyClass:
    def __init__(self):
        self.items = []  # Instance attribute
```

### 4. Using `__` Unnecessarily

```python
# ❌ Overkill
class User:
    def __init__(self, name):
        self.__name = name  # Name mangling non necessario

# ✅ Sufficiente
class User:
    def __init__(self, name):
        self._name = name  # Convenzione basta
```

---

## 📝 Best Practices

### ✅ DO:

```python
# 1. Usa nomi descrittivi
class BankAccount:  # ✅ Chiaro
    pass

# 2. Single Responsibility Principle
class User:
    def save_to_db(self):  # ❌ User should not handle DB
        pass

class UserRepository:
    def save(self, user):  # ✅ Separato
        pass

# 3. Usa @property per computed values
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):  # ✅ Computed on-the-fly
        return 3.14159 * self.radius ** 2

# 4. Usa __str__ e __repr__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# 5. Prefer composition over inheritance (quando ha senso)
```

### ❌ DON'T:

```python
# 1. Non creare God classes (troppo responsabilità)
class Application:  # ❌ Fa troppo
    def connect_db(self): pass
    def send_email(self): pass
    def render_ui(self): pass
    def process_payment(self): pass

# 2. Non abusare di inheritance
class Button(Widget, Clickable, Draggable, Resizable):  # ❌ Troppo!
    pass

# 3. Non usare __name per tutto
class MyClass:
    def __init__(self):
        self.__x = 1  # ❌ Overkill
        self.__y = 2  # ❌ Overkill

# 4. Non dimenticare super() in __init__
class Child(Parent):
    def __init__(self, x):
        # super().__init__()  # ❌ Dimenticato!
        self.x = x
```

---

## 📚 Quick Reference

```python
# Class definition
class MyClass:
    class_attribute = "shared"
    
    def __init__(self, value):
        self.instance_attribute = value
    
    def instance_method(self):
        return self.instance_attribute
    
    @classmethod
    def class_method(cls):
        return cls.class_attribute
    
    @staticmethod
    def static_method(x):
        return x * 2
    
    @property
    def computed(self):
        return self.instance_attribute * 2

# Inheritance
class Child(Parent):
    def __init__(self, x):
        super().__init__(x)
    
    def method(self):
        super().method()  # Call parent

# Magic methods
def __str__(self): return "string"
def __repr__(self): return "repr"
def __eq__(self, other): return True
def __add__(self, other): return result

# Abstract class
from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def must_implement(self):
        pass
```

---

## 🎓 Recap

**Fondamentali:**
- Classes & Objects (blueprint → instances)
- `__init__` e `self`
- Instance vs Class attributes
- Instance/Class/Static methods
- Encapsulation (`_private`, `@property`)
- Inheritance & `super()`
- Polymorphism (duck typing)
- Magic methods (`__str__`, `__add__`, etc.)

**Patterns:**
- Composition over inheritance (quando appropriato)
- Abstract Base Classes (interfacce)
- Properties per computed values
- Class methods per alternative constructors

**Prossimi passi:**
- Pratica con esercizi OOP (Exercise 7-15)
- Leggi codebases altrui per vedere pattern
- Progetta classi per progetti reali
- Evita over-engineering (KISS principle)
