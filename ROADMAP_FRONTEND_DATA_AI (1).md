# PYTHON ROADMAP — FRONTEND → DATA & AI ENGINEERING (MVP)
## 10-12 settimane: da frontend developer a profilo ibrido Frontend + Data + AI Engineering

🎯 **OBIETTIVO:** Consolidare Python e costruire competenze pratiche in Data Analysis, API, SQL/BigQuery mindset e AI Engineering, senza perdere il vantaggio competitivo da frontend developer.

Questa roadmap parte dalla roadmap originale, ma la modifica per il tuo profilo attuale:

- Frontend developer con React / JavaScript / TypeScript
- Esperienza su campagne, analytics e investigations
- SQL e GCP / BigQuery già usati sul lavoro
- Primo progetto già fatto con LangGraph
- Obiettivo: avere più opzioni professionali tra frontend, data e applied AI

---

## FILOSOFIA

**✅ DO:**
- Continuare giorno per giorno con i fondamentali Python
- Imparare Python come strumento per data, automation, backend e AI
- Usare Jupyter presto, non solo script `.py`
- Collegare ogni concetto a casi reali: API, dati, analytics, AI workflows
- Costruire 3 progetti portfolio + 1 progetto realistico legato ad analytics/BigQuery
- Mantenere il vantaggio frontend: React + UX + product thinking
- Studiare SQL come competenza centrale, non secondaria

**❌ DON'T:**
- Non puntare a diventare “Data Scientist puro”
- Non fare mesi di NumPy avanzato o matematica ML prima del necessario
- Non inseguire mille tool AI senza fondamenta Python/Data
- Non comprare altri corsi per ora: prima completare questa fase
- Non trasformare ogni progetto in un prodotto perfetto: MVP > perfezione
- Non abbandonare React: è parte del tuo vantaggio competitivo

---

## STRUCTURE

**Week 1-2:** Core Python Fundamentals  
**Week 3:** Files, JSON, APIs, Environment  
**Week 4:** 🎬 PROJECT 1 — Movie Data Collector  
**Week 5-6:** Pandas, Jupyter, Matplotlib, NumPy basics  
**Week 6:** 🎬 PROJECT 2 — Movie Analytics Dashboard  
**Week 7:** 📊 PROJECT 2B — Real-World Analytics Notebook  
**Week 8-9:** SQL, BigQuery mindset, FastAPI, Pydantic  
**Week 10:** 🎬🤖 PROJECT 3 — Cinema Mood Recommender  
**Week 11-12:** AI Engineering Bridge: LLM APIs, structured outputs, LangGraph, RAG basics

---

## SKILL PRIORITIES

### Tier 1 — Da padroneggiare
- Python fundamentals
- Pandas
- SQL / BigQuery-style SQL
- Jupyter
- APIs / JSON
- FastAPI basics

### Tier 2 — Conoscenza pratica
- Polars
- NumPy basics
- Matplotlib
- Pydantic
- LangGraph
- LLM APIs

### Tier 3 — Dopo questa roadmap
- Docker
- CI/CD
- Advanced ML
- MLOps
- Kubernetes
- Advanced distributed systems

---

# WEEK 1-2: CORE PYTHON FUNDAMENTALS

## DAY 1-2: Data Types & Control Flow

### Esercizio 1.0 - Git & GitHub workflow setup

**Perché farlo subito:** ogni esercizio deve vivere in una repo pulita. Il tuo obiettivo non è solo imparare Python, ma mostrare un percorso professionale e credibile.

