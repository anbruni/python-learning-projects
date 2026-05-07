# PYTHON ROADMAP — LEARN BY DOING
## Da zero a job-ready con esercizi + mini progetti reali

🎬 **TEMA UNIFICANTE: CINEMA & MOVIE DATA**
I progetti principali (2, 5, 8, Final) sono tutti basati su dati cinematografici.

**Perché cinema?**
1. **Motivazione**: Impari meglio lavorando su qualcosa che ti appassiona
2. **Portfolio unico**: "Movie AI Platform" > "Generic CRUD App"
3. **Colloqui**: Parli con entusiasmo di progetti → più credibile
4. **Dati reali**: TMDB API è professionale, ben documentata, gratuita
5. **Storytelling**: Ogni progetto ha un filo narrativo che lo lega agli altri

---

## METODO

Per ogni argomento:
1. **Esercizio mirato** (isola il concetto)
2. **Esercizio combinato** (usa più concetti insieme)
3. **Mini progetto** (fine sezione, mette insieme tutto)

Niente video. Niente tutorial lunghi. Solo **fare**.

---

## SECTION 1 — CORE PYTHON (FONDAMENTA)

### 1.1-1.4 Data Structures + Mutability

**Esercizio 1.1** - List operations
- Data: lista di transazioni bancarie
- Task: filtra, ordina, trova massimo/minimo senza usare max()

**Esercizio 1.2** - Dict manipulation
- Data: dizionario di studenti con voti
- Task: calcola medie, trova top 3, crea report

**Esercizio 1.3** - Mutability trap
- Task: scrivi una funzione che modifica una lista in modo inaspettato
- Poi fixala usando copy
- Capisci shallow vs deep copy

**Esercizio 1.4** - Nested structures
- Data: JSON simulato (dict con liste di dict)
- Task: estrai dati specifici, flatten, riorganizza

---

### 1.5 Comprehensions

**Esercizio 1.5** - Transform data
- Input: lista di user dict
- Task: filtra attivi, estrai email, crea lookup dict
- Tutto con comprehensions (no loops)

**Esercizio 1.6** - Data cleaning
- Input: lista di stringhe sporche
- Task: pulisci, normalizza, rimuovi duplicati
- List + dict + set comprehension

---

### 1.6-1.7 Functions + Iteration Tools

**Esercizio 1.7** - Pure functions
- Scrivi 5 funzioni pure per trasformare dati
- Poi scrivi versioni impure (side effects)
- Confronta

