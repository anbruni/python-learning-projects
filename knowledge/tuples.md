# Python Tuples - Guida Completa

## 🎯 Cos'è una Tuple?

**Definizione:** Una collezione **ordinata** e **immutabile** di elementi (possono essere di tipi diversi).

```python
# Tuple con tipi misti
my_tuple = (1, "hello", 3.14, True)
print(my_tuple)  # (1, "hello", 3.14, True)

# Tuple vuota
empty = ()

# Tuple con elementi dello stesso tipo (più comune)
coordinates = (10, 20)
rgb_color = (255, 128, 0)
```

**Differenza chiave con List:**
```python
# List (mutabile)
my_list = [1, 2, 3]
my_list[0] = 99      # ✅ Funziona
my_list.append(4)    # ✅ Funziona

# Tuple (immutabile)
my_tuple = (1, 2, 3)
# my_tuple[0] = 99   # ❌ TypeError: 'tuple' object does not support item assignment
# my_tuple.append(4) # ❌ AttributeError: 'tuple' object has no attribute 'append'
```

---

## 📊 Tuple vs List vs Set vs Dict

| Feature | Tuple | List | Set | Dict |
|---------|-------|------|-----|------|
| **Mutabile** | ❌ Immutabile | ✅ Modificabile | ✅ Modificabile | ✅ Modificabile |
| **Ordinato** | ✅ Mantiene ordine | ✅ Mantiene ordine | ❌ Non ordinato | ✅ (da Python 3.7+) |
| **Duplicati** | ✅ Permessi | ✅ Permessi | ❌ Rimossi auto | Chiavi uniche |
| **Indici** | ✅ `tuple[0]` | ✅ `list[0]` | ❌ No indici | ✅ `dict["key"]` |
| **Performance** | Veloce | Buona | O(1) lookup | O(1) lookup |
| **Memory** | Meno | Più | Media | Più |
| **Dict key** | ✅ Sì (se hashable) | ❌ No | ❌ No | N/A |
| **Uso** | Dati fissi | Dati dinamici | Unicità | Key-value |

---

## 🚀 Creare Tuple

### Metodo 1: Con parentesi (esplicito)

```python
# Tuple normale
point = (3, 5)
person = ("Alice", 25, "Engineer")

# Tuple con un elemento (SERVE LA VIRGOLA!)
single = (42,)      # ✅ Tuple con un elemento
not_tuple = (42)    # ❌ Questo è solo un int in parentesi!

print(type(single))     # <class 'tuple'>
print(type(not_tuple))  # <class 'int'>

# Perché la virgola? Disambiguazione
result = (2 + 3)      # 5 (int)
result = (2 + 3,)     # (5,) (tuple)
```

### Metodo 2: Senza parentesi (tuple packing)

```python
# Python capisce che è una tuple dalle virgole
point = 3, 5           # Stesso di (3, 5)
person = "Alice", 25   # Stesso di ("Alice", 25)

print(type(point))  # <class 'tuple'>

# Singolo elemento
single = 42,  # (42,)
```

### Metodo 3: Constructor tuple()

```python
# Da lista
from_list = tuple([1, 2, 3])  # (1, 2, 3)

# Da stringa
from_string = tuple("abc")  # ('a', 'b', 'c')

# Da range
from_range = tuple(range(5))  # (0, 1, 2, 3, 4)

# Tuple vuota
empty = tuple()  # ()
```

### Metodo 4: Tuple comprehension? NO!

```python
# ❌ Questo crea un GENERATOR, non una tuple!
gen = (x**2 for x in range(5))
print(type(gen))  # <class 'generator'>

# ✅ Devi convertire esplicitamente
my_tuple = tuple(x**2 for x in range(5))
print(my_tuple)  # (0, 1, 4, 9, 16)
```

---

## 🔒 Immutabilità

### Cosa significa immutabile?

```python
# NON puoi modificare elementi
my_tuple = (1, 2, 3)
# my_tuple[0] = 99  # ❌ TypeError!

# NON puoi aggiungere/rimuovere elementi
# my_tuple.append(4)  # ❌ AttributeError!
# my_tuple.remove(2)  # ❌ AttributeError!

# NON puoi ordinare in place
# my_tuple.sort()  # ❌ AttributeError!
```