**Cosa imparare:**
- Branch workflow: `main` → feature branch → PR → merge
- Conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`
- `.gitignore` per Python
- Pull request template
- README professionale

**Esercizio:**
1. Crea repo `python-data-ai-roadmap`
2. Aggiungi `.gitignore`, `README.md`, `.github/pull_request_template.md`
3. Ogni esercizio = branch + PR + merge

**Deliverable:** repo pubblica o privata ordinata, con README iniziale.

---

### Esercizio 1.1 - Type conversions & None
- Input: dati misti da simulare come se arrivassero da API o CSV
- Task: convertire in modo sicuro, gestire `None`, controllare tipi

### Esercizio 1.2 - Control flow challenges
- FizzBuzz variations
- Nested loops con break/continue
- Ternary operators
- Mini use case: classificare record di campagne come `valid`, `warning`, `invalid`

**Concetti coperti:** int, float, str, bool, None, if/elif/else, for, while, break, continue, pass

---

## DAY 3-5: Data Structures

### Esercizio 1.3 - Lists deep dive
- append, extend, insert, pop, remove, sort, reverse
- slicing
- list of lists
- Use case: lista di campaign IDs, event logs, records

### Esercizio 1.4 - Tuples & unpacking
- Immutability vs lists
- Tuple unpacking
- Multiple return values
- Use case: funzioni che ritornano `(status, result)`

### Esercizio 1.5 - Dictionaries mastery
- Creation
- `.get()` vs `[]`
- keys, values, items
- nested dicts JSON-like
- counting, grouping, lookup

**Focus extra:** i dizionari sono fondamentali per JSON, API, LangGraph state e structured outputs.

### Esercizio 1.6 - Sets operations
- uniqueness
- union, intersection, difference
- membership testing
- Use case: confrontare liste di utenti, campaign IDs, segment IDs

**Deliverable:** 4 esercizi completati con esempi vicini a dati reali.

---

## DAY 6-8: Mutability & Memory

### Esercizio 1.7 - Mutability gotchas
- Mutable vs immutable
- Assignment vs copy
- Function side effects
- Default argument trap

### Esercizio 1.8 - Shallow vs deep copy
- `list.copy()`
- `copy.deepcopy()`
- nested dictionaries
- Use case: modificare una copia di configurazione senza toccare l'originale

**Concetti coperti:** mutability, reference, copy, shallow copy, deep copy, side effects

**Perché è importante per AI/Data:** molti bug in pipeline dati, LangGraph state e config LLM derivano da mutabilità gestita male.

---

## DAY 9-11: Functions

### Esercizio 1.9 - Functions basics
- Parameters vs arguments
- Return values
- Scope
- Docstrings

### Esercizio 1.10 - Default parameters
- Correct way: `default=None`
- Avoid mutable defaults

### Esercizio 1.11 - *args and **kwargs
- Variable arguments
- Practical use cases
- Use case: funzione generica per logging o data validation

### Esercizio 1.12 - List, Dict & Set Comprehensions
- List comprehensions
- Dict comprehensions
- Set comprehensions
- Trasformare dataset piccoli in modo leggibile

### Esercizio 1.13 - Pure vs impure functions
- Pure functions
- Side effects
- Deterministic functions

**Deliverable:** funzioni piccole, testabili, leggibili.

---

## DAY 12-14: Iteration Tools, Strings, Errors

### Esercizio 1.16 - Iteration tools
- `enumerate()`
- `zip()`
- `map()`
- `filter()`
- comprehension vs map/filter

### Esercizio 1.17 - String manipulation
- split, join, replace, strip, lower, upper
- f-strings
- parsing di stringhe da log o CSV

### Esercizio 1.18 - Error handling
- try/except/finally
- ValueError, KeyError, TypeError
- custom error messages
- when to catch vs when to fail

**Checkpoint:** sei qui adesso. Completa bene questo esercizio prima di andare avanti.

---

# WEEK 2 CHECKPOINT

**✅ Hai coperto:**
- Data types
- Data structures
- Mutability
- Functions
- Comprehensions
- Iteration
- Strings
- Error handling

**📝 Self-assessment:**
Crea 5 mini esercizi misti:

1. Parse di una lista di campaign records
2. Validazione campi obbligatori
3. Conteggio eventi per categoria
4. Gestione errori su input sporchi
5. Funzione pura che trasforma record grezzi in record normalizzati

---

# WEEK 3: FILES, JSON, API, JUPYTER

## Setup Jupyter

### Esercizio 2.0 - JupyterLab setup

```bash
pip install jupyterlab
jupyter lab
```

**Perché:** per Data Analysis, investigations e AI experimentation, Jupyter è uno strumento quotidiano.

**Deliverable:** cartella `notebooks/` nella repo.

---

## File I/O

### Esercizio 2.1 - Reading files
- `with open(...)`
- read, readline, readlines
- encoding utf-8

### Esercizio 2.2 - Writing files
- write, writelines
- modes: `r`, `w`, `a`

### Esercizio 2.3 - CSV handling manuale
- parse CSV senza Pandas
- scrivere CSV
- capire formato e edge cases

**Nota:** anche se poi userai Pandas, capire CSV manualmente aiuta molto.

---

## JSON

### Esercizio 2.4 - JSON read/write
- `json.load`
- `json.loads`
- `json.dump`
- `json.dumps`
- nested JSON

### Esercizio 2.5 - Config loader
- leggere `config.json`
- validare campi obbligatori
- default values
- errori chiari

**Use case:** config per API keys, query settings, LLM settings.

---

## API Integration

### Esercizio 2.6 - HTTP basics
- `requests.get`
- status codes
- headers
- query params

### Esercizio 2.7 - Error handling APIs
- timeout
- invalid JSON
- 4xx / 5xx
- retry semplice

### Esercizio 2.8 - API with pagination
- fetch multiple pages
- combine results
- stop condition

---

## Environment Variables

### Esercizio 2.9 - Using `.env`

```bash
pip install python-dotenv
```

- `os.getenv`
- `.env`
- `.env.example`
- `.gitignore`

**Deliverable Week 3:** mini API client funzionante + notebook esplorativo.

---

# 🎬 WEEK 4: PROJECT 1 — MOVIE DATA COLLECTOR

## What to Build

CLI tool che fetcha dati TMDB e li salva localmente.

### Features MVP

```bash
python movie_cli.py fetch trending
python movie_cli.py search "Inception"
python movie_cli.py details 27205
```

### Core functionality
1. Call TMDB API
2. Save JSON files locally
3. Cache: if data < 24h old, don't re-fetch
4. Pretty print terminal results
5. Error handling

### Tech Stack
- `requests`
- `json`
- `argparse`
- `dotenv`
- basic logging

### File Structure

```text
movie-data-collector/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── movie_cli.py
├── api_client.py
├── cache.py
└── data/              # gitignored
```

### Deliverables
✅ Working CLI  
✅ Cache working  
✅ Error handling  
✅ README  
✅ Push to GitHub  

### Skills Applied
- API integration
- File I/O
- JSON
- CLI
- Environment variables
- Code organization

---

# WEEK 5-6: DATA STACK — PANDAS, JUPYTER, MATPLOTLIB, NUMPY BASICS

## Pandas Fundamentals

### Esercizio 3.1 - DataFrames & Series

```python
import pandas as pd

