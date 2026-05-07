# PYTHON ROADMAP — BASI SOLIDE, PROGETTI REALI (MVP)
## 8 settimane: da zero a job-ready con fondamenta solide

🎯 **OBIETTIVO:** Toccare TUTTI gli argomenti essenziali con basi solide + 3 progetti cinema MVP per portfolio

---

## FILOSOFIA

**✅ DO:**
- Coprire tutti i fondamentali (niente skip)
- Esercizi mirati per ogni concetto
- 3 progetti MVP (qualità > quantità)
- Progressione: base → intermedio → avanzato
- Basi così solide da poter continuare da solo

**❌ DON'T:**
- Features avanzate non essenziali (Docker, Redis, JWT)
- Perfezionismo (MVP > perfetto)
- 10 progetti mediocri (meglio 3 solidi)
- Topics che impari meglio on-the-job

---

## STRUCTURE

**Week 1-4:** Fondamentali Python (exercises only)
**Week 5:** 🎬 PROJECT 1 - Movie Data Collector
**Week 6:** 🎬 PROJECT 2 - Movie Analytics Dashboard  
**Week 7-8:** 🎬 PROJECT 3 - Movie Recommendation API (MVP)

---

# WEEK 1-2: CORE PYTHON FUNDAMENTALS

## DAY 1-2: Data Types & Control Flow

### Esercizio 1.0 - Git & GitHub workflow setup ⚡ NEW (2-3h)

**Perché farlo subito:** è la *prima cosa* che un recruiter vede. Repo con commit `"update"` × 50 e nessun README = cestino. Da qui in poi **ogni esercizio e ogni progetto vive su GitHub** seguendo questo workflow.

**Cosa imparare:**
- **Branch workflow**: `main` → feature branches (`feat/<feature>`, `fix/<bug>`) → PR → merge
- **Conventional Commits**: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:` (niente più commit `"update"`)
- **`.gitignore`** generato per Python con [gitignore.io](https://www.toptal.com/developers/gitignore)
- **Pull Request template**: `.github/pull_request_template.md` con sezioni *What / Why / How tested*
- **README professionale**: badge, descrizione, stack, setup, esempi, architettura
- **GitHub profile README**: il "biglietto da visita" pubblico

**Esercizio:**
1. Crea repo `python-roadmap-exercises` su GitHub
2. `.gitignore` Python + `README.md` con piano del percorso
3. Aggiungi `.github/pull_request_template.md`
4. Crea il tuo profile README pubblico (`github.com/<tuo-handle>/<tuo-handle>`)
5. **Da ora:** ogni esercizio = branch + PR + merge (non commit diretti su main)

📚 **Risorse:**
- [GitHub flow — guida ufficiale](https://docs.github.com/en/get-started/using-github/github-flow)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Awesome README templates](https://github.com/matiassingers/awesome-readme) ⭐
- [Profile README inspiration](https://github.com/abhisheknaiidu/awesome-github-profile-readme)
- [Atlassian Git tutorials](https://www.atlassian.com/git/tutorials) (visualmente molto chiari)

**Deliverable:** repo pubblico iniziato + profile README live.

---

### Esercizio 1.1 - Type conversions & None
- Input: mixed data (strings, numbers, None)
- Task: convert safely, handle None, check types

### Esercizio 1.2 - Control flow challenges
- FizzBuzz variations
- Nested loops con break/continue
- Ternary operators

**Concetti coperti:** int, float, str, bool, None, if/elif/else, for, while, break, continue, pass

---

## DAY 3-5: Data Structures (CRITICO)

### Esercizio 1.3 - Lists deep dive
- Methods: append, extend, insert, pop, remove, sort, reverse
- Slicing: [start:end:step]
- List operations: concatenation, repetition
- Nesting: list of lists

### Esercizio 1.4 - Tuples & unpacking
- Immutability vs lists
- Tuple unpacking: `a, b = (1, 2)`
- Multiple return values
- Named tuples (quick intro)

### Esercizio 1.5 - Dictionaries mastery
- Creation: literal, dict(), dict comprehension
- Access: `[]` vs `.get()`
- Methods: keys(), values(), items()
- Nested dicts (JSON-like structures)
- Common patterns: counting, grouping, lookup

### Esercizio 1.6 - Sets operations
- Uniqueness
- Operations: union, intersection, difference
- Membership testing (performance)

**Deliverable:** 4 esercizi completati, solide basi su tutte le strutture dati

---

## DAY 6-8: Mutability & Memory (FONDAMENTALE)

### Esercizio 1.7 - Mutability gotchas
- Mutable (list, dict, set) vs Immutable (int, str, tuple)
- Assignment vs copy
- Function side effects
- Default argument trap: `def func(data=[]):`

### Esercizio 1.8 - Shallow vs deep copy
- `list.copy()` vs `copy.deepcopy()`
- When it matters (nested structures)
- Practical examples

**Concetti coperti:** mutability, reference, copy, shallow copy, deep copy, side effects

---

## DAY 9-11: Functions (SUPER IMPORTANTE)

### Esercizio 1.9 - Functions basics
- Parameters vs arguments
- Return values (single, multiple)
- Scope (local, global, nonlocal)
- Docstrings

### Esercizio 1.10 - Default parameters
- Correct way: `def func(x, default=None):`
- TRAP: `def func(x, data=[]):`  # DON'T
- When to use None as default

### Esercizio 1.11 - *args and **kwargs
- Variable arguments
- Practical use cases
- Combining positional, keyword, *args, **kwargs

### Esercizio 1.12 - Lambda functions
- Syntax: `lambda x: x * 2`
- When to use (map, filter, sort key)
- When NOT to use (complex logic)

### Esercizio 1.13 - Pure vs impure functions
- Pure: no side effects, deterministic
- Impure: modifies state, I/O
- Why it matters (testing, debugging)

**Deliverable:** 5 esercizi funzioni, capire scope e side effects

---

## DAY 12-14: Comprehensions & Iteration Tools

### Esercizio 1.14 - List comprehensions
- Basic: `[x*2 for x in range(10)]`
- With filter: `[x for x in range(10) if x % 2 == 0]`
- Nested: `[x+y for x in range(3) for y in range(3)]`

### Esercizio 1.15 - Dict & set comprehensions
- Dict: `{k: v for k, v in pairs}`
- Set: `{x for x in data}`
- Transform datasets

### Esercizio 1.16 - Iteration tools
- `enumerate()`: index + value
- `zip()`: parallel iteration
- `map()`: transform
- `filter()`: select
- When to use comprehension vs map/filter

**Concetti coperti:** comprehensions (list, dict, set), enumerate, zip, map, filter

---

# WEEK 2 (DAY 8-14): MORE FUNDAMENTALS

## Strings & Error Handling

### Esercizio 1.17 - String manipulation
- Methods: split, join, replace, strip, lower, upper
- f-strings: `f"Hello {name}"`
- Parsing: extract data from strings

### Esercizio 1.18 - Error handling
- try/except/finally
- Catching specific exceptions (ValueError, KeyError, etc)
- Raising exceptions
- When to catch, when to let fail

**Concetti coperti:** string methods, f-strings, try/except, exception types

---

## Generators & Iterators (IMPORTANTE)

### Esercizio 1.19 - Generators basics
```python
def big_range(n):
    for i in range(n):
        yield i  # Memory efficient
```
- `yield` vs `return`
- Generator expressions: `(x for x in range(1000))`
- When to use (large datasets)
- Interview question: list vs generator

**Concetti coperti:** yield, generators, memory efficiency, iterators

---

## Collections Module

### Esercizio 1.20 - defaultdict & Counter
```python
from collections import defaultdict, Counter

# defaultdict: avoid KeyError
d = defaultdict(list)
d['key'].append(value)  # No need to check if 'key' exists

