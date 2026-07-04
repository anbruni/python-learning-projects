"""
Exercise 2.8 - API Pagination
===============================

LEARNING GOALS:
- pagination params: _page + _limit per scorrere le pagine
- stop condition: interrompere il loop quando la pagina è vuota
- accumulate results: combinare i risultati di più pagine in una lista unica
- target count: fermarsi appena raccogli abbastanza elementi

API USATA: https://jsonplaceholder.typicode.com
    GET /posts?_page=N&_limit=M             → pagina N con M elementi
    GET /posts?userId=U&_page=N&_limit=M    → pagina N filtrata per utente U

    Totale: 100 posts, 10 utenti (10 posts each)
    _page=1&_limit=5   → posts 1–5
    _page=2&_limit=5   → posts 6–10
    ...
    _page=20&_limit=5  → posts 96–100
    _page=21&_limit=5  → []   ← lista vuota → stop condition

STRUCTURE:
- Part 1: Concept  — page-based vs cursor-based, stop conditions, accumulation
- Part 2: fetch_page(page, per_page)             → singola pagina
- Part 3: fetch_all_pages(per_page, max_pages)   → accumula tutte le pagine
- Part 4: fetch_until_count(target, per_page)    → stop appena hai abbastanza
- Part 5: Cinema task — get_director_filmography(user_id, per_page)
"""

import truststore
import requests

truststore.inject_into_ssl()

JSONPLACEHOLDER = "https://jsonplaceholder.typicode.com"


# =============================================================================
# PART 1 - CONCEPT: pagination, stop conditions, accumulation
# =============================================================================
"""
PERCHÉ LE API USANO LA PAGINATION:

    Un endpoint come GET /movies potrebbe restituire migliaia di risultati.
    Mandare tutto in una sola risposta è lento, consuma banda e rischia timeout.
    La soluzione: dividi i risultati in "pagine" e mandane una per volta.

    Il client scorre le pagine con un loop finché non ha tutto quello che serve.

TIPI DI PAGINATION:

    PAGE-BASED (più comune nelle API REST semplici):
        GET /posts?_page=1&_limit=10
        GET /posts?_page=2&_limit=10
        Parametri: numero di pagina + dimensione pagina.
        Limite: se qualcuno aggiunge un post mentre stai paginando,
                potresti saltare un elemento o vederne uno due volte.

    OFFSET-BASED (variante della page-based):
        GET /posts?_start=0&_limit=10   → elementi 0–9
        GET /posts?_start=10&_limit=10  → elementi 10–19
        Parametri: indice di partenza + numero di elementi.
        Molto simile alla page-based — _start = (page - 1) * limit.

    CURSOR-BASED (più robusto, usato da API come TMDB, GitHub, Meta):
        GET /posts
        → risposta include "next_cursor": "eyJpZCI6MTB9"
        GET /posts?cursor=eyJpZCI6MTB9
        → risposta include "next_cursor": "eyJpZCI6MjB9"
        Stop quando "next_cursor" è null o la risposta non include "next".
        Non soffre dei problemi di inserimento/cancellazione concorrente.

STOP CONDITIONS — quando smettere di paginare:

    1. PAGINA VUOTA:    if not page_data: break
       La risposta è [] → non ci sono più elementi.
       La stop condition più comune con page-based e offset-based.

    2. MAX PAGES:       if page > max_pages: break
       Protezione di sicurezza: evita loop infiniti in caso di bug dell'API.
       Sempre utile da avere anche quando usi la stop condition #1.

    3. TARGET COUNT:    if len(accumulated) >= target: break
       Vuoi N elementi in totale → fermati appena li hai.
       Poi `[:target]` per ritagliare esattamente N dalla lista.

    4. NO "NEXT" LINK:  if "next" not in response_data: break
       Tipico delle API cursor-based che includono link di navigazione
       nella risposta (come TMDB, GitHub API).

ACCUMULATION PATTERN — combinare le pagine:

    # SBAGLIATO — append aggiunge la lista come elemento singolo
    all_results.append(page_data)       → [[1,2,3], [4,5,6], ...]

    # CORRETTO — extend aggiunge tutti gli elementi della lista
    all_results.extend(page_data)       → [1, 2, 3, 4, 5, 6, ...]

    # Alternativa con +=  (identica a extend)
    all_results += page_data

JS COMPARISON:
    // JS — spesso con async generator o loop asincrono
    async function* paginate(url, limit) {
        let page = 1
        while (true) {
            const res = await fetch(`${url}?_page=${page}&_limit=${limit}`)
            const data = await res.json()
            if (!data.length) return
            yield* data
            page++
        }
    }

    // Python — loop sincrono, più diretto
    def paginate(url, per_page):
        page = 1
        all_data = []
        while True:
            response = requests.get(url, params={"_page": page, "_limit": per_page})
            data = response.json()
            if not data:
                break
            all_data.extend(data)
            page += 1
        return all_data
"""


# =============================================================================
# PART 2 - Singola pagina
# =============================================================================


