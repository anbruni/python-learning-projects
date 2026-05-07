# Python Lists - Guida Completa

## 🎯 Cos'è una List?

**Definizione:** Una collezione **ordinata** e **mutabile** di elementi (possono essere di tipi diversi).

```python
# List con tipi misti
my_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(my_list)  # [1, "hello", 3.14, True, [1, 2, 3]]

# List vuota
empty = []

# List con elementi dello stesso tipo (più comune)
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
```

---

## 📊 List vs Tuple vs Set vs Dict

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| **Mutabile** | ✅ Modificabile | ❌ Immutabile | ✅ Modificabile | ✅ Modificabile |
| **Ordinato** | ✅ Mantiene ordine | ✅ Mantiene ordine | ❌ Non ordinato | ✅ (da Python 3.7+) |
| **Duplicati** | ✅ Permessi | ✅ Permessi | ❌ Rimossi auto | Chiavi uniche |
| **Indici** | ✅ `list[0]` | ✅ `tuple[0]` | ❌ No indici | ✅ `dict["key"]` |
| **Performance** | Buona | Migliore | O(1) lookup | O(1) lookup |
| **Uso** | Collezioni mutabili | Dati immutabili | Unicità, math ops | Key-value pairs |

---

## 🚀 Creare List

```python
# 1. Literal syntax (più comune)
numbers = [1, 2, 3, 4, 5]

# 2. Constructor list()
from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(5))  # [0, 1, 2, 3, 4]

# 3. List comprehension (potente!)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# 4. Repetition
zeros = [0] * 5  # [0, 0, 0, 0, 0]

# 5. Empty list
empty = []
empty2 = list()
```

---

## 📦 List Methods - Reference Completa

### AGGIUNGERE ELEMENTI

```python
numbers = [1, 2, 3]

# append() - aggiunge UN elemento alla fine
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

numbers.append([5, 6])  # Aggiunge LA LISTA come elemento
print(numbers)  # [1, 2, 3, 4, [5, 6]]

# extend() - aggiunge TUTTI gli elementi di un iterable
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # [1, 2, 3, 4, 5, 6]

numbers.extend("abc")  # Aggiunge ogni carattere
print(numbers)  # [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']

# insert(index, item) - inserisce elemento in posizione specifica
numbers = [1, 2, 3]
numbers.insert(1, 99)  # Inserisce 99 all'indice 1
print(numbers)  # [1, 99, 2, 3]

numbers.insert(0, 0)  # Inserisce all'inizio
print(numbers)  # [0, 1, 99, 2, 3]

numbers.insert(100, 999)  # Index troppo grande = append
print(numbers)  # [0, 1, 99, 2, 3, 999]
```

**Confronto con JavaScript:**
```javascript
// JavaScript
arr.push(4);              // Python: append(4)
arr.push(4, 5, 6);        // Python: extend([4, 5, 6])
arr.splice(1, 0, 99);     // Python: insert(1, 99)
```

### RIMUOVERE ELEMENTI

```python
numbers = [1, 2, 3, 4, 3, 5]

# remove(item) - rimuove PRIMA occorrenza (ValueError se non esiste)
numbers.remove(3)
print(numbers)  # [1, 2, 4, 3, 5] - rimuove solo il primo 3

try:
    numbers.remove(99)  # ❌ ValueError!
except ValueError:
    print("Elemento non trovato!")

# pop() - rimuove e ritorna ULTIMO elemento
numbers = [1, 2, 3, 4, 5]
last = numbers.pop()
print(last)      # 5
print(numbers)   # [1, 2, 3, 4]

# pop(index) - rimuove e ritorna elemento a index
second = numbers.pop(1)
print(second)    # 2
print(numbers)   # [1, 3, 4]

# clear() - rimuove TUTTO
numbers.clear()
print(numbers)   # []

# del statement (non è un metodo)
numbers = [1, 2, 3, 4, 5]
del numbers[1]    # Rimuove elemento all'indice 1
print(numbers)    # [1, 3, 4, 5]

del numbers[1:3]  # Rimuove slice
print(numbers)    # [1, 5]
```

**Confronto con JavaScript:**
```javascript
// JavaScript
arr.splice(arr.indexOf(3), 1);  // Python: remove(3)
arr.pop();                       // Python: pop()
arr.shift();                     // Python: pop(0)
arr.splice(1, 1);                // Python: del arr[1] o pop(1)
arr.length = 0;                  // Python: clear()
```

