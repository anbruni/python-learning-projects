"""
Exercise 2.5 - Config Loader
==============================

LEARNING GOALS:
- Caricare un file JSON come config (json.load + error handling)
- dict.get(key, default)     → accesso sicuro con valore di fallback
- {**defaults, **config}     → merge di dizionari (config sovrascrive i default)
- Validare campi obbligatori → raise ValueError con messaggi chiari
- Combinare tutto in un loader riutilizzabile

DATA FILE: data/config.json   (config per una movie search app)
OUTPUT:    nessun file di output — questo esercizio lavora in memoria

STRUCTURE:
- Part 1: Concept  — config pattern, dict.get(), merge di dict, raise vs default
- Part 2: load_config()          → json.load con error handling
- Part 3: get_config_value()     → dict.get() con default e type check
- Part 4: apply_defaults()       → merge di dizionari senza mutare l'originale
- Part 5: validate_required()    → raise ValueError per campi mancanti
- Part 6: Cinema task            → load_movie_search_config() — il loader completo
"""

import json
import os

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "data", "config.json")


# =============================================================================
# PART 1 - CONCEPT: config pattern, dict.get(), merge di dizionari
# =============================================================================
"""
IL PROBLEMA CHE RISOLVIAMO:

    Hai un'app che legge settings da un file JSON.
    Alcuni settings sono OBBLIGATORI (es. api_key) — senza di essi l'app non può partire.
    Altri sono OPZIONALI (es. language) — hanno un valore di default sensato.
    Il file potrebbe non esistere o essere JSON malformato.

    Serve un loader che:
    1. Legga il file → raise chiaro se non trovato o JSON invalido
    2. Applichi i default per i campi opzionali non presenti nel file
    3. Validi i campi obbligatori → raise con messaggio che dice QUALE campo manca
    4. Ritorni un dict completo e validato

dict.get(key, default):
    Accesso a un dict SENZA KeyError se la chiave manca.

    config = {"language": "it-IT"}

    config["max_results"]             # KeyError!
    config.get("max_results")         # None (nessun errore)
    config.get("max_results", 20)     # 20  (default se mancante)
    config.get("language", "en-US")   # "it-IT"  (il file sovrascrive il default)

    JS comparison:
        config.maxResults ?? 20       ≈  config.get("max_results", 20)
        config?.cache?.enabled ?? true ≈  config.get("cache", {}).get("enabled", True)

MERGE DI DIZIONARI — {**a, **b}:
    In Python 3.9+ puoi anche scrivere: a | b
    Ma {**a, **b} funziona ovunque e crei un NUOVO dict senza mutare nessuno dei due.

    defaults = {"language": "en-US", "max_results": 20, "include_adult": False}
    loaded   = {"language": "it-IT", "max_results": 10}

    config = {**defaults, **loaded}
    # → {"language": "it-IT", "max_results": 10, "include_adult": False}
    # loaded sovrascrive defaults, e "include_adult" viene dal default

    JS comparison:
        const config = { ...defaults, ...loaded }  ←→  {**defaults, **loaded}

RAISE VS DEFAULT — quando usare cosa:
    Campo OBBLIGATORIO mancante → raise ValueError  (l'app non può partire senza)
    Campo OPZIONALE mancante    → usa il default    (l'app funziona comunque)
    File non trovato            → raise ValueError  (dipende dal contesto:
                                                     se il file è obbligatorio, raise)
    JSON malformato             → raise ValueError  (non si può recuperare)
"""


# =============================================================================
# PART 2 - Caricare il file con error handling
# =============================================================================


