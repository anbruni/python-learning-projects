# Python Dictionaries - Guida Completa

## 🎯 Cos'è un Dictionary?

**Definizione:** Una collezione **non ordinata** (ordinata da Python 3.7+) di coppie **chiave-valore** (key-value pairs).

```python
# Dictionary semplice
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

print(person["name"])  # "Alice"
```

**Caratteristiche chiave:**
- ✅ **Key-Value pairs**: ogni elemento è una coppia chiave-valore
- ✅ **Ordered** (da Python 3.7+): mantiene ordine di inserimento
- ✅ **Mutable**: può essere modificato
- ✅ **Keys uniche**: ogni chiave può apparire una sola volta
- ✅ **Fast lookup**: accesso O(1) per chiave
- ✅ **Keys immutable**: chiavi devono essere hashable (str, int, tuple)

---

## 📊 Dict vs List vs Tuple vs Set

| Feature | Dict | List | Tuple | Set |
|---------|------|------|-------|-----|
| **Structure** | Key-Value | Indexed | Indexed | Unique items |
| **Ordered** | ✅ (3.7+) | ✅ | ✅ | ❌ |
| **Mutable** | ✅ | ✅ | ❌ | ✅ |
| **Duplicates** | Keys NO, Values YES | ✅ | ✅ | ❌ |
| **Access** | `dict[key]` | `list[index]` | `tuple[index]` | No access |
| **Lookup** | O(1) by key | O(n) by value | O(n) by value | O(1) by value |
| **Use case** | Key-value mapping | Ordered collection | Fixed data | Unique values |

---

## 🚀 Creare Dictionaries

### Metodo 1: Literal Syntax (più comune)

```python
# Dict con vari tipi
person = {
    "name": "Alice",
    "age": 25,
    "is_active": True,
    "hobbies": ["reading", "coding"]
}

# Dict vuoto
empty = {}

# Con chiavi di tipi diversi
mixed = {
    "string_key": 1,
    42: "numeric key",
    (1, 2): "tuple key"  # Tuple OK (immutable)
}
```

### Metodo 2: Constructor dict()

```python
# Con keyword arguments
person = dict(name="Alice", age=25, city="NYC")
# {"name": "Alice", "age": 25, "city": "NYC"}

# Da lista di tuple
pairs = [("name", "Alice"), ("age", 25)]
person = dict(pairs)
# {"name": "Alice", "age": 25}

# Da due liste con zip()
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
person = dict(zip(keys, values))
# {"name": "Alice", "age": 25, "city": "NYC"}
```

### Metodo 3: Dict Comprehension

**Sintassi generale:**
```python
{key_expression: value_expression for item in iterable}
{key_expression: value_expression for item in iterable if condition}
{key_expression: value_expression for key, value in dict.items()}
{key_expression: value_expression for key, value in dict.items() if condition}
```

**Template da ricordare:**
```python
# Template base
{key: value for key, value in dict.items()}

# Con filtro
{key: value for key, value in dict.items() if condition}

# Trasformazione
{key: transform(value) for key, value in dict.items()}

# Filtro + trasformazione
{key: transform(value) for key, value in dict.items() if condition}
```

**Esempi pratici:**

```python
# 1. Squares (da range)
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 2. Con condizione (filtrare)
evens = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 3. Da lista (word → length)
words = ["apple", "banana", "cherry"]
lengths = {word: len(word) for word in words}
# {"apple": 5, "banana": 6, "cherry": 6}

# 4. Filtrare dict esistente per VALUE
data = {"a": 10, "b": 5, "c": 20}
filtered = {k: v for k, v in data.items() if v >= 10}
# {"a": 10, "c": 20}

# 5. Filtrare dict esistente per KEY
data = {"apple": 1, "banana": 2, "cherry": 3}
filtered = {k: v for k, v in data.items() if k.startswith("a")}
# {"apple": 1}

# 6. Trasformare VALUES
data = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in data.items()}
# {"a": 2, "b": 4, "c": 6}

# 7. Trasformare KEYS
data = {"a": 1, "b": 2, "c": 3}
upper_keys = {k.upper(): v for k, v in data.items()}
# {"A": 1, "B": 2, "C": 3}

# 8. Invertire dict (swap key-value)
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
# {1: "a", 2: "b", 3: "c"}

# 9. Nested: filtrare + trasformare
data = {"a": 1, "b": 5, "c": 10, "d": 3}
result = {k: v * 10 for k, v in data.items() if v > 2}
# {"b": 50, "c": 100, "d": 30}
```

