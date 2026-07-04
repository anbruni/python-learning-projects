# File I/O in Python

> Reading and writing files — the Python way, compared to Node.js

## Table of Contents
1. [Opening Files — `with open()`](#opening-files--with-open)
2. [Read Methods](#read-methods)
3. [Iterating Lines](#iterating-lines)
4. [Encoding — Why utf-8 Matters](#encoding--why-utf-8-matters)
5. [Writing Files](#writing-files)
6. [File Paths with `os.path` and `pathlib`](#file-paths-with-ospath-and-pathlib)
7. [CSV — the `csv` Module](#csv--the-csv-module)
8. [Common Patterns](#common-patterns)

---

## Opening Files — `with open()`

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
# file automatically closed here — even if an error occurred
```

The `with` statement is a **context manager**: it guarantees `f.close()` is
called when the block exits, regardless of exceptions.

**JS comparison:**
```javascript
// Node.js sync equivalent
const content = fs.readFileSync("file.txt", "utf-8");
// No explicit close needed for sync reads, but Python's with is the idiom
```

### Modes

| Mode | Meaning |
|------|---------|
| `"r"` | Read (default). Fails if file doesn't exist. |
| `"w"` | Write. Creates or **overwrites**. |
| `"a"` | Append. Creates if missing, adds to the end. |
| `"x"` | Create new. Fails if file already exists. |
| `"rb"` / `"wb"` | Binary mode (images, PDFs, etc.) |

---

## Read Methods

```python
with open("movies.txt", "r", encoding="utf-8") as f:

    # 1. read() — entire file as one string
    content = f.read()
    # "The Godfather,1972,...\nThe Shawshank..."

    # 2. readlines() — list of lines, each WITH \n at the end
    lines = f.readlines()
    # ["The Godfather,1972,...\n", "The Shawshank...\n", ...]

    # 3. readline() — one line at a time, advances the cursor
    first = f.readline()   # "The Godfather,1972,...\n"
    second = f.readline()  # "The Shawshank...\n"
```

> After `read()` or `readlines()`, the file cursor is at the end.
> Call `f.seek(0)` to reset it to the beginning.

### Stripping newlines

```python
lines = f.readlines()
clean = [line.rstrip("\n") for line in lines]   # or line.strip()
```

---

## Iterating Lines

The most memory-efficient way — Python reads one line at a time:

```python
with open("movies.txt", "r", encoding="utf-8") as f:
    for line in f:                    # iterates line by line
        title = line.strip().split(",")[0]
        print(title)
```

Use this for large files. `readlines()` loads the entire file into memory.

---

## Encoding — Why utf-8 Matters

```python
# Always be explicit:
with open("file.txt", "r", encoding="utf-8") as f:
    ...

# Without encoding= Python uses the OS locale default:
# - Mac/Linux: usually utf-8 (safe)
# - Windows:   often cp1252 or latin-1 → breaks on accented chars (é, ñ, ü)
```

**Rule:** always pass `encoding="utf-8"` when reading or writing text files.

---

## Writing Files

```python
# Write (creates or overwrites)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("line one\n")
    f.write("line two\n")

# Append (adds to the end)
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("new entry\n")

# Write multiple lines at once
lines = ["Godfather\n", "Inception\n", "Matrix\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)   # no separator added — include \n yourself
```

---

## File Paths with `os.path` and `pathlib`

### `os.path` (classic, works everywhere)

```python
import os

# Path relative to the current script
BASE_DIR = os.path.dirname(__file__)
data_file = os.path.join(BASE_DIR, "data", "movies.txt")

# Check if a file exists before opening
if os.path.exists(data_file):
    with open(data_file, "r", encoding="utf-8") as f:
        ...
```

### `pathlib.Path` (modern, recommended for new code)

```python
from pathlib import Path

BASE_DIR = Path(__file__).parent
data_file = BASE_DIR / "data" / "movies.txt"   # / operator builds paths

# Shorthand for reading
content = data_file.read_text(encoding="utf-8")

# Shorthand for writing
data_file.write_text("hello\n", encoding="utf-8")
```

**JS comparison:**
```javascript
const path = require("path");
const dataFile = path.join(__dirname, "data", "movies.txt");
// __dirname  ≈  os.path.dirname(__file__)  or  Path(__file__).parent
```

---

## CSV — the `csv` Module

### Perché non usare `split(",")`

```python
# Questo sembra funzionare...
line = "The Godfather,1972,Francis Ford Coppola,9.2"
parts = line.split(",")  # ['The Godfather', '1972', 'Francis Ford Coppola', '9.2'] ✓

# ...ma fallisce sui CSV reali:
line = '"The Good, the Bad and the Ugly",1966,Sergio Leone,8.8'
parts = line.split(",")
# ['"The Good', ' the Bad and the Ugly"', '1966', 'Sergio Leone', '8.8']  ✗
# il titolo viene spezzato in due!
```

Il formato CSV standard (RFC 4180) usa le virgolette per racchiudere campi che
contengono virgole, newlines o virgolette. Il modulo `csv` gestisce tutto questo.

---

### `csv.reader` — leggere righe come liste

```python
import csv

with open("movies.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)          # legge (e salta) la prima riga header
    for row in reader:
        # row è una lista di stringhe
        title, year, director, rating, genre = row
        print(title)               # "The Good, the Bad and the Ugly" — campo unico ✓
```

---

### `csv.writer` — scrivere CSV correttamente

```python
import csv

rows = [
    ["The Good, the Bad and the Ugly", 1966, "Sergio Leone", 8.8, "Western"],
    ["Inception", 2010, "Christopher Nolan", 8.8, "Sci-Fi"],
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "year", "director", "rating", "genre"])  # header
    writer.writerows(rows)
# Il file risultante:
# title,year,director,rating,genre
# "The Good, the Bad and the Ugly",1966,Sergio Leone,8.8,Western
# Inception,2010,Christopher Nolan,8.8,Sci-Fi
```

> `newline=""` è necessario su Windows per evitare righe vuote doppie.
> Su Mac non cambia nulla ma è buona pratica aggiungerlo sempre.

---

### `csv.DictReader` — leggere come dizionari

Più comodo di `csv.reader` quando l'header è presente: ogni riga diventa
un `dict` con i nomi delle colonne come chiavi.

```python
import csv

with open("movies.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    # DictReader legge l'header automaticamente — non serve next()
    for row in reader:
        # row: {'title': 'The Godfather', 'year': '1972', 'rating': '9.2', ...}
        title = row["title"]
        rating = float(row["rating"])   # i valori sono sempre stringhe — converti!
        year = int(row["year"])
```

---

### `csv.DictWriter` — scrivere da dizionari

```python
import csv

movies = [
    {"title": "Inception", "year": 2010, "director": "Christopher Nolan",
     "rating": 8.8, "genre": "Sci-Fi"},
]

fieldnames = ["title", "year", "director", "rating", "genre"]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()       # scrive la riga header dai fieldnames
    writer.writerows(movies)
```

---

### Edge cases del formato CSV

| Caso | Come appare nel file | Come lo legge csv |
|------|----------------------|-------------------|
| Campo con virgola | `"The Good, the Bad"` | `'The Good, the Bad'` |
| Campo con virgolette | `"He said ""hello"""` | `'He said "hello"'` |
| Campo con newline | `"line one\nline two"` | `'line one\nline two'` |
| Campo vuoto | `,,` | `['', '', '']` |

---

### `csv` vs `pandas` — quando usare cosa

| Situazione | Strumento |
|------------|-----------|
| File piccoli, logica semplice | `csv` module |
| Nessuna dipendenza esterna | `csv` module |
| Analisi dati, aggregazioni, join | `pandas` |
| File grandi (milioni di righe) | `pandas` con chunking |

---

## Common Patterns

### Parse CSV-like file manualmente (solo per dati semplici)

```python
movies = []
with open("movies.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        movies.append({
            "title":    parts[0],
            "year":     int(parts[1]),
            "director": parts[2],
            "rating":   float(parts[3]),
        })
```

> Usa `split()` solo se sei certo che i dati non conterranno mai virgole.
> Per qualsiasi CSV reale, usa il modulo `csv`.

### Safe open with error handling

```python
try:
    with open("movies.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No read permission")
```

### Read JSON file

```python
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)   # parses JSON → dict/list
```

---

## Quick Reference

```python
# Read whole file
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Read lines as list
with open(path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f]

# Write file
with open(path, "w", encoding="utf-8") as f:
    f.write(content)

# Modern path building
from pathlib import Path
data = Path(__file__).parent / "data" / "file.txt"
```