df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
df.head()
df.info()
df.describe()
```

### Esercizio 3.2 - Selection & Filtering
- `df['column']`
- `df.loc[]`
- `df.iloc[]`
- boolean indexing
- multiple conditions

### Esercizio 3.3 - Data cleaning
- missing values
- duplicates
- data types
- `pd.to_datetime`

### Esercizio 3.4 - Transformations
- new columns
- `apply`
- `map`
- string methods

### Esercizio 3.5 - GroupBy & aggregations
- sum
- mean
- count
- multi-column groupby
- `.agg()`

### Esercizio 3.6 - Merge & join
- inner join
- left join
- concat

### Esercizio 3.7 - Useful methods
- `value_counts()`
- `sort_values()`
- `reset_index()`
- `pivot_table()`

---

## Jupyter Workflow

### Esercizio 3.8 - Notebook structure

Ogni notebook deve avere:

1. Title
2. Goal
3. Data loading
4. Cleaning
5. Analysis
6. Charts
7. Insights
8. Next steps

**Regola:** un notebook non è solo codice. Deve raccontare una storia.

---

## Matplotlib Basics

### Esercizio 3.9 - Basic charts
- line chart
- bar chart
- scatter plot
- labels
- title
- legend
- save as PNG

---

## NumPy Basics Only

### Esercizio 3.10 - NumPy essentials

```python
import numpy as np