# Counter: count occurrences
counts = Counter(words)
```
- When to use defaultdict
- Counter for frequency analysis
- **Molto usato in interviews!**

**Concetti coperti:** defaultdict, Counter, deque (quick mention)

---

## Moduli & Environment

### Esercizio 1.21 - Import & modules
- `import module`
- `from module import function`
- `import module as alias`
- Creating your own module (separate .py file)
- `if __name__ == "__main__":`

### Esercizio 1.22 - Virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
pip install requests
pip freeze > requirements.txt
```
- Why use venv
- requirements.txt
- Managing dependencies

**Concetti coperti:** import, modules, venv, pip, requirements.txt

---

# END OF WEEK 2 CHECKPOINT

**✅ Hai coperto:**
- Data types, structures (list, dict, set, tuple)
- Mutability & memory
- Functions (scope, *args, **kwargs, lambda, pure functions)
- Comprehensions
- Strings, error handling
- Generators (memory efficiency)
- Collections module
- Imports & venv

**📝 Self-assessment:** Fai 5 esercizi misti che combinano tutto. Se ok → next week.

---

# WEEK 3: FILES, JSON, API

## File I/O

### Esercizio 2.1 - Reading files
```python
# Old way (bad)
f = open('file.txt')
data = f.read()
f.close()

# Context manager (good)
with open('file.txt') as f:
    data = f.read()
```
- Why `with` is better (auto-close, exception-safe)
- read(), readline(), readlines()
- Encoding issues (utf-8)

### Esercizio 2.2 - Writing files
- write(), writelines()
- Modes: 'r', 'w', 'a', 'r+'
- Create file if not exists

### Esercizio 2.3 - CSV handling (manual)
- Parse CSV without pandas (to understand format)
- Write CSV
- Handle edge cases (commas in data, quotes)

**Concetti coperti:** file I/O, context managers (with), CSV format

---

## JSON

### Esercizio 2.4 - JSON read/write
```python
import json

# Load from file
with open('data.json') as f:
    data = json.load(f)

# Load from string
data = json.loads(string)

# Write to file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
```
- load vs loads
- dump vs dumps
- Nested JSON structures
- JSON validation

### Esercizio 2.5 - Config loader class
- Read config.json
- Validate required fields
- Provide defaults
- Raise error if invalid

**Concetti coperti:** JSON, validation, config management

---

## API Integration

### Esercizio 2.6 - HTTP basics
```python
import requests

response = requests.get('https://api.example.com/data')
print(response.status_code)  # 200, 404, 500, etc
print(response.json())
```
- GET vs POST
- Status codes (2xx, 4xx, 5xx)
- Headers
- Query params

### Esercizio 2.7 - Error handling APIs
- Timeout
- Connection errors
- Invalid JSON response
- Rate limiting (retry logic)

### Esercizio 2.8 - API with pagination
- Fetch multiple pages
- Combine results
- Stop when no more data

**Concetti coperti:** HTTP, requests library, error handling, pagination

---

## Environment Variables

### Esercizio 2.9 - Using .env files
```python
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
```
- Why not hardcode secrets
- .env file format
- .gitignore (.env should NOT be committed)

**Concetti coperti:** environment variables, secrets management

---

# 🎬 WEEK 4: PROJECT 1 — MOVIE DATA COLLECTOR

**Deadline:** Fine Week 4

## What to Build

CLI tool che fetcha dati TMDB e li salva localmente.

### Features (MVP)

**Commands:**
```bash
python movie_cli.py fetch trending
python movie_cli.py search "Inception"
python movie_cli.py details 27205
```

**Core functionality:**
1. Call TMDB API (trending, search, details)
2. Save responses in JSON files (`data/trending.json`, `data/movies/{id}.json`)
3. Cache: if data < 24h old, don't re-fetch
4. Pretty print results in terminal
5. Error handling (API down, invalid ID, rate limit)

### Tech Stack
- `requests` for API
- `json` for storage
- `argparse` for CLI
- `dotenv` for API key
- Basic logging

### File Structure
```
movie-data-collector/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── movie_cli.py (main script)
├── api_client.py (TMDB API wrapper)
├── cache.py (cache logic)
└── data/ (gitignored, local storage)
```

### Deliverables
✅ Working CLI (3 commands)
✅ Cache working (avoid redundant API calls)
✅ Error handling
✅ README with setup instructions
✅ Push to GitHub

### Skills Applied
- API integration
- File I/O (JSON)
- Error handling
- CLI with argparse
- Environment variables
- Code organization (multiple files)

---

# WEEK 5: PANDAS & VISUALIZATION

## Pandas Fundamentals

### Esercizio 3.1 - DataFrames & Series
```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})

# Load CSV
df = pd.read_csv('data.csv')

# Inspect
df.head()
df.info()
df.describe()
```

### Esercizio 3.2 - Selection & Filtering
- `df['column']` vs `df.column`
- `df.loc[row, col]` (label-based)
- `df.iloc[row, col]` (position-based)
- Boolean indexing: `df[df['age'] > 25]`
- Multiple conditions: `df[(df['age'] > 25) & (df['city'] == 'NYC')]`

### Esercizio 3.3 - Data cleaning
- Missing values: `df.isnull()`, `df.dropna()`, `df.fillna()`
- Duplicates: `df.duplicated()`, `df.drop_duplicates()`
- Data types: `df.astype()`, `pd.to_datetime()`

### Esercizio 3.4 - Transformations
- New columns: `df['new'] = df['a'] + df['b']`
- apply(): `df['col'].apply(lambda x: x*2)`
- map(): `df['col'].map({'a': 1, 'b': 2})`
- String methods: `df['name'].str.lower()`

### Esercizio 3.5 - Groupby & aggregations
```python
df.groupby('category')['sales'].sum()
df.groupby('category').agg({'sales': 'sum', 'quantity': 'mean'})
df.groupby(['region', 'category'])['sales'].sum()
```

### Esercizio 3.6 - Merge & join
```python
pd.merge(df1, df2, on='id')  # inner join
pd.merge(df1, df2, on='id', how='left')  # left join
pd.concat([df1, df2])  # vertical stack
```

### Esercizio 3.7 - Useful methods
- `value_counts()`: frequency
- `sort_values()`: sort by column
- `reset_index()`: fix index after operations
- `pivot_table()`: reshape data

**Concetti coperti:** DataFrame, Series, selection, cleaning, groupby, merge

---

## Visualization

### Esercizio 3.8 - Matplotlib basics
```python
import matplotlib.pyplot as plt

plt.plot(x, y)  # line
plt.bar(categories, values)  # bar
plt.scatter(x, y)  # scatter
plt.savefig('plot.png')
```
- Line, bar, scatter plots
- Labels, titles, legend
- Subplots
- Save to file

---

# 🎬 WEEK 5-6: PROJECT 2 — MOVIE ANALYTICS DASHBOARD

**Deadline:** Fine Week 6

## What to Build

Script Python che analizza dati film e genera report con grafici.

### Data Source
Use data saved from PROJECT 1 OR download public TMDB dataset (5000 movies CSV available online).

### Analysis Required

**1. Top films**
- Top 20 by rating
- Top 20 by revenue
- Top 20 by popularity

**2. Genre trends**
- Movies per genre over years (line chart)
- Revenue by genre (bar chart)

**3. Budget vs Revenue**
- Scatter plot
- Correlation coefficient

**4. Release patterns**
- Which months have most releases? (bar chart)
- Best months for blockbusters?

**5. Basic statistics**
- Average runtime
- Average budget/revenue
- Most common genres

### Deliverables
✅ Python script or Jupyter notebook
✅ 5-6 charts saved as PNG
✅ Report in markdown format with insights
✅ Clean, commented code
✅ README with findings
✅ Push to GitHub

### Skills Applied
- Pandas (load, clean, groupby, merge)
- Data cleaning (missing values, types)
- Aggregations
- Matplotlib (multiple chart types)
- Statistical analysis

