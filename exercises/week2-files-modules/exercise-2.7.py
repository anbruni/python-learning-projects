"""
Exercise 2.7 - Error Handling APIs
=====================================

LEARNING GOALS:
- timeout              → requests.get(url, timeout=N) + catch Timeout
- invalid JSON         → catch json.JSONDecodeError dalla risposta
- 4xx / 5xx            → raise_for_status() + distinguere client vs server error
- retry semplice       → riprovare su errori transitori con time.sleep

API USATA: https://httpbin.org  (echo server — restituisce ciò che vuoi testare)
    GET /delay/{n}        → aspetta N secondi prima di rispondere  (test timeout)
    GET /status/{code}    → risponde con lo status code scelto     (test 4xx/5xx)
    GET /html             → risponde con HTML, non JSON            (test JSONDecodeError)
    GET /get              → risposta normale JSON                  (test happy path)

STRUCTURE:
- Part 1: Concept  — gerarchia eccezioni requests, transient vs permanent, retry
- Part 2: timeout                → fetch_with_timeout(url, seconds)
- Part 3: invalid JSON           → safe_json_fetch(url)
- Part 4: 4xx / 5xx              → fetch_status_aware(url)
- Part 5: Cinema task — retry    → fetch_with_retry(url, max_retries, delay)
"""

import time
import truststore
import requests

truststore.inject_into_ssl()

HTTPBIN = "https://httpbin.org"


# =============================================================================
# PART 1 - CONCEPT: gerarchia eccezioni, transient vs permanent, retry
# =============================================================================
"""
GERARCHIA ECCEZIONI DI requests:

    requests.exceptions.RequestException   ← base di tutto
    ├── ConnectionError                     ← server irraggiungibile / DNS fail
    ├── Timeout                             ← richiesta troppo lenta
    │   ├── ConnectTimeout                  ← non riesce a connettersi in tempo
    │   └── ReadTimeout                     ← connesso ma server non risponde
    └── HTTPError                           ← lanciato da raise_for_status()
                                              (status >= 400)

    TIP: cattura sempre dal più specifico al più generico.
    Catching RequestException cattura tutto — utile come fallback finale.

TRANSIENT vs PERMANENT:

    ERRORI TRANSITORI — vale la pena riprovare (retry):
        Timeout          → server lento, rete instabile
        ConnectionError  → connessione caduta temporaneamente
        5xx              → server momentaneamente in errore

    ERRORI PERMANENTI — il retry non aiuta:
        400 Bad Request  → la tua richiesta è malformata, non cambierà
        401 Unauthorized → manca il token, aggiungerlo prima
        403 Forbidden    → non hai i permessi
        404 Not Found    → la risorsa non esiste

TIMEOUT — usa sempre (connect, read):

    requests.get(url, timeout=10)          # stesso timeout per connect e read
    requests.get(url, timeout=(3, 10))     # connect max 3s, read max 10s

    Senza timeout il codice può bloccarsi per sempre — mai ometterlo in produzione.

JS COMPARISON:
    // In fetch, il timeout non esiste nativamente — si usa AbortController
    const controller = new AbortController()
    const timeout = setTimeout(() => controller.abort(), 5000)
    const res = await fetch(url, { signal: controller.signal })

    # In requests, timeout è un parametro diretto — molto più semplice
    response = requests.get(url, timeout=5)
"""


# =============================================================================
# PART 2 - Timeout
# =============================================================================


def fetch_with_timeout(url: str, seconds: float) -> dict | None:
    """
    YOUR TASK:
    Fai una GET request con timeout=seconds.
    Se la risposta arriva in tempo → return response.json()
    Se scade il timeout           → return None (non crashare)

    HINT:
        try:
            response = requests.get(url, timeout=seconds)
            return response.json()
        except requests.Timeout:
            return None

    EXPECTED con url=HTTPBIN+"/get", seconds=5:
        dict con la risposta di httpbin  (arriva in ~200ms)

    EXPECTED con url=HTTPBIN+"/delay/3", seconds=1:
        None  (server ritarda 3s, ma noi aspettiamo solo 1s → Timeout)
    """
    try:
        response = requests.get(url, timeout=seconds)
        return response.json()
    except requests.Timeout:
        return None


