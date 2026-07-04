"""
Exercise 2.6 - HTTP Basics
============================

LEARNING GOALS:
- requests.get(url)          → fare una richiesta GET
- response.status_code       → leggere il codice di stato HTTP
- response.json()            → parsare la risposta come JSON
- params={}                  → aggiungere query params all'URL
- headers={}                 → aggiungere header alla richiesta

SETUP (una volta sola):
    source venv/bin/activate          # attiva il venv
    pip install requests              # già nel requirements.txt

API USATA: https://jsonplaceholder.typicode.com  (mock API pubblica, no auth)
    GET /posts/{id}         → un singolo "post" (lo trattiamo come review)
    GET /posts              → lista di post (con params per filtrare)
    GET /users/{id}         → profilo utente (lo trattiamo come regista)

NOTA: In 2.9 userai una vera API cinema con chiave API e .env.
      I pattern che impari qui (GET, params, headers) sono identici.

STRUCTURE:
- Part 1: Concept  — HTTP, requests vs fetch, oggetto Response, status codes
- Part 2: requests.get + status_code   → fetch_review(review_id)
- Part 3: query params                 → list_reviews(limit, user_id)
- Part 4: custom headers               → fetch_with_headers(url, token)
- Part 5: Cinema task                  → get_director_movies(user_id, limit)
"""

import truststore
import requests

# macOS + Homebrew Python non usa il keychain di sistema per SSL.
# truststore.inject_into_ssl() risolve una volta sola — nessuna modifica alle chiamate requests.
truststore.inject_into_ssl()

BASE_URL = "https://jsonplaceholder.typicode.com"
HTTPBIN_URL = "https://httpbin.org/get"


# =============================================================================
# PART 1 - CONCEPT: HTTP, requests vs fetch, Response object
# =============================================================================
"""
HTTP IN PYTHON — LA LIBRERIA requests:

    requests è la libreria standard de facto per HTTP in Python.
    Non è nella stdlib (devi installarla) ma è la più usata in assoluto.

    pip install requests    ← già nel requirements.txt del progetto

IL CICLO REQUEST → RESPONSE:

    client (il tuo script)              server (API)
    ─────────────────────               ────────────
    requests.get(url)         →         riceve GET /posts/1
                              ←         risponde con JSON + status 200

L'OGGETTO Response:

    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    response.status_code    → 200              (int: codice HTTP)
    response.json()         → {"id": 1, ...}   (dict/list: corpo JSON)
    response.text           → '{"id": 1, ...}' (str: corpo raw)
    response.headers        → {"Content-Type": "application/json", ...}

STATUS CODES — i più importanti:

    2xx  → Successo
    200  OK            → tutto ok, hai i dati
    201  Created       → risorsa creata (POST)

    4xx  → Errore client (colpa tua)
    400  Bad Request   → richiesta malformata
    401  Unauthorized  → non autenticato (manca il token)
    403  Forbidden     → autenticato ma non hai i permessi
    404  Not Found     → la risorsa non esiste

    5xx  → Errore server (colpa loro)
    500  Internal Server Error  → bug sul server
    503  Service Unavailable    → server down

JS COMPARISON:
    // fetch in JS (asincrono, promesse)
    const res = await fetch("https://api.example.com/posts/1")
    const data = await res.json()          // due await necessari

    # requests in Python (sincrono, blocca fino alla risposta)
    response = requests.get("https://api.example.com/posts/1")
    data = response.json()                 # un solo passaggio

    La differenza chiave: requests è SINCRONO — il codice aspetta la risposta
    prima di andare avanti. Per I/O asincrono in Python si usa httpx o aiohttp.
"""


# =============================================================================
# PART 2 - requests.get + status_code
# =============================================================================