### ORDINARE E INVERTIRE

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# sort() - ordina IN PLACE (modifica l'originale)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# sort(reverse=True) - ordine decrescente
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# sort(key=...) - ordinamento custom
words = ["apple", "pie", "a", "cherry"]
words.sort(key=len)  # Ordina per lunghezza
print(words)  # ['a', 'pie', 'apple', 'cherry']

# sorted() - ritorna NUOVA lista ordinata (originale intatto)
numbers = [3, 1, 4, 1, 5]
sorted_nums = sorted(numbers)
print(sorted_nums)  # [1, 1, 3, 4, 5]
print(numbers)      # [3, 1, 4, 1, 5] - originale intatto!

# reverse() - inverte IN PLACE
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# reversed() - ritorna iterator (devi convertire)
numbers = [1, 2, 3, 4, 5]
rev = list(reversed(numbers))
print(rev)      # [5, 4, 3, 2, 1]
print(numbers)  # [1, 2, 3, 4, 5] - originale intatto!
```

**Differenza chiave:**
```python
# MODIFICA ORIGINALE (in place)
numbers.sort()      # ✅ Modifica numbers
numbers.reverse()   # ✅ Modifica numbers

# RITORNA NUOVO (originale intatto)
sorted(numbers)     # ✅ Ritorna nuova lista
list(reversed(numbers))  # ✅ Ritorna nuova lista
```

**Confronto con JavaScript:**
```javascript
// JavaScript
arr.sort();           // Python: sort() (ma comportamento diverso!)
arr.reverse();        // Python: reverse()
[...arr].sort();      // Python: sorted(arr)
```

⚠️ **IMPORTANTE:** JavaScript `sort()` converte a string per default! Python ordina numericamente.

### CERCARE E CONTARE

```python
numbers = [1, 2, 3, 4, 3, 5, 3]

# index(item) - ritorna indice PRIMA occorrenza (ValueError se non esiste)
idx = numbers.index(3)
print(idx)  # 2 (prima occorrenza)

try:
    numbers.index(99)  # ❌ ValueError!
except ValueError:
    print("Elemento non trovato!")

# index(item, start, end) - cerca in un range
idx = numbers.index(3, 3, 7)  # Cerca 3 da indice 3 a 7
print(idx)  # 4 (seconda occorrenza)

# count(item) - conta occorrenze
count = numbers.count(3)
print(count)  # 3

# Membership test (non è un metodo, ma importante!)
print(3 in numbers)      # True
print(99 not in numbers) # True
```

**Confronto con JavaScript:**
```javascript
// JavaScript
arr.indexOf(3);           // Python: index(3)
arr.includes(3);          // Python: 3 in arr
arr.filter(x => x === 3).length;  // Python: count(3)
```

### COPIARE

```python
original = [1, 2, 3]

# copy() - shallow copy (copia superficiale)
copied = original.copy()
copied.append(4)
print(original)  # [1, 2, 3] - intatto!
print(copied)    # [1, 2, 3, 4]

# Alternative per shallow copy
copied2 = original[:]          # Slicing
copied3 = list(original)       # Constructor

# ATTENZIONE: shallow copy con nested lists!
matrix = [[1, 2], [3, 4]]
shallow = matrix.copy()
shallow[0].append(99)  # Modifica lista interna
print(matrix)   # [[1, 2, 99], [3, 4]] ← Anche matrix cambia!
print(shallow)  # [[1, 2, 99], [3, 4]]

# Deep copy per nested structures
import copy
matrix = [[1, 2], [3, 4]]
deep = copy.deepcopy(matrix)
deep[0].append(99)
print(matrix)  # [[1, 2], [3, 4]] ← Intatto!
print(deep)    # [[1, 2, 99], [3, 4]]
```

---

## ✂️ List Slicing - Guida Completa

**Sintassi:** `list[start:end:step]`

- `start`: indice di partenza (inclusive), default 0
- `end`: indice di fine (exclusive), default len(list)
- `step`: incremento, default 1

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# BASIC SLICING
numbers[2:5]      # [2, 3, 4] - da 2 a 5 (escluso)
numbers[:5]       # [0, 1, 2, 3, 4] - dall'inizio a 5
numbers[5:]       # [5, 6, 7, 8, 9] - da 5 alla fine
numbers[:]        # [0, 1, ..., 9] - copia intera lista

# STEP (salto)
numbers[::2]      # [0, 2, 4, 6, 8] - ogni 2 elementi
numbers[1::2]     # [1, 3, 5, 7, 9] - ogni 2 da indice 1
numbers[::3]      # [0, 3, 6, 9] - ogni 3 elementi

# NEGATIVE STEP (reverse)
numbers[::-1]     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - lista inversa
numbers[::-2]     # [9, 7, 5, 3, 1] - ogni 2, al contrario

# NEGATIVE INDICES
numbers[-1]       # 9 - ultimo elemento
numbers[-2]       # 8 - penultimo
numbers[-3:]      # [7, 8, 9] - ultimi 3 elementi
numbers[:-3]      # [0, 1, 2, 3, 4, 5, 6] - tutti tranne ultimi 3
numbers[-5:-2]    # [5, 6, 7] - da -5 a -2 (escluso)

# COMBINAZIONI AVANZATE
numbers[2:8:2]    # [2, 4, 6] - da 2 a 8, ogni 2
numbers[-2::-1]   # [8, 7, 6, 5, 4, 3, 2, 1, 0] - da penultimo a inizio
numbers[5:2:-1]   # [5, 4, 3] - da 5 a 2 all'indietro
```