arr = np.array([1, 2, 3])
arr.mean()
arr.std()
```

Studiare solo:
- arrays
- mean
- median
- std
- min/max
- basic vector operations

**Non approfondire per ora:** algebra lineare avanzata, broadcasting complesso, performance tuning.

---

## Polars Intro

### Esercizio 3.11 - Polars basics

```python
import polars as pl

df = pl.read_csv("data.csv")
df.head()
```

Studiare:
- read CSV
- select
- filter
- group_by
- lazy execution concept

**Obiettivo:** capire che Polars esiste, quando può essere più veloce di Pandas, e come leggere codice base.

---

# 🎬 WEEK 6: PROJECT 2 — MOVIE ANALYTICS DASHBOARD

## What to Build

Notebook + report che analizza dati film e produce insight.

### Data Source
Usa dati dal Project 1 oppure dataset pubblico TMDB.

### Analysis Required

**1. Top films**
- Top 20 by rating
- Top 20 by revenue
- Top 20 by popularity

**2. Genre trends**
- Movies per genre over years
- Revenue by genre

**3. Budget vs Revenue**
- Scatter plot
- Correlation coefficient

**4. Release patterns**
- Months with most releases
- Best months for blockbusters

**5. Basic statistics**
- Average runtime
- Average budget/revenue
- Most common genres

### Deliverables
✅ Jupyter notebook  
✅ 5-6 charts saved as PNG  
✅ Markdown report with insights  
✅ Clean code  
✅ README with findings  
✅ Push to GitHub  

### Skills Applied
- Pandas
- Data cleaning
- GroupBy
- Merge
- Matplotlib
- Storytelling

---

# 📊 WEEK 7: PROJECT 2B — REAL-WORLD ANALYTICS NOTEBOOK

## Perché questo progetto è importante

Questo è il progetto più vicino al tuo lavoro reale.

Serve a collegare:

- SQL
- BigQuery / GCP mindset
- Pandas
- investigations
- reporting
- AI-assisted summaries

---

## What to Build

Un notebook che parte da dati realistici e produce un report di investigation.

Puoi usare:

- dati fittizi simili a campagne marketing
- exported CSV da BigQuery senza dati sensibili
- dataset pubblico simile a campaign events
- dati anonimizzati o generati artificialmente

---

## Variante A — Campaign Investigation Notebook

### Scenario

Una campagna mostra anomalie di performance.

### Questions
1. Quali segmenti hanno CTR anomalo?
2. Quali paesi o placement mostrano comportamento insolito?
3. Ci sono spike temporali?
4. Ci sono pattern per browser/device?
5. Quali dati meritano escalation?

### Deliverables
✅ Notebook  
✅ Query SQL simulate o reali anonimizzate  
✅ Pandas analysis  
✅ Charts  
✅ Executive summary  

---

## Variante B — BigQuery Export Analysis

### Pipeline

```text
BigQuery
↓
CSV export / query result
↓
Jupyter
↓
Pandas cleaning
↓
Analysis
↓
Markdown report
```

### Skills Applied
- SQL thinking
- Pandas
- data cleaning
- analytics storytelling
- business-oriented communication

---

## Variante C — AI Summary Layer

Dopo aver generato gli insight, aggiungi un piccolo script che prende il report e genera un summary con LLM.

### Example output

```text
Key findings:
1. Campaign X shows abnormal CTR in segment Y.
2. Traffic from country Z increased 240% over baseline.
3. Recommendation: review targeting settings and exclude suspicious placements.
```

### Nota
Questo è opzionale, ma molto utile per collegare data work e AI Engineering.

---

# WEEK 8-9: SQL, BIGQUERY MINDSET, FASTAPI

## SQL grezzo

### Esercizio 5.0a - SELECT, WHERE, ORDER BY, LIMIT

```sql
SELECT title, year, rating
FROM movies
WHERE year >= 2010 AND rating > 7.5
ORDER BY rating DESC
LIMIT 10;
```

### Esercizio 5.0b - JOINs

```sql
SELECT m.title, a.name
FROM movies m
INNER JOIN movie_actors ma ON m.id = ma.movie_id
INNER JOIN actors a ON a.id = ma.actor_id;
```

### Esercizio 5.0c - GROUP BY + HAVING

```sql
SELECT genre, AVG(rating) AS avg_rating, COUNT(*) AS film_count
FROM movies
GROUP BY genre
HAVING COUNT(*) > 10
ORDER BY avg_rating DESC;
```

### Esercizio 5.0d - CTEs

```sql
WITH high_rated AS (
  SELECT * FROM movies WHERE rating > 8
)
SELECT genre, COUNT(*)
FROM high_rated
GROUP BY genre;
```

### Esercizio 5.0e - Window functions

```sql
SELECT
  title,
  genre,
  rating,
  RANK() OVER (PARTITION BY genre ORDER BY rating DESC) AS rank_in_genre