def fetch_page(page: int, per_page: int) -> list[dict]:
    """
    YOUR TASK:
    Fai una GET request a JSONPLACEHOLDER + "/posts" con i parametri:
        _page   = page
        _limit  = per_page
    Se status_code == 200  → return response.json()  (lista di post)
    Altrimenti             → return []

    HINT:
        response = requests.get(
            JSONPLACEHOLDER + "/posts",
            params={"_page": page, "_limit": per_page},
            timeout=10
        )
        if response.status_code == 200:
            return response.json()
        return []

    NOTA: response.json() ritorna [] (lista vuota) quando la pagina richiesta
          non contiene elementi — es. _page=99 con solo 100 posts e _limit=5.
          Una lista vuota è truthy=False in Python: `not []` → True.

    EXPECTED con page=1, per_page=5:
        lista di 5 post, id 1–5

    EXPECTED con page=3, per_page=5:
        lista di 5 post, id 11–15

    EXPECTED con page=99, per_page=5:
        []   (pagina inesistente → lista vuota)
    """
    response = requests.get(
        JSONPLACEHOLDER + "/posts",
        params={"_page": page, "_limit": per_page},
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()
    return []


# =============================================================================
# PART 3 - Accumulare tutte le pagine
# =============================================================================


def fetch_all_pages(per_page: int = 10, max_pages: int = 50) -> list[dict]:
    """
    YOUR TASK:
    Scarica TUTTE le pagine di /posts.
    Loop dalla pagina 1 in poi, finché:
    - la pagina ritorna una lista vuota []  → break (stop condition primaria)
    - raggiungi max_pages                   → break (protezione di sicurezza)

    Accumula i risultati in una lista unica e ritornala.

    STRUTTURA:
        all_results = []
        page = 1
        while page <= max_pages:
            results = fetch_page(page, per_page)
            if not results:
                break
            all_results.extend(results)
            page += 1
        return all_results

    NOTA: `not results` è True quando results == [] (lista vuota è falsy).
          È il modo Pythonic di scrivere `len(results) == 0`.

    NOTA: `.extend()` aggiunge tutti gli elementi di results alla fine di
          all_results (in place). Molto più efficiente che fare:
              for item in results:
                  all_results.append(item)

    EXPECTED con per_page=10, max_pages=50:
        lista di 100 post  (JSONPlaceholder ha esattamente 100 posts in tutto)

    EXPECTED con per_page=5, max_pages=3:
        lista di 15 post  (3 pagine × 5 = 15, poi max_pages raggiunto)
    """
    all_results = []
    page = 1
    while page <= max_pages:
        results = fetch_page(page, per_page)
        if not results:
            break
        all_results.extend(results)
        page += 1
    return all_results


# =============================================================================
# PART 4 - Stop appena hai abbastanza risultati
# =============================================================================


def fetch_until_count(target_count: int, per_page: int = 10) -> list[dict]:
    """
    YOUR TASK:
    Scarica pagine di /posts finché non accumuli almeno `target_count` risultati,
    poi ritorna ESATTAMENTE `target_count` elementi (usa slice [:target_count]).
    Se le pagine finiscono prima → ritorna tutto quello che hai.

    STRUTTURA:
        all_results = []
        page = 1
        while len(all_results) < target_count:
            results = fetch_page(page, per_page)
            if not results:
                break
            all_results.extend(results)
            page += 1
        return all_results[:target_count]

    NOTA: lo slice `[:target_count]` taglia la lista all'indice target_count.
          Se hai 10 elementi e target_count=7 → prende i primi 7.
          Se hai 5 elementi e target_count=7  → ritorna tutti e 5 (nessun errore).

    EXPECTED con target_count=7, per_page=5:
        lista di esattamente 7 post
        (pagina 1 → 5 post, pagina 2 → 5 post, poi slice [:7] → 7 post)

    EXPECTED con target_count=12, per_page=10:
        lista di esattamente 12 post
        (pagina 1 → 10 post, pagina 2 → 10 post, poi slice [:12] → 12 post)

    EXPECTED con target_count=200, per_page=10:
        lista di 100 post  (JSONPlaceholder ne ha solo 100, prende tutto)
    """
    all_results = []
    page = 1
    while len(all_results) < target_count:
        results = fetch_page(page, per_page)
        if not results:
            break
        all_results.extend(results)
        page += 1
    return all_results[:target_count]


# =============================================================================
# PART 5 - CINEMA TASK: filmografia completa di un regista
# =============================================================================


def get_director_filmography(user_id: int, per_page: int = 3) -> list[dict]:
    """
    YOUR TASK:
    Simula il fetch della filmografia COMPLETA di un "regista" (userId).
    Pagina attraverso i post filtrati per user_id finché la pagina è vuota.

    Per ogni post, includi SOLO i campi: {"id": ..., "title": ..., "body": ...}
    (scarta "userId" — non serve nel risultato finale)

    STRUTTURA:
        filmography = []
        page = 1
        while True:
            response = requests.get(
                JSONPLACEHOLDER + "/posts",
                params={"userId": user_id, "_page": page, "_limit": per_page},
                timeout=10
            )
            if response.status_code != 200:
                break
            page_data = response.json()
            if not page_data:
                break
            for post in page_data:
                filmography.append({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"],
                })
            page += 1
        return filmography

    NOTA: ogni utente in JSONPlaceholder ha esattamente 10 posts.
          Con per_page=3:
              pagina 1 → 3 post, pagina 2 → 3, pagina 3 → 3, pagina 4 → 1
              pagina 5 → []  →  stop  →  10 post totali
          Con per_page=5:
              pagina 1 → 5 post, pagina 2 → 5 post
              pagina 3 → []  →  stop  →  10 post totali

    NOTA: questa funzione fa le requests dirette (non usa fetch_page) per poter
          aggiungere il filtro userId al dict params — dimostra come si combinano
          filtro + paginazione in una singola chiamata.

    NOTA: la projection {"id", "title", "body"} è lo stesso pattern dell'Esercizio 2.6,
          Part 5. La differenza: qui raccogliamo TUTTE le pagine invece di
          limitarci a un numero fisso.

    EXPECTED con user_id=1, per_page=3:
        lista di 10 dict, ognuno con chiavi ["id", "title", "body"]
        nessun campo "userId" nel risultato
        id dei post: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    EXPECTED con user_id=2, per_page=5:
        lista di 10 dict
        id dei post: 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    """
    page = 1
    filmography = []
    while True:
        response = requests.get(
            JSONPLACEHOLDER + "/posts",
            params={"userId": user_id, "_page": page, "_limit": per_page},
            timeout=10,
        )
        if response.status_code != 200:
            break
        page_data = response.json()
        if not page_data:
            break
        form_response = [
            {"id": r["id"], "title": r["title"], "body": r["body"]} for r in page_data
        ]
        filmography.extend(form_response)
        page += 1
    return filmography


# =============================================================================
# RUNNER
# =============================================================================

if __name__ == "__main__":
    # print("=" * 55)
    # print("EXERCISE 2.8 — API Pagination")
    # print("=" * 55)

    # Part 2 — fetch_page
    # print("\n--- Part 2: fetch_page ---")
    # page1 = fetch_page(page=1, per_page=5)
    # if page1 is not None:
    #     print(f"  Pagina 1 (limit=5): {len(page1)} post  (atteso: 5)")
    #     print(f"  IDs: {[p['id'] for p in page1]}  (atteso: [1,2,3,4,5])")
    # else:
    #     print("  fetch_page: non ancora implementata.")

    # page3 = fetch_page(page=3, per_page=5)
    # if page3 is not None:
    #     print(
    #         f"  Pagina 3 (limit=5): IDs {[p['id'] for p in page3]}  (atteso: [11,12,13,14,15])"
    #     )

    # empty = fetch_page(page=99, per_page=5)
    # if empty is not None:
    #     print(f"  Pagina 99 → {empty}  (atteso: [])")

    # # Part 3 — fetch_all_pages
    # print("\n--- Part 3: fetch_all_pages ---")
    # all_posts = fetch_all_pages(per_page=10, max_pages=50)
    # if all_posts is not None:
    #     print(f"  Tutti i post (limit=10): {len(all_posts)}  (atteso: 100)")
    # else:
    #     print("  fetch_all_pages: non ancora implementata.")

    # limited = fetch_all_pages(per_page=5, max_pages=3)
    # if limited is not None:
    #     print(f"  max_pages=3, limit=5: {len(limited)} post  (atteso: 15)")

    # Part 4 — fetch_until_count
    # print("\n--- Part 4: fetch_until_count ---")
    # seven = fetch_until_count(target_count=7, per_page=5)
    # if seven is not None:
    #     print(f"  target=7, limit=5: {len(seven)} post  (atteso: 7)")
    #     print(f"  IDs: {[p['id'] for p in seven]}")
    # else:
    #     print("  fetch_until_count: non ancora implementata.")

    # too_many = fetch_until_count(target_count=200, per_page=10)
    # if too_many is not None:
    #     print(
    #         f"  target=200: {len(too_many)} post  (atteso: 100 — massimo disponibile)"
    #     )

    # Part 5 — get_director_filmography
    print("\n--- Part 5: filmografia completa regista ---")
    filmography = get_director_filmography(user_id=1, per_page=3)
    if filmography is not None:
        print(f"  Regista #1 (limit=3/pagina): {len(filmography)} film  (atteso: 10)")
        if filmography:
            has_user_id = any("userId" in f for f in filmography)
            print(f"  userId rimosso: {not has_user_id}  (atteso: True)")
            print(f"  IDs: {[f['id'] for f in filmography]}")
    else:
        print("  get_director_filmography: non ancora implementata.")

    filmography2 = get_director_filmography(user_id=2, per_page=5)
    if filmography2 is not None:
        print(
            f"\n  Regista #2 (limit=5/pagina): {len(filmography2)} film  (atteso: 10)"
        )
        if filmography2:
            print(f"  IDs: {[f['id'] for f in filmography2]}")
