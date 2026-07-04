"""
Exercise 2.9 - Environment Variables
======================================

LEARNING GOALS:
- .env file           → file di testo che contiene variabili d'ambiente
- python-dotenv       → libreria per caricare il .env in os.environ
- os.getenv(key)      → legge una variabile, ritorna None se mancante
- os.getenv(key, def) → legge con valore di default
- os.environ[key]     → legge con KeyError se mancante
- .env.example        → template committato, documenta le variabili necessarie
- .gitignore          → il .env NON va mai committato (contiene segreti)

SETUP (una volta sola):
    pip install python-dotenv     (già in requirements.txt)

FILE DI SUPPORTO (già creati):
    .env          → valori reali per l'esercizio (già in .gitignore)
    .env.example  → template committato, senza valori reali

STRUCTURE:
- Part 1: Concept  — perché le env vars, .env format, os.getenv vs os.environ
- Part 2: load_env(env_path)             → carica il .env con python-dotenv
- Part 3: get_required_env(name)         → legge var obbligatoria, raise se mancante
- Part 4: build_api_config()             → costruisce config da env vars con default
- Part 5: Cinema task — fetch_posts(limit) → chiama API usando config da .env
"""

import os
import truststore
import requests
from dotenv import load_dotenv

truststore.inject_into_ssl()

ENV_FILE = os.path.join(os.path.dirname(__file__), ".env")


# =============================================================================
# PART 1 - CONCEPT: env vars, .env, os.getenv, .gitignore
# =============================================================================
"""
PERCHÉ LE VARIABILI D'AMBIENTE:

    NON fare questo:
        API_KEY = "sk-abc123xyz"          # la chiave finisce nel codice
        BASE_URL = "https://api.tmdb.org" # e nel git history — per sempre

    Fare questo invece:
        API_KEY = os.getenv("APP_API_KEY") # la chiave vive solo nella macchina

    Le variabili d'ambiente separano la CONFIGURAZIONE dal CODICE.
    Il codice va su GitHub. Le chiavi API restano sul tuo computer (e sui server).

IL FILE .env:

    Formato semplice — una variabile per riga:

        APP_API_KEY=sk-abc123xyz
        APP_BASE_URL=https://api.themoviedb.org/3
        APP_MAX_RESULTS=20
        APP_DEBUG=false

    Regole:
    - nessuno spazio intorno a =
    - i valori sono sempre stringhe (anche i numeri — devi convertire tu)
    - righe che iniziano con # sono commenti
    - il file .env NON va committato (già in .gitignore di questo progetto)

.env vs .env.example:

    .env          → valori reali, sul tuo computer, MAI su GitHub → in .gitignore
    .env.example  → template vuoto, su GitHub → documenta quali variabili servono

    Workflow:
        git clone progetto
        cp .env.example .env
        # apri .env e inserisci le tue chiavi
        python app.py

OS.GETENV vs OS.ENVIRON:

    os.getenv("APP_API_KEY")           → None se mancante (non crasha)
    os.getenv("APP_API_KEY", "default") → "default" se mancante
    os.environ["APP_API_KEY"]          → KeyError se mancante (crasha!)
    os.environ.get("APP_API_KEY")      → equivalente a os.getenv

    ATTENZIONE: tutti i valori sono STRING.
        os.getenv("APP_MAX_RESULTS")     → "10"  (stringa, non int!)
        int(os.getenv("APP_MAX_RESULTS", "20"))  → 10  (converti tu)

PYTHON-DOTENV — carica il .env in os.environ:

    from dotenv import load_dotenv
    load_dotenv("/path/to/.env")      # carica il file nel processo corrente
    # ora os.getenv("APP_API_KEY") funziona come se la var fosse impostata

    load_dotenv() senza argomenti cerca .env nella cartella corrente e nelle
    cartelle superiori — comodo per progetti con struttura a cartelle.

JS COMPARISON:
    // Node.js — stessa identica idea con il pacchetto dotenv
    require('dotenv').config()
    const apiKey = process.env.APP_API_KEY        // string | undefined
    const maxResults = parseInt(process.env.APP_MAX_RESULTS || "20")

    # Python
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("APP_API_KEY")            # str | None
    max_results = int(os.getenv("APP_MAX_RESULTS", "20"))
"""


