# Mutabilità in Python - Guida Completa

---

## 🎯 Concetto Base

### **Immutabile** ❄️ = NON puoi modificare l'oggetto dopo averlo creato

Se vuoi "cambiarlo", Python crea un **nuovo oggetto** in memoria.

### **Mutabile** 🔥 = PUOI modificare l'oggetto direttamente

L'oggetto rimane lo stesso in memoria, ma il suo contenuto cambia.

---

## 📊 Tipi Mutabili vs Immutabili

| **IMMUTABILI** ❄️ | **MUTABILI** 🔥 |
|-------------------|-----------------|
| `int` | `list` |
| `float` | `dict` |
| `str` | `set` |
| `tuple` | (oggetti personalizzati) |
| `bool` | |
| `frozenset` | |
| `None` | |

**Regola semplice:**
- Se puoi fare `.append()`, `.remove()`, `[0] = nuovo_valore` → **Mutabile**
- Se ogni modifica crea un nuovo oggetto → **Immutabile**

---

## 🔍 Esempi Pratici - Immutabili

### 1. Stringhe (Immutabili)

```python
name = "Alice"
print(id(name))  # 140234567890 (indirizzo memoria)

# Provi a "modificare" la stringa
name = name.upper()
print(name)      # "ALICE"
print(id(name))  # 140234567999 ← DIVERSO! Nuovo oggetto!
```

**Cosa succede in memoria:**
```
PRIMA:
name → "Alice" (indirizzo: 140234567890)

DOPO name.upper():
name → "ALICE" (indirizzo: 140234567999) ← NUOVO OGGETTO!
       "Alice" (indirizzo: 140234567890) ← rimane in memoria, poi garbage collector lo elimina
```

### 2. Numeri (Immutabili)

```python
x = 10
print(id(x))  # 140234560000

x = x + 5
print(x)      # 15
print(id(x))  # 140234560160 ← DIVERSO! Nuovo oggetto!
```

**Non puoi modificare il numero 10 stesso:**
```python
x = 10
# Non esiste un modo per "cambiare" il 10 in 15
# Puoi solo riassegnare x ad un nuovo numero
```

### 3. Tuple (Immutabili)

```python
coords = (1, 2, 3)
print(id(coords))  # 140234570000

# Provi a modificare
# coords[0] = 99  # ❌ TypeError: 'tuple' object does not support item assignment

# Puoi solo creare una NUOVA tupla
coords = (99, 2, 3)
print(id(coords))  # 140234570111 ← NUOVO OGGETTO!
```

---

## 🔥 Esempi Pratici - Mutabili

### 1. Liste (Mutabili)

```python
numbers = [1, 2, 3]
print(id(numbers))  # 140234580000

# Modifichi la lista DIRETTAMENTE
numbers.append(4)
print(numbers)      # [1, 2, 3, 4]
print(id(numbers))  # 140234580000 ← STESSO OGGETTO!

numbers[0] = 99
print(numbers)      # [99, 2, 3, 4]
print(id(numbers))  # 140234580000 ← ANCORA LO STESSO!
```

**Cosa succede in memoria:**
```
MEMORIA:
numbers → [1, 2, 3] (indirizzo: 140234580000)

Dopo append(4):
numbers → [1, 2, 3, 4] (indirizzo: 140234580000) ← STESSO OGGETTO!
          ↑ il contenuto è cambiato, ma l'oggetto è lo stesso
```

### 2. Dizionari (Mutabili)

```python
person = {"name": "Alice", "age": 25}
print(id(person))  # 140234590000

# Modifichi il dizionario
person["age"] = 26
print(person)      # {"name": "Alice", "age": 26}
print(id(person))  # 140234590000 ← STESSO OGGETTO!

person["city"] = "NYC"
print(id(person))  # 140234590000 ← SEMPRE LO STESSO!
```

### 3. Set (Mutabili)

```python
tags = {"python", "coding"}
print(id(tags))  # 140234595000

tags.add("tutorial")
print(tags)      # {"python", "coding", "tutorial"}
print(id(tags))  # 140234595000 ← STESSO OGGETTO!
```

---

## ⚠️ Il Problema dei Riferimenti (CRITICO!)

### Con Immutabili (Safe ✅)

```python
a = 10
b = a  # b copia il VALORE

a = 20  # crea un NUOVO oggetto

print(a)  # 20
print(b)  # 10 ← NON è cambiato! ✅
```