---

# WEEK 6-7: OOP & BACKEND PREP

## OOP Basics (focused)

### Esercizio 4.1 - Classes & objects (già fatto Ex 7!)
- `__init__`
- `self`
- Instance attributes
- Methods

### Esercizio 4.2 - Class vs instance attributes (già fatto Ex 8!)
- Shared vs unique data
- `@classmethod`
- `@staticmethod`

### Esercizio 4.3 - Properties (già fatto Ex 9!)
- `@property`
- `@attribute.setter`
- Validation in setters

### Esercizio 4.4 - Magic methods (important)
```python
class Movie:
    def __str__(self):
        return f"{self.title} ({self.year})"
    
    def __repr__(self):
        return f"Movie('{self.title}', {self.year})"
    
    def __eq__(self, other):
        return self.id == other.id
```
- `__str__` (user-friendly)
- `__repr__` (dev-friendly)
- `__eq__` (equality)

### Esercizio 4.4b - Inheritance & ABC ⚡ NEW (2h)

**Perché:** chiesto regolarmente in colloquio ("design these classes...", "what's an ABC?"). Con 2 ore lo copri al livello richiesto per Mid.

**Inheritance basics**
```python
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def info(self):
        return f"{self.title} ({self.year})"

class Documentary(Movie):
    def __init__(self, title, year, topic):
        super().__init__(title, year)  # chiama il parent
        self.topic = topic

    def info(self):  # override
        return f"{super().info()} — Topic: {self.topic}"
```
- `super()` per chiamare il parent
- Method override
- `isinstance()` e `issubclass()`

**Abstract Base Classes (ABC)**
```python
from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def fetch(self, query: str) -> list:
        pass

class TMDBSource(DataSource):
    def fetch(self, query: str) -> list:
        return [...]

class LocalCSVSource(DataSource):
    def fetch(self, query: str) -> list:
        return [...]

# Non puoi istanziare DataSource() — è astratta
```
**Concetto chiave:** ABC = "contratto" che le sottoclassi *devono* rispettare. Cardine di design pulito.

**Composition vs Inheritance** (da saper spiegare in interview)
- *"Favor composition over inheritance"* — perché?
- Inheritance: relazione "è un"
- Composition: relazione "ha un"

**Esercizio pratico:** riprogetta il client di Project 1 usando:
- `DataSource` (ABC) con metodo astratto `fetch()`
- `TMDBSource(DataSource)` per l'API
- `CachedSource(DataSource)` che wrappa un'altra source con cache (composition!)
- Polimorfismo: `for source in sources: source.fetch(...)`