FROM movies;
```

### Esercizio 5.0f - BigQuery mindset

Studiare:
- CTE leggibili
- partitioned tables concept
- cost awareness
- avoid `SELECT *` su grandi dataset
- window functions
- nested / repeated fields concept

**Deliverable:** file `queries.sql` con almeno 15 query commentate.

---

## FastAPI Fundamentals

### Esercizio 5.1 - Hello API

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

### Esercizio 5.2 - Request body with Pydantic

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
```

### Esercizio 5.3 - Response models
- response_model
- validation
- clean API contracts

### Esercizio 5.4 - Error handling
- HTTPException
- 404
- 400
- validation errors

---

## Testing Basics

### Esercizio 5.5 - pytest basics

```python
def test_sum():
    assert sum([1, 2, 3]) == 6
```

### Esercizio 5.6 - Testing FastAPI

```python
from fastapi.testclient import TestClient
```

**Focus:** pochi test, ma utili. Non puntare subito a coverage perfetta.

---

# 🎬🤖 WEEK 10: PROJECT 3 — CINEMA MOOD RECOMMENDER

## What to Build

AI-powered movie recommender integrato nel tuo sito personale React, con FastAPI backend + LLM recommendations.

---

## Core Features

### Frontend
- React + TypeScript
- Form input: genre, mood, liked movie, year range
- Display 5 recommendations
- Loading states
- Error states
- Responsive UI

### Backend

**POST `/api/recommend`**

Request:

```json
{
  "genre": "Sci-Fi",
  "mood": "mind-bending, philosophical",
  "liked_movie": "Inception",
  "year_min": 2010,
  "year_max": 2024
}
```

Logic:
1. Fetch candidate movies from TMDB
2. Call LLM with structured prompt
3. Return top 5 recommendations with explanations
4. Validate response with Pydantic

Response:

```json
{
  "recommendations": [
    {
      "title": "Interstellar",
      "year": 2014,
      "rating": 8.6,
      "reason": "Similar emotional and sci-fi tone..."
    }
  ]
}
```

---

## Tech Stack

**Frontend:**
- React
- TypeScript
- Axios or fetch
- Existing personal website

**Backend:**
- FastAPI
- Pydantic
- TMDB API
- LLM API
- Logging
- pytest

---

## Deliverables

✅ FastAPI app  
✅ TMDB integration  
✅ LLM recommendation logic  
✅ Pydantic schemas  
✅ Error handling  
✅ Basic tests  
✅ React integration  
✅ README  
✅ Screenshot/GIF  

---

## AI Engineering Focus

Questo progetto non serve solo a imparare FastAPI.

Serve a imparare:

- prompt design
- structured outputs
- API orchestration
- validation
- error handling with LLMs
- product thinking

---

# WEEK 11-12: AI ENGINEERING BRIDGE

Questa fase arriva solo dopo Project 1, Project 2, Project 2B e Project 3.

## LLM APIs

### Esercizio 6.1 - Basic LLM call
- system/user messages
- temperature
- max tokens
- error handling

### Esercizio 6.2 - Structured outputs
- Pydantic schemas
- JSON validation
- never parse random text manually if structured output is possible

### Esercizio 6.3 - Streaming basics
- streaming response
- UX implications for frontend

### Esercizio 6.4 - Tool calling concept
- define tool schema
- model requests tool
- execute tool
- return result to model

---

## LangGraph

### Esercizio 6.5 - LangGraph fundamentals
- State
- Nodes
- Edges
- Conditional routing

### Esercizio 6.6 - Mini workflow

Build a simple investigation workflow:

```text
Input question
↓
Decide data source
↓
Run analysis function
↓
Generate summary
↓
Return answer
```

---

## RAG Basics

### Esercizio 6.7 - RAG concepts
- documents
- chunks
- embeddings
- vector DB
- retrieval
- generation
- citations

### Esercizio 6.8 - Tiny RAG prototype

Use a small dataset:
- movie descriptions
- campaign documentation
- fake knowledge base

Build:
1. ingest documents
2. retrieve top-k
3. answer with context

---

# WHAT'S NOT A PRIORITY RIGHT NOW

❌ Encertify or other paid course  
❌ Advanced NumPy  
❌ Advanced ML math  
❌ Docker deep dive  
❌ Kubernetes  
❌ MLOps platforms  
❌ Fine-tuning models  
❌ Advanced SQLAlchemy  
❌ Complex auth systems  

These can come later.

---

# FINAL DELIVERABLES

## Repository 1 — `movie-data-collector`
- CLI
- TMDB API
- JSON cache
- README

## Repository 2 — `movie-analytics-dashboard`
- Jupyter notebook
- Pandas analysis
- charts
- markdown report

## Repository 3 — `real-world-analytics-notebook`
- campaign/investigation-style analysis
- SQL queries
- Pandas notebook
- executive summary

## Repository 4 — `cinema-mood-recommender`
- React frontend
- FastAPI backend
- LLM integration
- Pydantic schemas
- tests

---

# SUCCESS CRITERIA

At the end of this roadmap, you can:

✅ Write solid Python fundamentals  
✅ Work with files, JSON, APIs and `.env`  
✅ Use Jupyter for investigations  
✅ Analyze data with Pandas  
✅ Create useful visualizations  
✅ Write SQL with joins, CTEs and window functions  
✅ Think in BigQuery-style analytics workflows  
✅ Build a basic FastAPI backend  
✅ Integrate LLM APIs into a real product  
✅ Connect React frontend with Python backend  
✅ Explain your projects clearly in interviews  

---

# TARGET PROFILE

Non stai cercando di diventare solo:

❌ Python Developer  
❌ Data Scientist Junior  
❌ Backend Developer puro  

Il target è:

✅ Frontend Engineer  
✅ Data-capable Developer  
✅ Applied AI Engineer  
✅ AI Product Engineer  

Capace di lavorare su:

- React applications
- campaign analytics
- SQL investigations
- Python data workflows
- FastAPI backends
- LLM-powered features
- agentic workflows

---

# HOW TO USE THIS ROADMAP

## Daily Routine

Se hai poco tempo:

- 45-60 min al giorno
- 4-5 giorni a settimana
- 1 sessione più lunga nel weekend

Se hai più tempo:

- 2h al giorno
- project work nel weekend

---

## Weekly Routine

Ogni settimana:

1. Completa gli esercizi
2. Scrivi note brevi nel README
3. Fai commit puliti
4. Crea almeno una PR
5. Alla fine della settimana scrivi:
   - cosa ho imparato
   - cosa non è chiaro
   - cosa voglio approfondire

---

## When You're Stuck

1. Prova da solo 20-30 minuti
2. Scrivi cosa non capisci
3. Chiedi un hint, non la soluzione completa
4. Se resta bloccante, passa oltre e torna dopo

---

# NEXT STEPS AFTER THIS ROADMAP

Dopo questa roadmap, scegli una direzione:

## Option A — AI Engineering Track
- RAG
- LangGraph
- MCP
- Evaluation
- Observability

## Option B — Data Engineering / Analytics Track
- BigQuery advanced
- dbt
- data modeling
- scheduled pipelines
- dashboards

## Option C — AI Product Frontend Track
- AI UX patterns
- streaming UI
- chat interfaces
- tool execution UI
- human-in-the-loop workflows

---

# RECOMMENDATION

Completa questa roadmap fino a Project 2B prima di comprare altri corsi.

Dopo Project 2B avrai molta più chiarezza su cosa ti manca davvero:

- più Python?
- più Pandas?
- più SQL?
- più AI Engineering?
- più backend?

A quel punto il prossimo investimento sarà molto più mirato.