**Memoria:**
```
INIZIALMENTE:
a → 10 (indirizzo: 1000)
b → 10 (indirizzo: 1000)  ← stesso oggetto OK (è immutabile)

DOPO a = 20:
a → 20 (indirizzo: 1100)  ← nuovo oggetto
b → 10 (indirizzo: 1000)  ← rimane com'era
```

### Con Mutabili (DANGEROUS! ⚠️)

```python
list1 = [1, 2, 3]
list2 = list1  # list2 NON copia! Punta allo STESSO oggetto!

list1.append(4)

print(list1)  # [1, 2, 3, 4]
print(list2)  # [1, 2, 3, 4] ← È CAMBIATO ANCHE list2! ⚠️
```

**Memoria:**
```
list1 → [1, 2, 3] ← indirizzo: 140234580000
list2 → [1, 2, 3] ← indirizzo: 140234580000 (STESSO!)

Dopo list1.append(4):
list1 → [1, 2, 3, 4] ← indirizzo: 140234580000
list2 → [1, 2, 3, 4] ← indirizzo: 140234580000 (ancora lo STESSO!)
```

**list1 e list2 sono due nomi che puntano allo STESSO oggetto in memoria!**

---

## 🛡️ Come Fare una Vera Copia (Mutabili)

### 1. Shallow Copy (copia superficiale)

**Per liste semplici (non nidificate):**

```python
list1 = [1, 2, 3]
list2 = list1.copy()  # VERA copia!
# Alternativi:
# list2 = list(list1)
# list2 = list1[:]

list1.append(4)

print(list1)  # [1, 2, 3, 4]
print(list2)  # [1, 2, 3] ← NON è cambiato! ✅

print(id(list1))  # 140234580000
print(id(list2))  # 140234580111 ← DIVERSO!
```

**Per dizionari:**

```python
dict1 = {"a": 1, "b": 2}
dict2 = dict1.copy()

dict1["c"] = 3
print(dict1)  # {"a": 1, "b": 2, "c": 3}
print(dict2)  # {"a": 1, "b": 2} ✅
```

### 2. Deep Copy (per strutture nidificate)

#### Il Problema con Shallow Copy

```python
list1 = [[1, 2], [3, 4]]
list2 = list1.copy()  # Shallow copy

list1[0].append(99)

print(list1)  # [[1, 2, 99], [3, 4]]
print(list2)  # [[1, 2, 99], [3, 4]] ← È cambiato! ⚠️
```

**Perché?** Shallow copy copia solo il **primo livello**.

#### Primo Livello vs Livelli Annidati

```python
list1 = [[1, 2], [3, 4]]
```

**Struttura:**
```
list1 (primo livello) → contiene 2 elementi:
                        ├─ elemento [0] → [1, 2]  ← secondo livello
                        └─ elemento [1] → [3, 4]  ← secondo livello
```

**Memoria con Shallow Copy:**
```
list1 → [riferimento_A, riferimento_B]
           ↓              ↓
list2 → [riferimento_A, riferimento_B]  ← puntano agli STESSI oggetti!
           ↓              ↓
        [1, 2]         [3, 4]  ← condivisi!
```

#### La Soluzione: Deep Copy

```python
import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)  # Deep copy

list1[0].append(99)

print(list1)  # [[1, 2, 99], [3, 4]]
print(list2)  # [[1, 2], [3, 4]] ← NON cambiato! ✅
```

**Memoria con Deep Copy:**
```
list1 → [riferimento_A, riferimento_B]
           ↓              ↓
        [1, 2]         [3, 4]

list2 → [riferimento_C, riferimento_D]
           ↓              ↓
        [1, 2]         [3, 4]  ← COPIE SEPARATE!
```

#### Quando Usare Shallow vs Deep Copy

| Situazione | Usa |
|------------|-----|
| Lista semplice `[1, 2, 3]` | Shallow copy (`.copy()`) |
| Lista di liste `[[1, 2], [3, 4]]` | **Deep copy** (`copy.deepcopy()`) |
| Dict semplice `{"a": 1}` | Shallow copy (`.copy()`) |
| Dict nidificato `{"user": {"name": "Alice"}}` | **Deep copy** |

---

## 💣 Gotcha Classico: Default Arguments

### IL PROBLEMA (uno dei bug più comuni!)

```python
def add_item(item, my_list=[]):  # ❌ PERICOLOSO!
    my_list.append(item)
    return my_list

# Prima chiamata
result1 = add_item("apple")
print(result1)  # ["apple"] ✅

# Seconda chiamata
result2 = add_item("banana")
print(result2)  # ["apple", "banana"] ⚠️ WTF?!

# Terza chiamata
result3 = add_item("cherry")
print(result3)  # ["apple", "banana", "cherry"] ⚠️⚠️⚠️
```