**Confronto con List Comprehension:**

```python
# List comprehension (genera lista)
[x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Dict comprehension (genera dict)
{x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension (genera set)
{x**2 for x in range(5)}
# {0, 1, 4, 9, 16}
```

**⚠️ Common mistake:**

```python
data = {"a": 10, "b": 5, "c": 20}

# ❌ SBAGLIATO - Set comprehension, non dict!
result = {data for v in data.values() if v >= 10}

# ✅ CORRETTO - Dict comprehension
result = {k: v for k, v in data.items() if v >= 10}
```

### Metodo 4: fromkeys()

```python
# Tutte le chiavi con stesso valore
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
# {"a": 0, "b": 0, "c": 0}

# Senza valore (default None)
none_dict = dict.fromkeys(keys)
# {"a": None, "b": None, "c": None}
```

---

## 🔍 Accedere a Valori

### `[]` Operator (KeyError se manca)

```python
person = {"name": "Alice", "age": 25}

# Accesso normale
print(person["name"])  # "Alice"

# KeyError se chiave non esiste
try:
    print(person["job"])  # ❌ KeyError: 'job'
except KeyError:
    print("Key not found!")
```

### `.get()` Method (sicuro, ritorna None)

```python
person = {"name": "Alice", "age": 25}

# Get con None come default
print(person.get("name"))  # "Alice"
print(person.get("job"))   # None (no error!)

# Get con default personalizzato
print(person.get("job", "Unknown"))  # "Unknown"
print(person.get("age", 0))          # 25 (esiste già)
```

### Quando usare cosa?

```python
# ✅ Usa [] quando:
# - Sei SICURO che la chiave esiste
# - VUOI un errore se manca (fail fast)
print(config["database_url"])  # Must exist!

# ✅ Usa .get() quando:
# - La chiave POTREBBE non esistere
# - Vuoi un default se manca
age = user.get("age", 0)
theme = settings.get("theme", "light")
```

---

## 🔧 Dict Methods - Reference Completa

### AGGIUNGERE/MODIFICARE

```python
person = {"name": "Alice"}

# Aggiungere/modificare singolo elemento
person["age"] = 25
person["name"] = "Alice Smith"  # Modifica

# update() - merge con altro dict
person.update({"city": "NYC", "job": "Engineer"})
print(person)
# {"name": "Alice Smith", "age": 25, "city": "NYC", "job": "Engineer"}

# update() sovrascrive valori esistenti
person.update({"age": 26, "country": "USA"})

# setdefault() - setta solo se NON esiste
person.setdefault("age", 30)     # Non fa nulla (age esiste)
person.setdefault("salary", 50000)  # Aggiunge (salary non esiste)
```

### RIMUOVERE

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# del - rimuove chiave (KeyError se non esiste)
del person["city"]
print(person)  # {"name": "Alice", "age": 25}

# pop() - rimuove e ritorna valore
age = person.pop("age")
print(age)      # 25
print(person)   # {"name": "Alice"}

# pop() con default (no KeyError)
job = person.pop("job", "Unknown")
print(job)  # "Unknown" (job non esisteva)

# popitem() - rimuove e ritorna ultima coppia (k, v)
last_item = person.popitem()
print(last_item)  # ("name", "Alice")

# clear() - rimuove tutto
person.clear()
print(person)  # {}
```

### VISUALIZZARE

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# keys() - vista delle chiavi
print(person.keys())    # dict_keys(["name", "age", "city"])
print(list(person.keys()))  # ["name", "age", "city"]

# values() - vista dei valori
print(person.values())  # dict_values(["Alice", 25, "NYC"])
print(list(person.values()))  # ["Alice", 25, "NYC"]

# items() - vista delle coppie (k, v)
print(person.items())
# dict_items([("name", "Alice"), ("age", 25), ("city", "NYC")])
print(list(person.items()))
# [("name", "Alice"), ("age", 25), ("city", "NYC")]
```