### ⚠️ Gotcha: Nested mutable objects

```python
# Tuple con lista dentro
my_tuple = ([1, 2], [3, 4])

# ❌ NON puoi modificare la tuple
# my_tuple[0] = [99, 99]  # TypeError!

# ✅ MA puoi modificare la LISTA dentro la tuple!
my_tuple[0].append(99)
print(my_tuple)  # ([1, 2, 99], [3, 4])
```

**Perché?** La tuple è immutabile (non puoi cambiare QUALE oggetto contiene), ma gli oggetti DENTRO possono essere mutabili.

```python
# Visualizzazione:
my_tuple = ([1, 2], [3, 4])
#           ↑       ↑
#           reference a lista (non cambia)
#           ma il CONTENUTO della lista può cambiare!
```

### Creare nuove tuple (workaround)

```python
# Non puoi modificare, ma puoi creare NUOVE tuple
original = (1, 2, 3)

# Aggiungere elemento (crea nuova tuple)
new_tuple = original + (4,)
print(new_tuple)  # (1, 2, 3, 4)
print(original)   # (1, 2, 3) ← intatto

# Concatenazione
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = (1, 2) * 3
print(repeated)  # (1, 2, 1, 2, 1, 2)

# Slicing (crea nuova tuple)
my_tuple = (1, 2, 3, 4, 5)
sub_tuple = my_tuple[1:4]
print(sub_tuple)  # (2, 3, 4)
```

---

## 📦 Tuple Packing

**Tuple packing** = raggruppare valori in una tuple (senza parentesi).

```python
# Packing (implicito)
point = 3, 5              # Tuple (3, 5)
person = "Alice", 25      # Tuple ("Alice", 25)

print(type(point))  # <class 'tuple'>

# Multiple return values (pattern comune!)
def get_coordinates():
    return 10, 20  # Packing: ritorna (10, 20)

result = get_coordinates()
print(result)  # (10, 20)
print(type(result))  # <class 'tuple'>
```

---

## 📤 Tuple Unpacking

**Tuple unpacking** = estrarre valori da una tuple in variabili separate.

### Basic Unpacking

```python
# Crea tuple
point = (3, 5)

# Unpacking
x, y = point
print(x)  # 3
print(y)  # 5

# Funziona anche senza parentesi
x, y = 3, 5
print(x, y)  # 3 5

# Unpacking in una riga
name, age, job = ("Alice", 25, "Engineer")
print(name)  # Alice
print(age)   # 25
print(job)   # Engineer
```

### Swap Values (senza variabile temp!)

```python
# Metodo tradizionale (altri linguaggi)
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)  # 20 10

# Metodo Python (elegante!)
a = 10
b = 20
a, b = b, a  # Swap!
print(a, b)  # 20 10
```

**Come funziona?**
```python
a, b = b, a
# ↓
a, b = 20, 10  # Packing sul lato destro
# ↓
# Unpacking sul lato sinistro
```

### Extended Unpacking (*rest)

```python
# Prendi primo e resto
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print(first)  # 1
print(rest)   # [2, 3, 4, 5] ← Nota: è una LISTA!

# Prendi ultimo e resto
*rest, last = numbers
print(rest)  # [1, 2, 3, 4]
print(last)  # 5

# Prendi primo, ultimo, e mezzo
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

### Ignore Values (_)

```python
# Ignora valori che non ti servono
person = ("Alice", 25, "Engineer", "NYC")

# Voglio solo nome e città
name, _, _, city = person
print(name, city)  # Alice NYC

# Con *_
name, *_, city = person
print(name, city)  # Alice NYC
```

### Nested Unpacking

```python
# Tuple annidate
data = ("Alice", (25, "Engineer"))

# Unpacking annidato
name, (age, job) = data
print(name)  # Alice
print(age)   # 25
print(job)   # Engineer

# Altro esempio
point_3d = ((1, 2), 3)
(x, y), z = point_3d
print(x, y, z)  # 1 2 3
```

### Unpacking in Loop

```python
# Lista di tuple
people = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35)
]

# Unpacking durante iterazione
for name, age in people:
    print(f"{name} is {age} years old")

# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old
```

### Unpacking in Function Arguments

```python
def greet(name, age):
    print(f"Hello {name}, you are {age}")