### SLICE ASSIGNMENT (modificare con slicing)

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sostituire una slice
numbers[2:5] = [20, 30, 40]
print(numbers)  # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# Sostituire con meno elementi (lista si accorcia)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[2:5] = [99]
print(numbers)  # [0, 1, 99, 5, 6, 7, 8, 9]

# Sostituire con più elementi (lista si allunga)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[2:5] = [20, 30, 40, 50, 60]
print(numbers)  # [0, 1, 20, 30, 40, 50, 60, 5, 6, 7, 8, 9]

# Inserire elementi (slice vuota)
numbers = [0, 1, 2, 3, 4]
numbers[2:2] = [99, 88]  # Inserisce a indice 2
print(numbers)  # [0, 1, 99, 88, 2, 3, 4]

# Rimuovere elementi (assegnare lista vuota)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[2:5] = []
print(numbers)  # [0, 1, 5, 6, 7, 8, 9]

# Sostituire ogni secondo elemento
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] = [10, 20, 30, 40, 50]
print(numbers)  # [10, 1, 20, 3, 30, 5, 40, 7, 50, 9]
```

**Confronto con JavaScript:**
```javascript
// JavaScript
arr.slice(2, 5);          // Python: arr[2:5]
arr.slice(-3);            // Python: arr[-3:]
arr.slice();              // Python: arr[:] (copia)
[...arr].reverse();       // Python: arr[::-1]
arr.filter((_, i) => i % 2 === 0);  // Python: arr[::2]
```

---

## 🔗 Reference vs Copy (MOLTO IMPORTANTE!)

### Il problema delle Reference

```python
# REFERENCE (stesso oggetto)
a = [1, 2, 3]
b = a           # b punta allo STESSO oggetto
b.append(4)
print(a)        # [1, 2, 3, 4] ← a è cambiato!
print(b)        # [1, 2, 3, 4]
print(a is b)   # True - stesso oggetto in memoria

# SHALLOW COPY (nuovo oggetto, stessi elementi)
a = [1, 2, 3]
b = a.copy()    # o a[:] o list(a)
b.append(4)
print(a)        # [1, 2, 3] ← a NON cambia
print(b)        # [1, 2, 3, 4]
print(a is b)   # False - oggetti diversi
```

### Shallow Copy Gotcha con Nested Lists

```python
# SHALLOW COPY con nested lists
matrix = [[1, 2], [3, 4]]
shallow = matrix.copy()

# Modifico lista esterna
shallow.append([5, 6])
print(matrix)   # [[1, 2], [3, 4]] ← intatto
print(shallow)  # [[1, 2], [3, 4], [5, 6]]

# ⚠️ MA modifico lista INTERNA
shallow[0].append(99)
print(matrix)   # [[1, 2, 99], [3, 4]] ← CAMBIA!
print(shallow)  # [[1, 2, 99], [3, 4], [5, 6]]
```

**Perché?** Shallow copy copia la lista esterna, ma le liste interne sono ancora reference!

```python
# Visualizzazione:
matrix = [[1, 2], [3, 4]]
shallow = matrix.copy()

# Dopo copy:
# matrix[0] e shallow[0] puntano ALLO STESSO [1, 2]!
print(matrix[0] is shallow[0])  # True ← stesso oggetto!
```

### Deep Copy per Nested Structures

```python
import copy

# DEEP COPY (copia tutto ricorsivamente)
matrix = [[1, 2], [3, 4]]
deep = copy.deepcopy(matrix)