### COPIARE

```python
original = {"name": "Alice", "age": 25}

# copy() - shallow copy
copied = original.copy()
copied["age"] = 30
print(original)  # {"name": "Alice", "age": 25} ← intatto
print(copied)    # {"name": "Alice", "age": 30}

# ⚠️ Shallow copy con nested structures
original = {"user": {"name": "Alice"}}
copied = original.copy()
copied["user"]["name"] = "Bob"
print(original)  # {"user": {"name": "Bob"}} ← modificato!

# Deep copy per nested structures
import copy
original = {"user": {"name": "Alice"}}
deep = copy.deepcopy(original)
deep["user"]["name"] = "Bob"
print(original)  # {"user": {"name": "Alice"}} ← intatto!
```

### ALTRI

```python
person = {"name": "Alice", "age": 25}

# len() - numero di coppie
print(len(person))  # 2

# in - check se chiave esiste
print("name" in person)    # True
print("job" in person)     # False

# not in
print("job" not in person)  # True

# Iterare (loop diretto = loop su keys)
for key in person:
    print(key, person[key])
```

---

## 🔄 Iterare su Dictionaries

### Loop su Keys (default)

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Metodo 1: loop diretto (itera su keys)
for key in person:
    print(key, person[key])

# Metodo 2: esplicito con .keys()
for key in person.keys():
    print(key, person[key])
```

### Loop su Values

```python
# Solo valori
for value in person.values():
    print(value)
# Alice
# 25
# NYC
```

### Loop su Items (più comune!)

```python
# Coppie (key, value)
for key, value in person.items():
    print(f"{key}: {value}")
# name: Alice
# age: 25
# city: NYC
```

### Enumerate con Dict

```python
# Con indice
for i, (key, value) in enumerate(person.items()):
    print(f"{i}: {key} = {value}")
# 0: name = Alice
# 1: age = 25
# 2: city = NYC
```

### Dict Comprehension (filtrare/trasformare)

```python
# Filtrare per valore
filtered = {k: v for k, v in person.items() if isinstance(v, int)}
print(filtered)  # {"age": 25}

# Trasformare valori
doubled = {k: v*2 for k, v in person.items() if isinstance(v, int)}
print(doubled)  # {"age": 50}
```

---

## 📐 Nested Dictionaries (JSON-like)

### Creare Nested Dicts

```python
# User con address
user = {
    "name": "Alice",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "NYC",
        "zip": "10001"
    },
    "hobbies": ["reading", "coding"]
}

# Accesso nested
print(user["address"]["city"])  # "NYC"
print(user["hobbies"][0])       # "reading"
```

### Accesso Sicuro a Nested Dicts

```python
user = {
    "name": "Alice",
    "address": {
        "city": "NYC"
    }
}

# ❌ Unsafe (KeyError se manca)
# print(user["address"]["country"])  # KeyError!

# ✅ Safe con .get()
city = user.get("address", {}).get("city")
print(city)  # "NYC"

country = user.get("address", {}).get("country")
print(country)  # None (no error)

# ✅ Safe function
def get_nested(data, *keys, default=None):
    """Get value from nested dict safely"""
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
            if data is None:
                return default
        else:
            return default
    return data

print(get_nested(user, "address", "city"))     # "NYC"
print(get_nested(user, "address", "country"))  # None
print(get_nested(user, "address", "country", default="USA"))  # "USA"
```

### Flatten Nested Dict

```python
def flatten_dict(nested, parent_key='', sep='_'):
    """Flatten nested dictionary"""
    items = []
    for k, v in nested.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

nested = {
    "user": {
        "name": "Alice",
        "age": 25,
        "address": {
            "city": "NYC"
        }
    }
}

flat = flatten_dict(nested)
print(flat)
# {
#     "user_name": "Alice",
#     "user_age": 25,
#     "user_address_city": "NYC"
# }
```

#### 📖 Come Funziona `flatten_dict` (Step-by-Step)

**COSA FA:**
Trasforma un dizionario nidificato in uno "piatto", concatenando le chiavi con un separatore.

```python
# PRIMA (nidificato)
{
    "user": {
        "name": "Alice",
        "age": 25,
        "address": {
            "city": "NYC"
        }
    }
}