def fetch_review(review_id: int) -> dict | None:
    """
    YOUR TASK:
    Fai una GET request a BASE_URL + "/posts/{review_id}".
    Se status_code == 200 → return response.json()
    Altrimenti → return None

    HINT:
        url = f"{BASE_URL}/posts/{review_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    NOTA: response.json() è equivalente a json.loads(response.text)
          ma più comodo — requests lo fa per te.

    EXPECTED con review_id=1:
        {"userId": 1, "id": 1,
         "title": "sunt aut facere...",
         "body": "quia et suscipit..."}
        status_code: 200

    EXPECTED con review_id=9999:
        None  (la risorsa non esiste → 404)
    """
    full_url = f"{BASE_URL}/posts/{review_id}"
    response = requests.get(full_url)
    status = response.status_code
    if status == 200:
        return response.json()
    return None


# =============================================================================
# PART 3 - Query params: params={}
# =============================================================================


def list_reviews(limit: int = 5, user_id: int | None = None) -> list[dict]:
    """
    YOUR TASK:
    Fai una GET request a BASE_URL + "/posts" con query params.
    Costruisci il dict params con:
      - "_limit": limit   → sempre presente
      - "userId": user_id → solo se user_id non è None

    Ritorna response.json() (una lista di dict).

    HINT:
        params = {"_limit": limit}
        if user_id is not None:
            params["userId"] = user_id
        response = requests.get(BASE_URL + "/posts", params=params)
        return response.json()

    NOTA: requests costruisce l'URL per te:
        params={"_limit": 5, "userId": 1}
        → URL diventa: .../posts?_limit=5&userId=1
        Non devi mai fare string concatenation per i params!

    EXPECTED con limit=3:
        lista di 3 post (id 1, 2, 3)
        URL chiamata: https://jsonplaceholder.typicode.com/posts?_limit=3

    EXPECTED con limit=3, user_id=1:
        lista dei primi 3 post dove userId == 1
        URL chiamata: .../posts?_limit=3&userId=1
    """
    params = {"_limit": limit}
    if user_id is not None:
        params["userId"] = user_id
    response = requests.get(BASE_URL + "/posts", params=params)
    return response.json()


# =============================================================================
# PART 4 - Custom headers: headers={}
# =============================================================================


def fetch_with_headers(url: str, token: str | None = None) -> dict:
    """
    YOUR TASK:
    Fai una GET request a `url` con headers custom.
    Costruisci il dict headers con:
      - "Accept": "application/json"     → sempre presente
      - "User-Agent": "MovieApp/1.0"     → sempre presente
      - "Authorization": f"Bearer {token}" → solo se token non è None

    Ritorna response.json().

    HINT:
        headers = {
            "Accept": "application/json",
            "User-Agent": "MovieApp/1.0",
        }
        if token is not None:
            headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)
        return response.json()

    NOTA: puoi usare HTTPBIN_URL = "https://httpbin.org/get" per testare:
          httpbin echoes back la tua richiesta, inclusi gli headers che hai inviato.
          La risposta avrà un campo "headers" con quello che hai mandato.

    EXPECTED con url=HTTPBIN_URL, token=None:
        risposta con "headers": {"Accept": "application/json",
                                 "User-Agent": "MovieApp/1.0", ...}

    EXPECTED con url=HTTPBIN_URL, token="my_secret_token":
        risposta con "headers": {"Authorization": "Bearer my_secret_token", ...}
    """
    # --- scrivi il tuo codice qui sotto ---
    headers = {"Accept": "application/json", "User-Agent": "MovieApp/1.0"}
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    response = requests.get(url, headers=headers)
    return response.json()


# =============================================================================
# PART 5 - CINEMA TASK: filmografia di un regista
# =============================================================================