deep[0].append(99)
print(matrix)  # [[1, 2], [3, 4]] ← INTATTO!
print(deep)    # [[1, 2, 99], [3, 4]]

print(matrix[0] is deep[0])  # False - oggetti diversi
```

### Funzioni e References

```python
# ⚠️ Liste passate a funzioni sono REFERENCE!
def add_item(my_list, item):
    my_list.append(item)  # Modifica l'originale!

original = [1, 2, 3]
add_item(original, 4)
print(original)  # [1, 2, 3, 4] ← cambiato!

# ✅ Soluzione: copia dentro la funzione
def add_item_safe(my_list, item):
    result = my_list.copy()  # Copia prima!
    result.append(item)
    return result

original = [1, 2, 3]
new_list = add_item_safe(original, 4)
print(original)  # [1, 2, 3] ← intatto
print(new_list)  # [1, 2, 3, 4]
```

**Confronto con JavaScript:**
```javascript
// JavaScript - stesso comportamento!
const a = [1, 2, 3];
const b = a;           // Reference
b.push(4);
console.log(a);        // [1, 2, 3, 4] - cambia!

const c = [...a];      // Shallow copy (Python: a.copy())
const d = structuredClone(a);  // Deep copy (Python: deepcopy(a))
```

---

## 📐 Nested Lists (Liste 2D - Matrici)

```python
# Matrice 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accesso
print(matrix[0])      # [1, 2, 3] - prima riga
print(matrix[0][1])   # 2 - riga 0, colonna 1
print(matrix[1][2])   # 6 - riga 1, colonna 2

# Modificare
matrix[0][0] = 99
print(matrix)  # [[99, 2, 3], [4, 5, 6], [7, 8, 9]]

# Iterare
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # Newline
# Output:
# 99 2 3 
# 4 5 6 
# 7 8 9

# Con indici
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"[{i}][{j}] = {matrix[i][j]}")
```

### Creare Matrici

```python
# ❌ SBAGLIATO - crea reference!
matrix = [[0] * 3] * 3
matrix[0][0] = 99
print(matrix)  # [[99, 0, 0], [99, 0, 0], [99, 0, 0]] ← tutte cambiano!

# ✅ CORRETTO - list comprehension
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 99
print(matrix)  # [[99, 0, 0], [0, 0, 0], [0, 0, 0]] ← solo prima riga

# Matrice custom
matrix = [[i + j for j in range(3)] for i in range(3)]
print(matrix)
# [[0, 1, 2],
#  [1, 2, 3],
#  [2, 3, 4]]
```

### Operazioni comuni su Matrici

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten (2D → 1D)
flat = [item for row in matrix for item in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Transpose (scambiare righe e colonne)
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Con zip (più elegante)
transposed = list(map(list, zip(*matrix)))
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Max in 2D
max_val = max(max(row) for row in matrix)
print(max_val)  # 9

# Sum all elements
total = sum(sum(row) for row in matrix)
print(total)  # 45
```

---

## ⚡ List Operations

```python
# CONCATENATION
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# REPETITION
repeated = [1, 2] * 3
print(repeated)  # [1, 2, 1, 2, 1, 2]

# MEMBERSHIP
print(3 in [1, 2, 3, 4])      # True
print(99 not in [1, 2, 3, 4]) # True

# LENGTH
print(len([1, 2, 3, 4, 5]))  # 5

# MIN/MAX/SUM (con numeri)
numbers = [3, 1, 4, 1, 5, 9, 2]
print(min(numbers))  # 1
print(max(numbers))  # 9
print(sum(numbers))  # 25

# MIN/MAX con stringhe (alfabetico)
words = ["apple", "banana", "cherry"]
print(min(words))  # "apple"
print(max(words))  # "cherry"

# ANY/ALL
print(any([False, False, True, False]))  # True (almeno uno True)
print(all([True, True, True, True]))     # True (tutti True)
print(all([True, False, True]))          # False
```

---

## 🎨 List Comprehension (pattern fondamentale)

```python
# BASIC
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# CON CONDIZIONE (filter)
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# CON IF-ELSE (map + filter)
values = [x if x % 2 == 0 else -x for x in range(5)]
print(values)  # [0, -1, 2, -3, 4]

# NESTED (matrici)
matrix = [[i + j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# CON FUNZIONI
def double(x):
    return x * 2

doubled = [double(x) for x in range(5)]
print(doubled)  # [0, 2, 4, 6, 8]

# FLATTEN con nested comprehension
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [item for row in matrix for item in row]
print(flat)  # [1, 2, 3, 4, 5, 6]
```