# DOPO (piatto)
{
    "user_name": "Alice",
    "user_age": 25,
    "user_address_city": "NYC"
}
```

**I PARAMETRI:**
- `nested`: Il dizionario da appiattire
- `parent_key`: La "strada" percorsa finora (es: "user_address")
- `sep`: Il separatore da usare (default `_`)

**ESEMPIO STEP-BY-STEP:**

```python
nested = {
    "user": {
        "name": "Alice",
        "age": 25,
        "address": {
            "city": "NYC"
        }
    }
}

flatten_dict(nested)
```

**CHIAMATA PRINCIPALE (livello 1):**
```python
nested = {"user": {...}}
parent_key = ''
items = []

# Loop 1: k="user", v={"name": "Alice", "age": 25, "address": {...}}
new_key = "user"  # parent_key è vuoto
isinstance(v, dict) → True  # v è un dizionario!
# RICORSIONE: flatten_dict({"name": "Alice", "age": 25, "address": {...}}, "user", '_')
```

**CHIAMATA RICORSIVA #1 (livello 2):**
```python
nested = {"name": "Alice", "age": 25, "address": {"city": "NYC"}}
parent_key = 'user'  # ← ereditato dalla chiamata precedente!
items = []

# Loop 1: k="name", v="Alice"
new_key = f"user_name"
isinstance(v, dict) → False  # v è una stringa!
items.append(("user_name", "Alice"))
# items = [("user_name", "Alice")]

# Loop 2: k="age", v=25
new_key = f"user_age"
isinstance(v, dict) → False
items.append(("user_age", 25))
# items = [("user_name", "Alice"), ("user_age", 25)]

# Loop 3: k="address", v={"city": "NYC"}
new_key = f"user_address"
isinstance(v, dict) → True  # v è ANCORA un dizionario!
# RICORSIONE #2: flatten_dict({"city": "NYC"}, "user_address", '_')
```

**CHIAMATA RICORSIVA #2 (livello 3):**
```python
nested = {"city": "NYC"}
parent_key = 'user_address'  # ← costruito dal parent precedente!
items = []

# Loop 1: k="city", v="NYC"
new_key = f"user_address_city"
isinstance(v, dict) → False  # v è una stringa!
items.append(("user_address_city", "NYC"))
# items = [("user_address_city", "NYC")]

# Return: {"user_address_city": "NYC"}
```

**Torna alla CHIAMATA RICORSIVA #1:**
```python
# Loop 3 (continua):
items.extend([("user_address_city", "NYC")])
# items = [("user_name", "Alice"), ("user_age", 25), ("user_address_city", "NYC")]

# Return: {"user_name": "Alice", "user_age": 25, "user_address_city": "NYC"}
```

**Torna alla CHIAMATA PRINCIPALE:**
```python
# Loop 1 (continua):
items.extend([("user_name", "Alice"), ("user_age", 25), ("user_address_city", "NYC")])
# items = [("user_name", "Alice"), ("user_age", 25), ("user_address_city", "NYC")]

# Return: {"user_name": "Alice", "user_age": 25, "user_address_city": "NYC"}
```

**PUNTI CHIAVE:**

1. **`.extend()` vs `.append()`**
```python
# .append() aggiunge UN elemento
items.append(("key", "value"))

# .extend() aggiunge TUTTI gli elementi di un iterabile
items.extend([("k1", "v1"), ("k2", "v2")])
```

2. **La ricorsione "costruisce" le chiavi**
```python
# Livello 1: parent_key = ""
new_key = "user"

# Livello 2: parent_key = "user"
new_key = f"user_{name}" → "user_name"

# Livello 3: parent_key = "user_address"
new_key = f"user_address_{city}" → "user_address_city"
```

3. **items è una lista di tuple**
```python
items = [("user_name", "Andrea"), ("user_age", 30)]
dict(items) → {"user_name": "Andrea", "user_age": 30}
```

---

## 💡 Patterns Comuni

### 1. Counting (Frequenza)

```python
# Count character frequency
text = "hello world"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Con setdefault
freq = {}
for char in text:
    freq.setdefault(char, 0)
    freq[char] += 1

