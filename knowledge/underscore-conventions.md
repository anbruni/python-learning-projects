# Underscore (_) in Python - Guida Completa

## 🎯 TL;DR - Quando usare underscore

| Tipo | Esempio | Significato | Uso |
|------|---------|-------------|-----|
| **Single `_`** | `_variable` | "Internal use" | Attributi classe/modulo |
| **Double `__`** | `__variable` | Name mangling | Evita collisioni nomi |
| **Leading + trailing** | `__init__` | Magic/dunder | Metodi speciali Python |
| **Single standalone** | `_` | Throwaway | Variabile che non serve |

---

## 📚 1. Single Leading Underscore `_name`

### Significato: "Uso interno" (convenzione)

È una **convenzione**, non un enforcement. Significa: "Questa variabile/metodo è per uso interno, non usarla direttamente."

### ✅ Quando usare (Classe)

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # ✅ "Internal" - usa i metodi!
        self.owner = "Alice"     # Pubblico
    
    def get_balance(self):
        return self._balance
    
    def _internal_calculation(self):  # ✅ Metodo interno
        return self._balance * 0.05

# Uso
account = BankAccount(100)
print(account.owner)         # ✅ OK - pubblico
print(account.get_balance()) # ✅ OK - metodo pubblico

# Tecnicamente possibile, ma non dovresti:
print(account._balance)  # ⚠️ Funziona, ma convenzione dice "non farlo"
```

**Cosa fa Python?**
- NIENTE. Python non blocca l'accesso.
- È solo una convenzione per sviluppatori.

### ✅ Quando usare (Modulo)

```python
# my_module.py

def public_function():
    """Questa è pubblica, documentata"""
    return _helper_function()

def _helper_function():
    """Uso interno del modulo"""
    return 42

_INTERNAL_CONSTANT = 100  # Costante interna

# main.py
from my_module import *  # Import con *

# Disponibile:
public_function()

# NON importato automaticamente con *:
# _helper_function()  # Non disponibile
# _INTERNAL_CONSTANT  # Non disponibile

# Ma se importi esplicitamente, funziona:
from my_module import _helper_function
_helper_function()  # ✅ Funziona
```

**Comportamento `from module import *`:**
- Variabili con `_` NON vengono importate con `*`
- Devono essere importate esplicitamente

### ❌ Quando NON usare

```python
def calculate_sum(numbers):
    _total = 0  # ❌ Non serve! È già locale
    for num in numbers:
        _total += num
    return _total

# Meglio così:
def calculate_sum(numbers):
    total = 0  # ✅ Pulito
    for num in numbers:
        total += num
    return total
```

**Perché?**
- Variabili locali in funzioni sono **già private** per definizione
- Esistono solo dentro la funzione
- L'underscore non aggiunge nulla

---

## 🔒 2. Double Leading Underscore `__name` (Name Mangling)

### Significato: Python rinomina la variabile (name mangling)

Python trasforma `__name` in `_ClassName__name` per evitare collisioni in ereditarietà.

### Come funziona

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Name mangling
    
    def get_balance(self):
        return self.__balance

# Uso
account = BankAccount(100)

# Questo NON funziona:
# print(account.__balance)  # ❌ AttributeError!

# Ma Python lo rinomina internamente:
print(account._BankAccount__balance)  # ✅ 100 (ma brutto!)

# Il metodo funziona perché è dentro la classe:
print(account.get_balance())  # ✅ 100
```

**Cosa succede?**
Python rinomina `self.__balance` in `self._BankAccount__balance`.

### Quando usare (raro!)

**Caso d'uso: Evitare collisioni in ereditarietà**

```python
class Base:
    def __init__(self):
        self.__private = "Base private"
        self._protected = "Base protected"
    
    def get_private(self):
        return self.__private

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__private = "Derived private"  # NON sovrascrive Base.__private!
    
    def get_derived_private(self):
        return self.__private

# Test
obj = Derived()
print(obj.get_private())         # "Base private" (non sovrascritto!)
print(obj.get_derived_private()) # "Derived private"

# Python ha creato due variabili diverse:
print(obj._Base__private)    # "Base private"
print(obj._Derived__private) # "Derived private"
```

**Con single underscore:**
```python
class Base:
    def __init__(self):
        self._protected = "Base"

class Derived(Base):
    def __init__(self):
        super().__init__()
        self._protected = "Derived"  # Sovrascrive!

obj = Derived()
print(obj._protected)  # "Derived" (sovrascritto)
```

