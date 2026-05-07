# Python Sets - Guida Completa

## 🎯 Cos'è un Set?

**Definizione:** Una collezione **non ordinata** di elementi **unici** (senza duplicati).

```python
# List (può avere duplicati)
my_list = [1, 2, 2, 3, 3, 3]
print(my_list)  # [1, 2, 2, 3, 3, 3]

# Set (rimuove automaticamente i duplicati)
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3}
```

---

## 📊 Set vs List vs Dict

| Feature | List | Set | Dict |
|---------|------|-----|------|
| **Duplicati** | ✅ Permessi | ❌ Automaticamente rimossi | Chiavi uniche |
| **Ordinato** | ✅ Mantiene ordine | ❌ Non ordinato | ✅ (da Python 3.7+) |
| **Indici** | ✅ `list[0]` | ❌ No indici | ✅ `dict["key"]` |
| **Mutabile** | ✅ append, remove | ✅ add, remove | ✅ dict[k] = v |
| **Membership test** | O(n) lento | **O(1) velocissimo** | O(1) |

---

## 🚀 Operazioni Base

### 1. Creare un Set

```python
# Metodo 1: Literal syntax
set1 = {1, 2, 3}

# Metodo 2: Da una lista (rimuove duplicati!)
numbers = [1, 2, 2, 3, 3, 3]
set2 = set(numbers)  # {1, 2, 3}

# Metodo 3: Set vuoto (ATTENZIONE!)
empty = set()  # ✅ Corretto
# empty = {}   # ❌ SBAGLIATO! Questo crea un dict vuoto
```

### 2. Aggiungere elementi

```python
my_set = {1, 2, 3}

# add() - aggiunge UN elemento
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

my_set.add(2)  # Già esiste, ignorato
print(my_set)  # {1, 2, 3, 4}

# update() - aggiunge MULTIPLI elementi
my_set.update([5, 6, 7])
print(my_set)  # {1, 2, 3, 4, 5, 6, 7}
```

### 3. Rimuovere elementi

```python
my_set = {1, 2, 3, 4}

# remove() - errore se elemento non esiste
my_set.remove(3)
print(my_set)  # {1, 2, 4}
# my_set.remove(10)  # ❌ KeyError!

# discard() - NO errore se elemento non esiste
my_set.discard(10)  # Non fa nulla, nessun errore

# pop() - rimuove elemento casuale
element = my_set.pop()
print(element)  # 1 o 2 o 4 (random!)

# clear() - svuota tutto
my_set.clear()
print(my_set)  # set()
```

### 4. Membership test (IMPORTANTE!)

```python
my_set = {1, 2, 3, 4, 5}
my_list = [1, 2, 3, 4, 5]

# Con Set: O(1) - VELOCISSIMO
print(3 in my_set)  # True - instant!

# Con List: O(n) - LENTO (scorre tutta la lista)
print(3 in my_list)  # True - deve cercare

# Con 1 milione di elementi:
# Set: 0.0001 secondi
# List: 0.5 secondi (5000x più lento!)
```

---

## 🎨 Operazioni Matematiche (come a scuola!)

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# UNION (unione) - tutti gli elementi
print(set_a | set_b)  # {1, 2, 3, 4, 5, 6}
print(set_a.union(set_b))  # Stesso risultato

# INTERSECTION (intersezione) - elementi in comune
print(set_a & set_b)  # {3, 4}
print(set_a.intersection(set_b))  # Stesso risultato

# DIFFERENCE (differenza) - in A ma non in B
print(set_a - set_b)  # {1, 2}
print(set_a.difference(set_b))  # Stesso risultato

# SYMMETRIC DIFFERENCE - in A o B, ma non in entrambi
print(set_a ^ set_b)  # {1, 2, 5, 6}
print(set_a.symmetric_difference(set_b))  # Stesso risultato
```

---

## 💡 Casi d'uso reali (quando usare Set)

### Caso 1: Rimuovere duplicati da lista

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Metodo brutto (loop)
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

# Metodo elegante (set)
unique = list(set(numbers))  # [1, 2, 3, 4]
```

### Caso 2: Check "già visto" (tracking)

```python
def find_pairs_sum_to_target(numbers, target):
    seen = set()  # Track coppie già trovate
    result = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pair = (numbers[i], numbers[j])
                if pair not in seen:  # O(1) - veloce!
                    seen.add(pair)
                    result.append(pair)
    
    return result
```

**Perché Set è meglio di List qui?**
```python
# Con List:
if pair not in result:  # O(n) - deve cercare in tutta la lista

# Con Set:
if pair not in seen:    # O(1) - instant check!
```