# =============================================================================
# PART 3 - Invalid JSON
# =============================================================================


def safe_json_fetch(url: str) -> dict | list | None:
    """
    YOUR TASK:
    Fai una GET request e parsala come JSON.
    Se la risposta non è JSON valido → return None (non crashare).
    Se status != 200               → return None.

    HINT:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return None
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return None

    NOTA: requests.exceptions.JSONDecodeError è un alias di json.JSONDecodeError —
          puoi catturare entrambi, ma requests.exceptions.JSONDecodeError è più
          esplicito nel contesto HTTP.

    EXPECTED con url=HTTPBIN+"/get":
        dict JSON valido

    EXPECTED con url=HTTPBIN+"/html":
        None  (httpbin risponde con HTML → .json() lancia JSONDecodeError)
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return None


# =============================================================================
# PART 4 - 4xx / 5xx: distinguere client error da server error
# =============================================================================


def fetch_status_aware(url: str) -> dict:
    """
    YOUR TASK:
    Fai una GET request e gestisci i diversi status codes:
    - 200       → return {"status": "ok", "data": response.json()}
    - 4xx       → return {"status": "client_error", "code": response.status_code}
    - 5xx       → return {"status": "server_error", "code": response.status_code}

    NON usare raise_for_status() — controlla il codice manualmente.

    HINT:
        response = requests.get(url, timeout=10)
        code = response.status_code
        if code == 200:
            return {"status": "ok", "data": response.json()}
        elif 400 <= code < 500:
            return {"status": "client_error", "code": code}
        elif 500 <= code < 600:
            return {"status": "server_error", "code": code}

    NOTA: 400 <= code < 500 è un range check Python — molto più leggibile
          che scrivere code == 400 or code == 401 or ...

    EXPECTED con url=HTTPBIN+"/get":
        {"status": "ok", "data": {...}}

    EXPECTED con url=HTTPBIN+"/status/404":
        {"status": "client_error", "code": 404}

    EXPECTED con url=HTTPBIN+"/status/500":
        {"status": "server_error", "code": 500}
    """
    response = requests.get(url, timeout=10)
    code = response.status_code
    if code == 200:
        return {"status": "ok", "data": response.json()}
    elif 400 <= code < 500:
        return {"status": "client_error", "code": code}
    elif 500 <= code < 600:
        return {"status": "server_error", "code": code}
    return {"status": "unknown", "code": code}


# =============================================================================
# PART 5 - CINEMA TASK: retry su errori transitori
# =============================================================================


def fetch_with_retry(url: str, max_retries: int = 3, delay: float = 1.0) -> dict | None:
    """
    YOUR TASK:
    Fai fino a `max_retries` tentativi di GET request.
    Riprova (retry) su errori TRANSITORI: Timeout, ConnectionError, 5xx.
    Fallisci subito (no retry) su errori PERMANENTI: 4xx.
    Se tutti i tentativi falliscono → return None.

    STRUTTURA:
        for attempt in range(1, max_retries + 1):
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    return response.json()
                elif 400 <= response.status_code < 500:
                    return None             # errore permanente — non riprovare
                # 5xx: cade nel finally e riprova
            except (requests.Timeout, requests.ConnectionError):
                pass                        # errore transitorio — riprova
            if attempt < max_retries:
                time.sleep(delay)           # aspetta prima del prossimo tentativo
        return None

    NOTA: time.sleep(delay) tra un tentativo e l'altro evita di bombardare
          il server in difficoltà. In produzione si usa il "exponential backoff":
          delay raddoppia a ogni tentativo (1s, 2s, 4s...).

    EXPECTED con url=HTTPBIN+"/get", max_retries=3:
        dict JSON — risponde al primo tentativo

    EXPECTED con url=HTTPBIN+"/status/500", max_retries=2, delay=0.1:
        None  (500 è transitorio ma httpbin risponde sempre 500 → esaurisce i retry)

    EXPECTED con url=HTTPBIN+"/status/404", max_retries=3, delay=0.1:
        None  (404 è permanente → fallisce subito al primo tentativo, no retry)
    """
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=10)
            code = response.status_code
            if code == 200:
                return response.json()
            elif 400 <= code < 500:
                return None
        except (requests.Timeout, requests.ConnectionError):
            pass
        if attempt < max_retries:
            print(f"Tentativo {attempt}/{max_retries} fallito, riprovo tra {delay}s...")
            time.sleep(delay)
    return None


# =============================================================================
# RUNNER
# =============================================================================

if __name__ == "__main__":
    # print("=" * 55)
    # print("EXERCISE 2.7 — Error Handling APIs")
    # print("=" * 55)

    # # Part 2 — timeout
    # print("\n--- Part 2: timeout ---")
    # ok = fetch_with_timeout(HTTPBIN + "/get", seconds=5)
    # if ok is not None:
    #     print(f"  /get (timeout=5s) → OK, url: {ok.get('url')}")
    # else:
    #     print("  fetch_with_timeout: non ancora implementata.")

    # slow = fetch_with_timeout(HTTPBIN + "/delay/3", seconds=1)
    # if slow is None:
    #     print("  /delay/3 (timeout=1s) → None  (Timeout OK)")
    # else:
    #     print("  ERRORE: atteso None per timeout, ottenuto risposta")

    # # Part 3 — invalid JSON
    # print("\n--- Part 3: invalid JSON ---")
    # valid = safe_json_fetch(HTTPBIN + "/get")
    # if valid is not None:
    #     print(f"  /get → OK, tipo: {type(valid).__name__}")
    # else:
    #     print("  safe_json_fetch: non ancora implementata.")

    # html = safe_json_fetch(HTTPBIN + "/html")
    # if html is None:
    #     print("  /html → None  (JSONDecodeError gestito)")
    # else:
    #     print("  ERRORE: atteso None per HTML response, ottenuto risposta")

    # # Part 4 — status codes
    # print("\n--- Part 4: 4xx / 5xx ---")
    # r200 = fetch_status_aware(HTTPBIN + "/get")
    # if r200:
    #     print(f"  /get       → {r200.get('status')}  (atteso: ok)")
    # else:
    #     print("  fetch_status_aware: non ancora implementata.")

    # r404 = fetch_status_aware(HTTPBIN + "/status/404")
    # if r404:
    #     print(f"  /status/404 → {r404}  (atteso: client_error 404)")

    # r500 = fetch_status_aware(HTTPBIN + "/status/500")
    # if r500:
    #     print(f"  /status/500 → {r500}  (atteso: server_error 500)")

    # Part 5 — retry
    print("\n--- Part 5: retry ---")
    success = fetch_with_retry(HTTPBIN + "/get", max_retries=3)
    if success is not None:
        print(f"  /get → OK al primo tentativo")
    else:
        print("  fetch_with_retry: non ancora implementata.")

    print("  Test 5xx (max_retries=2, delay=0.1s):")
    r5xx = fetch_with_retry(HTTPBIN + "/status/500", max_retries=2, delay=0.1)
    print(f"  /status/500 → {r5xx}  (atteso: None dopo 2 tentativi)")

    print("  Test 4xx (max_retries=3, delay=0.1s):")
    r4xx = fetch_with_retry(HTTPBIN + "/status/404", max_retries=3, delay=0.1)
    print(f"  /status/404 → {r4xx}  (atteso: None senza retry)")