**Confronto con JavaScript:**
```javascript
// JavaScript
arr.map(x => x ** 2);             // Python: [x**2 for x in arr]
arr.filter(x => x % 2 === 0);     // Python: [x for x in arr if x % 2 == 0]
arr.map(x => x % 2 === 0 ? x : -x); // Python: [x if x%2==0 else -x for x in arr]
```

---

## 📈 Performance e Best Practices

### Performance Comparison

```python
import time

# Setup
n = 100000

# Append (O(1) amortized)
start = time.time()
result = []
for i in range(n):
    result.append(i)
print(f"Append: {time.time() - start:.4f}s")

# List comprehension (più veloce!)
start = time.time()
result = [i for i in range(n)]
print(f"Comprehension: {time.time() - start:.4f}s")

# Concatenation ripetuta (LENTO! O(n^2))
start = time.time()
result = []
for i in range(1000):  # Solo 1000 per non aspettare troppo
    result = result + [i]  # ❌ Crea nuova lista ogni volta!
print(f"Concatenation: {time.time() - start:.4f}s")

# Output tipico:
# Append: 0.0089s
# Comprehension: 0.0065s (25% più veloce!)
# Concatenation: 0.0234s (molto più lento!)
```

### Best Practices

```python
# ✅ DO: Usa list comprehension quando possibile
squares = [x**2 for x in range(10)]

# ❌ DON'T: Loop manuale se non necessario
squares = []
for x in range(10):
    squares.append(x**2)

# ✅ DO: Usa extend per aggiungere multipli elementi
my_list.extend([1, 2, 3])

# ❌ DON'T: Append in loop
for item in [1, 2, 3]:
    my_list.append(item)

# ✅ DO: Usa slicing per copiare
copy = original[:]

# ❌ DON'T: Loop manuale
copy = []
for item in original:
    copy.append(item)

# ✅ DO: Usa enumerate quando serve indice
for i, item in enumerate(my_list):
    print(f"{i}: {item}")

# ❌ DON'T: range(len())
for i in range(len(my_list)):
    print(f"{i}: {my_list[i]}")

# ✅ DO: Usa 'in' per membership test
if item in my_list:
    print("Found!")

# ❌ DON'T: Loop manuale
found = False
for x in my_list:
    if x == item:
        found = True
        break
```

---

## ⚠️ Common Gotchas (errori comuni)

### 1. Modificare lista durante iterazione

```python
# ❌ SBAGLIATO - comportamento imprevedibile
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # ❌ Modifica durante iterazione!
print(numbers)  # [1, 3, 5] - sembra OK, ma...

numbers = [2, 2, 4, 6]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # [2, 6] ← Salta elementi! Bug!

# ✅ CORRETTO - crea nuova lista
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # [1, 3, 5]

# ✅ O itera su copia
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # Copia!
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # [1, 3, 5]
```

### 2. Default mutable argument

```python
# ❌ SBAGLIATO - lista condivisa tra chiamate!
def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [1, 2] ← include chiamata precedente!
print(add_to_list(3))  # [1, 2, 3] ← include tutte!

# ✅ CORRETTO - usa None come default
def add_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [2] ← lista fresca!
print(add_to_list(3))  # [3] ← lista fresca!
```

### 3. Shallow copy con nested lists

```python
# ❌ Shallow copy non basta per nested
matrix = [[1, 2], [3, 4]]
copy = matrix.copy()
copy[0].append(99)
print(matrix)  # [[1, 2, 99], [3, 4]] ← modificato!

# ✅ Usa deepcopy
import copy
matrix = [[1, 2], [3, 4]]
deep = copy.deepcopy(matrix)
deep[0].append(99)
print(matrix)  # [[1, 2], [3, 4]] ← intatto!
```

### 4. List repetition con mutable objects

```python
# ❌ SBAGLIATO - crea reference!
matrix = [[0] * 3] * 3  # 3 righe, 3 colonne
matrix[0][0] = 99
print(matrix)  # [[99, 0, 0], [99, 0, 0], [99, 0, 0]] ← tutte!

# ✅ CORRETTO - list comprehension
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 99
print(matrix)  # [[99, 0, 0], [0, 0, 0], [0, 0, 0]] ← solo prima!
```

### 5. Confondere sort() con sorted()