**Esercizio 1.8** - *args/**kwargs
- Crea funzione che accetta config variabile
- Usa per creare API client configurabile

**Esercizio 1.9** - map/filter/zip
- Data: 3 liste (nomi, età, città)
- Task: combina, filtra, trasforma senza loop

---

### 1.9 Error Handling

**Esercizio 1.10** - Robust input parser
- Input: stringhe che potrebbero essere numeri/date/invalid
- Task: parse con try/except, return None se invalid
- Custom exception per casi specifici

---

### 🚀 MINI PROJECT 1 — DATA PROCESSOR
**Cosa costruire:**
CLI tool che:
1. Legge lista di transazioni (hardcoded list of dicts)
2. Pulisce dati (gestisce missing/invalid)
3. Calcola statistiche (totale, media, groupby categoria)
4. Trova anomalie (outliers)
5. Output: report formattato

**Skills usate:**
- Data structures (dict, list)
- Comprehensions
- Functions con args/kwargs
- Error handling
- String formatting

**Deliverable:** Script che stampa report professionale

---

## SECTION 2 — FILES, JSON, API (REAL WORLD)

### 2.1-2.2 Files + JSON

**Esercizio 2.1** - File I/O
- Task: leggi CSV manualmente (no pandas), parse in dict
- Gestisci errori (file missing, malformed)

**Esercizio 2.2** - JSON processor
- Input: JSON file con dati nested
- Task: flatten, transform, write to new JSON
- Gestisci encoding issues

**Esercizio 2.3** - Config loader
- Crea classe che legge config da JSON
- Valida required fields
- Default values per missing

---

### 2.3 API

**Esercizio 2.4** - API client basics
- Task: chiama API pubblica (es. JSONPlaceholder)
- Parse response, gestisci errori HTTP
- Retry logic

**Esercizio 2.5** - API with params
- Task: chiama API con query params
- Pagina risultati (multiple requests)
- Combina dati

---

### 🚀 MINI PROJECT 2 — MOVIE DATA COLLECTOR 🎬
**Cosa costruire:**
CLI tool che:
1. Chiama TMDB API (gratuita, register at themoviedb.org)
2. Fetcha dati film: trending, top rated, search by title
3. Salva dati in JSON locale (database locale)
4. Cache intelligente: se dati < 24h, usa cache
5. CLI commands:
   - `fetch trending` → aggiorna trending movies
   - `search "Inception"` → cerca film
   - `details {movie_id}` → dettagli + cast
6. Error handling completo (API down, rate limits)

**Setup TMDB API (5 minuti):**
1. Vai su https://www.themoviedb.org/signup
2. Verifica email
3. Settings → API → Request API Key (scegli "Developer")
4. Copia API Key in file `.env`

**Skills usate:**
- File I/O (JSON)
- API requests (GET con params)
- Error handling
- Date/time logic (cache expiry)
- Config file per API key (.env)
- Environment variables

**Deliverable:** CLI funzionante con database locale film

---

## SECTION 3 — OOP (BASE)

### 3.1-3.4 Classes + Methods

**Esercizio 3.1** - BankAccount (già fatto!)
**Esercizio 3.2** - Student tracker (già fatto!)
**Esercizio 3.3** - Temperature converter (già fatto!)

**Esercizio 3.4** - Inventory system
- Classe Product (name, price, stock)
- Classe Inventory (gestisce products)
- Metodi: add, remove, search, low_stock_report

**Esercizio 3.5** - `__str__` e `__repr__`
- Aggiungi ai tuoi esercizi precedenti
- Rendi gli oggetti printable

---

### 🚀 MINI PROJECT 3 — TODO LIST APP (OOP)
**Cosa costruire:**
CLI todo app con:
1. Classe Task (id, title, status, priority, due_date)
2. Classe TodoList (gestisce tasks)
3. Metodi: add, complete, list, filter_by_status
4. Salva/carica da JSON
5. `__str__` per pretty print

**Skills usate:**
- OOP (classi, metodi)
- File I/O (persistence)
- Date handling
- String formatting

**Deliverable:** App funzionante con data persistence

---

## SECTION 4 — NUMPY (BASE)

### 4.1-4.4 Array Operations

**Esercizio 4.1** - Array basics
- Crea array 2D di numeri random
- Operazioni: sum, mean, std
- Confronta performance vs list

**Esercizio 4.2** - Indexing mastery
- Array multidimensionale
- Estrai slice complesse
- Boolean indexing

**Esercizio 4.3** - Broadcasting
- Normalizza array (subtract mean, divide by std)
- Operazioni su array di shape diverse

---

### 🚀 MINI PROJECT 4 — IMAGE PROCESSOR (numpy)
**Cosa costruire:**
Script che:
1. Carica immagine come array (usa PIL/Pillow)
2. Converte in grayscale (operazioni array)
3. Applica filtri (brightness, contrast)
4. Crop e resize
5. Salva risultato

**Skills usate:**
- NumPy array operations
- Broadcasting
- File I/O (images)

**Deliverable:** Script che trasforma immagini

---

## SECTION 5 — PANDAS (CORE SKILL)

### 5.1-5.7 DataFrame Operations

**Esercizio 5.1** - Load & explore
- Carica CSV (usa dataset pubblico: Titanic, etc)
- info(), describe(), head()
- Identifica missing values

**Esercizio 5.2** - Selection mastery
- loc vs iloc
- Filtri complessi (multiple conditions)
- Select columns dinamicamente

**Esercizio 5.3** - Data cleaning
- Drop duplicates
- Fill missing (mean, median, forward fill)
- Fix data types

**Esercizio 5.4** - Transform
- Crea nuove colonne (apply, map)
- Bin continuous data
- One-hot encoding manuale

**Esercizio 5.5** - Groupby
- Group by categoria
- Multiple aggregations
- Pivot table

**Esercizio 5.6** - Merge
- Join 2 datasets
- Handle missing keys
- Concat vertically

**Esercizio 5.7** - Time series
- Parse dates
- Resample (daily → monthly)
- Rolling average

---

### 🚀 MINI PROJECT 5 — MOVIE ANALYTICS DASHBOARD 🎬
**Cosa costruire:**
Script di analisi cinematografica:
1. Carica dataset TMDB (usa dati salvati da Project 2 O scarica CSV pubblico TMDB/IMDb)
2. Pulisci dati (missing values, duplicates, bad dates)
3. Analisi:
   - **Top 50 film** per rating, revenue, popularity
   - **Trend per genere** (azione, drama, etc) negli ultimi 20 anni
   - **Attori più prolifici** (merge con cast data)
   - **Budget vs Revenue correlation** (quali generi rendono di più?)
   - **Release timing** (quale mese ha più blockbuster?)
4. Export report (JSON + formatted markdown)
5. Salva 5-6 grafici (line, bar, scatter) in folder `reports/`

**Skills usate:**
- Pandas: load, clean, transform, groupby, merge
- Date handling (parse release dates)
- Statistics (correlation, aggregations)
- Matplotlib (multiple chart types)
- File I/O

**Deliverable:** Report analitico professionale + grafici

---

## SECTION 6 — VISUALIZATION

### 6.1 Matplotlib Basics

**Esercizio 6.1** - Basic plots
- Line: temperature nel tempo
- Bar: vendite per categoria
- Scatter: correlazione tra variabili

**Esercizio 6.2** - Subplots
- Crea dashboard con 4 grafici
- Titoli, labels, legend

---

### 🚀 MINI PROJECT 6 — EXTEND PROJECT 5
**Aggiorna Sales Analytics:**
- Aggiungi 5 grafici al report
- Salva come PNG
- Dashboard visivo

---

## SECTION 7 — BACKEND (FASTAPI + DATABASE)

### 7.1-7.2 FastAPI Basics

**Esercizio 7.1** - Hello API
- Crea API con 3 endpoints:
  - GET /: hello world
  - GET /users: lista users
  - GET /users/{id}: user specifico

**Esercizio 7.2** - POST request
- POST /users: crea user
- Request body validation
- Return created user

**Esercizio 7.3** - Query params
- GET /search?q=term&limit=10
- Filtra risultati
- Pagination

---

### 7.3 Database

**Esercizio 7.4** - SQLite basics
- Crea DB, tabella users
- CRUD operations (raw SQL)
- Query con JOIN

**Esercizio 7.5** - SQLAlchemy ORM
- Definisci modelli (User, Post)
- Relazioni (one-to-many)
- CRUD con ORM

---

### 🚀 MINI PROJECT 7 — TASK API (FULL BACKEND)
**Cosa costruire:**
REST API per todo app:
1. **Endpoints:**
   - GET /tasks (list, with filters)
   - GET /tasks/{id}
   - POST /tasks (create)
   - PUT /tasks/{id} (update)
   - DELETE /tasks/{id}
2. **Database:** SQLite con SQLAlchemy
3. **Validation:** Pydantic models
4. **Error handling:** 404, 400, 500
5. **Testing:** pytest per tutti gli endpoints
6. **Docs:** FastAPI auto-generated (Swagger)

**Skills usate:**
- FastAPI (routing, request/response)
- Database (SQLAlchemy ORM)
- Validation (Pydantic)
- Testing (pytest)
- Async (async def)

**Deliverable:** API funzionante + tests

---

## SECTION 8 — AI WORKFLOW

### 8.1-8.3 Data Pipeline + LLM Integration

**Esercizio 8.1** - ETL pipeline
- Extract: leggi dati da API
- Transform: pulisci, normalizza
- Load: salva in DB
- Idempotent (rieseguibile)

**Esercizio 8.2** - Feature engineering
- Dataset tabellare
- Crea nuove features
- Encoding categorie
- Scaling numeri

**Esercizio 8.3** - LLM API call
- Chiama OpenAI/Anthropic API
- Parse response JSON
- Gestisci rate limits
- Retry logic

---

### 🚀 MINI PROJECT 8 — MOVIE RECOMMENDATION API (AI-POWERED) 🎬🤖
**Cosa costruire:**
API intelligente che raccomanda film:

**Endpoints:**
1. **POST /recommend**
   - Input: `{"liked_movie": "Inception", "mood": "mind-bending"}`
   - Process:
     - Fetcha dettagli film da TMDB
     - Chiama LLM: "Perché piace Inception? Cosa cerca l'utente?"
     - Cerca film simili (TMDB API + LLM reasoning)
     - Ranking intelligente (combina rating TMDB + LLM score)
   - Output: Top 5 raccomandazioni con spiegazione

2. **GET /history**
   - Lista ricerche passate (salva in DB)

3. **POST /analyze-review**
   - Input: review testuale
   - LLM analizza sentiment + estrae temi
   - Suggerisce film basati su quello che piace

**Features:**
- Cache raccomandazioni (stesso input → stessa risposta)
- Async calls (TMDB + LLM in parallelo)
- Background job: salva tutte le ricerche per future analysis
- Rate limiting (proteggi API key)

**Skills usate:**
- FastAPI (async, background tasks)
- LLM API integration (OpenAI/Anthropic)
- TMDB API integration
- Database (SQLite: salva history)
- Environment variables (API keys)
- Caching strategy
- Error handling robusto

**Deliverable:** API funzionante con AI + docs Swagger

---

## SECTION 9 — ADVANCED TOPICS

### Type Hints + Async + Testing + Logging

**Esercizio 9.1** - Type hints
- Aggiungi type hints a progetti precedenti
- Usa mypy per check

**Esercizio 9.2** - Async basics
- Converti API calls in async
- Chiama 3 APIs in parallelo
- Confronta tempo sync vs async

**Esercizio 9.3** - Testing
- Scrivi pytest per le tue funzioni
- Test edge cases
- Mocking API calls

**Esercizio 9.4** - Logging
- Sostituisci print() con logging
- Diversi livelli (INFO, ERROR)
- Log to file

---

### 🚀 MINI PROJECT 9 — REFACTOR PROJECT 7
**Migliora Task API:**
- ✅ Type hints everywhere
- ✅ Async database queries
- ✅ 90%+ test coverage
- ✅ Logging invece di print
- ✅ Environment config (.env)

**Deliverable:** Production-ready API

---

## SECTION 10 — FINAL PROJECT (PORTFOLIO PIECE)

### 🏆 FINAL PROJECT — CINEMATIC: MOVIE INTELLIGENCE PLATFORM 🎬🚀

**Cosa costruire:**
Sistema completo per cinefili con 3 componenti integrati:

---

**1. DATA COLLECTOR (Background Service)**
Script che gira ogni 24h (cron job o scheduler):
- Fetcha dati da TMDB API:
  - Trending movies/series (daily, weekly)
  - New releases
  - Top rated updates
  - Cast & crew details
- Pulisce e normalizza con Pandas
- Salva in PostgreSQL/SQLite:
  - Tabelle: movies, actors, genres, reviews
  - Relazioni: movie_actors, movie_genres
- Log completo di ogni run

---

**2. CINEMATIC API (FastAPI Backend)**

**Core Endpoints:**
- `GET /movies` - Lista film (filtri: genere, anno, rating, sort)
- `GET /movies/{id}` - Dettagli film + cast
- `GET /actors/{id}` - Attore + filmografia
- `GET /search?q=...` - Search intelligente

**AI Endpoints:**
- `POST /recommend` - AI recommendations (usa LLM + TMDB data)
  - Input: film piaciuti, mood, preferenze
  - Output: top 10 con spiegazioni
- `POST /analyze-review` - Sentiment analysis recensione
- `POST /chat` - Chat con AI su film ("Chi ha diretto Inception?")

**User Features:**
- `POST /watchlist` - Aggiungi a watchlist personale
- `GET /watchlist` - La tua lista
- `POST /rating` - Valuta film
- Auth JWT (login/signup)

**Analytics Endpoints:**
- `GET /stats/trending` - Cosa guardano gli utenti
- `GET /stats/top-rated` - Best rated this month
- `GET /insights/{genre}` - Insights per genere

**Tech specs:**
- Async tutto (database, external APIs)
- Pydantic models per validation
- Error handling robusto (4xx, 5xx)
- Rate limiting (proteggi LLM API)
- Cache Redis (opzionale, o in-memory)
- Background tasks per operazioni pesanti

---

**3. ANALYTICS DASHBOARD (Report Generator)**
Script mensile che genera report:
- **Statistiche generali:**
  - Top 20 film del mese (rating, views)
  - Generi in crescita
  - Attori trending
- **User insights:**
  - Film più aggiunti a watchlist
  - Rating distribution
  - Pattern temporali (quando guardano film)
- **AI performance:**
  - Accuracy raccomandazioni (user feedback)
  - Query più comuni
- **Export:**
  - PDF report con grafici (matplotlib + reportlab)
  - JSON data export
  - Email digest (optional: SendGrid API)

---

**DATABASE SCHEMA (SQLAlchemy ORM):**
```
movies
  - id, title, release_date, runtime, budget, revenue
  - overview, poster_path, backdrop_path
  - tmdb_id, imdb_id

actors
  - id, name, profile_path, tmdb_id

genres
  - id, name

movie_actors (many-to-many)
  - movie_id, actor_id, character_name, order

movie_genres (many-to-many)
  - movie_id, genre_id

users
  - id, email, hashed_password, created_at

watchlist
  - user_id, movie_id, added_at

ratings
  - user_id, movie_id, score, review_text, created_at

recommendations_log
  - user_id, input_data, recommendations, created_at
```

---

**REQUISITI TECNICI:**
✅ Type hints ovunque
✅ Async operations (DB queries, API calls)
✅ Tests pytest (80%+ coverage):
  - Unit tests (funzioni pure)
  - Integration tests (API endpoints)
  - Mock external APIs (TMDB, LLM)
✅ Logging (logging module, diversi livelli)
✅ Environment config (.env file)
✅ Docker Compose:
  - Service 1: API (FastAPI)
  - Service 2: Database (PostgreSQL)
  - Service 3: Redis (cache, optional)
✅ CI/CD basic (GitHub Actions: run tests)
✅ README professionale:
  - Setup instructions
  - API documentation
  - Architecture diagram
  - Screenshots

**BONUS (portfolio wow-factor):**
- Frontend semplice (HTML/JS che chiama API)
- Deploy su Railway/Render (free tier)
- Demo video (2 min)
- Grafana dashboard (monitoring, optional)

---

**SKILLS USATE:**
🎯 Tutto quello che hai imparato:
- Core Python (data structures, functions, comprehensions)
- File I/O + JSON
- OOP (models, classes)
- NumPy + Pandas (data cleaning, analytics)
- FastAPI (routing, async, validation)
- Database (SQLAlchemy ORM, relations, queries)
- LLM API integration
- External APIs (TMDB)
- Testing (pytest, mocking)
- Type hints
- Async/await
- Logging
- Docker

---

**DELIVERABLE:**
📦 Repository GitHub con:
- `/api` - FastAPI app
- `/collector` - Data collector script
- `/analytics` - Report generator
- `/tests` - Test suite
- `docker-compose.yml`
- `README.md` completo
- `requirements.txt`
- `.env.example`

🚀 **Live demo** (deployed) + **video walkthrough**

💼 **Portfolio killer** → mostra in ogni colloquio

---

## TIMELINE PRATICA

**Week 1-2:** Section 1 + Mini Project 1 (Data Processor)
**Week 3:** Section 2 + Mini Project 2 🎬 (Movie Data Collector)
**Week 4:** Section 3 + Mini Project 3 (Todo App OOP)
**Week 5:** Section 5 + Mini Project 5 🎬 (Movie Analytics Dashboard)
**Week 6:** Section 7 + Mini Project 7 (Task API)
**Week 7:** Section 8 + Mini Project 8 🎬 (Movie Recommendation AI)
**Week 8:** Section 9 + Final Project 🎬🚀 (CINEMATIC Platform)

**Totale: 8 settimane → Job ready + Portfolio cinematografico**

---

## COME USARE QUESTO PIANO

1. **Ogni giorno:**
   - 1-2 esercizi mirati (1h)
   - Lavora su mini-progetto in corso (1h)

2. **Fine sezione:**
   - Completa mini-progetto
   - Push su GitHub
   - LinkedIn post (optional)

3. **Non bloccarti:**
   - Se esercizio prende >30min, chiedi hint
   - Obiettivo: FARE, non perfezionare

4. **Portfolio finale:**
   - 10 mini-progetti + 1 final project
   - Tutti su GitHub con README
   - Mostra durante colloqui

---

## COSA HAI ALLA FINE

✅ **10+ progetti funzionanti su GitHub**
✅ **Full-stack capability** (data + backend + API + AI)
✅ **LLM integration experience** (raccomandazioni intelligenti)
✅ **Testing + best practices** (production-ready code)
✅ **Portfolio UNICO** con tema cinematografico (ti distingui)
✅ **1 progetto finale impressive** (CINEMATIC Platform)

**Progetti cinema nel portfolio:**
- 🎬 Movie Data Collector (API integration)
- 🎬 Movie Analytics Dashboard (Pandas + viz)
- 🎬 AI Movie Recommendations (LLM + FastAPI)
- 🎬 CINEMATIC Platform (full-stack, deploy live)

**Sei pronto per:** Junior/Mid Python Developer (AI/Data/Backend)

**Plus:** In colloqui puoi parlare di qualcosa che ti appassiona → più naturale, più credibile