# =============================================================================
# PART 2 - Caricare il .env con python-dotenv
# =============================================================================


def load_env(env_path: str) -> bool:
    """
    YOUR TASK:
    Carica le variabili dal file .env nel processo corrente usando load_dotenv.
    Ritorna True se il file è stato trovato e caricato, False altrimenti.

    HINT:
        return load_dotenv(env_path)

    NOTA: load_dotenv() ritorna True se il file .env esiste, False se non esiste.
          Dopo la chiamata, le variabili del file sono disponibili tramite
          os.getenv() per tutta la durata del processo.

    NOTA: load_dotenv non sovrascrive variabili già impostate nell'ambiente
          del sistema operativo. Questo è il comportamento corretto:
          le variabili di sistema hanno precedenza su quelle del .env.

    EXPECTED con env_path=ENV_FILE:
        True  (il file .env esiste)
        dopo la chiamata, os.getenv("APP_API_KEY") non è più None

    EXPECTED con env_path="ghost.env":
        False  (file inesistente)
    """
    return load_dotenv(env_path)


# =============================================================================
# PART 3 - Leggere variabile obbligatoria
# =============================================================================


def get_required_env(name: str) -> str:
    """
    YOUR TASK:
    Leggi la variabile d'ambiente `name` con os.getenv.
    Se la variabile è None o stringa vuota → raise ValueError con messaggio:
        "Missing required environment variable: <name>"

    HINT:
        value = os.getenv(name)
        if not value:
            raise ValueError(f"Missing required environment variable: {name}")
        return value

    NOTA: `not value` è True sia per None (variabile mancante) sia per "" (stringa
          vuota). Entrambi i casi sono invalidi per una variabile obbligatoria.

    NOTA: get_required_env funziona SOLO dopo aver chiamato load_env() —
          le var del .env non sono visibili finché non le carichi.

    EXPECTED con name="APP_API_KEY" (dopo load_env):
        "test_key_exercise_29"  (il valore dal .env)

    EXPECTED con name="VAR_CHE_NON_ESISTE":
        ValueError: "Missing required environment variable: VAR_CHE_NON_ESISTE"
    """
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


# =============================================================================
# PART 4 - Costruire la config completa da env vars
# =============================================================================


def build_api_config() -> dict:
    """
    YOUR TASK:
    Costruisci e ritorna un dict di configurazione leggendo le variabili d'ambiente.
    Usa get_required_env per le variabili obbligatorie e os.getenv con default per
    le opzionali. Converti i tipi dove necessario.

    Struttura del dict da ritornare:
        {
            "api_key":     get_required_env("APP_API_KEY"),         # str, obbligatoria
            "base_url":    get_required_env("APP_BASE_URL"),        # str, obbligatoria
            "max_results": int(os.getenv("APP_MAX_RESULTS", "10")), # int, default 10
            "language":    os.getenv("APP_LANGUAGE", "en-US"),      # str, default "en-US"
            "debug":       os.getenv("APP_DEBUG", "false") == "true", # bool, default False
        }

    HINT: costruisci il dict direttamente con le espressioni sopra.

    NOTA: i valori del .env sono SEMPRE stringhe.
          "10"     → int("10")      → 10
          "false"  → "false" == "true"  → False
          "true"   → "true"  == "true"  → True

    NOTA: questa funzione presuppone che load_env() sia già stato chiamato.

    EXPECTED (con i valori del .env dell'esercizio):
        {
            "api_key":     "test_key_exercise_29",
            "base_url":    "https://jsonplaceholder.typicode.com",
            "max_results": 10,
            "language":    "it-IT",
            "debug":       False,
        }
    """
    value_dict = {
        "api_key": get_required_env("APP_API_KEY"),
        "base_url": get_required_env("APP_BASE_URL"),
        "max_results": int(os.getenv("APP_MAX_RESULTS", "10")),
        "language": os.getenv("APP_LANGUAGE", "en-US"),
        "debug": os.getenv("APP_DEBUG", "false") == "true",
    }
    return value_dict


# =============================================================================
# PART 5 - CINEMA TASK: fetch usando config da .env
# =============================================================================


