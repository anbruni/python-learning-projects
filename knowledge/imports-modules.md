# Imports & Modules in Python

> Organizzare il codice in file riutilizzabili e usare la standard library

## Table of Contents
1. [import module](#import-module)
2. [from module import](#from-module-import)
3. [import as alias](#import-as-alias)
4. [Creare un modulo custom](#creare-un-modulo-custom)
5. [if __name__ == "__main__"](#if-__name__--__main__)
6. [Standard Library — moduli essenziali](#standard-library--moduli-essenziali)

---

## import module

```python
import math
import random
import datetime

# Accesso con prefisso del modulo
math.sqrt(16)       # 4.0
math.pi             # 3.14159...
random.randint(1, 10)
datetime.date.today()
```

**Quando usarlo:** quando usi più funzioni/costanti dello stesso modulo — il prefisso rende chiaro da dove viene ogni cosa.

---

## from module import

```python
from math import sqrt, pi
from random import choice, shuffle
from datetime import datetime, timedelta

# Accesso diretto, senza prefisso
sqrt(16)        # 4.0
print(pi)       # 3.14159...
choice(["a", "b", "c"])
```

**Quando usarlo:** quando hai bisogno solo di una o due cose da un modulo.

**Attenzione:** può causare conflitti di nomi:
```python
from math import floor
floor = "ground floor"  # sovrascrive la funzione importata!
```

---

## import as alias

```python
import numpy as np          # convenzione standard
import pandas as pd         # convenzione standard
import datetime as dt
from math import sqrt as sq

np.array([1, 2, 3])
pd.DataFrame(data)
dt.datetime.now()
sq(16)  # 4.0
```

**Quando usarlo:**
- Nomi lunghi che scrivi spesso (`numpy`, `pandas`, `datetime`)
- Convenzioni del settore (`np`, `pd`, `plt` per matplotlib)

---

## Creare un modulo custom

Qualsiasi file `.py` è un modulo. Basta importarlo:

```
# struttura del progetto
my_project/
    main.py
    cinema_utils.py   ← modulo custom
```

```python
# cinema_utils.py
CURRENT_YEAR = 2026

def format_title(title, year):
    return f"{title} ({year})"

def is_valid_rating(rating):
    return 0 <= rating <= 10
```

```python
# main.py — tre modi di importare cinema_utils

# Modo 1: import module
import cinema_utils
cinema_utils.format_title("Inception", 2010)   # "Inception (2010)"
cinema_utils.CURRENT_YEAR                       # 2026

# Modo 2: from module import
from cinema_utils import format_title
format_title("Inception", 2010)                # no prefisso

# Modo 3: alias
from cinema_utils import is_valid_rating as valid
valid(9.3)   # True
```

### Dove Python cerca i moduli

```python
import sys
print(sys.path)  # lista di directory dove Python cerca i file .py
# include la directory corrente → i tuoi file .py locali funzionano subito
```

---

## if __name__ == "__main__"

Ogni file `.py` ha una variabile `__name__`:

| Come viene eseguito | Valore di `__name__` |
|---------------------|----------------------|
| `python cinema_utils.py` (diretto) | `"__main__"` |
| `import cinema_utils` (importato) | `"cinema_utils"` |

```python
# cinema_utils.py

def format_title(title, year):
    return f"{title} ({year})"

if __name__ == "__main__":
    # Questo blocco esegue SOLO quando fai: python cinema_utils.py
    # Viene SALTATO quando un altro file fa: import cinema_utils
    print("Testing format_title:")
    print(format_title("Inception", 2010))
```

**Perché è importante:**
```python
# Senza if __name__ == "__main__":
# ogni volta che qualcuno importa il tuo modulo,
# il codice di test esegue automaticamente → indesiderato!

import cinema_utils
# → "Testing format_title: Inception (2010)"  ← NON vogliamo questo
```

**Pattern standard in ogni progetto Python:**
```python
def main():
    # logica principale del programma
    pass

if __name__ == "__main__":
    main()
```

---

## Standard Library — moduli essenziali

| Modulo | Usi principali |
|--------|---------------|
| `math` | `sqrt`, `floor`, `ceil`, `pi`, `log`, `pow` |
| `random` | `random()`, `randint()`, `choice()`, `shuffle()`, `sample()` |
| `datetime` | `date.today()`, `datetime.now()`, `timedelta` |
| `os` | `os.path.join()`, `os.listdir()`, `os.environ` |
| `json` | `json.loads()`, `json.dumps()` |
| `collections` | `Counter`, `defaultdict`, `deque` |
| `pathlib` | `Path` — gestione path moderna |
| `re` | regex — pattern matching su stringhe |
| `sys` | `sys.argv`, `sys.path`, `sys.exit()` |
| `itertools` | `chain`, `islice`, `product` — iteratori avanzati |

### Esempi rapidi

```python
# math
import math
math.sqrt(25)        # 5.0
math.ceil(7.1)       # 8
math.floor(7.9)      # 7

# random
import random
random.randint(1, 6)          # dado: 1-6
random.choice(["a","b","c"])  # elemento casuale
random.shuffle(lista)         # mescola in-place

# datetime
from datetime import datetime, timedelta
now = datetime.now()
print(now.strftime("%Y-%m-%d"))   # "2026-06-03"
week_ago = now - timedelta(days=7)

# collections
from collections import Counter, defaultdict
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
Counter(words)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

d = defaultdict(list)
d["films"].append("Inception")  # no KeyError anche se "films" non esiste
```