# Con Counter (più semplice!)
from collections import Counter
freq = Counter(text)
print(freq)  # Counter({'l': 3, 'o': 2, ...})
print(dict(freq))  # Converti a dict normale
```

### 2. Grouping (Raggruppare)

```python
# Group words by first letter
words = ["apple", "banana", "apricot", "cherry", "avocado"]

grouped = {}
for word in words:
    first_letter = word[0]
    if first_letter not in grouped:
        grouped[first_letter] = []
    grouped[first_letter].append(word)

print(grouped)
# {
#     'a': ['apple', 'apricot', 'avocado'],
#     'b': ['banana'],
#     'c': ['cherry']
# }

# Con setdefault (più conciso)
grouped = {}
for word in words:
    grouped.setdefault(word[0], []).append(word)

# Con defaultdict (ancora più semplice!)
from collections import defaultdict
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
```

### 3. Lookup Table (Tabella di ricerca)

```python
# Map country codes to names
countries = {
    "US": "United States",
    "UK": "United Kingdom",
    "IT": "Italy",
    "FR": "France"
}

code = "IT"
country_name = countries.get(code, "Unknown")
print(country_name)  # "Italy"

# Use case: traduzione
translations = {
    "hello": "ciao",
    "world": "mondo",
    "goodbye": "arrivederci"
}

def translate(word):
    return translations.get(word.lower(), word)

print(translate("hello"))  # "ciao"
print(translate("pizza"))  # "pizza" (not found, return original)
```

### 4. Caching/Memoization

```python
# Cache function results
cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    
    result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

print(fibonacci(10))  # 55 (fast with caching!)

# Con decorator (più elegante)
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### 5. Default Values

```python
# Config con defaults
default_config = {
    "theme": "light",
    "language": "en",
    "timeout": 30
}

user_config = {
    "theme": "dark"
}

# Merge con defaults
config = {**default_config, **user_config}
print(config)
# {"theme": "dark", "language": "en", "timeout": 30}

# O con update
config = default_config.copy()
config.update(user_config)
```

### 6. Invert Dict (Swap Keys/Values)

```python
# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: "a", 2: "b", 3: "c"}

# ⚠️ Attenzione: valori duplicati
original = {"a": 1, "b": 1, "c": 2}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: "b", 2: "c"} ← "a" perso! (b sovrascrive a)

# Soluzione: group by value
from collections import defaultdict
inverted = defaultdict(list)
for k, v in original.items():
    inverted[v].append(k)
print(dict(inverted))  # {1: ["a", "b"], 2: ["c"]}
```

---

## ⚡ Performance & Memory

### Time Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Get item | O(1) | O(n) |
| Set item | O(1) | O(n) |
| Delete item | O(1) | O(n) |
| Search (key in dict) | O(1) | O(n) |
| Iteration | O(n) | O(n) |

### Memory Usage

```python
import sys

# Dict vs List memory
my_list = list(range(1000))
my_dict = {i: i for i in range(1000)}

print(f"List: {sys.getsizeof(my_list)} bytes")  # ~9 KB
print(f"Dict: {sys.getsizeof(my_dict)} bytes")  # ~36 KB

# Dict usa più memoria per velocità!
```

### When to use Dict vs List?

**✅ Usa Dict quando:**
- Serve accesso rapido per chiave (O(1))
- Dati come key-value pairs (config, JSON, etc.)
- Lookup tables
- Counting/grouping
- Caching

**✅ Usa List quando:**
- Ordine sequenziale importante
- Accesso per indice
- Dati omogenei senza chiave naturale
- Memoria limitata

---

## 🆚 Python Dict vs JavaScript Object

### Syntax Comparison

```javascript
// JavaScript Object
const person = {
    name: "Alice",
    age: 25,
    "complex-key": "value"
};

// Access
console.log(person.name);        // "Alice"
console.log(person["name"]);     // "Alice"
console.log(person.job);         // undefined
console.log(person.job || "Unknown");  // "Unknown"

// Add/modify
person.city = "NYC";
person.age = 26;

// Delete
delete person.city;

// Check key
"name" in person;  // true
person.hasOwnProperty("name");  // true

// Iterate
Object.keys(person);      // ["name", "age"]
Object.values(person);    // ["Alice", 26]
Object.entries(person);   // [["name", "Alice"], ["age", 26]]

for (const [key, value] of Object.entries(person)) {
    console.log(key, value);
}
```