### ❌ Quando NON usare

**99% dei casi!**

```python
class User:
    def __init__(self, name):
        self.__name = name  # ❌ Overkill

# Meglio:
class User:
    def __init__(self, name):
        self._name = name  # ✅ Sufficiente
```

**Regola pratica:**
- Usa `_name` (single) nella maggior parte dei casi
- Usa `__name` (double) solo se hai problemi di collisione in ereditarietà complessa

---

## ✨ 3. Double Underscore Leading & Trailing `__name__` (Magic Methods)

### Significato: Metodi speciali di Python

Chiamati "dunder methods" (double underscore) o "magic methods".

### Metodi comuni

```python
class Movie:
    def __init__(self, title, year):
        """Costruttore - chiamato quando crei oggetto"""
        self.title = title
        self.year = year
    
    def __str__(self):
        """Rappresentazione user-friendly - usata da print()"""
        return f"{self.title} ({self.year})"
    
    def __repr__(self):
        """Rappresentazione developer-friendly - usata nel debugger"""
        return f"Movie('{self.title}', {self.year})"
    
    def __eq__(self, other):
        """Uguaglianza - usata da =="""
        return self.title == other.title and self.year == other.year
    
    def __len__(self):
        """Lunghezza - usata da len()"""
        return len(self.title)

# Uso
movie = Movie("Inception", 2010)

print(movie)           # Chiama __str__ → "Inception (2010)"
print(repr(movie))     # Chiama __repr__ → "Movie('Inception', 2010)"
print(len(movie))      # Chiama __len__ → 9
print(movie == Movie("Inception", 2010))  # Chiama __eq__ → True
```

### Lista metodi magic comuni

| Metodo | Uso | Quando chiamato |
|--------|-----|-----------------|
| `__init__` | Costruttore | `obj = Class()` |
| `__str__` | String user-friendly | `print(obj)`, `str(obj)` |
| `__repr__` | String developer | `repr(obj)`, console |
| `__eq__` | Uguaglianza | `obj1 == obj2` |
| `__lt__` | Less than | `obj1 < obj2` |
| `__gt__` | Greater than | `obj1 > obj2` |
| `__len__` | Lunghezza | `len(obj)` |
| `__add__` | Addizione | `obj1 + obj2` |
| `__getitem__` | Accesso indice | `obj[key]` |
| `__setitem__` | Set indice | `obj[key] = value` |
| `__call__` | Callable | `obj()` |
| `__enter__/__exit__` | Context manager | `with obj:` |

### ❌ NON creare tuoi magic methods

```python
# ❌ Non farlo!
def __my_function():
    pass

class MyClass:
    def __my_method(self):  # ❌ Questo è name mangling, non magic!
        pass
```

**Usa solo magic methods esistenti di Python.**

---

## 🗑️ 4. Single Standalone Underscore `_`

### Significato: "Non mi interessa questo valore"

Usato come variabile "throwaway" quando devi ricevere un valore ma non lo usi.

### Caso 1: Loop quando non serve la variabile

```python
# ❌ Variabile non usata
for i in range(5):
    print("Hello")

# ✅ Più chiaro
for _ in range(5):
    print("Hello")
```

### Caso 2: Unpacking quando ignori alcuni valori

```python
# Tuple unpacking
data = ("Alice", 25, "Engineer", "NYC")

# Voglio solo nome e città
name, _, _, city = data
print(name, city)  # Alice NYC

# Con multiple values
name, *_, city = data  # Ignora tutto in mezzo
print(name, city)  # Alice NYC
```

### Caso 3: Nei loop con enumerate

```python
names = ["Alice", "Bob", "Charlie"]

# Se non ti serve l'indice:
for _, name in enumerate(names):
    print(name)
```

### Caso 4: In REPL/Jupyter

```python
>>> 2 + 2
4
>>> _ + 1  # _ contiene l'ultimo risultato
5
>>> result = _ * 2
>>> result
10
```

---

## 📊 Confronto con JavaScript

### JavaScript (private fields - ES2022)

```javascript
class BankAccount {
    #balance;  // VERO private
    
    constructor(balance) {
        this.#balance = balance;
    }
    
    getBalance() {
        return this.#balance;
    }
}

const account = new BankAccount(100);
console.log(account.getBalance());  // 100
console.log(account.#balance);  // ❌ SyntaxError! Impossibile accedere
```