```python
# sort() modifica IN PLACE, ritorna None
numbers = [3, 1, 2]
result = numbers.sort()
print(result)   # None ← non ritorna nulla!
print(numbers)  # [1, 2, 3] ← modificato

# sorted() ritorna NUOVA lista
numbers = [3, 1, 2]
result = sorted(numbers)
print(result)   # [1, 2, 3]
print(numbers)  # [3, 1, 2] ← intatto
```

---

## 🆚 Python List vs JavaScript Array

| Operazione | Python | JavaScript |
|-----------|--------|-----------|
| Creare | `[1, 2, 3]` | `[1, 2, 3]` |
| Lunghezza | `len(arr)` | `arr.length` |
| Aggiungere fine | `arr.append(x)` | `arr.push(x)` |
| Aggiungere multipli | `arr.extend([x, y])` | `arr.push(x, y)` |
| Aggiungere inizio | `arr.insert(0, x)` | `arr.unshift(x)` |
| Rimuovere fine | `arr.pop()` | `arr.pop()` |
| Rimuovere inizio | `arr.pop(0)` | `arr.shift()` |
| Rimuovere per valore | `arr.remove(x)` | `arr.splice(arr.indexOf(x), 1)` |
| Trovare indice | `arr.index(x)` | `arr.indexOf(x)` |
| Contare | `arr.count(x)` | `arr.filter(v => v === x).length` |
| Membership | `x in arr` | `arr.includes(x)` |
| Slice | `arr[1:3]` | `arr.slice(1, 3)` |
| Reverse | `arr[::-1]` | `[...arr].reverse()` |
| Map | `[f(x) for x in arr]` | `arr.map(f)` |
| Filter | `[x for x in arr if cond]` | `arr.filter(cond)` |
| Sort in place | `arr.sort()` | `arr.sort()` |
| Sort copia | `sorted(arr)` | `[...arr].sort()` |
| Copy | `arr.copy()` o `arr[:]` | `[...arr]` o `arr.slice()` |

**Differenze chiave:**
- Python: `len()` è funzione, JS: `.length` è property
- Python: metodi ritornano `None` se modificano in place
- Python: slicing `[1:3]`, JS: metodo `.slice(1, 3)`
- Python: negative indices `[-1]`, JS: no (ma c'è `at(-1)`)

---

## 📝 Quick Reference

```python
# CREAZIONE
arr = [1, 2, 3]
arr = list("abc")           # ['a', 'b', 'c']
arr = [x**2 for x in range(5)]

# ACCESSO
arr[0]                      # Primo
arr[-1]                     # Ultimo
arr[1:3]                    # Slice

# MODIFICARE
arr[0] = 99
arr[1:3] = [10, 20]
arr.append(4)               # Aggiungi fine
arr.extend([5, 6])          # Aggiungi multipli
arr.insert(0, 0)            # Inserisci a indice
arr.remove(3)               # Rimuovi primo 3
arr.pop()                   # Rimuovi ultimo
arr.pop(0)                  # Rimuovi a indice
arr.clear()                 # Svuota

# ORDINARE
arr.sort()                  # In place
arr.reverse()               # In place
sorted(arr)                 # Nuova lista
list(reversed(arr))         # Nuova lista

# CERCARE
arr.index(3)                # Indice
arr.count(3)                # Occorrenze
3 in arr                    # Membership

# COPIARE
arr.copy()                  # Shallow
arr[:]                      # Shallow
import copy; copy.deepcopy(arr)  # Deep

# INFO
len(arr)
min(arr)
max(arr)
sum(arr)
```

---

## 🎓 Recap

**Liste sono:**
- ✅ Ordinate (mantengono ordine inserimento)
- ✅ Mutabili (possono essere modificate)
- ✅ Permettono duplicati
- ✅ Accessibili per indice
- ✅ Possono contenere tipi misti

**Quando usare List:**
- Collezione di elementi con ordine importante
- Serve accesso per indice
- Serve modificare/aggiungere/rimuovere
- Duplicati sono permessi

**Pattern chiave da ricordare:**
1. List comprehension > loop quando possibile
2. `append()` per singoli, `extend()` per multipli
3. Slicing `[:]` per copiare
4. `sort()` modifica, `sorted()` ritorna nuovo
5. Attenzione a reference vs copy!

**Prossimi passi:**
- Pratica slicing fino a padroneggiarlo completamente
- Usa list comprehension invece dei loop
- Attenzione a shallow vs deep copy con nested lists
- Confronta con Tuple quando serve immutabilità