```python
# Python Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "complex-key": "value"
}

# Access
print(person["name"])         # "Alice"
# print(person["job"])        # KeyError!
print(person.get("job"))      # None
print(person.get("job", "Unknown"))  # "Unknown"

# Add/modify
person["city"] = "NYC"
person["age"] = 26

# Delete
del person["city"]

# Check key
"name" in person  # True

# Iterate
person.keys()      # dict_keys(["name", "age"])
person.values()    # dict_values(["Alice", 26])
person.items()     # dict_items([("name", "Alice"), ("age", 26)])

for key, value in person.items():
    print(key, value)
```

### Key Differences

| Feature | Python Dict | JavaScript Object |
|---------|-------------|-------------------|
| Missing key | `KeyError` or `.get()` | `undefined` |
| Key types | Any immutable | String/Symbol only |
| Dot notation | ❌ No | ✅ Yes (`obj.key`) |
| Ordered | ✅ (3.7+) | ✅ (ES2015+) |
| Methods | `.keys()`, `.values()`, `.items()` | `Object.keys()`, etc. |
| Check key | `key in dict` | `key in obj` or `hasOwnProperty` |

---

## ⚠️ Common Gotchas

### 1. Mutable Keys (NO!)

```python
# ❌ List as key (unhashable)
# my_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'

# ❌ Dict as key
# my_dict = {{"a": 1}: "value"}  # TypeError

# ✅ Tuple as key (immutable)
my_dict = {(1, 2): "value"}  # OK

# ✅ String, int, float as keys
my_dict = {"key": 1, 42: "value", 3.14: "pi"}  # OK
```

### 2. Modifying Dict During Iteration

```python
# ❌ SBAGLIATO
person = {"name": "Alice", "age": 25, "city": "NYC"}
for key in person:
    if key == "age":
        del person[key]  # RuntimeError!

# ✅ CORRETTO - itera su copia
for key in list(person.keys()):
    if key == "age":
        del person[key]

# ✅ O crea nuovo dict
person = {k: v for k, v in person.items() if k != "age"}
```

### 3. Default Mutable Arguments

```python
# ❌ SBAGLIATO
def add_item(item, my_dict={}):  # ❌ Dict condiviso!
    my_dict[item] = True
    return my_dict

print(add_item("a"))  # {"a": True}
print(add_item("b"))  # {"a": True, "b": True} ← Condiviso!

# ✅ CORRETTO
def add_item(item, my_dict=None):
    if my_dict is None:
        my_dict = {}
    my_dict[item] = True
    return my_dict
```

### 4. Shallow Copy Gotcha

```python
# Shallow copy con nested dicts
original = {"user": {"name": "Alice"}}
copied = original.copy()

copied["user"]["name"] = "Bob"
print(original)  # {"user": {"name": "Bob"}} ← Modificato!

# Usa deepcopy
import copy
deep = copy.deepcopy(original)
deep["user"]["name"] = "Charlie"
print(original)  # {"user": {"name": "Bob"}} ← Intatto
```

### 5. Dict Order Before 3.7

```python
# Python < 3.7: ordine non garantito
# Python >= 3.7: ordine di inserimento garantito

my_dict = {"c": 3, "a": 1, "b": 2}
print(my_dict)
# Python 3.7+: {"c": 3, "a": 1, "b": 2} (ordine mantenuto)
# Python 3.6-: ordine imprevedibile

# Se serve ordine garantito in 3.6-, usa OrderedDict
from collections import OrderedDict
ordered = OrderedDict([("c", 3), ("a", 1), ("b", 2)])
```

---

## 📝 Best Practices

### ✅ DO:

```python
# 1. Usa .get() per chiavi potenzialmente mancanti
age = user.get("age", 0)  # ✅ Safe

# 2. Usa 'in' per check esistenza prima di accedere
if "email" in user:
    print(user["email"])

# 3. Usa dict comprehension per filtrare/trasformare
filtered = {k: v for k, v in data.items() if v > 0}

# 4. Usa items() per iterare su key-value
for key, value in person.items():
    print(f"{key}: {value}")

# 5. Usa setdefault per default values
counts.setdefault(key, 0)
counts[key] += 1

# 6. Usa ** per merge dicts (Python 3.5+)
merged = {**dict1, **dict2}

# 7. Usa Counter per counting
from collections import Counter
freq = Counter(text)
```