**JavaScript blocca veramente l'accesso con `#`.**

### Python (convenzioni)

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Convenzione
    
    def get_balance(self):
        return self._balance

account = BankAccount(100)
print(account.get_balance())  # 100
print(account._balance)  # ⚠️ 100 - Funziona, ma non dovresti
```

**Python NON blocca l'accesso. Filosofia: "We're all consenting adults."**

---

## 🎯 Best Practices - Quando usare cosa

### ✅ Usa `_name` (single underscore)

**Per attributi "interni" di classe:**
```python
class User:
    def __init__(self, name, password):
        self.name = name           # Pubblico
        self._password = password  # ✅ Interno (usa hash!)
```

**Per metodi helper:**
```python
class DataProcessor:
    def process(self, data):
        cleaned = self._clean_data(data)
        return self._transform(cleaned)
    
    def _clean_data(self, data):  # ✅ Metodo interno
        return [x for x in data if x]
    
    def _transform(self, data):   # ✅ Metodo interno
        return [x * 2 for x in data]
```

**Per variabili di modulo interne:**
```python
# config.py
API_KEY = "public_key"
_INTERNAL_SECRET = "secret"  # ✅ Non esportato con *
```

### ❌ NON usare `_name` per variabili locali

```python
def calculate(x, y):
    _result = x + y  # ❌ Non serve!
    return _result

# Meglio:
def calculate(x, y):
    result = x + y   # ✅
    return result
```

### ⚠️ Usa `__name` (double) RARAMENTE

**Solo se hai problemi di naming collision in ereditarietà complessa:**
```python
class Framework:
    def __init__(self):
        self.__internal_state = {}  # Evita override accidentale
```

**Nella maggior parte dei casi, `_name` è sufficiente.**

### ✅ Usa `_` per throwaway

```python
# Loop senza usare variabile
for _ in range(5):
    print("Hello")

# Unpacking ignorando valori
name, _, age = ("Alice", "ignored", 25)
```

---

## 🚫 Common Mistakes (Errori comuni)

### 1. Underscore in variabili locali

```python
# ❌ Non serve
def process_data(items):
    _result = []
    _count = 0
    for _item in items:  # ❌❌❌
        _result.append(_item * 2)
        _count += 1
    return _result

# ✅ Pulito
def process_data(items):
    result = []
    count = 0
    for item in items:
        result.append(item * 2)
        count += 1
    return result
```

### 2. Usare `__name` senza motivo

```python
# ❌ Overkill
class User:
    def __init__(self, name):
        self.__name = name

# ✅ Sufficiente
class User:
    def __init__(self, name):
        self._name = name
```

### 3. Creare propri "magic methods"

```python
# ❌ Non farlo!
def __my_function():
    pass

# ✅ Usa nomi normali
def _my_helper_function():
    pass
```

---

## 📝 Quick Reference

```python
# Classe
class Example:
    public = "everyone can use"
    _internal = "internal use (convention)"
    __mangled = "name mangling (rare)"
    
    def public_method(self):
        pass
    
    def _internal_method(self):
        pass
    
    def __init__(self):  # Magic method
        pass

# Funzione
def process():
    local_var = 1      # Normale
    # _local_var = 1   # ❌ Non serve underscore

# Loop throwaway
for _ in range(5):
    print("Hi")

# Unpacking
name, _, age = ("Alice", "ignored", 25)
```

---

## 💡 Filosofia Python

> **"We're all consenting adults here."**
> — Python community

Python non forza il private. Usa convenzioni per guidare gli sviluppatori, ma si fida che userai le cose correttamente.

**Questo è diverso da Java/C++ dove `private` è enforced dal compilatore.**

---

## 🎓 Recap

| Pattern | Uso | Privacy level |
|---------|-----|---------------|
| `name` | Pubblico | Nessuna |
| `_name` | Interno (convenzione) | Soft (non in `import *`) |
| `__name` | Name mangling | Medium (rinominato) |
| `__name__` | Magic method | N/A (sistema) |
| `_` | Throwaway | N/A |

**Regola d'oro:**
- Variabili locali: NO underscore
- Attributi classe interni: `_name`
- Raramente: `__name`
- Mai creare tuoi `__magic__`

**Prossimi passi:**
- Quando crei classi, usa `_attribute` per attributi interni
- Non complicare con `__attribute` se non necessario
- Variabili locali = nomi normali, NO underscore