### Caso 3: Trovare elementi comuni tra liste

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Metodo brutto
common = [x for x in list1 if x in list2]  # O(n*m) - lento

# Metodo elegante
common = list(set(list1) & set(list2))  # O(n+m) - veloce!
print(common)  # [4, 5]
```

### Caso 4: Tag/Categories (user interests)

```python
# User tags
user1_interests = {"python", "javascript", "ai", "cinema"}
user2_interests = {"javascript", "java", "cinema", "gaming"}

# Interessi in comune
common = user1_interests & user2_interests
print(common)  # {"javascript", "cinema"}

# Tutti gli interessi (recommendation system)
all_interests = user1_interests | user2_interests
print(all_interests)  # {"python", "javascript", "ai", "cinema", "java", "gaming"}

# Interessi unici del primo utente
unique_to_user1 = user1_interests - user2_interests
print(unique_to_user1)  # {"python", "ai"}
```

---

## 🆚 Confronto con JavaScript

```javascript
// JavaScript
const mySet = new Set([1, 2, 2, 3, 3]);
console.log(mySet);  // Set {1, 2, 3}

mySet.add(4);
mySet.delete(2);
console.log(mySet.has(3));  // true
console.log(mySet.size);     // 3
```

```python
# Python - quasi identico!
my_set = {1, 2, 2, 3, 3}
print(my_set)  # {1, 2, 3}

my_set.add(4)
my_set.remove(2)  # o discard(2)
print(3 in my_set)  # True
print(len(my_set))  # 3
```

**Differenze chiave:**

| Python | JavaScript |
|--------|-----------|
| `remove(x)` | `delete(x)` |
| `x in my_set` | `mySet.has(x)` |
| `len(my_set)` | `mySet.size` |
| `{1, 2, 3}` | `new Set([1, 2, 3])` |

---

## ⚠️ Gotcha comuni

### 1. Set vuoto

```python
empty = {}       # ❌ Questo è un dict!
empty = set()    # ✅ Questo è un set vuoto

print(type({}))      # <class 'dict'>
print(type(set()))   # <class 'set'>
```

### 2. Set NON è ordinato (fino a Python 3.7+)

```python
my_set = {3, 1, 2}
print(my_set)  # Potrebbe stampare {1, 2, 3} o altro ordine
# Non fare affidamento sull'ordine!

# Se ti serve ordine + unicità, usa:
ordered_unique = list(dict.fromkeys([3, 1, 2, 1, 3]))
# [3, 1, 2]
```

### 3. Elementi devono essere immutabili (hashable)

```python
# OK - tipi immutabili
my_set = {1, 2, "hello", (1, 2), True}

# ERROR - tipi mutabili
# my_set = {1, 2, [1, 2]}        # ❌ TypeError: unhashable type: 'list'
# my_set = {1, 2, {3, 4}}        # ❌ TypeError: unhashable type: 'set'
# my_set = {1, 2, {"key": "val"}} # ❌ TypeError: unhashable type: 'dict'
```

**Regola:** Solo tipi **immutabili** (int, str, tuple, frozenset) possono stare in un set.

---

## 🎯 Quando usare Set vs List?

### Usa Set quando:
- ✅ **Non vuoi duplicati**
- ✅ **Ordine non importa**
- ✅ **Fai molti `in` checks** (membership test)
- ✅ **Vuoi operazioni matematiche** (union, intersection)
- ✅ **Performance critica** per lookup

### Usa List quando:
- ✅ **Ordine importa**
- ✅ **Vuoi duplicati**
- ✅ **Accesso per indice** (`list[0]`)
- ✅ **Devi modificare elementi in posizioni specifiche**
- ✅ **Serve slicing** (`list[1:3]`)

---

## 📊 Performance Comparison

```python
import time

# Setup
big_list = list(range(1000000))
big_set = set(range(1000000))

# Test membership (cercare un elemento)
start = time.time()
999999 in big_list  # O(n) - worst case
print(f"List lookup: {time.time() - start:.4f}s")

start = time.time()
999999 in big_set   # O(1) - constant time
print(f"Set lookup: {time.time() - start:.4f}s")