📚 **Risorse:**
- [Real Python — Inheritance and Composition](https://realpython.com/inheritance-composition-python/) ⭐
- [Python docs — abc module](https://docs.python.org/3/library/abc.html)
- [ArjanCodes — Composition over Inheritance (YouTube, 12 min)](https://www.youtube.com/watch?v=0mcP8ZpUR38) ⭐

**Skip per ora:** metaclasses, descriptors, multiple inheritance avanzata (non urgenti)

---

## Type Hints (modern Python)

### Esercizio 4.5 - Type hints basics
```python
def process_data(items: list[dict], limit: int = 10) -> dict:
    result: dict[str, int] = {}
    for item in items[:limit]:
        result[item['name']] = item['value']
    return result
```
- Function parameters
- Return types
- Variable annotations
- Optional types: `Optional[str]`
- Union types: `str | int`

**Why:** Better IDEs, catch errors early, self-documenting code

---

## Logging (sostituisci print)

### Esercizio 4.6 - Logging setup
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info("Processing started")
logger.warning("Cache miss")
logger.error("API failed")
```
- Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Log to file + console
- When to use each level

---

# WEEK 7-8: FASTAPI & DATABASE

## SQL grezzo (FAI PRIMA DI SQLALCHEMY) ⚡ NEW (3-4h)

**Perché farlo PRIMA dell'ORM:** in colloquio chiedono SQL puro **molto più spesso** di SQLAlchemy. Se sai solo l'ORM sei tagliato fuori. Anche per ruoli AI i dati ci sono sempre.

### Esercizio 5.0a - SELECT, WHERE, ORDER BY, LIMIT
```sql
SELECT title, year, rating
FROM movies
WHERE year >= 2010 AND rating > 7.5
ORDER BY rating DESC
LIMIT 10;
```

### Esercizio 5.0b - JOINs (CRITICO in interview)
```sql
-- INNER JOIN
SELECT m.title, a.name
FROM movies m
INNER JOIN movie_actors ma ON m.id = ma.movie_id
INNER JOIN actors a ON a.id = ma.actor_id
WHERE m.year = 2020;

-- LEFT JOIN (film senza recensioni)
SELECT m.title, COUNT(r.id) as review_count
FROM movies m
LEFT JOIN reviews r ON r.movie_id = m.id
GROUP BY m.id
HAVING review_count = 0;
```

### Esercizio 5.0c - GROUP BY + HAVING + aggregations
```sql
SELECT genre, AVG(rating) as avg_rating, COUNT(*) as film_count
FROM movies
GROUP BY genre
HAVING COUNT(*) > 10
ORDER BY avg_rating DESC;
```

### Esercizio 5.0d - Subqueries & CTE
```sql
-- CTE (più leggibile)
WITH high_rated AS (
  SELECT * FROM movies WHERE rating > 8
)
SELECT genre, COUNT(*) FROM high_rated GROUP BY genre;

-- Subquery
SELECT * FROM movies
WHERE rating > (SELECT AVG(rating) FROM movies);
```

### Esercizio 5.0e - Window functions (livello mid)
```sql
SELECT
  title, year, rating,
  RANK() OVER (PARTITION BY genre ORDER BY rating DESC) as rank_in_genre
FROM movies;
```

### Esercizio 5.0f - Indexing basics
- Quando creare un index (`CREATE INDEX idx_year ON movies(year);`)
- `EXPLAIN QUERY PLAN` per capire le performance

**Esercizio finale:** carica i film di Project 1 in SQLite (`sqlite3 movies.db`) e rispondi (solo SQL) a:
1. Top 10 film per rating dopo il 2015
2. Numero di film per genere
3. Genere con rating medio più alto (con almeno 20 film)
4. Film con rating sopra la media globale
5. Top 3 film per genere (window function)

📚 **Risorse:**
- ⭐ [SQLBolt — interactive lessons (GRATIS)](https://sqlbolt.com/) — 15 lessons, 2-3 ore totali
- [SQL Murder Mystery](https://mystery.knightlab.com/) (gratis, gioco)
- [Mode SQL Tutorial](https://mode.com/sql-tutorial/) ⭐
- [Use the Index, Luke!](https://use-the-index-luke.com/) (per indexing)
- Per practice colloqui: [DataLemur](https://datalemur.com/) e [LeetCode SQL](https://leetcode.com/problemset/database/)

**Deliverable:** file `queries.sql` con 10+ query commentate, da committare in Project 3.

---

## FastAPI Fundamentals

### Esercizio 5.1 - Hello API
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
- Run: `uvicorn main:app --reload`
- Auto docs: http://localhost:8000/docs
- Path parameters
- Query parameters

### Esercizio 5.2 - Request body with Pydantic
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "price": item.price}
```
- Pydantic for validation
- Automatic JSON parsing
- Error handling (422 if invalid)

### Esercizio 5.3 - Response models
```python
class ItemResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

@app.get("/items/{id}", response_model=ItemResponse)
def get_item(id: int):
    # ... fetch from DB
    return ItemResponse(id=id, name="Item", created_at=datetime.now())
```

### Esercizio 5.4 - Error handling
```python
from fastapi import HTTPException

@app.get("/items/{id}")
def get_item(id: int):
    item = db.get(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```

---

## Database with SQLAlchemy

### Esercizio 5.5 - SQLAlchemy models
```python
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer)
    rating = Column(Float)
```

### Esercizio 5.6 - CRUD operations
```python
# Create
movie = Movie(title="Inception", year=2010, rating=8.8)
session.add(movie)
session.commit()

# Read
movies = session.query(Movie).filter(Movie.year > 2000).all()

# Update
movie = session.query(Movie).filter(Movie.id == 1).first()
movie.rating = 9.0
session.commit()

# Delete
session.query(Movie).filter(Movie.id == 1).delete()
session.commit()
```

### Esercizio 5.7 - Relations
```python
class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MovieActor(Base):
    __tablename__ = "movie_actors"
    movie_id = Column(Integer, ForeignKey('movies.id'))
    actor_id = Column(Integer, ForeignKey('actors.id'))
```

**Concetti coperti:** ORM, models, CRUD, relationships, sessions

---

## Testing with pytest

### Esercizio 5.8 - Unit tests
```python
def test_sum():
    assert sum([1, 2, 3]) == 6

def test_filter_movies():
    movies = [{'rating': 8.0}, {'rating': 6.0}]
    result = filter_high_rated(movies, threshold=7.0)
    assert len(result) == 1
```

### Esercizio 5.9 - Testing FastAPI
```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
```

**Concetti coperti:** pytest, assertions, TestClient, mocking basics

---

# 🎬 WEEK 7-8: PROJECT 3 — MOVIE RECOMMENDATION API (MVP)

**Deadline:** Fine Week 8

## What to Build

FastAPI che raccomanda film usando TMDB + LLM.

### Core Endpoints (MVP)

**1. GET /movies**
- List movies from DB
- Query params: `genre`, `year_min`, `year_max`, `sort_by`, `limit`
- Returns: list of movies

**2. GET /movies/{id}**
- Movie details
- Returns: movie + cast (if available)

**3. POST /recommend**
Request:
```json
{
  "liked_movie": "Inception",
  "mood": "mind-bending"
}
```
Logic:
1. Search movie in TMDB
2. Get similar movies (TMDB API has `/similar` endpoint)
3. Call LLM: "Why does user like Inception? Rank these similar movies."
4. Return top 5 with explanations

Response:
```json
{
  "recommendations": [
    {
      "title": "Interstellar",
      "year": 2014,
      "reason": "Similar director (Nolan), complex narrative, sci-fi themes",
      "rating": 8.6
    }
  ]
}
```

**4. GET /history**
- List past recommendations (from DB)

### Tech Stack (MVP)

**Backend:**
- FastAPI (sync, no async for simplicity)
- SQLite (not PostgreSQL)
- SQLAlchemy ORM
- Pydantic models

**External APIs:**
- TMDB API (movie data)
- OpenAI/Anthropic API (LLM recommendations)

**No Docker, no Redis, no JWT auth** (hardcoded API key ok for MVP)

### Database Schema

```python
# models.py
class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    tmdb_id = Column(Integer, unique=True)
    title = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    overview = Column(String)

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True)
    input_movie = Column(String)
    recommended_movies = Column(String)  # JSON string
    created_at = Column(DateTime)
```

### File Structure
```
movie-recommendation-api/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── main.py (FastAPI app)
├── models.py (SQLAlchemy models)
├── schemas.py (Pydantic models)
├── database.py (DB connection)
├── tmdb_client.py (TMDB API wrapper)
├── llm_client.py (LLM API wrapper)
├── tests/
│   ├── test_api.py
│   └── test_recommendations.py
└── movies.db (SQLite, gitignored)
```

### Deliverables

✅ Working API (4 endpoints)
✅ Database with movies
✅ LLM integration (recommendations)
✅ 5-6 pytest tests (critical paths)
✅ Swagger docs (auto-generated)
✅ README with:
  - Setup instructions
  - API examples (curl)
  - Architecture explanation
✅ Push to GitHub
✅ **BONUS:** Deploy to Render/Railway (free tier)
✅ **BONUS:** Dockerize (vedi sezione sotto ⬇️)

### Skills Applied
- FastAPI (routing, Pydantic, error handling)
- Database (SQLAlchemy ORM, CRUD)
- API integration (TMDB + LLM)
- Environment variables
- Testing (pytest)
- Type hints
- Logging
- Documentation

---

## Docker basics (stretch goal Week 8) ⚡ NEW (2-3h)

**Perché:** un `Dockerfile` di 15 righe sul Project 3 alza moltissimo la percezione del CV. È *quasi gratis* in termini di tempo.

### Esercizio Docker.1 - Dockerfile minimal per FastAPI
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Esercizio Docker.2 - Build & run
```bash
docker build -t movie-api .
docker run -p 8000:8000 --env-file .env movie-api
```

### Esercizio Docker.3 - docker-compose (multi-service)
```yaml
services:
  api:
    build: .
    ports: ["8000:8000"]
    env_file: .env
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: dev
```

**Concetti chiave da saper spiegare in interview:**
- Image vs container
- Layer caching (perché copiare `requirements.txt` *prima* del codice)
- `.dockerignore` (importantissimo)
- Multi-stage builds (cenno)

**Deliverable:** Project 3 con `Dockerfile` + `.dockerignore` + sezione "Run with Docker" nel README.

📚 **Risorse:**
- [Docker for Beginners (gratis, ufficiale)](https://docker-curriculum.com/) ⭐
- [FastAPI in Containers — guida ufficiale](https://fastapi.tiangolo.com/deployment/docker/)
- [Play with Docker (browser)](https://labs.play-with-docker.com/) — prova senza installare niente
- [Docker Cheat Sheet (PDF)](https://docs.docker.com/get-started/docker_cheatsheet.pdf)

---

# WEEK 8: POLISH & DEPLOY

## Final Week Tasks

### Day 1-2: Testing & Documentation
- Add tests to Project 3 (aim for 5-6 critical tests)
- Write comprehensive READMEs for all 3 projects
- Add docstrings to functions
- Type hints everywhere

### Day 3-4: Deploy
- Deploy Project 3 to Render or Railway (free tier)
- Test live API
- Update README with live URL

### Day 5: Portfolio
- GitHub profile README showcasing 3 projects
- LinkedIn post about projects
- Prepare 2-minute demo video (Loom)

### Day 6-7: Interview Prep
- Review all concepts covered
- Practice explaining projects
- Prepare answers for common Python questions

---

# TOPICS COVERED (COMPLETE LIST)

## ✅ Core Python
- Data types (int, float, str, bool, None)
- Data structures (list, dict, set, tuple)
- Control flow (if/else, for, while, break, continue)
- Functions (scope, *args, **kwargs, lambda, pure functions)
- Comprehensions (list, dict, set)
- Mutability & memory (reference, copy, shallow/deep)
- Strings (methods, f-strings)
- Error handling (try/except, exceptions)
- Generators (yield, memory efficiency)
- Collections (defaultdict, Counter)
- Imports & modules
- Virtual environments

## ✅ Files & APIs
- File I/O (context managers)
- JSON (load/dump)
- CSV (manual parsing)
- HTTP (requests library)
- API integration (GET, POST, params, headers)
- Error handling (timeouts, status codes)
- Environment variables (.env)

## ✅ Pandas & Visualization
- DataFrames & Series
- Selection (loc, iloc, boolean indexing)
- Data cleaning (missing values, duplicates, types)
- Transformations (apply, map, new columns)
- Groupby & aggregations
- Merge & join
- Matplotlib (line, bar, scatter plots)

## ✅ OOP
- Classes & objects (__init__, self)
- Instance vs class attributes
- Methods (instance, class, static)
- Properties (@property, setter)
- Magic methods (__str__, __repr__, __eq__)

## ✅ Backend & Database
- FastAPI (routing, request/response)
- Pydantic (validation, models)
- SQLAlchemy ORM (models, CRUD, relationships)
- SQLite (database basics)
- Error handling (HTTP exceptions)
- Swagger docs (auto-generated)

## ✅ Advanced Topics
- Type hints (functions, variables)
- Logging (levels, handlers)
- Testing (pytest, assertions, TestClient)
- LLM API integration
- Deployment basics

## ✅ Tools & Workflow
- Git & GitHub
- Virtual environments (venv, requirements.txt)
- .env files (secrets management)
- CLI tools (argparse)
- Project structure
- README writing
- Documentation

---

# WHAT'S NOT COVERED (Learn On-The-Job)

These are valuable but not essential for first job:

❌ Docker & containers
❌ Redis & caching systems
❌ JWT & advanced auth
❌ PostgreSQL (SQLite is enough to start)
❌ Async/await advanced patterns
❌ CI/CD pipelines
❌ Microservices architecture
❌ Advanced OOP (inheritance, abstract classes, metaclasses)
❌ NumPy (not needed for backend/API work)
❌ Advanced testing (mocking, fixtures, 80%+ coverage)
❌ Decorators (custom, beyond @property)
❌ Context managers (custom __enter__/__exit__)
❌ Descriptors, metaclasses

**You'll learn these when you need them at work.**

---

# FINAL DELIVERABLES (Portfolio)

## 3 GitHub Repositories

**1. movie-data-collector** 🎬
- CLI tool
- TMDB API integration
- Caching
- ~300-400 LOC

**2. movie-analytics-dashboard** 🎬
- Pandas analysis
- 5-6 charts
- Report with insights
- ~200-300 LOC

**3. movie-recommendation-api** 🎬🤖
- FastAPI backend
- Database (SQLite)
- LLM integration
- Tests
- Deployed live
- ~500-700 LOC

## Supporting Materials
- Professional READMEs (setup, usage, architecture)
- Demo video (2 min)
- GitHub profile README
- LinkedIn post

---

# SUCCESS CRITERIA

At the end of 8 weeks, you can:

✅ **Explain every fundamental Python concept** (data structures, functions, OOP, etc)
✅ **Build a REST API** from scratch (FastAPI + database)
✅ **Integrate external APIs** (TMDB, LLM)
✅ **Clean and analyze data** (Pandas)
✅ **Write tests** (pytest basics)
✅ **Deploy an application** (live API)
✅ **Show 3 portfolio projects** that demonstrate real skills
✅ **Talk confidently** about your projects in interviews

**You're ready for:** Junior Python Developer (Backend/Data/AI)

---

# HOW TO USE THIS ROADMAP

## Daily Routine (2-3 hours/day)

**Weeks 1-2 (Fundamentals):**
- Do 2-3 exercises per day
- Focus on understanding, not speed
- Ask for hints if stuck >30min

**Week 3 (Files/API/JSON):**
- 1-2 exercises per day
- Start thinking about Project 1

**Week 4 (Project 1):**
- Build Movie Data Collector
- 2-3 hours/day coding
- Push to GitHub end of week

**Week 5-6 (Pandas + Project 2):**
- Learn Pandas (exercises)
- Build Movie Analytics Dashboard
- Generate report + charts

**Week 7-8 (Backend + Project 3):**
- Learn FastAPI/DB (exercises)
- Build Movie Recommendation API
- Test, document, deploy

## When You're Stuck

1. Try for 20-30 minutes yourself
2. Ask for a hint (not full solution)
3. If still stuck, ask for explanation
4. Move on if it's taking >1 hour (comeback later)

## Quality > Speed

- Don't rush through exercises
- Make sure you understand WHY, not just HOW
- 3 solid projects > 10 mediocre projects
- Better to spend 9 weeks doing it right than 8 weeks doing it rushed

---

# NEXT STEPS AFTER THIS ROADMAP

Once you complete this (8-9 weeks), you can:

**Option A: Start applying for jobs**
- You have enough for Junior roles
- Learn the rest on the job

**Option B: Add 1-2 more skills** (2-3 weeks each):
- Docker basics (containerization)
- PostgreSQL (production DB)
- JWT auth (authentication)
- React basics (if you want frontend too)
- AWS basics (S3, Lambda, EC2)

**Option C: Build 1 more advanced project** (3-4 weeks):
- Add the "nice-to-haves" to Project 3 (Docker, Redis, CI/CD)
- This becomes your "wow" project

**My recommendation:** Option A. Get a job, learn the rest while getting paid.

---

# READY TO START?

You're currently on **Exercise 9 (Properties)** in the OOP section.

**Two paths forward:**

**Path 1:** Finish current OOP track (Exercise 9-15)
- Pros: Complete what you started
- Cons: Some concepts (abstract classes, etc) not urgent

**Path 2:** Switch to this MVP roadmap now
- Pros: More focused, realistic timeline
- Cons: "Wasted" the OOP exercises so far (not really wasted, you learned!)

**My recommendation:** Switch to MVP roadmap. You've already done Exercises 7-9 which cover the essential OOP (classes, class vs instance, properties). The rest (inheritance, abstract classes) you can learn later when needed.

**Next step:** Start with **Week 1, Day 1: Data Types & Control Flow** → fresh start, solid foundation.

What do you think?

---
---

# 🚀 PHASE 2 — APPLIED AI ENGINEER TRACK
## 8-10 settimane dopo Phase 1 — da "Junior Python Developer" a "Applied AI Engineer Mid"

🎯 **OBIETTIVO:** Diventare credibile come **AI Engineer / Applied AI Engineer** capace di costruire sistemi RAG, agentic workflows, e backend AI di produzione.

📌 **PRE-REQUISITO:** Completata Phase 1 (Python fundamentals + FastAPI + SQLAlchemy + 3 progetti)

📌 **TARGET RUOLI:**
- Applied AI Engineer / AI Engineer
- Backend Engineer (AI-focused)
- Forward Deployed Engineer (in aziende AI)
- ML Engineer (lato applicato, no training di modelli)

📌 **STIPENDI ATTESI EU (Mid):** 65-110k € · Senior 100-180k €

---

## STRUCTURE PHASE 2

| Settimana | Focus | Output |
|---|---|---|
| **Week 9** | Async Python + Modern FastAPI (production-grade) | Refactor Project 3 con async + tests robusti |
| **Week 10** | LLM APIs deep dive — OpenAI, Claude, structured outputs, streaming | Mini-progetto "AI tagger" |
| **Week 11-12** | 🤖 **PROJECT 4** — RAG Movie Assistant (vector DB + retrieval + eval) | App RAG completa + deploy |
| **Week 13** | LangGraph & Agentic systems | Mini-agent multi-tool |
| **Week 14-15** | 🤖 **PROJECT 5** — Agentic Movie Companion (LangGraph + MCP + tool use) | Agent system completo |
| **Week 16** | Production AI: observability, eval, costs, caching, security | Refactor Project 5 con LangSmith + cost tracking |
| **Week 17 (opz.)** | Docker + deploy serio + GitHub Actions CI | Tutti i progetti dockerizzati |

---

# WEEK 9 — ASYNC PYTHON & PRODUCTION FASTAPI

**Perché:** Quasi ogni interview AI/Backend chiede `async def`. FastAPI brilla in async. RAG/agent fanno molte chiamate I/O bound = async essenziale.

## Esercizio 9.1 - Async basics
```python
import asyncio

async def fetch_data(url):
    await asyncio.sleep(1)  # simula I/O
    return f"data from {url}"

async def main():
    results = await asyncio.gather(
        fetch_data("api1"),
        fetch_data("api2"),
        fetch_data("api3"),
    )
    print(results)

asyncio.run(main())
```
- `async def`, `await`, event loop
- `asyncio.gather` (parallel) vs sequential
- **Concetto chiave:** I/O-bound = async; CPU-bound = multiprocessing

📚 **Risorse:**
- [Real Python — Async IO in Python](https://realpython.com/async-io-python/) (il miglior tutorial in assoluto)
- [FastAPI docs — Concurrency](https://fastapi.tiangolo.com/async/) (spiega *quando* usare async)

## Esercizio 9.2 - httpx (la versione async di requests)
```python
import httpx

async with httpx.AsyncClient() as client:
    response = await client.get("https://api.example.com")
    data = response.json()
```
- Sostituire `requests` con `httpx` per chiamate concorrenti
- Timeout, retry, connection pooling

📚 **Risorse:**
- [httpx docs](https://www.python-httpx.org/async/)

## Esercizio 9.3 - FastAPI async endpoints
- Refactor di Project 3: tutti gli endpoint diventano `async def`
- Multiple chiamate API in parallelo con `asyncio.gather`
- Background tasks (`BackgroundTasks`)
- Dependency injection (`Depends`)

📚 **Risorse:**
- [FastAPI tutorial completo (gratis)](https://fastapi.tiangolo.com/tutorial/) — leggi *Advanced* dopo Tutorial
- [TestDriven.io — Async FastAPI](https://testdriven.io/blog/fastapi-crud/) (paywall ma alcuni gratis)

## Esercizio 9.4 - Pytest avanzato + async testing
- `pytest-asyncio`
- Fixtures (`@pytest.fixture`)
- Mocking con `unittest.mock` e `pytest-mock`
- Coverage con `pytest-cov` (puntare ≥70%)

📚 **Risorse:**
- [pytest docs](https://docs.pytest.org/en/stable/)
- [Real Python — Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)

**Deliverable Week 9:** Project 3 refactored → async, ≥70% test coverage, deploy ancora funzionante.

---

# WEEK 10 — LLM APIs DEEP DIVE

**Perché:** Saper chiamare un LLM è il "Hello World" dell'AI Engineering. Devi padroneggiare structured outputs, streaming, function calling, costi.

## Esercizio 10.1 - OpenAI & Anthropic SDK basics
```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello"}],
)
```
- System / user / assistant messages
- `temperature`, `max_tokens`, `top_p`
- Differenze OpenAI vs Anthropic SDK
- Stessa cosa in Anthropic:
```python
from anthropic import Anthropic
client = Anthropic()
msg = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
```

📚 **Risorse:**
- [OpenAI Cookbook](https://cookbook.openai.com/) — esempi pratici di tutto
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [OpenAI API docs](https://platform.openai.com/docs/api-reference)

## Esercizio 10.2 - Structured outputs (CRITICO)
Mai più "parse del testo" — fai output strutturati con Pydantic:
```python
from pydantic import BaseModel

class MovieReview(BaseModel):
    title: str
    rating: int
    sentiment: str
    keywords: list[str]

response = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[...],
    response_format=MovieReview,
)
review: MovieReview = response.choices[0].message.parsed
```
- OpenAI: `response_format=PydanticModel` (structured outputs)
- Anthropic: tool use con JSON schema
- **Use case:** estrazione dati, classificazione, parsing di documenti

📚 **Risorse:**
- [OpenAI Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs)
- [Instructor library](https://python.useinstructor.com/) (libreria che astrae structured outputs su tutti i provider — molto popolare)

## Esercizio 10.3 - Streaming
```python
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```
- Streaming per UX migliore (chat in tempo reale)
- Server-Sent Events (SSE) in FastAPI per stream verso il front-end

📚 **Risorse:**
- [FastAPI streaming guide](https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse)

## Esercizio 10.4 - Function / Tool calling
```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_movie_rating",
        "parameters": {...}
    }
}]
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    tools=tools,
)
```
- Definire tool con JSON schema
- Loop: model → tool call → execute → return result → model
- **Concetto fondante** per agenti

📚 **Risorse:**
- [OpenAI Function Calling guide](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Tool Use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)

## Esercizio 10.5 - Prompt engineering pratico
- System prompts efficaci
- Few-shot examples
- Chain-of-thought
- Output formatting (JSON, markdown, XML tags per Claude)
- **Anti-patterns:** istruzioni vaghe, prompt monolitici

📚 **Risorse:**
- [Anthropic Prompt Engineering Course (gratis)](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial) — ⭐ il migliore in circolazione
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Prompting Guide (community)](https://www.promptingguide.ai/)

## Mini-progetto Week 10: "AI Movie Tagger"
Script che prende una recensione di film, e tramite LLM con structured output ritorna:
```python
class MovieTag(BaseModel):
    sentiment: Literal["positive", "negative", "mixed"]
    themes: list[str]
    target_audience: str
    spoiler_warning: bool
```
+ batch processing di 100 recensioni in async + cost tracking.

**Deliverable Week 10:** repo con il tagger, README con esempi, batch async funzionante.

---

# WEEK 11-12 — 🤖 PROJECT 4: RAG MOVIE ASSISTANT

**Il progetto che ti rende credibile come AI Engineer.** Tutto quello che impari qui è quello che chiedono nei colloqui.

## Cosa costruisci

API + interfaccia minimale che permette di chiedere in linguaggio naturale:
> *"Suggeriscimi 3 film simili a Inception ma più leggeri e brevi"*
> *"Quali sono i film thriller del 2010-2015 con rating > 8?"*
> *"Trova film dove un protagonista perde la memoria"*

Il sistema retrieva da un vector DB (recensioni + metadata di 5000 film) + risponde con citazioni.

## Stack

| Componente | Tool consigliato | Alternativa |
|---|---|---|
| Vector DB | **Chroma** (locale, semplice) | pgvector (Postgres), Qdrant, Weaviate |
| Embeddings | OpenAI `text-embedding-3-small` | open-source: `sentence-transformers/all-MiniLM-L6-v2` |
| LLM | Claude Sonnet o GPT-4o-mini | Llama 3.1 via Groq (gratis fast) |
| Framework | **LlamaIndex** o **LangChain** | scrivere a mano (educativo ma più lento) |
| Backend | FastAPI (già sai) | — |
| Front-end demo | Streamlit | Gradio, Next.js |
| Eval | RAGAS | manuale |
| Deploy | Render / Railway / Fly.io | — |

📚 **Risorse fondamentali:**
- [LlamaIndex docs — RAG starter](https://docs.llamaindex.ai/en/stable/getting_started/starter_example/) ⭐
- [LangChain RAG tutorial](https://python.langchain.com/docs/tutorials/rag/) ⭐
- [Chroma docs](https://docs.trychroma.com/)
- [Pinecone Learning Center — Retrieval Augmented Generation](https://www.pinecone.io/learn/retrieval-augmented-generation/) (concetti)
- [Anthropic guide — Building effective RAG](https://www.anthropic.com/news/contextual-retrieval) (tecniche avanzate)

## Step by step

### Step 1: Ingestion pipeline
- Carica 5000 film TMDB (riusa Project 1)
- Per ogni film crea documento: `f"{title} ({year}) - {overview} - Genre: {genre} - Cast: {cast}"`
- Chunk strategy: 1 documento per film (non serve splittare, sono brevi)
- Embedding + salvataggio in Chroma

📚 **Concetti da padroneggiare:**
- Chunking strategies (fixed-size, semantic, recursive)
- Embedding models (dimensione, costo, qualità)
- Metadata filtering

### Step 2: Retrieval
- Naive retrieval: top-k similarity search
- Hybrid retrieval: similarity + keyword (BM25)
- Metadata filtering (es. `year >= 2010`)
- Reranking con Cohere Rerank o cross-encoder

📚 **Risorse avanzate:**
- [Hybrid search con Chroma](https://docs.trychroma.com/guides/hybrid-search)
- [Cohere Rerank](https://docs.cohere.com/docs/rerank-overview)

### Step 3: Generation
- Prompt template con context retrieved + query
- Citazioni nelle risposte (es. `"... [Inception (2010), Interstellar (2014)]"`)
- Streaming response via FastAPI

### Step 4: API endpoints
```python
POST /ask          # query naturale → risposta + citazioni
POST /ingest       # caricare nuovi film nel DB
GET  /movies/{id}  # ritorna film + similarity-based "similar to"
```

### Step 5: Evaluation (CRITICO — la parte che pochi fanno)
Crea un **eval set** di 20 query con expected behavior, e misura:
- **Retrieval quality**: i film "giusti" sono nei top-k?
- **Faithfulness**: la risposta cita davvero i documenti retrieved?
- **Answer relevance**: la risposta risponde alla domanda?

Usa [RAGAS](https://docs.ragas.io/) per le metriche automatiche.

📚 **Risorse eval:**
- [RAGAS docs](https://docs.ragas.io/en/latest/)
- [Anthropic — Building evals](https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests)

### Step 6: Front-end demo
- Streamlit app super minimale (50 righe)
- Input testo → output risposta con citazioni cliccabili

### Step 7: Deploy
- Backend su Render/Railway (free tier)
- Front-end Streamlit su Streamlit Community Cloud (gratis)
- Vector DB embedded nel backend (Chroma persistente su disco)

### Deliverable finale Project 4
✅ Repo GitHub con README serio (architettura, scelte, eval results)
✅ Demo live raggiungibile
✅ Post LinkedIn / Twitter sul progetto
✅ Eval report con numeri (es. "Faithfulness: 87%, MRR@5: 0.72")
✅ ~600-1000 LOC

**Costo totale:** ~10-25€ in API credits.
**Cosa hai dimostrato:** sai fare RAG end-to-end, valutarlo, deployarlo. Sei sopra l'80% dei candidati che dicono "so fare RAG".

---

# WEEK 13 — LANGGRAPH & AGENTIC SYSTEMS

**Perché:** Gli agenti sono il next big thing. LangGraph è lo standard de-facto per orchestrare agenti multi-step in produzione (usato da Replit, Uber, LinkedIn, ecc.).

## Esercizio 13.1 - Concetti agentici
- ReAct pattern (Reason + Act)
- Tool use loop (LLM → tool → result → LLM → ...)
- Stato condiviso vs stateless
- Quando agente vs workflow deterministico

📚 **Risorse concettuali:**
- [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) ⭐ **leggi prima di tutto**
- [Lilian Weng — LLM-powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) (il post di riferimento)

## Esercizio 13.2 - LangGraph basics
```python
from langgraph.graph import StateGraph, END

class State(TypedDict):
    messages: list
    next_action: str

graph = StateGraph(State)
graph.add_node("plan", plan_node)
graph.add_node("execute", execute_node)
graph.add_edge("plan", "execute")
graph.add_conditional_edges("execute", should_continue, {True: "plan", False: END})
```
- Nodes (funzioni)
- Edges (transizioni)
- Conditional edges (routing dinamico)
- State management

📚 **Risorse LangGraph:**
- [LangGraph Quickstart](https://langchain-ai.github.io/langgraph/) ⭐
- [LangGraph tutorials (gratis)](https://langchain-ai.github.io/langgraph/tutorials/) — fai ALMENO il "Customer Support" e l'"Agentic RAG"
- [LangChain Academy — Intro to LangGraph (gratis)](https://academy.langchain.com/courses/intro-to-langgraph) ⭐⭐ corso completo gratuito

## Esercizio 13.3 - Multi-tool agent
Costruisci un agente con 3 tool:
- `search_movies(query: str)` → cerca su TMDB
- `get_movie_details(id: int)` → dettagli
- `compare_movies(id1, id2)` → confronto

L'agente decide autonomamente quali tool chiamare in base alla query utente.

## Esercizio 13.4 - Memory & persistence
- Short-term memory (conversation history)
- Long-term memory (vector store di interazioni passate)
- Checkpointing (LangGraph `MemorySaver`, `SqliteSaver`)

📚 **Risorse memory:**
- [LangGraph Memory concepts](https://langchain-ai.github.io/langgraph/concepts/memory/)

## Esercizio 13.5 - MCP (Model Context Protocol) basics
- Cos'è MCP, perché è importante (standard aperto Anthropic per tool integration)
- Costruisci un MCP server semplice (es. esposizione di TMDB come MCP server)
- Connetti un client (Claude Desktop o app custom) al server

📚 **Risorse MCP:**
- [MCP introduction](https://modelcontextprotocol.io/introduction) ⭐
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Anthropic MCP guide](https://docs.anthropic.com/en/docs/build-with-claude/mcp)

**Deliverable Week 13:** mini-agent multi-tool funzionante + 1 MCP server semplice.

---

# WEEK 14-15 — 🤖 PROJECT 5: AGENTIC MOVIE COMPANION

**Il progetto "wow" — quello che ti distingue.**

## Cosa costruisci

Un assistente conversazionale che:
- Risponde a domande complesse multi-step (es. "trova film simili a Inception del regista X disponibili su Netflix Italia, poi suggeriscimi un ordine di visione")
- Usa il RAG di Project 4 + tool TMDB + tool web search
- Mantiene memoria della conversazione
- Esposto sia via API che via MCP server

## Architettura

```
                  ┌─────────────────────┐
                  │  LangGraph Agent     │
                  │  ┌───────────────┐   │
User Query ──────▶│  │  Planner Node │   │
                  │  └───────┬───────┘   │
                  │          ▼           │
                  │  ┌───────────────┐   │
                  │  │ Tool Selector │───┼─▶ TMDB API
                  │  └───────┬───────┘   │   RAG vector DB
                  │          ▼           │   Web Search (Tavily)
                  │  ┌───────────────┐   │
                  │  │  Synthesizer  │   │
                  │  └───────┬───────┘   │
                  └──────────┼──────────-┘
                             ▼
                       Response + citations
```

## Stack
- **LangGraph** per orchestrazione
- **Anthropic Claude Sonnet** o **GPT-4o** per il planner (servono modelli grossi)
- **GPT-4o-mini** per task semplici (cost optimization)
- Tool: TMDB, RAG (Project 4), [Tavily Search](https://tavily.com/) (web search per AI, ha free tier)
- Memory: `SqliteSaver` di LangGraph
- Esposizione: FastAPI + endpoint MCP-compatibile
- Front-end: Streamlit chat

## Step
1. Definisci stato condiviso (`messages`, `retrieved_context`, `tool_results`)
2. Implementa nodes (planner, tool_executor, synthesizer)
3. Routing condizionale (agente decide se serve un altro tool o se può rispondere)
4. Aggiungi memoria persistente (sopravvive a riavvii)
5. Esponi come MCP server (così Claude Desktop può usarlo come tool)
6. Eval: 30 query complesse, misura task completion rate
7. Deploy + demo video

### Deliverable Project 5
✅ Repo con README architetturale serio
✅ Diagramma del grafo (LangGraph supporta `.draw_mermaid()`)
✅ Demo video 3 minuti
✅ Eval report
✅ MCP server documentato
✅ ~1000-1500 LOC

📚 **Risorse extra Project 5:**
- [LangGraph + RAG tutorial](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/)
- [LangGraph multi-agent](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/)

---

# WEEK 16 — PRODUCTION AI: OBSERVABILITY, EVAL, COSTS

**Perché:** "Funziona sulla mia macchina" non basta. Production AI = osservabilità + eval continui + cost control.

## Esercizio 16.1 - LangSmith / observability
- Trace ogni chiamata LLM
- Vedere input/output/latency/cost di ogni step
- Debug di flussi agent complessi

📚 **Risorse:**
- [LangSmith docs](https://docs.smith.langchain.com/) (free tier generoso)
- Alternative: [Langfuse (open source)](https://langfuse.com/), [Helicone](https://www.helicone.ai/), [Phoenix di Arize](https://docs.arize.com/phoenix)

## Esercizio 16.2 - Cost tracking
- Logging strutturato di token/$ per request
- Dashboard semplice (DB + endpoint `/stats`)
- Strategie di riduzione costi: caching, model routing (cheap-first), prompt compression

📚 **Risorse:**
- [OpenAI usage best practices](https://platform.openai.com/docs/guides/production-best-practices)

## Esercizio 16.3 - Caching
- Semantic cache (cache embedding-based per query simili)
- Tool: [GPTCache](https://github.com/zilliztech/GPTCache) o redis con embedding key

## Esercizio 16.4 - Eval continui
- Eval set come "test suite" → ogni cambio prompt = run eval
- Setup CI che esegue eval su PR
- Guardrail (es. moderation API per output unsafe)

📚 **Risorse:**
- [Hamel Husain — Your AI product needs evals](https://hamel.dev/blog/posts/evals/) ⭐⭐ il post di riferimento del settore
- [Eugene Yan — Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/) ⭐

## Esercizio 16.5 - Security & Safety basics
- Prompt injection awareness
- Input sanitization
- Output moderation (OpenAI Moderation API)
- Rate limiting per utente
- Secret management

📚 **Risorse:**
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Anthropic — Mitigations for prompt injection](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)

**Deliverable Week 16:** Project 5 con LangSmith integrato, cost tracking, eval pipeline, security basics.

---

# WEEK 17 (OPZIONALE) — DOCKER & CI/CD

**Perché opzionale:** lo impari benissimo on-the-job. Ma averlo nel CV alza la percezione.

## Esercizio 17.1 - Docker basics
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
- `docker build`, `docker run`
- `docker-compose` per multi-service (app + Postgres + Redis)
- Multi-stage builds per immagini piccole

📚 **Risorse:**
- [Docker for Beginners (free, ufficiale)](https://docker-curriculum.com/)
- [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)

## Esercizio 17.2 - GitHub Actions CI
```yaml
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install -r requirements.txt
      - run: pytest --cov
```
- Test on push
- Lint con `ruff`
- Type check con `mypy`
- Auto-deploy su merge

📚 **Risorse:**
- [GitHub Actions docs](https://docs.github.com/en/actions/quickstart)

**Deliverable Week 17:** Project 4 e Project 5 dockerizzati + CI verde.

---

# 📚 RISORSE TRASVERSALI (USA SPESSO)

## Concetti AI/LLM (per fondamenta solide)
- ⭐ [Andrej Karpathy — Intro to LLMs (1h video)](https://www.youtube.com/watch?v=zjkBMFhNj_g) — gratis, must-watch
- ⭐ [Karpathy — Let's build GPT from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY) — capisci come funzionano davvero i transformer
- [Hugging Face — NLP Course (free)](https://huggingface.co/learn/nlp-course) — eccellente
- [Full Stack LLM Bootcamp (free)](https://fullstackdeeplearning.com/llm-bootcamp/) — corso completo gratuito di Berkeley

## Newsletter / blog da seguire
- [Latent Space (podcast + newsletter)](https://www.latent.space/) — il #1 sull'AI engineering
- [Eugene Yan blog](https://eugeneyan.com/) ⭐ — pattern reali di production AI
- [Hamel Husain blog](https://hamel.dev/) ⭐ — eval, fine-tuning, ML in produzione
- [Simon Willison's blog](https://simonwillison.net/) — link curated quotidiano sul mondo AI
- [Anthropic Engineering blog](https://www.anthropic.com/engineering)

## Comunità
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) — open source LLMs
- [Latent Space Discord](https://www.latent.space/) — community AI engineer
- [LangChain Discord](https://www.langchain.com/community)
- [Hugging Face Discord](https://huggingface.co/join/discord)

## Libri (opzionali ma eccellenti)
- *Designing Machine Learning Systems* — Chip Huyen ⭐ (il libro per ML in produzione)
- *Building LLMs for Production* — Bouchard & Peters
- *Designing Data-Intensive Applications* — Martin Kleppmann (classico per backend serio)

## Job board specifici AI
- [AI Jobs (aijobs.net)](https://aijobs.net/)
- [Pallet — AI/ML jobs](https://pallet.com/jobs/ai-ml)
- [Y Combinator Work at a Startup](https://www.workatastartup.com/) — filtra per AI
- LinkedIn jobs: query `"Applied AI Engineer" OR "AI Engineer" OR "Forward Deployed Engineer"`

---

# 🎯 PHASE 2 — SUCCESS CRITERIA

Alla fine di Phase 2 (8-10 settimane dopo Phase 1) sei capace di:

✅ Scrivere FastAPI **async** production-grade con test ≥70% coverage
✅ Integrare **OpenAI / Anthropic API** con structured outputs, streaming, tool use
✅ Costruire **RAG end-to-end**: ingestion, retrieval (hybrid + rerank), generation, eval
✅ Costruire **agenti multi-step con LangGraph** (planner, tool use, memory, persistence)
✅ Costruire un **MCP server** custom
✅ **Valutare** sistemi AI con metriche reali (RAGAS, custom eval)
✅ **Osservare** sistemi AI in produzione (LangSmith / Langfuse)
✅ **Controllare costi** (cache, routing, monitoring)
✅ Avere **5 progetti** sul GitHub di cui 2 AI-heavy con demo live
✅ Parlare di **trade-off architetturali** in colloquio (chunking, embedding choice, agent vs workflow)

**Sei pronto per:** Applied AI Engineer / AI Engineer Mid · Backend Engineer (AI-focused) Mid · Forward Deployed Engineer in azienda AI

---

# 🗺️ LA MAPPA COMPLETA

```
PHASE 1 (8 settimane) — Python fundamentals + Backend
├─ Week 1-2: Core Python
├─ Week 3: Files / API / JSON
├─ Week 4: 🎬 Project 1 — Movie Data Collector
├─ Week 5-6: Pandas + Project 2 (Analytics)
├─ Week 7-8: FastAPI + DB + Project 3 (Recommendation API)
└─ Output: Junior Python Developer credibile

PHASE 2 (8-10 settimane) — Applied AI Engineer
├─ Week 9: Async + Production FastAPI
├─ Week 10: LLM APIs deep dive
├─ Week 11-12: 🤖 Project 4 — RAG Movie Assistant
├─ Week 13: LangGraph + MCP basics
├─ Week 14-15: 🤖 Project 5 — Agentic Movie Companion
├─ Week 16: Production AI (observability, eval, costs)
├─ Week 17 (opz.): Docker + CI/CD
└─ Output: Applied AI Engineer Mid

DURATA TOTALE: 4-5 mesi part-time (~2-3h/giorno) → cambio carriera completo
```

---

# 💡 CONSIGLI STRATEGICI PHASE 2

1. **Posta su LinkedIn ogni progetto finito.** Project 4 e 5 sono *materiale virale* nel mondo AI. Un buon post = 5-15k impressions = recruiter che ti scrivono spontaneamente.

2. **Contribuisci a 1 progetto open source** (anche piccolo): LangChain, LlamaIndex, LangGraph hanno sempre `good-first-issue`. Avere 1 PR mergiato = enorme credibility boost.

3. **Scrivi 2-3 articoli tecnici** (Medium, dev.to, blog personale): "What I learned building a RAG system", "Comparing chunking strategies", ecc. Posiziona te stesso come thought leader entry-level.

4. **Aggiorna il CV iterativamente.** Dopo Project 4 → headline "Marketing & AI Engineer". Dopo Project 5 → "Applied AI Engineer · Marketing background".

5. **Inizia colloqui durante Phase 2**, non dopo. I colloqui *sono* parte dell'apprendimento — fanno emergere i gap reali.

6. **Track metriche dei tuoi progetti.** Non basta "ho fatto un RAG". Serve "RAG con MRR@5 = 0.72, latenza p95 = 1.2s, costo medio per query = $0.003". I numeri vendono.

