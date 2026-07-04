# JSON in Python

> Leggere e scrivere JSON — le 4 funzioni fondamentali, confronto con JS

## Table of Contents
1. [Le 4 funzioni — load / loads / dump / dumps](#le-4-funzioni)
2. [Mapping tipi Python ↔ JSON](#mapping-tipi-python--json)
3. [Leggere JSON](#leggere-json)
4. [Scrivere JSON](#scrivere-json)
5. [Nested JSON — strutture annidate](#nested-json)
6. [Opzioni comuni](#opzioni-comuni)
7. [Errori frequenti](#errori-frequenti)
8. [JSON vs CSV — quando usare cosa](#json-vs-csv)
9. [Quick Reference](#quick-reference)

---

## Le 4 funzioni

```
json.load(f)        → file object  → Python object   (legge da file)
json.loads(s)       → stringa      → Python object   (legge da stringa)
json.dump(obj, f)   → Python obj   → file            (scrive su file)
json.dumps(obj)     → Python obj   → stringa         (scrive su stringa)
```

**Mnemonico:** la **`s`** finale sta per **string** — `loads`/`dumps` lavorano con stringhe.

**JS comparison:**
```javascript
JSON.parse(jsonString)         ≈  json.loads(json_str)
JSON.stringify(obj, null, 2)   ≈  json.dumps(obj, indent=2)
// Node.js non ha un json.load built-in per file — devi fare:
const obj = JSON.parse(fs.readFileSync("file.json", "utf-8"))
// Python json.load() legge direttamente dal file object — più diretto
```

---

## Mapping tipi Python ↔ JSON

| Python | JSON |
|--------|------|
| `dict` | `{}` object |
| `list` | `[]` array |
| `str` | `"stringa"` |
| `int` | `42` |
| `float` | `3.14` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |
| `tuple` | `[]` array (ma si rilegge come list!) |

> **Attenzione:** le tuple Python diventano array JSON. Quando le rileggi, ottieni una list,
> non una tuple.

---

## Leggere JSON

### `json.load()` — da file

```python
import json

with open("movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)   # ritorna il tipo Python corrispondente

# Se il file contiene un array → movies è una list
# Se il file contiene un object → movies è un dict
print(type(movies))   # <class 'list'>
print(movies[0])      # {'title': 'The Godfather', 'year': 1972, ...}
```

I tipi sono già convertiti — nessun `int(row["year"])` necessario come con CSV.

### `json.loads()` — da stringa

```python
import json

json_str = '{"title": "Inception", "year": 2010, "rating": 8.8}'
movie = json.loads(json_str)   # stringa JSON → dict Python

print(movie["year"])            # 2010  (int, non stringa)
print(type(movie["rating"]))    # <class 'float'>
```

Uso tipico: risposta di un'API HTTP (il body è una stringa).

---

## Scrivere JSON

### `json.dump()` — su file

```python
import json

movies = [
    {"title": "Inception", "year": 2010, "rating": 8.8},
]

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(movies, f, indent=2, ensure_ascii=False)
```

### `json.dumps()` — su stringa

```python
import json

movie = {"title": "Inception", "year": 2010, "rating": 8.8}

json_str = json.dumps(movie, indent=2)
print(json_str)
# {
#   "title": "Inception",
#   "year": 2010,
#   "rating": 8.8
# }
```

---

## Nested JSON

JSON supporta strutture arbitrariamente annidate — dict dentro dict, liste di dict, ecc.

```python
movie = {
    "title": "The Godfather",
    "year": 1972,
    "cast": ["Marlon Brando", "Al Pacino", "James Caan"],   # lista
    "awards": {"oscars": 3, "nominations": 11},              # dict annidato
    "streaming": ["Paramount+"]
}

# Accedere a una lista annidata
lead_actor = movie["cast"][0]          # "Marlon Brando"
all_cast = movie["cast"]               # ['Marlon Brando', 'Al Pacino', 'James Caan']

# Accedere a un dict annidato
oscars = movie["awards"]["oscars"]     # 3
nominations = movie["awards"]["nominations"]  # 11

# Verificare se un valore è in una lista annidata
is_on_paramount = "Paramount+" in movie["streaming"]  # True
```

### Aggregare su più film

```python
# Totale nomination da tutti i film
total = sum(m["awards"]["nominations"] for m in movies)

# Tutti i film disponibili su Netflix
netflix_movies = [m["title"] for m in movies if "Netflix" in m["streaming"]]

# Tutti gli attori protagonisti (cast[0])
leads = [m["cast"][0] for m in movies]
```

### Modificare strutture annidate — copia prima!

```python
# SBAGLIATO — modifica l'originale
movie["watched"] = True   # ok se vuoi modificare l'originale

# CORRETTO — vuoi una copia senza toccare l'originale
entry = dict(movie)        # copia superficiale del dict
entry["watched"] = False   # safe: modifica solo la copia

# Attenzione: dict() è una copia superficiale (shallow copy)
# Le liste e i dict annidati sono ancora condivisi
# Per copia profonda usa: import copy; copy.deepcopy(movie)
```

---

## Opzioni comuni

### `indent` — formattazione leggibile

```python
# Senza indent: tutto su una riga (compatto, meno leggibile)
json.dumps(data)
# '{"title": "Inception", "year": 2010}'

# Con indent=2: formattato con 2 spazi (leggibile)
json.dumps(data, indent=2)
# {
#   "title": "Inception",
#   "year": 2010
# }
```

### `ensure_ascii=False` — caratteri non-ASCII

```python
data = {"regista": "Sergio Leone", "nota": "capolavoro del cinema italiano"}

# Default ensure_ascii=True: caratteri non-ASCII diventano escape \uXXXX
json.dumps(data)
# '{"regista": "Sergio Leone", "nota": "capolavoro del cinema italiano"}'
# (in questo caso va bene, ma con accenti: "città" invece di "città")

# Con ensure_ascii=False: caratteri Unicode preservati
json.dumps(data, ensure_ascii=False)
# '{"regista": "Sergio Leone", "nota": "capolavoro del cinema italiano"}'
# usa sempre ensure_ascii=False quando scrivi file con testo non inglese
```

### `sort_keys=True` — chiavi ordinate

```python
json.dumps(data, indent=2, sort_keys=True)
# chiavi in ordine alfabetico — utile per diff leggibili in git
```

---

## Errori frequenti

### `json.JSONDecodeError` — JSON non valido

```python
try:
    data = json.loads("{'key': 'value'}")   # SBAGLIATO: JSON vuole "key", non 'key'
except json.JSONDecodeError as e:
    print(f"JSON non valido: {e}")
```

Cause comuni:
- Virgolette singole invece di doppie (`'key'` → `"key"`)
- Virgola finale prima di `}` o `]` (JavaScript lo accetta, JSON no)
- `True`/`False` con maiuscola invece di `true`/`false`
- `None` invece di `null`

### `TypeError: Object of type X is not JSON serializable`

```python
from datetime import date
import json

data = {"date": date.today()}
json.dumps(data)   # TypeError! — date non è un tipo JSON nativo

# Soluzione 1: convertire prima di serializzare
data["date"] = str(date.today())   # "2026-06-15"

# Soluzione 2: custom encoder (avanzato)
json.dumps(data, default=str)   # usa str() come fallback per tipi non serializzabili
```

---

## JSON vs CSV

| Situazione | Strumento |
|------------|-----------|
| Dati tabulari semplici (righe + colonne) | CSV |
| Compatibilità con Excel / pandas | CSV |
| Strutture annidate (liste, dict dentro dict) | JSON |
| API REST (ricevere/inviare dati) | JSON |
| File di configurazione | JSON |
| Tipi preservati (int, float, bool) | JSON |
| File grandi con analisi dati | pandas (legge entrambi) |

---

## Quick Reference

```python
import json

# Leggere da file
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Leggere da stringa (es. risposta API)
data = json.loads(response_body)

# Scrivere su file
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Scrivere su stringa
json_str = json.dumps(data, indent=2, ensure_ascii=False)

# Accedere a strutture annidate
oscars = movie["awards"]["oscars"]       # dict annidato
lead   = movie["cast"][0]               # lista annidata
on_netflix = "Netflix" in movie["streaming"]  # membership check

# Aggregare con list comprehension
total_oscars = sum(m["awards"]["oscars"] for m in movies)
netflix_titles = [m["title"] for m in movies if "Netflix" in m["streaming"]]
```