person = ("Alice", 25)

# Unpacking con *
greet(*person)  # Hello Alice, you are 25

# Equivalente a:
greet("Alice", 25)
```

---

## 🔍 Tuple Methods (solo 2!)

Le tuple hanno **solo 2 metodi** (perché sono immutabili).

### 1. count(value) - Conta occorrenze

```python
numbers = (1, 2, 3, 2, 1, 2, 4)

count_2 = numbers.count(2)
print(count_2)  # 3

count_5 = numbers.count(5)
print(count_5)  # 0 (non presente)
```

### 2. index(value) - Trova indice

```python
numbers = (1, 2, 3, 4, 5)

idx = numbers.index(3)
print(idx)  # 2

# Con elemento non presente
try:
    numbers.index(99)
except ValueError:
    print("Element not found!")

# index(value, start, end) - cerca in un range
numbers = (1, 2, 3, 2, 1, 2)
idx = numbers.index(2, 2)  # Cerca 2 dall'indice 2
print(idx)  # 3
```

---

## 🎨 Tuple Operations

```python
# CONCATENATION
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)

# REPETITION
repeated = (1, 2) * 3
print(repeated)  # (1, 2, 1, 2, 1, 2)

# MEMBERSHIP
print(3 in (1, 2, 3, 4))      # True
print(99 not in (1, 2, 3, 4)) # True

# LENGTH
print(len((1, 2, 3, 4, 5)))  # 5

# MIN/MAX/SUM
numbers = (3, 1, 4, 1, 5, 9, 2)
print(min(numbers))  # 1
print(max(numbers))  # 9
print(sum(numbers))  # 25

# SLICING (crea nuova tuple)
my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple[2:5])    # (2, 3, 4)
print(my_tuple[:3])     # (0, 1, 2)
print(my_tuple[7:])     # (7, 8, 9)
print(my_tuple[::2])    # (0, 2, 4, 6, 8)
print(my_tuple[::-1])   # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

# CONVERSION
my_list = list(my_tuple)     # Tuple → List
back_to_tuple = tuple(my_list)  # List → Tuple
```

---

## 🏷️ Named Tuples (game changer!)

Named tuples = tuple + nomi campi = codice leggibile!

### Perché Named Tuples?

```python
# Regular tuple (cosa significa [1]?)
person = ("Alice", 25, "Engineer")
print(person[1])  # 25 ← Che cos'è questo?

# Named tuple (self-documenting!)
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'job'])
person = Person("Alice", 25, "Engineer")
print(person.age)  # 25 ← Chiaro!
```

### Creare Named Tuple

```python
from collections import namedtuple

# Metodo 1: Lista di stringhe
Point = namedtuple('Point', ['x', 'y'])

# Metodo 2: Stringa separata da spazi
Point = namedtuple('Point', 'x y')

# Metodo 3: Stringa separata da virgole
Point = namedtuple('Point', 'x, y')
```

### Usare Named Tuple

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

# Creare istanze
p1 = Point(3, 5)
p2 = Point(x=10, y=20)  # Con named arguments

# Accesso per nome (readable!)
print(p1.x)  # 3
print(p1.y)  # 5

# Accesso per indice (ancora funziona)
print(p1[0])  # 3
print(p1[1])  # 5

# Unpacking funziona
x, y = p1
print(x, y)  # 3 5

# Ancora immutabile
# p1.x = 99  # ❌ AttributeError!

# Conversione a dict
print(p1._asdict())  # {'x': 3, 'y': 5}
```

### Named Tuple - Esempi Reali

```python
from collections import namedtuple

# 1. Person
Person = namedtuple('Person', ['name', 'age', 'city'])
alice = Person('Alice', 25, 'NYC')
print(f"{alice.name} lives in {alice.city}")

# 2. RGB Color
Color = namedtuple('Color', ['red', 'green', 'blue'])
orange = Color(255, 128, 0)
print(f"RGB: ({orange.red}, {orange.green}, {orange.blue})")

# 3. Coordinate
Coordinate = namedtuple('Coordinate', ['lat', 'lon'])
location = Coordinate(40.7128, -74.0060)
print(f"Location: {location.lat}, {location.lon}")

# 4. Database Row
User = namedtuple('User', ['id', 'username', 'email'])
user = User(1, 'alice', 'alice@example.com')
print(f"User {user.username}: {user.email}")
```