# Output tipico:
# List lookup: 0.0089s
# Set lookup: 0.0000s  (9000x più veloce!)
```

---

## 🔥 Set Comprehension (bonus)

Come list comprehension, ma crea un set:

```python
# List comprehension
squares_list = [x**2 for x in range(10)]
print(squares_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Set comprehension (note le graffe!)
squares_set = {x**2 for x in range(10)}
print(squares_set)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Rimuove automaticamente duplicati
numbers = [1, 2, 2, 3, 3, 3]
unique_doubled = {x * 2 for x in numbers}
print(unique_doubled)  # {2, 4, 6}
```

---

## ❄️ frozenset (Set Immutabile)

**frozenset** è la versione **immutabile** del set. Una volta creato, NON puoi modificarlo.

```python
# Creare un frozenset
frozen = frozenset([1, 2, 3, 4])
print(frozen)  # frozenset({1, 2, 3, 4})

# NON puoi modificarlo
# frozen.add(5)     # ❌ AttributeError: 'frozenset' object has no attribute 'add'
# frozen.remove(1)  # ❌ AttributeError: 'frozenset' object has no attribute 'remove'

# Ma PUOI usare operazioni matematiche (creano nuovi frozenset)
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a | b)  # frozenset({1, 2, 3, 4, 5})
print(a & b)  # frozenset({3})
print(a - b)  # frozenset({1, 2})
```

### Perché usare frozenset?

#### 1. Come chiave di un dizionario

Set normali NON possono essere chiavi di dict (perché mutabili), ma frozenset SÌ!

```python
# Set normale come chiave - ERROR
# cache = {
#     {1, 2, 3}: "result_1"  # ❌ TypeError: unhashable type: 'set'
# }

# frozenset come chiave - OK
cache = {
    frozenset([1, 2, 3]): "result_1",
    frozenset([4, 5, 6]): "result_2"
}

# Uso reale: cache di coordinate
visited_positions = {
    frozenset([(0, 0), (1, 1), (2, 2)]): True,
    frozenset([(0, 1), (1, 2)]): False
}
```

#### 2. Come elemento di un set

Set normali NON possono contenere altri set, ma possono contenere frozenset!

```python
# Set di set - ERROR
# set_of_sets = {
#     {1, 2},      # ❌ TypeError: unhashable type: 'set'
#     {3, 4}
# }

# Set di frozenset - OK
set_of_sets = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([5, 6])
}

# Uso reale: gruppi di tag unici
tag_combinations = {
    frozenset(["python", "backend"]),
    frozenset(["javascript", "frontend"]),
    frozenset(["python", "ai"])
}
```

### Confronto set vs frozenset

```python
# Set normale - mutabile
normal_set = {1, 2, 3}
normal_set.add(4)       # ✅ OK
hash(normal_set)         # ❌ TypeError: unhashable type: 'set'

# frozenset - immutabile
frozen_set = frozenset([1, 2, 3])
# frozen_set.add(4)     # ❌ AttributeError
hash(frozen_set)         # ✅ OK - ritorna un hash number

# Questo significa che frozenset è "hashable"
# e può essere usato dove serve un tipo immutabile
```

---

## 📝 Quick Reference

```python
# Creazione
s = {1, 2, 3}
s = set([1, 2, 3])
s = set()  # vuoto

# Aggiunta
s.add(4)
s.update([5, 6])

# Rimozione
s.remove(4)      # KeyError se non esiste
s.discard(4)     # No error se non esiste
s.pop()          # Rimuove elemento casuale
s.clear()        # Svuota tutto

# Check
4 in s           # Membership test O(1)
len(s)           # Numero elementi

# Operazioni matematiche
a | b            # Union
a & b            # Intersection
a - b            # Difference
a ^ b            # Symmetric difference

# Metodi
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
a.issubset(b)
a.issuperset(b)
```

---

## 💪 Esercizio pratico

Prova questo codice per testare la tua comprensione:

```python
# Trova parole che appaiono in entrambe le frasi
sentence1 = "the quick brown fox jumps over the lazy dog"
sentence2 = "the lazy dog sleeps under the warm sun"

words1 = set(sentence1.split())
words2 = set(sentence2.split())

# Parole in comune
common = words1 & words2
print(f"Common words: {common}")
# Output: {'lazy', 'dog', 'the'}

# Parole solo in sentence1
unique1 = words1 - words2
print(f"Only in sentence 1: {unique1}")
# Output: {'brown', 'quick', 'over', 'jumps', 'fox'}

# Tutte le parole uniche
all_words = words1 | words2
print(f"All unique words: {len(all_words)} words")
```

---

## 🎓 Recap

**Set è perfetto per:**
- ✅ Rimuovere duplicati velocemente
- ✅ Check "ho già visto questo?" (tracking)
- ✅ Operazioni matematiche su collezioni
- ✅ Performance-critical membership tests

**Ricorda sempre:**
- `{}` è un dict, non un set!
- Set non ha ordine garantito
- Solo elementi immutabili (hashable)
- Membership test è O(1) vs O(n) delle liste

**Next steps:**
- Quando incontri un problema con duplicati → pensa a Set
- Quando fai molti `in` checks → usa Set invece di List
- Quando serve union/intersection → Set operations
