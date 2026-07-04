# API Pagination in Python

> Scorrere più pagine di risultati da un'API: tipi di pagination,
> stop conditions e accumulation pattern.

## Table of Contents
1. [Perché la pagination esiste](#perché-la-pagination-esiste)
2. [Tipi di pagination](#tipi-di-pagination)
3. [Page-based pagination — il pattern base](#page-based-pagination--il-pattern-base)
4. [Stop conditions](#stop-conditions)
5. [Accumulation pattern — .extend() vs .append()](#accumulation-pattern--extend-vs-append)
6. [Fetch until count](#fetch-until-count)
7. [Filtrare + paginare nella stessa chiamata](#filtrare--paginare-nella-stessa-chiamata)
8. [X-Total-Count header](#x-total-count-header)
9. [Confronto con JavaScript](#confronto-con-javascript)
10. [Quick Reference](#quick-reference)

---

## Perché la pagination esiste

Un endpoint tipo `GET /movies` potrebbe restituire migliaia di film.
Mandare tutto in una risposta è:
- **lento** — serializzare 50.000 record richiede tempo
- **costoso** — consuma banda del server e del client
- **rischioso** — può andare in timeout o esaurire la memoria

La soluzione: il server divide i risultati in "pagine" e manda una pagina
per volta. Il client cicla sulle pagine finché non ha quello che serve.

---

## Tipi di pagination

### Page-based (più comune nelle REST API semplici)

```
GET /posts?_page=1&_limit=10   → elementi 1–10
GET /posts?_page=2&_limit=10   → elementi 11–20
GET /posts?_page=3&_limit=10   → elementi 21–30
```

Parametri: numero di pagina + dimensione pagina.
Usato da JSONPlaceholder, molte API pubbliche.

### Offset-based (variante della page-based)

```
GET /posts?_start=0&_limit=10   → elementi 0–9
GET /posts?_start=10&_limit=10  → elementi 10–19
```

Relazione con page-based: `_start = (page - 1) * limit`
Usato da JSONPlaceholder (supporta entrambi).

### Cursor-based (più robusto, usato da API moderne)

```
GET /movies                          → risposta include "next_cursor": "eyJpZCI6MTB9"
GET /movies?cursor=eyJpZCI6MTB9      → risposta include "next_cursor": "eyJpZCI6MjB9"
GET /movies?cursor=eyJpZCI6MjB9      → risposta include "next_cursor": null  → stop
```

Il "cursore" è un token opaco (spesso base64 di un ID o timestamp) che
punta esattamente a dove siamo nella lista — non risente di inserimenti/
cancellazioni concorrenti. Usato da TMDB, GitHub API, Meta Graph API.

---

## Page-based pagination — il pattern base

```python
import requests

def fetch_all(url: str, per_page: int = 10) -> list[dict]:
    all_results = []
    page = 1

    while True:
        response = requests.get(
            url,
            params={"_page": page, "_limit": per_page},
            timeout=10
        )
        if response.status_code != 200:
            break

        data = response.json()
        if not data:          # lista vuota = non ci sono più pagine
            break

        all_results.extend(data)
        page += 1

    return all_results
```

Il loop continua finché `data` è vuoto o c'è un errore HTTP.

---

## Stop conditions

### 1. Pagina vuota (la più comune)

```python
data = response.json()
if not data:   # [] è falsy → True quando la lista è vuota
    break
```

Quando l'API non ha più elementi, risponde con `[]`.
`not []` → `True`, quindi il break scatta.

### 2. Max pages (protezione di sicurezza)

```python
MAX_PAGES = 100
page = 1

while page <= MAX_PAGES:
    ...
    page += 1
```

Evita loop infiniti in caso di bug dell'API che non manda mai `[]`.
Combinalo sempre con la stop condition per pagina vuota.

### 3. Target count (stop appena hai abbastanza)

```python
while len(all_results) < target_count:
    ...
    all_results.extend(data)

return all_results[:target_count]   # taglia esattamente al numero richiesto
```

Utile quando vuoi esattamente N risultati — non tutti.
Lo slice `[:target_count]` è sicuro anche se `len < target_count`.

### 4. No "next" link (cursor-based)

```python
response_data = response.json()
results = response_data.get("results", [])
next_cursor = response_data.get("next_cursor")

all_results.extend(results)

if not next_cursor:
    break
```

Tipico di API cursor-based come TMDB (`"next_page": null` quando finiscono).

---

## Accumulation pattern — .extend() vs .append()

```python
all_results = []

# SBAGLIATO — append aggiunge l'intera lista come un elemento singolo
all_results.append([{"id": 1}, {"id": 2}])
# → [[{"id": 1}, {"id": 2}]]  ← lista di liste, non lista di dict!

# CORRETTO — extend aggiunge ogni elemento individualmente
all_results.extend([{"id": 1}, {"id": 2}])
# → [{"id": 1}, {"id": 2}]   ← lista piatta di dict ✓

# Alternativa equivalente con +=
all_results += [{"id": 1}, {"id": 2}]
```

| Metodo | Cosa fa | Risultato con [1,2] + [3,4] |
|--------|---------|------------------------------|
| `.append([3,4])` | Aggiunge la lista come elemento | `[1, 2, [3, 4]]` |
| `.extend([3,4])` | Aggiunge ogni elemento | `[1, 2, 3, 4]` |
| `+= [3,4]` | Equivalente a extend | `[1, 2, 3, 4]` |

**Regola:** per la pagination usa sempre `.extend()` (o `+=`), mai `.append()`.

---

## Fetch until count

```python
def fetch_until_count(url: str, target_count: int, per_page: int = 10) -> list[dict]:
    all_results = []
    page = 1

    while len(all_results) < target_count:
        response = requests.get(
            url,
            params={"_page": page, "_limit": per_page},
            timeout=10
        )
        data = response.json()
        if not data:
            break                              # non ci sono più pagine

        all_results.extend(data)
        page += 1

    return all_results[:target_count]          # ritaglia esattamente N elementi
```

Lo slice `[:target_count]` funziona anche se `all_results` ha meno elementi
di `target_count` — restituisce tutto quello che c'è senza errori.

---

## Filtrare + paginare nella stessa chiamata

```python
def get_user_posts(user_id: int, per_page: int = 5) -> list[dict]:
    all_posts = []
    page = 1

    while True:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts",
            params={"userId": user_id, "_page": page, "_limit": per_page},
            timeout=10
        )
        data = response.json()
        if not data:
            break
        all_posts.extend(data)
        page += 1

    return all_posts
```

L'API applica il filtro (`userId`) al set completo e poi pagina il risultato
filtrato. `_page=2` con `userId=1&_limit=3` → post 4–6 dell'utente 1,
non post 4–6 di tutti.

---

## X-Total-Count header

Alcune API includono il numero totale di risultati negli header HTTP:

```python
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"_page": 1, "_limit": 10}
)

total = int(response.headers.get("X-Total-Count", 0))
# → 100  (JSONPlaceholder ha 100 posts in totale)

total_pages = (total + 9) // 10   # divisione intera con arrotondamento in su
# → 10  (100 / 10 = 10 pagine)
```

Questo permette di calcolare il numero di pagine in anticipo e mostrare
una progress bar o evitare il loop.

**Attenzione:** non tutte le API includono questo header. Verificalo prima
di dipenderci. Se non c'è, usa la stop condition con pagina vuota.

---

## Confronto con JavaScript

```javascript
// JavaScript — asincrono, spesso con async generator
async function* paginate(url, limit) {
    let page = 1
    while (true) {
        const res = await fetch(`${url}?_page=${page}&_limit=${limit}`)
        const data = await res.json()
        if (!data.length) return
        yield* data          // yield ogni elemento
        page++
    }
}

// Uso:
const allPosts = []
for await (const post of paginate(url, 10)) {
    allPosts.push(post)
}
```

```python
# Python — sincrono, loop diretto, più leggibile
def paginate(url: str, per_page: int) -> list[dict]:
    all_data = []
    page = 1
    while True:
        response = requests.get(url, params={"_page": page, "_limit": per_page}, timeout=10)
        data = response.json()
        if not data:
            break
        all_data.extend(data)
        page += 1
    return all_data
```

| | JavaScript | Python |
|--|-----------|--------|
| Async | ✅ `async/await` | ❌ sincrono (usa `httpx` per async) |
| Accumulation | `push`, spread | `.extend()`, `+=` |
| Stop condition | `!data.length` | `not data` |
| Generator | `yield*` | `yield` (se usi generator) |

---

## Quick Reference

```python
import requests

BASE_URL = "https://api.example.com"

# Accumulare tutte le pagine
def fetch_all(resource: str, per_page: int = 10) -> list[dict]:
    all_results = []
    page = 1
    while True:
        response = requests.get(
            f"{BASE_URL}/{resource}",
            params={"_page": page, "_limit": per_page},
            timeout=10
        )
        data = response.json()
        if not data:
            break
        all_results.extend(data)   # ← extend, non append
        page += 1
    return all_results

# Accumulare fino a N risultati
def fetch_n(resource: str, n: int, per_page: int = 10) -> list[dict]:
    all_results = []
    page = 1
    while len(all_results) < n:
        response = requests.get(
            f"{BASE_URL}/{resource}",
            params={"_page": page, "_limit": per_page},
            timeout=10
        )
        data = response.json()
        if not data:
            break
        all_results.extend(data)
        page += 1
    return all_results[:n]         # ← slice esatto

# Leggere il total count dall'header
response = requests.get(url, params={"_page": 1, "_limit": 10})
total = int(response.headers.get("X-Total-Count", 0))
total_pages = (total + per_page - 1) // per_page   # arrotondamento in su

# Stop condition: not data vs len(data) < per_page
# not data → True solo se la lista è completamente vuota
# len(data) < per_page → True anche sull'ultima pagina parziale
# Usa `not data` per semplicità; usa `len(data) < per_page` se l'API
# non garantisce che l'ultima pagina sia vuota ma solo più corta.
```