### Named Tuple Methods

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 5)

# _asdict() - converti a dict
print(p._asdict())  # {'x': 3, 'y': 5}

# _replace() - crea nuova istanza con valori modificati
p2 = p._replace(x=10)
print(p2)  # Point(x=10, y=5)
print(p)   # Point(x=3, y=5) ← originale intatto

# _fields - tuple con nomi campi
print(Point._fields)  # ('x', 'y')

# _make() - crea da iterable
values = [10, 20]
p3 = Point._make(values)
print(p3)  # Point(x=10, y=20)
```

---

## 💡 Quando usare Tuple vs List?

### ✅ Usa Tuple quando:

1. **Dati non devono cambiare**
   ```python
   RGB_RED = (255, 0, 0)     # Colore fisso
   ORIGIN = (0, 0)           # Coordinate fisse
   ```

2. **Return multipli valori**
   ```python
   def get_min_max(numbers):
       return min(numbers), max(numbers)
   
   min_val, max_val = get_min_max([1, 5, 3])
   ```

3. **Coordinate/Posizioni**
   ```python
   point = (10, 20)
   position_3d = (x, y, z)
   ```

4. **Chiavi di dict** (tuple hashable, list no!)
   ```python
   locations = {
       (0, 0): "Origin",
       (10, 20): "Point A"
   }
   ```

5. **Performance critica** (tuple più veloci)
   ```python
   # Tuple → più veloce, meno memoria
   coordinates = (3, 5)
   ```

### ✅ Usa List quando:

1. **Dati possono cambiare**
   ```python
   shopping_cart = ["apple", "banana"]
   shopping_cart.append("orange")  # Aggiunge items
   ```

2. **Collezione omogenea di elementi**
   ```python
   numbers = [1, 2, 3, 4, 5]
   names = ["Alice", "Bob", "Charlie"]
   ```

3. **Serve ordinare/modificare**
   ```python
   scores = [85, 92, 78, 95]
   scores.sort()
   ```

4. **Numero elementi può variare**
   ```python
   tasks = []
   tasks.append("Write code")
   tasks.append("Review PR")
   ```

---

## ⚡ Performance Comparison

```python
import sys
import time

# Memory comparison
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(list_example)} bytes")   # 104 bytes
print(f"Tuple size: {sys.getsizeof(tuple_example)} bytes") # 80 bytes

# Creation speed
import timeit

# List creation
list_time = timeit.timeit(lambda: [1, 2, 3, 4, 5], number=1000000)
print(f"List creation: {list_time:.4f}s")

# Tuple creation
tuple_time = timeit.timeit(lambda: (1, 2, 3, 4, 5), number=1000000)
print(f"Tuple creation: {tuple_time:.4f}s")

# Typical output:
# List size: 104 bytes
# Tuple size: 80 bytes
# List creation: 0.0891s
# Tuple creation: 0.0123s  (7x più veloce!)
```

**Perché tuple sono più veloci?**
- Python sa che non cambieranno mai
- Può allocare memoria fissa
- Meno overhead per tracking

---

## 🆚 Python Tuple vs JavaScript

JavaScript **NON ha tuple native**. Closest equivalents:

### 1. Array Immutabile (rare)

```javascript
// JavaScript - Array frozen (ma non ottimizzato)
const arr = Object.freeze([1, 2, 3]);
// arr[0] = 99;  // Non funziona in strict mode

// Python - Tuple nativa (ottimizzata)
my_tuple = (1, 2, 3)
# my_tuple[0] = 99  # TypeError
```

### 2. Destructuring

```javascript
// JavaScript
const [x, y] = [3, 5];
const [first, ...rest] = [1, 2, 3, 4, 5];

// Python - simile ma più potente
x, y = 3, 5  # No brackets needed!
first, *rest = (1, 2, 3, 4, 5)
```

### 3. Multiple Return

```javascript
// JavaScript - ritorna array
function getCoordinates() {
    return [10, 20];
}
const [x, y] = getCoordinates();

// Python - ritorna tuple (più chiaro)
def get_coordinates():
    return 10, 20  # Tuple packing

