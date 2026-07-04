# Environment Variables in Python

> Gestire la configurazione sensibile con variabili d'ambiente, file `.env`
> e la libreria `python-dotenv`.

## Table of Contents
1. [Perché le variabili d'ambiente](#perché-le-variabili-dambiente)
2. [Il file .env](#il-file-env)
3. [.env vs .env.example](#env-vs-envexample)
4. [.gitignore — mai committare .env](#gitignore--mai-committare-env)
5. [python-dotenv — caricare il .env](#python-dotenv--caricare-il-env)
6. [os.getenv vs os.environ](#osgetenv-vs-osenviron)
7. [Tipi — tutto è stringa](#tipi--tutto-è-stringa)
8. [Pattern: config da env vars](#pattern-config-da-env-vars)
9. [Confronto con JavaScript](#confronto-con-javascript)
10. [Quick Reference](#quick-reference)

---

## Perché le variabili d'ambiente

**Non fare questo:**
```python
# app.py
API_KEY = "sk-abc123xyz789"          # la chiave è nel codice
BASE_URL = "https://api.tmdb.org/3"  # e nel git history — per sempre
```

**Fare questo:**
```python
# app.py
API_KEY = os.getenv("TMDB_API_KEY")   # la chiave vive solo nella macchina
BASE_URL = os.getenv("TMDB_BASE_URL")
```

Le variabili d'ambiente separano la **configurazione** dal **codice**:
- Il codice va su GitHub → visibile a tutti
- Le chiavi restano sulla macchina (o nei secret del server) → private

---

## Il file .env

Un semplice file di testo — una variabile per riga:

```bash
# Commento — ignora questa riga
APP_API_KEY=sk-abc123xyz
APP_BASE_URL=https://api.themoviedb.org/3
APP_MAX_RESULTS=20
APP_DEBUG=false
APP_LANGUAGE=it-IT
```

**Regole di formato:**
- Nessuno spazio intorno a `=` → `KEY=value`, non `KEY = value`
- I valori sono sempre **stringhe** — anche numeri e booleani
- Righe che iniziano con `#` sono commenti
- Valori con spazi vanno tra virgolette: `APP_NAME="Movie App"`

---

## .env vs .env.example

| File | Commitato? | Contiene |
|------|-----------|----------|
| `.env` | ❌ No — in `.gitignore` | Valori reali (chiavi, password) |
| `.env.example` | ✅ Sì | Template vuoto, solo nomi delle variabili |

**Workflow tipico:**
```bash
git clone progetto
cp .env.example .env        # crea il tuo .env personale
# apri .env e inserisci le tue chiavi reali
python app.py
```

**Contenuto .env.example:**
```bash
# Copia questo file in .env e inserisci i tuoi valori
# NON committare il file .env

APP_API_KEY=la_tua_api_key_qui
APP_BASE_URL=https://api.themoviedb.org/3
APP_MAX_RESULTS=20
APP_LANGUAGE=en-US
```

---

## .gitignore — mai committare .env

```gitignore
# .gitignore
.env
.env.local
.env.production
```

Se committiamo per sbaglio una chiave API, rimane nella git history anche
dopo averla rimossa. L'unica soluzione è revocare la chiave e generarne una nuova.

**Verifica che .env sia ignorato:**
```bash
git status           # .env non deve apparire come "untracked"
git check-ignore -v .env   # → .gitignore:2:.env  .env  (ignorato)
```

---

## python-dotenv — caricare il .env

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
import os

load_dotenv()                          # cerca .env nella cartella corrente
load_dotenv("/path/to/.env")           # percorso esplicito
load_dotenv(override=True)            # sovrascrive vars già nell'ambiente

# Ora os.getenv funziona con i valori del .env
api_key = os.getenv("APP_API_KEY")
```

**Comportamento:**
- `load_dotenv()` carica le variabili nel processo corrente (`os.environ`)
- Per default, **non sovrascrive** variabili già impostate nel sistema
  (utile in produzione dove le vars di sistema hanno precedenza sul .env)
- Ritorna `True` se il file è stato trovato, `False` altrimenti

**Dove chiamarlo:**
```python
# All'inizio del programma, prima di usare os.getenv
from dotenv import load_dotenv
load_dotenv()

# poi ovunque nel codice
api_key = os.getenv("APP_API_KEY")
```

---

## os.getenv vs os.environ

```python
import os

# os.getenv — sicuro, non crasha
os.getenv("APP_KEY")              # → None se mancante
os.getenv("APP_KEY", "default")   # → "default" se mancante

# os.environ — dizionario diretto
os.environ["APP_KEY"]             # → KeyError se mancante  ← pericoloso
os.environ.get("APP_KEY")         # → None se mancante (equivalente a getenv)
os.environ.get("APP_KEY", "def")  # → "def" se mancante

# Impostare una variabile (solo nel processo corrente)
os.environ["APP_KEY"] = "valore"
```

**Quando usare cosa:**
| Situazione | Usa |
|-----------|-----|
| Variabile opzionale con default | `os.getenv("KEY", "default")` |
| Variabile obbligatoria | `os.getenv("KEY")` + raise se None |
| Debug: lista tutte le vars | `dict(os.environ)` |

---

## Tipi — tutto è stringa

Tutti i valori letti da env vars (e dal .env) sono **stringhe**.
Devi convertire tu i tipi.

```python
# .env contiene: APP_MAX_RESULTS=20 e APP_DEBUG=false

# SBAGLIATO — "20" non è 20
max_results = os.getenv("APP_MAX_RESULTS")    # → "20"  (stringa!)
limit = max_results + 5                        # TypeError!

# CORRETTO — converti al tipo giusto
max_results = int(os.getenv("APP_MAX_RESULTS", "10"))   # → 20  (int)

# Booleani — non esiste bool("false") == False in Python
# bool("false") → True  ← perché "false" è una stringa non vuota!

# SBAGLIATO:
debug = bool(os.getenv("APP_DEBUG"))   # → True anche se il valore è "false"!

# CORRETTO — confronto esplicito con la stringa
debug = os.getenv("APP_DEBUG", "false") == "true"   # → False ✓
debug = os.getenv("APP_DEBUG", "false").lower() in ("true", "1", "yes")  # più robusto
```

---

## Pattern: config da env vars

```python
import os
from dotenv import load_dotenv

def build_config() -> dict:
    """Carica e valida la configurazione dalle variabili d'ambiente."""
    load_dotenv()

    # Variabili obbligatorie — raise se mancanti
    api_key = os.getenv("APP_API_KEY")
    base_url = os.getenv("APP_BASE_URL")
    if not api_key:
        raise ValueError("Missing required environment variable: APP_API_KEY")
    if not base_url:
        raise ValueError("Missing required environment variable: APP_BASE_URL")

    return {
        "api_key":     api_key,
        "base_url":    base_url,
        "max_results": int(os.getenv("APP_MAX_RESULTS", "20")),
        "language":    os.getenv("APP_LANGUAGE", "en-US"),
        "debug":       os.getenv("APP_DEBUG", "false") == "true",
    }
```

**Helper per variabili obbligatorie:**
```python
def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value
```

---

## Confronto con JavaScript

```javascript
// Node.js — stesso concetto, pacchetto dotenv
require('dotenv').config()                // carica il .env
// oppure con ES modules:
import 'dotenv/config'

const apiKey = process.env.APP_API_KEY    // string | undefined
const maxResults = parseInt(process.env.APP_MAX_RESULTS || "20")
const debug = process.env.APP_DEBUG === "true"
```

```python
# Python
from dotenv import load_dotenv
import os

load_dotenv()                             # carica il .env

api_key = os.getenv("APP_API_KEY")       # str | None
max_results = int(os.getenv("APP_MAX_RESULTS", "20"))
debug = os.getenv("APP_DEBUG", "false") == "true"
```

| | JavaScript | Python |
|--|-----------|--------|
| Load .env | `require('dotenv').config()` | `load_dotenv()` |
| Leggi variabile | `process.env.KEY` | `os.getenv("KEY")` |
| Con default | `process.env.KEY \|\| "def"` | `os.getenv("KEY", "def")` |
| Variabile mancante | `undefined` | `None` |
| Tutti i valori | stringhe | stringhe |

---

## Quick Reference

```python
from dotenv import load_dotenv
import os

# Carica il .env (all'inizio del programma)
load_dotenv()                                  # cerca .env nella dir corrente
load_dotenv("/path/to/.env")                   # percorso esplicito

# Leggi variabili
value = os.getenv("KEY")                       # str | None
value = os.getenv("KEY", "default")            # str con default
value = os.environ["KEY"]                      # str | KeyError

# Converti tipi
n = int(os.getenv("MAX_RESULTS", "10"))        # int
flag = os.getenv("DEBUG", "false") == "true"   # bool

# Helper obbligatoria
def get_required_env(name: str) -> str:
    v = os.getenv(name)
    if not v:
        raise ValueError(f"Missing required environment variable: {name}")
    return v

# Pattern completo
load_dotenv()
config = {
    "api_key":  get_required_env("APP_API_KEY"),
    "base_url": get_required_env("APP_BASE_URL"),
    "limit":    int(os.getenv("APP_MAX_RESULTS", "20")),
    "debug":    os.getenv("APP_DEBUG", "false") == "true",
}
```