def get_director_movies(user_id: int, limit: int = 5) -> list[dict]:
    """
    YOUR TASK:
    Simula il fetch della filmografia di un "regista" (user).
    1. Chiama list_reviews(limit=limit, user_id=user_id) per ottenere i suoi post
    2. Per ogni post, crea un dict con SOLO questi campi:
           {"id": ..., "title": ..., "body": ...}
       (scarta "userId" — non serve nel risultato)
    3. Ritorna la lista dei dict trasformati

    HINT:
        raw = list_reviews(limit=limit, user_id=user_id)
        return [{"id": p["id"], "title": p["title"], "body": p["body"]} for p in raw]

    NOTA: questa operazione — "prendere solo alcuni campi da ogni dict" —
          si chiama "projection" nelle API e nei database. Lo vedrai spesso.

    EXPECTED con user_id=1, limit=3:
        [
          {"id": 1,  "title": "sunt aut facere...", "body": "quia et..."},
          {"id": 2,  "title": "qui est esse",       "body": "est rerum..."},
          {"id": 3,  "title": "ea molestias...",    "body": "et iusto..."},
        ]
        Nessun campo "userId" nella risposta.
    """
    # --- scrivi il tuo codice qui sotto ---
    reviews = list_reviews(limit=limit, user_id=user_id)
    all_director = []
    for rev in reviews:
        all_director.append(
            {"id": rev["id"], "title": rev["title"], "body": rev["body"]}
        )
    return all_director


# =============================================================================
# RUNNER
# =============================================================================

if __name__ == "__main__":
    # print("=" * 55)
    # print("EXERCISE 2.6 — HTTP Basics")
    # print("=" * 55)

    # # Part 2 — fetch_review
    # print("\n--- Part 2: requests.get + status_code ---")
    # review = fetch_review(1)
    # if review:
    #     print(f"  Review #1: {review['title'][:40]}...")
    #     print(f"  Keys: {list(review.keys())}")
    # else:
    #     print("  fetch_review: non ancora implementata.")

    # print("\n  Test id non esistente (9999):")
    # missing = fetch_review(9999)
    # if missing is None:
    #     print("  OK — fetch_review(9999) → None  (404)")
    # else:
    #     print(f"  ERRORE: atteso None, ottenuto {missing}")

    # Part 3 — list_reviews
    # print("\n--- Part 3: query params ---")
    # reviews = list_reviews(limit=3)
    # if reviews:
    #     print(f"  list_reviews(limit=3) → {len(reviews)} risultati  (atteso: 3)")
    #     print(f"  Primo titolo: {reviews[0]['title'][:40]}...")
    # else:
    #     print("  list_reviews: non ancora implementata.")

    # by_user = list_reviews(limit=3, user_id=1)
    # if by_user:
    #     print(f"\n  list_reviews(limit=3, user_id=1) → {len(by_user)} risultati")
    #     all_user1 = all(r["userId"] == 1 for r in by_user)
    #     print(f"  Tutti di userId=1: {all_user1}  (atteso: True)")
    # else:
    #     print("  list_reviews con user_id: non ancora implementata.")

    # Part 4 — fetch_with_headers
    # print("\n--- Part 4: custom headers (httpbin) ---")
    # result = fetch_with_headers(HTTPBIN_URL)
    # if result:
    #     sent_headers = result.get("headers", {})
    #     print(f"  Accept inviato:     {sent_headers.get('Accept')}")
    #     print(f"  User-Agent inviato: {sent_headers.get('User-Agent')}")
    # else:
    #     print("  fetch_with_headers: non ancora implementata.")

    # result_with_token = fetch_with_headers(HTTPBIN_URL, token="test_token_123")
    # if result_with_token:
    #     auth = result_with_token.get("headers", {}).get("Authorization")
    #     print(f"  Authorization:      {auth}  (atteso: Bearer test_token_123)")
    # else:
    #     print("  fetch_with_headers con token: non ancora implementata.")

    # Part 5 — get_director_movies
    print("\n--- Part 5: filmografia regista ---")
    movies = get_director_movies(user_id=1, limit=3)
    if movies:
        print(f"  Regista #1: {len(movies)} film trovati")
        for m in movies:
            keys = list(m.keys())
            print(f"    id={m['id']} | keys={keys}")
        has_user_id = any("userId" in m for m in movies)
        print(f"  userId rimosso: {not has_user_id}  (atteso: True)")
    else:
        print("  get_director_movies: non ancora implementata.")