x, y = get_coordinates()  # Tuple unpacking
```

### 4. Named Values

```javascript
// JavaScript - usa objects
const point = { x: 3, y: 5 };
point.x = 10;  // Mutable!

// Python - namedtuple (immutable)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 5)
# p.x = 10  # ❌ AttributeError!
```

**Tabella comparativa:**

| Feature | JavaScript | Python Tuple |
|---------|-----------|--------------|
| Immutabilità | Object.freeze() (workaround) | Nativa |
| Performance | Non ottimizzata | Ottimizzata |
| Destructuring | ✅ Arrays | ✅ Tuples |
| Named fields | Objects | namedtuple |
| Dict keys | ❌ No | ✅ Yes |

---

## ⚠️ Common Gotchas

### 1. Single element tuple (serve virgola!)

```python
# ❌ SBAGLIATO - è un int!
not_tuple = (42)
print(type(not_tuple))  # <class 'int'>

# ✅ CORRETTO - serve virgola
single = (42,)
print(type(single))  # <class 'tuple'>

# Anche senza parentesi
single = 42,
print(type(single))  # <class 'tuple'>
```

### 2. Tuple comprehension non esiste

```python
# ❌ Questo è un GENERATOR, non tuple!
gen = (x**2 for x in range(5))
print(type(gen))  # <class 'generator'>

# ✅ Devi convertire
my_tuple = tuple(x**2 for x in range(5))
print(type(my_tuple))  # <class 'tuple'>
```

### 3. Unpacking mismatch

```python
# ❌ Troppi valori da sinistra
x, y = (1, 2, 3)  # ValueError: too many values to unpack

# ❌ Troppi pochi valori da sinistra
x, y, z = (1, 2)  # ValueError: not enough values to unpack

# ✅ Deve matchare
x, y = (1, 2)     # OK
x, y, z = (1, 2, 3)  # OK

# ✅ O usa *rest
x, *rest = (1, 2, 3)  # x=1, rest=[2, 3]
```

### 4. Nested mutable objects

```python
# Tuple con lista dentro
my_tuple = ([1, 2], [3, 4])

# La tuple è immutabile
# my_tuple[0] = [99]  # ❌ TypeError!

# Ma la lista DENTRO può cambiare!
my_tuple[0].append(99)  # ✅ Funziona
print(my_tuple)  # ([1, 2, 99], [3, 4])

# Questo significa che tuple con liste NON può essere dict key!
# my_dict = {my_tuple: "value"}  # ❌ TypeError: unhashable type
```

### 5. Parentesi vs Tuple

```python
# Parentesi per precedenza
result = (2 + 3) * 4
print(result)  # 20 (int)

# Tuple
result = (2 + 3,) * 4
print(result)  # (5, 5, 5, 5) (tuple)

# No parentesi = tuple comunque
result = 2, 3
print(type(result))  # <class 'tuple'>
```

---

## 📝 Best Practices

### ✅ DO: Usa tuple per dati fissi

```python
# ✅ Coordinate (non cambiano)
point = (10, 20)

# ✅ RGB color (fisso)
RED = (255, 0, 0)

# ✅ Date (immutable)
date = (2024, 5, 3)
```

### ✅ DO: Return multipli valori

```python
# ✅ Chiaro e leggibile
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

min_val, max_val, avg = get_stats([1, 2, 3, 4, 5])
```

### ✅ DO: Named tuples per chiarezza

```python
# ❌ Cosa significa [1]?
user = ("Alice", 25, "alice@example.com")
print(user[1])  # 25 ← non chiaro

# ✅ Self-documenting!
from collections import namedtuple
User = namedtuple('User', ['name', 'age', 'email'])
user = User("Alice", 25, "alice@example.com")
print(user.age)  # 25 ← chiaro!
```

### ❌ DON'T: Tuple per collezioni dinamiche

```python
# ❌ Se devi modificare, usa list
tasks = ("Task 1", "Task 2")  # Non puoi aggiungere!

# ✅ Usa list
tasks = ["Task 1", "Task 2"]
tasks.append("Task 3")  # OK
```

### ❌ DON'T: Tuple troppo lunghe

```python
# ❌ Troppi elementi, usa class o dict
person = ("Alice", 25, "Engineer", "NYC", "alice@example.com", "555-1234")

