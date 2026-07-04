# API Error Handling in Python

> Gestire timeout, JSON invalido, status codes e retry — i pattern che ogni
> applicazione che chiama API esterne deve implementare.

## Table of Contents
1. [Gerarchia eccezioni di requests](#gerarchia-eccezioni-di-requests)
2. [Timeout](#timeout)
3. [JSONDecodeError — risposta non JSON](#jsondecodeerror--risposta-non-json)
4. [4xx vs 5xx — client error vs server error](#4xx-vs-5xx--client-error-vs-server-error)
5. [Transient vs Permanent — quando fare retry](#transient-vs-permanent--quando-fare-retry)
6. [Retry pattern](#retry-pattern)
7. [Pattern completo — il fetch robusto](#pattern-completo--il-fetch-robusto)
8. [Quick Reference](#quick-reference)

---

## Gerarchia eccezioni di requests

```
requests.exceptions.RequestException   ← base — cattura tutto
├── ConnectionError                     ← server irraggiungibile, DNS fail, reset
├── Timeout                             ← richiesta troppo lenta
│   ├── ConnectTimeout                  ← timeout durante la connessione
│   └── ReadTimeout                     ← connesso ma server non risponde
├── HTTPError                           ← lanciato da raise_for_status() su 4xx/5xx
└── TooManyRedirects                    ← troppi redirect (loop)
```

```python
import requests

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.Timeout:
    print("Richiesta troppo lenta")
except requests.ConnectionError:
    print("Impossibile connettersi")
except requests.HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")
except requests.RequestException as e:
    print(f"Errore generico: {e}")   # fallback per tutto il resto
```

> **Regola:** cattura prima le eccezioni specifiche, poi le generiche.
> `RequestException` come ultima riga cattura qualsiasi cosa sfugga.

---

## Timeout

Senza timeout, una richiesta può bloccare il programma per sempre.

```python
# Timeout singolo — stesso valore per connect e read
response = requests.get(url, timeout=10)

# Timeout doppio — (connect_timeout, read_timeout)
response = requests.get(url, timeout=(3, 10))
# connect: max 3s per stabilire la connessione
# read:    max 10s per ricevere la risposta completa
```

```python
def fetch_with_timeout(url: str, seconds: float) -> dict | None:
    try:
        response = requests.get(url, timeout=seconds)
        return response.json()
    except requests.Timeout:
        print(f"Timeout dopo {seconds}s: {url}")
        return None
```

**Valori comuni:**
| Contesto | Connect | Read |
|----------|---------|------|
| API veloci (ricerca, dati) | 3s | 10s |
| API lente (elaborazione, AI) | 5s | 60s |
| Download file grandi | 5s | 300s |

**JS comparison:**
```javascript
// fetch non ha timeout nativo — richiede AbortController
const controller = new AbortController()
const id = setTimeout(() => controller.abort(), 5000)
const res = await fetch(url, { signal: controller.signal })
clearTimeout(id)

// axios ha timeout diretto (più simile a requests)
axios.get(url, { timeout: 5000 })
```

---

## JSONDecodeError — risposta non JSON

Un server può rispondere con status 200 ma con body non JSON (HTML di errore,
testo plain, ecc.). Chiamare `.json()` senza protezione causa un crash.

```python
import requests

response = requests.get("https://httpbin.org/html")   # risponde con HTML
response.json()   # JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

```python
def safe_json_fetch(url: str) -> dict | None:
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None
        return response.json()
    except requests.exceptions.JSONDecodeError:
        # requests.exceptions.JSONDecodeError è un alias di json.JSONDecodeError
        return None
```

**Quando si verifica:**
- Server in errore che risponde con pagina HTML invece di JSON
- API che restituisce testo plain per certi endpoint
- Risposta vuota (status 204 No Content)
- Bug del server che manda JSON malformato

---

## 4xx vs 5xx — client error vs server error

```python
response = requests.get(url, timeout=10)
code = response.status_code

if code == 200:
    data = response.json()
elif 400 <= code < 500:
    # Errore CLIENT — colpa della richiesta
    # 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found
    print(f"Errore client {code} — controlla la richiesta")
elif 500 <= code < 600:
    # Errore SERVER — il server ha un problema
    # 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable
    print(f"Errore server {code} — riprova più tardi")
```

**`400 <= code < 500` è un range check Python** — equivale a `code >= 400 and code < 500`.
Molto più leggibile che elencare ogni singolo codice.

### raise_for_status() — alternativa compatta

```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()   # lancia HTTPError se status >= 400
    return response.json()
except requests.HTTPError as e:
    code = e.response.status_code
    if 400 <= code < 500:
        print(f"Client error: {code}")
    else:
        print(f"Server error: {code}")
    return None
```

**Quando usare quale approccio:**

| Approccio | Quando |
|-----------|--------|
| `raise_for_status()` | Quando qualsiasi errore HTTP è fatale — vuoi che propaghi |
| Check manuale `status_code` | Quando tratti diversamente 4xx vs 5xx vs 200 |

---

## Transient vs Permanent — quando fare retry

La regola fondamentale del retry:

```
RIPROVA su errori TRANSITORI (il problema potrebbe risolversi da solo):
    ✓ requests.Timeout         → server sovraccarico, rete lenta
    ✓ requests.ConnectionError → connessione caduta momentaneamente
    ✓ 5xx (500, 502, 503)      → server in difficoltà temporanea
    ✓ 429 Too Many Requests    → rate limit — aspetta e riprova

NON RIPROVARE su errori PERMANENTI (il retry è inutile):
    ✗ 400 Bad Request          → la richiesta è sbagliata — non cambierà
    ✗ 401 Unauthorized         → manca il token — prima autenticati
    ✗ 403 Forbidden            → non hai i permessi — non cambia con il retry
    ✗ 404 Not Found            → la risorsa non esiste — non apparirà
```

---

## Retry pattern

### Retry semplice

```python
import time
import requests

def fetch_with_retry(url: str, max_retries: int = 3, delay: float = 1.0) -> dict | None:
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                return response.json()

            if 400 <= response.status_code < 500:
                return None             # errore permanente — non riprovare

            # 5xx → fall through e riprova

        except (requests.Timeout, requests.ConnectionError):
            pass                        # errore transitorio → riprova

        if attempt < max_retries:
            print(f"Tentativo {attempt}/{max_retries} fallito, riprovo tra {delay}s...")
            time.sleep(delay)

    return None
```

### Exponential backoff (produzione)

In produzione il delay raddoppia a ogni tentativo per non bombardare un server già in difficoltà:

```python
def fetch_with_backoff(url: str, max_retries: int = 3) -> dict | None:
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as e:
            if attempt == max_retries - 1:
                return None
            wait = 2 ** attempt         # 1s, 2s, 4s, 8s...
            print(f"Tentativo {attempt + 1} fallito, riprovo tra {wait}s")
            time.sleep(wait)
    return None
```

**JS comparison:**
```javascript
// In JS non c'è un retry built-in — si usa lo stesso loop manuale
async function fetchWithRetry(url, maxRetries = 3, delay = 1000) {
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
        try {
            const res = await fetch(url)
            if (res.ok) return await res.json()
            if (res.status >= 400 && res.status < 500) return null
        } catch (e) {
            if (attempt === maxRetries) return null
        }
        await new Promise(r => setTimeout(r, delay))
    }
    return null
}
```

---

## Pattern completo — il fetch robusto

```python
import time
import requests

def robust_fetch(url: str, max_retries: int = 3) -> dict | None:
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=(3, 10))

            # Errori permanenti — non riprovare
            if 400 <= response.status_code < 500:
                return None

            response.raise_for_status()   # lancia su altri errori HTTP
            return response.json()

        except requests.Timeout:
            print(f"Timeout (tentativo {attempt}/{max_retries})")
        except requests.ConnectionError:
            print(f"Connessione fallita (tentativo {attempt}/{max_retries})")
        except requests.HTTPError:
            pass   # 5xx — riprova
        except requests.exceptions.JSONDecodeError:
            return None   # risposta non JSON — non ha senso riprovare

        if attempt < max_retries:
            time.sleep(2 ** (attempt - 1))   # backoff: 1s, 2s, 4s

    return None
```

---

## Quick Reference

```python
import time
import requests

# Timeout — sempre
response = requests.get(url, timeout=(3, 10))

# Catch specifici
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.Timeout:
    data = None
except requests.ConnectionError:
    data = None
except requests.HTTPError as e:
    print(e.response.status_code)
    data = None
except requests.exceptions.JSONDecodeError:
    data = None

# Range check status codes
if 400 <= code < 500:   # client error
    ...
if 500 <= code < 600:   # server error
    ...

# Retry base
for attempt in range(1, max_retries + 1):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        if 400 <= response.status_code < 500:
            return None       # permanente — stop
    except (requests.Timeout, requests.ConnectionError):
        pass                  # transitorio — riprova
    if attempt < max_retries:
        time.sleep(delay)
return None
```