def load_config(filepath: str) -> dict:
    """
    YOUR TASK:
    Leggi il file JSON e ritorna il dict.
    Se il file non esiste → raise ValueError con messaggio:
        "Config file not found: <filepath>"
    Se il JSON è malformato → raise ValueError con messaggio:
        "Invalid JSON in config file: <filepath>"

    HINT:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            raise ValueError(f"Config file not found: {filepath}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in config file: {filepath}")

    NOTA: `raise ValueError(...)` dentro un except NON interrompe il flusso del
          programma in modo silenzioso — propaga l'errore al chiamante con un
          messaggio leggibile. Molto diverso da `return {}`.

    EXPECTED con filepath valido: dict con le chiavi del config.json
    EXPECTED con filepath="ghost.json": ValueError: "Config file not found: ghost.json"
    EXPECTED con JSON malformato: ValueError: "Invalid JSON in config file: ..."
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Config file not found: {filepath}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in config file: {filepath}")


# =============================================================================
# PART 3 - Accesso con default: dict.get()
# =============================================================================


def get_config_value(config: dict, key: str, default=None, expected_type=None):
    """
    YOUR TASK:
    Ritorna config.get(key, default).
    Se `expected_type` è fornito e il valore trovato NON è di quel tipo,
    raise TypeError con messaggio:
        "Config key '<key>' must be <expected_type.__name__>, got <type(value).__name__>"

    HINT:
        value = config.get(key, default)
        if expected_type is not None and not isinstance(value, expected_type):
            raise TypeError(
                f"Config key '{key}' must be {expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        return value

    NOTA: isinstance(value, int) → True se value è int (più robusto che type(value) == int)

    EXAMPLES:
        config = {"max_results": 10, "language": "it-IT"}

        get_config_value(config, "max_results", 20)              → 10
        get_config_value(config, "missing_key", 20)              → 20  (usa il default)
        get_config_value(config, "max_results", 20, int)         → 10  (ok, è int)
        get_config_value(config, "max_results", 20, str)         → TypeError!
        get_config_value(config, "language", "en-US", str)       → "it-IT"
    """
    value = config.get(key, default)
    if expected_type is not None and not isinstance(value, expected_type):
        raise TypeError(
            f"Config key '{key}' must be {expected_type.__name__}, got {type(value).__name__}"
        )
    return value


# =============================================================================
# PART 4 - Merge di dizionari senza mutare l'originale
# =============================================================================


def apply_defaults(config: dict, defaults: dict) -> dict:
    """
    YOUR TASK:
    Ritorna un NUOVO dict che è la fusione di `defaults` e `config`.
    I valori di `config` sovrascrivono quelli di `defaults`.
    Non mutare né `config` né `defaults`.

    HINT:
        return {**defaults, **config}

    EXAMPLES:
        defaults = {"language": "en-US", "max_results": 20, "include_adult": False}
        config   = {"language": "it-IT", "max_results": 10}

        apply_defaults(config, defaults)
        # → {"language": "it-IT", "max_results": 10, "include_adult": False}
        # "language" e "max_results" vengono da config (sovrascrivono defaults)
        # "include_adult" viene da defaults (non era in config)

    ATTENZIONE: l'ordine di ** conta!
        {**config, **defaults}  → defaults sovrascrive config  ← SBAGLIATO
        {**defaults, **config}  → config sovrascrive defaults  ← CORRETTO

    VERIFICA IMMUTABILITÀ:
        dopo la chiamata, defaults e config devono essere invariati.
    """
    return {**defaults, **config}


# =============================================================================
# PART 5 - Validare i campi obbligatori
# =============================================================================


def validate_required(config: dict, required_keys: list[str]) -> None:
    """
    YOUR TASK:
    Per ogni chiave in `required_keys`, verifica che:
    - esista nel config (chiave presente)
    - non sia None
    - non sia una stringa vuota ""

    Se una chiave non supera la verifica → raise ValueError:
        "Missing required config key: '<key>'"

    HINT:
        for key in required_keys:
            value = config.get(key)
            if value is None or value == "":
                raise ValueError(f"Missing required config key: '{key}'")

    NOTA: config.get(key) ritorna None sia se la chiave manca
          sia se il valore è esplicitamente None — entrambi i casi sono invalidi.

    EXPECTED:
        config = {"api_key": "abc", "base_url": "https://api.example.com"}

        validate_required(config, ["api_key", "base_url"])  → None (nessuna eccezione)
        validate_required(config, ["api_key", "missing"])   → ValueError: "Missing required config key: 'missing'"
        validate_required({"api_key": ""}, ["api_key"])     → ValueError: "Missing required config key: 'api_key'"
    """
    for key in required_keys:
        value = config.get(key)
        if value is None or value == "":
            raise ValueError(f"Missing required config key: '{key}'")


# =============================================================================
# PART 6 - CINEMA TASK: il loader completo per Movie Search App
# =============================================================================

REQUIRED_KEYS = ["api_key", "base_url"]

DEFAULTS = {
    "language": "en-US",
    "max_results": 20,
    "include_adult": False,
    "genres": [],
    "cache": {"enabled": False, "ttl_seconds": 3600},
}


def load_movie_search_config(filepath: str) -> dict:
    """
    YOUR TASK:
    Carica, valida e applica i default al config di una movie search app.
    Combina le funzioni delle parti precedenti in questo ordine:

    1. Chiama load_config(filepath) → raw_config
    2. Chiama apply_defaults(raw_config, DEFAULTS) → config con default applicati
    3. Chiama validate_required(config, REQUIRED_KEYS) → raise se manca qualcosa
    4. Ritorna il config completo

    HINT:
        raw_config = load_config(filepath)
        config = apply_defaults(raw_config, DEFAULTS)
        validate_required(config, REQUIRED_KEYS)
        return config

    EXPECTED con data/config.json:
        {
          "api_key": "tmdb_abc123xyz",         ← dal file
          "base_url": "https://api.themoviedb.org/3",  ← dal file
          "language": "it-IT",                 ← dal file (sovrascrive default "en-US")
          "max_results": 10,                   ← dal file (sovrascrive default 20)
          "include_adult": False,              ← dal file (uguale al default)
          "genres": ["Drama", "Crime", "Sci-Fi"],  ← dal file
          "cache": {"enabled": True, "ttl_seconds": 1800}  ← dal file
        }

    EXPECTED con un file che manca api_key:
        ValueError: "Missing required config key: 'api_key'"

    EXPECTED con file inesistente:
        ValueError: "Config file not found: <filepath>"
    """
    raw_config = load_config(filepath)
    config = apply_defaults(raw_config, DEFAULTS)
    validate_required(config, REQUIRED_KEYS)
    return config


# =============================================================================
# RUNNER
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("EXERCISE 2.5 — Config Loader")
    print("=" * 55)

    # Part 2 — load_config
    print("\n--- Part 2: load_config ---")
    config_raw = load_config(CONFIG_FILE)
    # if config_raw:
    #     print(f"  Config caricato: {list(config_raw.keys())}")
    #     print(f"  api_key: {config_raw.get('api_key')}")
    # else:
    #     print("  load_config: non ancora implementata.")

    # print("\n  Test FileNotFoundError:")
    # try:
    #     load_config("ghost_config.json")
    #     print("  MANCA: doveva lanciare ValueError!")
    # except ValueError as e:
    #     print(f"  OK — ValueError: {e}")

    # # Part 3 — get_config_value
    # print("\n--- Part 3: get_config_value ---")
    # if config_raw:
    #     v1 = get_config_value(config_raw, "max_results", 20)
    #     v2 = get_config_value(config_raw, "missing_key", 99)
    #     print(f"  max_results (presente): {v1}  (atteso: 10)")
    #     print(f"  missing_key (assente):  {v2}  (atteso: 99)")

    #     print("\n  Test TypeError:")
    #     try:
    #         get_config_value(config_raw, "max_results", 20, str)
    #         print("  MANCA: doveva lanciare TypeError!")
    #     except TypeError as e:
    #         print(f"  OK — TypeError: {e}")

    # Part 4 — apply_defaults
    # print("\n--- Part 4: apply_defaults ---")
    # defaults = {"language": "en-US", "max_results": 20, "include_adult": False}
    # partial = {"language": "it-IT", "max_results": 10}
    # merged = apply_defaults(partial, defaults)
    # if merged:
    #     print(f"  Merged: {merged}")
    #     print(
    #         f"  Atteso: {{'language': 'it-IT', 'max_results': 10, 'include_adult': False}}"
    #     )
    #     print(f"  defaults invariato: {defaults}")
    #     print(f"  partial invariato:  {partial}")

    # Part 5 — validate_required
    # print("\n--- Part 5: validate_required ---")
    # test_config = {"api_key": "abc123", "base_url": "https://api.example.com"}
    # try:
    #     validate_required(test_config, ["api_key", "base_url"])
    #     print("  OK — nessuna eccezione per config valido")
    # except (ValueError, TypeError) as e:
    #     print(f"  ERRORE inatteso: {e}")

    # print("\n  Test chiave mancante:")
    # try:
    #     validate_required({"api_key": "abc"}, ["api_key", "base_url"])
    #     print("  MANCA: doveva lanciare ValueError!")
    # except ValueError as e:
    #     print(f"  OK — ValueError: {e}")

    # print("\n  Test chiave vuota:")
    # try:
    #     validate_required({"api_key": "", "base_url": "https://x.com"}, ["api_key"])
    #     print("  MANCA: doveva lanciare ValueError!")
    # except ValueError as e:
    #     print(f"  OK — ValueError: {e}")

    # Part 6 — loader completo
    print("\n--- Part 6: load_movie_search_config ---")
    config = load_movie_search_config(CONFIG_FILE)
    if config:
        print(f"  Config completo ({len(config)} chiavi):")
        for k, v in config.items():
            print(f"    {k}: {v}")
    else:
        print("  load_movie_search_config: non ancora implementata.")

    print("\n  Test api_key mancante:")
    missing_key_config = os.path.join(
        os.path.dirname(CONFIG_FILE), "config_no_key.json"
    )
    with open(missing_key_config, "w") as f:
        json.dump({"base_url": "https://api.example.com"}, f)
    try:
        load_movie_search_config(missing_key_config)
        print("  MANCA: doveva lanciare ValueError!")
    except ValueError as e:
        print(f"  OK — ValueError: {e}")
    finally:
        os.remove(missing_key_config)
