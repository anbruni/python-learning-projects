# HTTP Requests in Python — libreria `requests`

> Fare chiamate HTTP in Python: GET, status codes, headers, query params.
> Confronto diretto con `fetch` in JavaScript.

## Table of Contents
1. [Installazione e import](#installazione-e-import)
2. [requests.get() — la chiamata base](#requestsget--la-chiamata-base)
3. [L'oggetto Response](#loggetto-response)
4. [Status codes](#status-codes)
5. [Query params — params={}](#query-params--params)
6. [Request headers — headers={}](#request-headers--headers)
7. [raise_for_status() — errori automatici](#raise_for_status--errori-automatici)
8. [Confronto con fetch JS](#confronto-con-fetch-js)
9. [Pattern reali](#pattern-reali)
10. [Quick Reference](#quick-reference)

---

## Installazione e import

`requests` non è nella stdlib — va installata nel venv del progetto:

```bash
# Nel venv attivo
pip install requests
pip freeze > requirements.txt   # salva la dipendenza
```

```python
import requests
```

---

## requests.get() — la chiamata base

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)   # 200
print(response.json())        # {"userId": 1, "id": 1, "title": "...", "body": "..."}
```

`requests.get()` è **sincrono** — il codice aspetta la risposta prima di continuare.
(Per HTTP asincrono in Python si usa `httpx` o `aiohttp` — argomento avanzato.)

---

## L'oggetto Response

```python
response = requests.get("https://api.example.com/movies/1")

# Corpo della risposta
response.json()         # dict o list — parsa il JSON (come json.loads(response.text))
response.text           # str — corpo raw come stringa
response.content        # bytes — corpo raw come bytes (per file binari)

# Metadati
response.status_code    # int — codice HTTP: 200, 404, 500, ...
response.headers        # dict-like — headers della risposta
response.url            # str — URL finale (dopo redirect)

# Shortcut
response.ok             # bool — True se status_code < 400
```

**Attenzione:** `response.json()` lancia `json.JSONDecodeError` se il corpo non è JSON valido.
Controlla sempre `response.status_code` prima di chiamare `.json()`.

---

## Status codes

| Codice | Nome | Significato |
|--------|------|-------------|
| `200` | OK | Successo — hai i dati |
| `201` | Created | Risorsa creata (POST) |
| `204` | No Content | Successo ma nessun corpo (DELETE) |
| `400` | Bad Request | Richiesta malformata — controlla i params |
| `401` | Unauthorized | Non autenticato — manca o è invalido il token |
| `403` | Forbidden | Autenticato ma non hai i permessi |
| `404` | Not Found | La risorsa non esiste |
| `422` | Unprocessable Entity | Dati validi ma logica fallisce (spesso nelle API REST) |
| `429` | Too Many Requests | Rate limit superato — aspetta prima di riprovare |
| `500` | Internal Server Error | Bug sul server — non dipende da te |
| `503` | Service Unavailable | Server temporaneamente down |

```python
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
elif response.status_code == 404:
    print("Risorsa non trovata")
elif response.status_code == 401:
    print("Controlla l'API key")
else:
    print(f"Errore {response.status_code}")
```

---

## Query params — params={}

I query params sono le variabili dopo il `?` nell'URL: `url?key=val&key2=val2`

```python
# MAI costruire l'URL a mano — requests lo fa per te
# SBAGLIATO:
url = f"https://api.example.com/movies?language=it&page=1"

# CORRETTO: passa un dict, requests costruisce l'URL
response = requests.get(
    "https://api.example.com/movies",
    params={"language": "it", "page": 1}
)
# URL effettivo: https://api.example.com/movies?language=it&page=1
print(response.url)   # mostra l'URL completo costruito da requests
```

**Params opzionali:**
```python
def search_movies(query: str, page: int = 1, language: str | None = None):
    params = {"query": query, "page": page}
    if language is not None:
        params["language"] = language
    return requests.get("https://api.themoviedb.org/3/search/movie", params=params)
```

**JS comparison:**
```javascript
// Con URLSearchParams
const params = new URLSearchParams({ query: "inception", page: 1 })
fetch(`https://api.example.com/search?${params}`)

// O con librerie come axios:
axios.get("https://api.example.com/search", { params: { query: "inception" } })
```

---

## Request headers — headers={}

Gli headers HTTP trasmettono metadati della richiesta: autenticazione, formato accettato, identità del client.

```python
response = requests.get(
    "https://api.example.com/movies",
    headers={
        "Accept": "application/json",          # tipo di risposta attesa
        "User-Agent": "MovieApp/1.0",           # chi fa la richiesta
        "Authorization": "Bearer my_api_token", # autenticazione
    }
)
```

**Headers comuni:**

| Header | Significato | Esempio |
|--------|-------------|---------|
| `Accept` | Formato di risposta atteso | `"application/json"` |
| `Authorization` | Credenziali di autenticazione | `"Bearer TOKEN"` |
| `User-Agent` | Identità del client | `"MovieApp/1.0"` |
| `Content-Type` | Tipo del corpo inviato (POST/PUT) | `"application/json"` |
| `X-Api-Key` | API key (alcuni provider la vogliono in header) | `"abc123"` |

**Aggiungere headers condizionalmente:**
```python
def build_headers(token: str | None = None) -> dict:
    headers = {
        "Accept": "application/json",
        "User-Agent": "MovieApp/1.0",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

response = requests.get(url, headers=build_headers(token="my_token"))
```

**Verificare gli headers inviati con httpbin:**
```python
# httpbin.org/get echoes back la tua richiesta — ottimo per debugging
response = requests.get(
    "https://httpbin.org/get",
    headers={"Authorization": "Bearer test", "User-Agent": "MyApp/1.0"}
)
print(response.json()["headers"])
# → {"Authorization": "Bearer test", "User-Agent": "MyApp/1.0", ...}
```

---

## raise_for_status() — errori automatici

Invece di controllare `status_code` manualmente, puoi usare `raise_for_status()`:

```python
response = requests.get(url)
response.raise_for_status()   # lancia HTTPError se status >= 400
data = response.json()
```

```python
import requests

try:
    response = requests.get("https://api.example.com/movies/999")
    response.raise_for_status()       # lancia se 4xx o 5xx
    data = response.json()
except requests.HTTPError as e:
    print(f"HTTP error: {e.response.status_code} — {e}")
except requests.ConnectionError:
    print("Impossibile connettersi al server")
except requests.Timeout:
    print("Richiesta scaduta")
```

**Quando usare raise_for_status():**
- Quando un errore HTTP è un errore fatale (non puoi continuare senza i dati)
- Quando vuoi lasciare che l'eccezione propaghi in alto

**Quando NON usarlo:**
- Quando 404 è un caso normale ("risorsa non trovata" → return None)
- Quando vuoi gestire diversamente 401 vs 404 vs 500

---

## Confronto con fetch JS

```javascript
// JavaScript — asincrono, richiede await
async function fetchMovie(id) {
    const res = await fetch(`https://api.example.com/movies/${id}`)
    if (!res.ok) return null
    return await res.json()   // due await: uno per fetch, uno per .json()
}
```

```python
# Python — sincrono, più lineare
def fetch_movie(movie_id: int) -> dict | None:
    response = requests.get(f"https://api.example.com/movies/{movie_id}")
    if response.status_code != 200:
        return None
    return response.json()   # un solo passaggio
```

| | JavaScript `fetch` | Python `requests` |
|--|-------------------|------------------|
| Async | ✅ Sì (await) | ❌ No (sincrono) |
| Query params | URLSearchParams o manuale | `params={}` dict |
| Headers | `{ headers: {...} }` | `headers={}` dict |
| Parsare JSON | `await res.json()` | `response.json()` |
| Status code | `res.ok`, `res.status` | `response.ok`, `response.status_code` |
| Installazione | Built-in browser/Node | `pip install requests` |

---

## Pattern reali

### Chiamata base con controllo errore

```python
def get_movie(movie_id: int) -> dict | None:
    response = requests.get(f"https://api.example.com/movies/{movie_id}")
    if response.status_code == 200:
        return response.json()
    return None
```

### Chiamata con params e headers

```python
def search_movies(query: str, api_key: str, language: str = "en-US") -> list[dict]:
    response = requests.get(
        "https://api.themoviedb.org/3/search/movie",
        params={"query": query, "language": language, "page": 1},
        headers={"Authorization": f"Bearer {api_key}"},
    )
    response.raise_for_status()
    return response.json().get("results", [])
```

### Timeout — non lasciare mai la richiesta senza

```python
# Senza timeout il codice può bloccarsi per sempre se il server non risponde
response = requests.get(url, timeout=10)      # 10 secondi max
# oppure
response = requests.get(url, timeout=(3, 10)) # (connect_timeout, read_timeout)
```

> Aggiungi sempre `timeout=` alle chiamate HTTP in produzione.
> Il valore di default è `None` — aspetta per sempre.

---

## Quick Reference

```python
import requests

# GET base
response = requests.get("https://api.example.com/movies/1")
data = response.json()              # dict/list
status = response.status_code       # 200, 404, ...

# GET con query params
response = requests.get(url, params={"query": "inception", "page": 1})
print(response.url)                 # mostra l'URL costruito

# GET con headers
response = requests.get(url, headers={
    "Authorization": "Bearer TOKEN",
    "Accept": "application/json",
})

# GET con timeout
response = requests.get(url, timeout=10)

# Controllo errori
if response.status_code == 200:
    data = response.json()
elif response.status_code == 404:
    data = None

# oppure
response.raise_for_status()        # HTTPError se 4xx/5xx
data = response.json()
```