# ✅ Usa named tuple o class
Person = namedtuple('Person', ['name', 'age', 'job', 'city', 'email', 'phone'])
person = Person("Alice", 25, "Engineer", "NYC", "alice@example.com", "555-1234")
```

---

## 🎯 Use Cases Reali

### 1. Coordinate/Posizioni

```python
# 2D
point = (10, 20)
x, y = point

# 3D
position = (10, 20, 30)
x, y, z = position

# Dict con coordinate come chiavi
grid = {
    (0, 0): "Start",
    (10, 20): "Checkpoint",
    (50, 50): "End"
}
```

### 2. RGB Colors

```python
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def create_color(r, g, b):
    return (r, g, b)

orange = create_color(255, 128, 0)
```

### 3. Database Rows

```python
from collections import namedtuple

User = namedtuple('User', ['id', 'username', 'email'])

# Simula query result
def get_users():
    return [
        User(1, 'alice', 'alice@example.com'),
        User(2, 'bob', 'bob@example.com'),
        User(3, 'charlie', 'charlie@example.com')
    ]

for user in get_users():
    print(f"User {user.id}: {user.username}")
```

### 4. Function Return Multiple Values

```python
def parse_name(full_name):
    parts = full_name.split()
    if len(parts) == 2:
        return parts[0], parts[1]
    return parts[0], None

first, last = parse_name("John Doe")

def calculate_stats(numbers):
    return len(numbers), min(numbers), max(numbers), sum(numbers)/len(numbers)

count, min_val, max_val, avg = calculate_stats([1, 2, 3, 4, 5])
```

### 5. Configuration/Settings

```python
# Settings immutabili
DATABASE_CONFIG = (
    "localhost",
    5432,
    "mydb",
    "user",
    "password"
)

host, port, db, user, pwd = DATABASE_CONFIG

# Meglio con named tuple
from collections import namedtuple

DBConfig = namedtuple('DBConfig', ['host', 'port', 'database', 'user', 'password'])
config = DBConfig('localhost', 5432, 'mydb', 'user', 'password')

# Accesso leggibile
print(f"Connecting to {config.host}:{config.port}")
```

---

## 📊 Quick Reference

```python
# CREAZIONE
t = (1, 2, 3)
t = 1, 2, 3              # Senza parentesi
t = (42,)                # Single element (virgola!)
t = tuple([1, 2, 3])
t = tuple("abc")

# ACCESSO
t[0]                     # Primo
t[-1]                    # Ultimo
t[1:3]                   # Slice

# NON PUOI MODIFICARE
# t[0] = 99              # ❌ TypeError
# t.append(4)            # ❌ AttributeError

# METODI (solo 2!)
t.count(2)               # Conta occorrenze
t.index(3)               # Trova indice

# OPERATIONS
t1 + t2                  # Concatenazione
t * 3                    # Ripetizione
3 in t                   # Membership
len(t)                   # Lunghezza

# UNPACKING
x, y = (3, 5)
first, *rest = (1, 2, 3, 4)
first, *middle, last = (1, 2, 3, 4, 5)

# CONVERSIONE
list(t)                  # Tuple → List
tuple(my_list)           # List → Tuple

# NAMED TUPLE
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 5)
print(p.x, p.y)
```

---

## 🎓 Recap

**Tuples sono:**
- ✅ Ordinate (mantengono ordine inserimento)
- ❌ Immutabili (NON modificabili)
- ✅ Permettono duplicati
- ✅ Accessibili per indice
- ✅ Possono contenere tipi misti
- ✅ Hashable (se elementi hashable)

**Quando usare Tuple:**
- Dati che non devono cambiare
- Multiple return values
- Coordinate/posizioni
- Dict keys
- Performance critica

**Pattern chiave da ricordare:**
1. `(42,)` serve virgola per single element
2. Unpacking: `x, y = (3, 5)`
3. Extended unpacking: `first, *rest = tuple`
4. Named tuples per codice leggibile
5. Swap: `a, b = b, a`

**Prossimi passi:**
- Usa tuple per dati fissi/coordinate
- Usa named tuples per chiarezza
- Return multipli valori con tuple
- Ricorda: immutabili = sicure e veloci