### ❌ DON'T:

```python
# 1. Non usare [] se chiave può mancare
# value = data["key"]  # ❌ KeyError risk
value = data.get("key", default)  # ✅

# 2. Non modificare dict durante iterazione
# for k in d: del d[k]  # ❌ RuntimeError
for k in list(d.keys()): del d[k]  # ✅

# 3. Non usare liste come chiavi
# d = {[1, 2]: "value"}  # ❌ TypeError
d = {(1, 2): "value"}  # ✅ Tuple

# 4. Non creare nested dicts manualmente se complessi
# Usa defaultdict o JSON
from collections import defaultdict
nested = defaultdict(lambda: defaultdict(list))
```

---

## 🎯 Use Cases Reali

### 1. Config/Settings

```python
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "cache": {
        "enabled": True,
        "ttl": 3600
    }
}

db_host = config["database"]["host"]
```

### 2. JSON Data (APIs)

```python
import json

# Parse JSON
user_json = '{"name": "Alice", "age": 25, "hobbies": ["reading"]}'
user = json.loads(user_json)
print(user["name"])  # "Alice"

# Create JSON
data = {"status": "success", "data": [1, 2, 3]}
json_string = json.dumps(data)
```

### 3. Word Frequency

```python
text = "hello world hello python world"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)  # {"hello": 2, "world": 2, "python": 1}

# Top 3 most common
from collections import Counter
freq = Counter(text.split())
print(freq.most_common(3))
```

### 4. Database Results

```python
# Simulate DB query result
users = [
    {"id": 1, "name": "Alice", "role": "admin"},
    {"id": 2, "name": "Bob", "role": "user"},
    {"id": 3, "name": "Charlie", "role": "user"}
]

# Index by ID
users_by_id = {user["id"]: user for user in users}
print(users_by_id[2])  # {"id": 2, "name": "Bob", ...}

# Group by role
from collections import defaultdict
by_role = defaultdict(list)
for user in users:
    by_role[user["role"]].append(user)

print(by_role["admin"])  # [{"id": 1, "name": "Alice", ...}]
```

### 5. Caching

```python
# Function result cache
cache = {}

def expensive_function(x):
    if x in cache:
        return cache[x]
    
    # Expensive computation
    result = x ** 2
    cache[x] = result
    return result
```

---

## 📊 Quick Reference

```python
# CREAZIONE
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)
d = dict([("a", 1), ("b", 2)])
d = {x: x**2 for x in range(5)}

# ACCESSO
d["key"]               # KeyError if missing
d.get("key")           # None if missing
d.get("key", default)  # default if missing

# AGGIUNGERE/MODIFICARE
d["key"] = value
d.update({"k": v})
d.setdefault("k", v)

# RIMUOVERE
del d["key"]
d.pop("key")
d.popitem()
d.clear()

# VISUALIZZARE
d.keys()
d.values()
d.items()

# ITERARE
for key in d:
    pass
for key, value in d.items():
    pass

# CHECK
"key" in d
len(d)

# COPIARE
d.copy()               # Shallow
copy.deepcopy(d)       # Deep
```

---

## 🎓 Recap

**Dictionaries sono:**
- ✅ Key-value pairs
- ✅ Ordered (3.7+)
- ✅ Mutable
- ✅ O(1) lookup
- ✅ Keys immutable only

**Quando usare Dict:**
- Key-value mapping (config, JSON)
- Fast lookup per chiave
- Counting/frequency
- Grouping data
- Caching

**Pattern chiave:**
- `.get()` per accesso sicuro
- `items()` per iterazione
- Comprehension per filtrare/trasformare
- `Counter` per counting
- `defaultdict` per grouping

**Prossimi passi:**
- Pratica con Exercise 1.5
- Usa dict per JSON/API data
- Impara `Counter` e `defaultdict`
- Patterns: counting, grouping, lookup