**Perché succede?**

La lista `[]` viene creata **UNA SOLA VOLTA** quando la funzione viene **definita**, NON ogni volta che viene chiamata!

```python
# Quando Python legge questa riga:
def add_item(item, my_list=[]):  # ← lista creata QUI, una volta sola!
    ...

# Tutte le chiamate usano la STESSA lista in memoria!
```

### LA SOLUZIONE

```python
def add_item(item, my_list=None):  # ✅ CORRETTO!
    if my_list is None:
        my_list = []  # Crea una NUOVA lista ogni volta
    my_list.append(item)
    return my_list

result1 = add_item("apple")
print(result1)  # ["apple"] ✅

result2 = add_item("banana")
print(result2)  # ["banana"] ✅ Corretto!

result3 = add_item("cherry")
print(result3)  # ["cherry"] ✅ Perfetto!
```

**Regola d'oro:** 
```python
# ❌ MAI fare questo con mutabili:
def func(data=[]):
def func(data={}):
def func(data=set()):

# ✅ Usa sempre None:
def func(data=None):
    if data is None:
        data = []  # o {} o set()
```

---

## 🔍 Side Effects nelle Funzioni

### Esempio 1: Modificare una lista passata

```python
def add_exclamation(words):
    words.append("!")  # Modifica la lista originale!
    return words

my_words = ["hello", "world"]
result = add_exclamation(my_words)

print(result)    # ["hello", "world", "!"]
print(my_words)  # ["hello", "world", "!"] ← cambiato! ⚠️
```

**Questo è un "side effect" (effetto collaterale).**

### Versione Senza Side Effects (Meglio!)

```python
def add_exclamation(words):
    new_words = words.copy()  # Copia!
    new_words.append("!")
    return new_words

my_words = ["hello", "world"]
result = add_exclamation(my_words)

print(result)    # ["hello", "world", "!"]
print(my_words)  # ["hello", "world"] ← NON cambiato! ✅
```

### Esempio 2: Con Immutabili (Sempre Safe)

```python
def add_exclamation(text):
    return text + "!"  # Crea una NUOVA stringa

my_text = "hello"
result = add_exclamation(my_text)

print(result)   # "hello!"
print(my_text)  # "hello" ← NON cambiato! ✅ (str è immutabile)
```

---

## 🆚 Confronto con JavaScript

### JavaScript

```javascript
// Immutabili (primitives)
let x = 10;
let y = x;
x = 20;
console.log(y);  // 10 ✅

// Mutabili (objects, arrays)
const arr1 = [1, 2, 3];
const arr2 = arr1;  // riferimento!
arr1.push(4);
console.log(arr2);  // [1, 2, 3, 4] ⚠️

// Copia vera
const arr3 = [...arr1];        // spread operator
const arr4 = Array.from(arr1);
const arr5 = arr1.slice();

// Deep copy
const obj1 = {user: {name: "Alice"}};
const obj2 = structuredClone(obj1);  // deep copy (nuovo!)
// o JSON.parse(JSON.stringify(obj1)) (vecchio modo)
```

### Python

```python
# Immutabili
x = 10
y = x
x = 20
print(y)  # 10 ✅

# Mutabili
arr1 = [1, 2, 3]
arr2 = arr1  # riferimento!
arr1.append(4)
print(arr2)  # [1, 2, 3, 4] ⚠️

# Copia vera
arr3 = arr1.copy()
arr4 = list(arr1)
arr5 = arr1[:]

# Deep copy
import copy
obj1 = {"user": {"name": "Alice"}}
obj2 = copy.deepcopy(obj1)
```

**Molto simili!**

---

## 📝 Quick Test

Indovina l'output:

```python
# Test 1
x = "hello"
y = x
x = x.upper()
print(y)  # ???

# Test 2
list1 = [1, 2, 3]
list2 = list1
list1.append(4)
print(list2)  # ???

# Test 3
tuple1 = (1, 2, [3, 4])
tuple1[2].append(5)
print(tuple1)  # ???

# Test 4
def modify(data):
    data.append(99)

my_list = [1, 2, 3]
modify(my_list)
print(my_list)  # ???
```

<details>
<summary>Risposte:</summary>