def fetch_posts(limit: int | None = None) -> list[dict]:
    """
    YOUR TASK:
    Usa build_api_config() per ottenere la configurazione, poi fai una GET request
    a config["base_url"] + "/posts" con il parametro _limit.

    Se `limit` è None → usa config["max_results"] come limite.
    Se `limit` è fornito → usa quello.

    Ritorna response.json() se status 200, altrimenti [].

    STRUTTURA:
        config = build_api_config()
        effective_limit = limit if limit is not None else config["max_results"]
        response = requests.get(
            config["base_url"] + "/posts",
            params={"_limit": effective_limit},
            timeout=10
        )
        if response.status_code == 200:
            return response.json()
        return []

    NOTA: `limit if limit is not None else config["max_results"]` è l'equivalente
          Pythonic di `limit ?? config.max_results` in JavaScript.
          Non usare `limit or config["max_results"]` — fallirebbe se limit=0.

    EXPECTED con limit=None:
        lista di 10 post  (usa APP_MAX_RESULTS=10 dal .env)

    EXPECTED con limit=3:
        lista di 3 post  (sovrascrive il valore del .env)
    """
    config = build_api_config()
    url = config["base_url"]
    if limit is None:
        effective_limit = config["max_results"]
    else:
        effective_limit = limit

    response = requests.get(
        url + "/posts", params={"_limit": effective_limit}, timeout=10
    )
    if response.status_code == 200:
        return response.json()
    return []


# =============================================================================
# RUNNER
# =============================================================================

if __name__ == "__main__":
    # Part 2 — load_env
    # print("=" * 55)
    # print("EXERCISE 2.9 — Environment Variables")
    # print("=" * 55)

    # print("\n--- Part 2: load_env ---")
    # loaded = load_env(ENV_FILE)
    # if loaded is not None:
    #     print(f"  load_env(ENV_FILE) → {loaded}  (atteso: True)")
    #     print(f"  APP_API_KEY dopo load: {os.getenv('APP_API_KEY')}")
    # else:
    #     print("  load_env: non ancora implementata.")

    # print("\n  Test file inesistente:")
    # missing = load_env("ghost.env")
    # print(f"  load_env('ghost.env') → {missing}  (atteso: False)")

    # Part 3 — get_required_env
    # print("\n--- Part 3: get_required_env ---")
    # if load_env(ENV_FILE):
    #     key = get_required_env("APP_API_KEY")
    #     if key is not None:
    #         print(f"  APP_API_KEY → '{key}'  (atteso: 'test_key_exercise_29')")
    #     else:
    #         print("  get_required_env: non ancora implementata.")

    #     print("\n  Test variabile mancante:")
    #     try:
    #         get_required_env("VAR_CHE_NON_ESISTE")
    #         print("  MANCA: doveva lanciare ValueError!")
    #     except ValueError as e:
    #         print(f"  OK — ValueError: {e}")

    # Part 4 — build_api_config
    # print("\n--- Part 4: build_api_config ---")
    # if load_env(ENV_FILE):
    #     config = build_api_config()
    #     if config:
    #         print(f"  Config caricata ({len(config)} chiavi):")
    #         for k, v in config.items():
    #             print(f"    {k}: {v!r}  (tipo: {type(v).__name__})")
    #         print(f"\n  max_results è int: {isinstance(config.get('max_results'), int)}  (atteso: True)")
    #         print(f"  debug è bool:      {isinstance(config.get('debug'), bool)}  (atteso: True)")
    #     else:
    #         print("  build_api_config: non ancora implementata.")

    # Part 5 — fetch_posts
    print("\n--- Part 5: fetch_posts da .env ---")
    loaded = load_env(ENV_FILE)
    if loaded is not None:
        posts = fetch_posts()
        if posts is not None:
            print(
                f"  fetch_posts() → {len(posts)} post  (atteso: 10, da APP_MAX_RESULTS)"
            )
            if posts:
                print(f"  Primo titolo: {posts[0]['title'][:40]}...")
        else:
            print("  fetch_posts: non ancora implementata.")

        posts_3 = fetch_posts(limit=3)
        if posts_3 is not None:
            print(f"\n  fetch_posts(limit=3) → {len(posts_3)} post  (atteso: 3)")
    else:
        print("  load_env: non ancora implementata.")