```python
# Test 1
print(y)  # "hello" 
# str è immutabile, y non cambia ✅

# Test 2
print(list2)  # [1, 2, 3, 4]
# list è mutabile, list2 punta allo stesso oggetto ⚠️

# Test 3
print(tuple1)  # (1, 2, [3, 4, 5])
# Tuple è immutabile (stessi 3 elementi), 
# ma la lista dentro è mutabile! ⚠️

# Test 4
print(my_list)  # [1, 2, 3, 99]
# La funzione modifica la lista originale (side effect) ⚠️
```
</details>

---

## 🎓 Regole da Ricordare

### 1. Immutabile = nuovo oggetto ogni volta

```python
# int, float, str, tuple, bool, frozenset, None
x = "hello"
x = x.upper()  # Crea un NUOVO oggetto
```

### 2. Mutabile = modifichi l'oggetto stesso

```python
# list, dict, set
my_list = [1, 2, 3]
my_list.append(4)  # Modifica lo STESSO oggetto
```

### 3. Assegnazione con mutabili = riferimento!

```python
list2 = list1        # ❌ NON è una copia! Stesso oggetto
list2 = list1.copy() # ✅ Questa è una copia vera
```

### 4. Default arguments con mutabili = usa None!

```python
def func(data=None):  # ✅ Corretto
    if data is None:
        data = []

def func(data=[]):    # ❌ Bug classico!
```

### 5. Shallow copy vs Deep copy

```python
# Lista semplice
list2 = list1.copy()  # ✅ Shallow copy OK

# Lista nidificata
import copy
list2 = copy.deepcopy(list1)  # ✅ Deep copy necessario
```

### 6. frozenset esiste per essere immutabile

```python
my_set = {1, 2, 3}        # Mutabile
frozen = frozenset([1, 2, 3])  # Immutabile

# frozenset può essere:
# - chiave di dict
# - elemento di un set
# - argomento hashable
```

---

## 💡 Best Practices

### ✅ DO:

```python
# Usa copy() per evitare side effects
def process_list(items):
    result = items.copy()
    result.sort()
    return result

# Usa None come default
def add_user(name, friends=None):
    if friends is None:
        friends = []
    friends.append(name)
    return friends

# Usa deepcopy per strutture nidificate
import copy
config_backup = copy.deepcopy(config)
```

### ❌ DON'T:

```python
# Non modificare liste passate senza copy
def process_list(items):
    items.sort()  # ❌ Side effect!
    return items

# Non usare mutabili come default
def add_user(name, friends=[]):  # ❌ Bug!
    friends.append(name)
    return friends

# Non fare shallow copy di strutture nidificate
nested = [[1, 2], [3, 4]]
copy = nested.copy()  # ❌ Non basta!
```

---

## 🔗 Relazione con Altri Concetti

### Mutabilità e Hashing

```python
# Solo oggetti immutabili possono essere "hashed"
hash(5)          # ✅ OK
hash("hello")    # ✅ OK
hash((1, 2))     # ✅ OK

# hash([1, 2])   # ❌ TypeError: unhashable type: 'list'
# hash({1, 2})   # ❌ TypeError: unhashable type: 'set'

# Questo significa:
# - Solo immutabili possono essere chiavi di dict
# - Solo immutabili possono essere elementi di set
```

### Mutabilità e Memory

```python
# Immutabili: Python può riusare oggetti
a = 257
b = 257
print(a is b)  # False (numeri grandi = oggetti diversi)

a = 5
b = 5
print(a is b)  # True (piccoli numeri = stesso oggetto, ottimizzazione)

# Mutabili: sempre oggetti diversi
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False (liste diverse anche se contenuto uguale)
```

---

## 🎯 Summary

| Tipo | Mutabile? | Dopo modifica | Use case |
|------|-----------|---------------|----------|
| `int`, `float`, `str` | ❌ No | Nuovo oggetto | Valori semplici |
| `tuple` | ❌ No | Nuovo oggetto | Dati immutabili, chiavi dict |
| `frozenset` | ❌ No | Nuovo oggetto | Set come chiave dict |
| `list` | ✅ Sì | Stesso oggetto | Collezioni dinamiche |
| `dict` | ✅ Sì | Stesso oggetto | Mappature chiave-valore |
| `set` | ✅ Sì | Stesso oggetto | Elementi unici |

**Ricorda:** Mutabilità ≠ "Buono" o "Cattivo". Sono strumenti diversi per scopi diversi. La chiave è **sapere cosa stai usando** e **fare copie quando necessario**! 🎯
