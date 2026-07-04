# Config Patterns in Python

> Caricare, validare e applicare default a file di configurazione JSON —
> il pattern usato da ogni applicazione backend e API client reale.

## Table of Contents
1. [Il problema che questo pattern risolve](#il-problema)
2. [dict.get() — accesso sicuro con default](#dictget--accesso-sicuro-con-default)
3. [Merge di dizionari — {**a, **b}](#merge-di-dizionari--ab)
4. [Validare campi obbligatori](#validare-campi-obbligatori)
5. [Caricare JSON con error handling](#caricare-json-con-error-handling)
6. [Il config loader completo](#il-config-loader-completo)
7. [Eccezioni custom (avanzato)](#eccezioni-custom-avanzato)
8. [Quick Reference](#quick-reference)

---

## Il problema

Un'applicazione reale ha tre tipi di configurazione:

```
OBBLIGATORI → raise se mancanti   (api_key, database_url — senza l'app non parte)
OPZIONALI   → usa il default      (language, timeout — hanno un valore sensato)
FILE        → può non esistere     (raise chiaro o crea file di default)
```

Il loader deve gestire tutti e tre i casi senza crashare in modo silenzioso.

---

## dict.get() — accesso sicuro con default

`dict.get(key, default)` ritorna il valore se la chiave esiste, altrimenti `default`.
Non lancia mai `KeyError`.

```python
config = {"language": "it-IT", "max_results": 10}

# KeyError — CRASH se la chiave manca
config["missing"]           # KeyError!

# get — sicuro, mai KeyError
config.get("missing")       # None
config.get("missing", 20)   # 20   (default)
config.get("language")      # "it-IT"
config.get("language", "en-US")  # "it-IT"  (il file vince sul default)
```

**JS comparison:**
```javascript
config.maxResults ?? 20          // ≈  config.get("max_results", 20)
config?.cache?.enabled ?? true   // ≈  config.get("cache", {}).get("enabled", True)
```

### Quando usare get() vs []

| Situazione | Strumento |
|-----------|-----------|
| Chiave DEVE esistere — è un bug se manca | `config["key"]` — il KeyError è utile |
| Chiave opzionale con default sensato | `config.get("key", default)` |
| Vuoi distinguere "manca" da "è None" | `"key" in config` |

---

## Merge di dizionari — {**a, **b}

Crea un **nuovo** dict combinando due dict. Le chiavi del secondo sovrascrivono quelle del primo.

```python
defaults = {"language": "en-US", "max_results": 20, "include_adult": False}
loaded   = {"language": "it-IT", "max_results": 10}

# config = defaults OVERRIDE con loaded
config = {**defaults, **loaded}
# → {"language": "it-IT", "max_results": 10, "include_adult": False}
#   loaded sovrascrive defaults           ↑↑↑           defaults aggiunge include_adult
```

**L'ordine conta:**
```python
{**defaults, **loaded}  # loaded sovrascrive defaults  ← CORRETTO per config
{**loaded, **defaults}  # defaults sovrascrive loaded  ← defaults sempre vince (sbagliato)
```

**Nessuna mutazione:**
```python
# {**a, **b} crea SEMPRE un nuovo dict — a e b restano invariati
config = {**defaults, **loaded}
# defaults è ancora {"language": "en-US", ...}
# loaded   è ancora {"language": "it-IT", ...}
```

**Python 3.9+ — operatore `|`:**
```python
config = defaults | loaded   # stesso risultato, più leggibile
```

**JS comparison:**
```javascript
const config = { ...defaults, ...loaded }  ←→  {**defaults, **loaded}
```

---

## Validare campi obbligatori

```python
REQUIRED_KEYS = ["api_key", "base_url"]

def validate_required(config: dict, required_keys: list[str]) -> None:
    for key in required_keys:
        value = config.get(key)
        if value is None or value == "":
            raise ValueError(f"Missing required config key: '{key}'")
```

**Perché `raise ValueError` e non `return False`:**

```python
# BAD — il chiamante deve controllare il return value
if not validate_required(config, REQUIRED_KEYS):
    # facile dimenticare questo check!
    return

# GOOD — il chiamante non può ignorare un'eccezione
validate_required(config, REQUIRED_KEYS)   # lancia se qualcosa manca
# se arriva qui, il config è valido — garantito
start_app(config)
```

**Messaggio d'errore utile:**
```python
# BAD — non dice quale chiave manca
raise ValueError("Invalid config")

# GOOD — dice esattamente cosa fare
raise ValueError(f"Missing required config key: 'api_key'. "
                 f"Set it in config.json or as environment variable API_KEY.")
```

---

## Caricare JSON con error handling

```python
import json

def load_config(filepath: str) -> dict:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Config file not found: {filepath}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config file: {filepath} — {e}")
```

**Perché re-raise come ValueError invece di propagare l'originale:**
- `FileNotFoundError` e `json.JSONDecodeError` sono errori di basso livello
- Il chiamante vuole sapere "il config è invalido", non i dettagli del file system
- Un unico tipo di eccezione (`ValueError`) è più facile da gestire a monte

```python
# Il chiamante non deve conoscere FileNotFoundError e JSONDecodeError
try:
    config = load_config("config.json")
except ValueError as e:
    print(f"Impossibile caricare il config: {e}")
    sys.exit(1)
```

---

## Il config loader completo

Il pattern completo usato in applicazioni reali:

```python
import json
import os

REQUIRED_KEYS = ["api_key", "base_url"]

DEFAULTS = {
    "language": "en-US",
    "max_results": 20,
    "include_adult": False,
    "timeout": 10,
}

def load_config(filepath: str) -> dict:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Config file not found: {filepath}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in config file: {filepath}")

def apply_defaults(config: dict, defaults: dict) -> dict:
    return {**defaults, **config}

def validate_required(config: dict, required_keys: list[str]) -> None:
    for key in required_keys:
        value = config.get(key)
        if value is None or value == "":
            raise ValueError(f"Missing required config key: '{key}'")

def load_app_config(filepath: str) -> dict:
    raw = load_config(filepath)
    config = apply_defaults(raw, DEFAULTS)
    validate_required(config, REQUIRED_KEYS)
    return config

# Uso
config = load_app_config("config.json")
print(config["api_key"])       # garantito non-None
print(config["max_results"])   # 20 (default) oppure quello nel file
```

---

## Eccezioni custom (avanzato)

Per applicazioni più grandi puoi definire un'eccezione dedicata al config:

```python
class ConfigError(ValueError):
    """Raised when config is missing or invalid."""
    pass

def validate_required(config: dict, required_keys: list[str]) -> None:
    for key in required_keys:
        if not config.get(key):
            raise ConfigError(f"Missing required config key: '{key}'")
```

**Vantaggi:**
- Il chiamante può distinguere errori di config da altri ValueError
- Cattura sia ConfigError che ValueError (eredita da ValueError):

```python
try:
    config = load_app_config("config.json")
except ConfigError as e:
    print(f"Config error: {e}")    # solo errori di config
except ValueError as e:
    print(f"Value error: {e}")     # altri ValueError
```

**Quando vale la pena:**
- Libreria pubblica / SDK — i tuoi utenti beneficiano di tipi specifici
- Applicazione grande con molti moduli — distinguere l'origine degli errori aiuta
- In un esercizio o app piccola: `ValueError` è sufficiente

---

## Quick Reference

```python
import json

# Accesso sicuro con default
value = config.get("key", default_value)

# Merge — config sovrascrive defaults
final = {**defaults, **config}   # o:  defaults | config  (Python 3.9+)

# Caricare file con errori chiari
def load_config(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Config file not found: {filepath}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in: {filepath}")

# Validare obbligatori
def validate_required(config, keys):
    for key in keys:
        if not config.get(key):
            raise ValueError(f"Missing required config key: '{key}'")

# Il loader completo
def load_app_config(filepath):
    raw    = load_config(filepath)
    config = {**DEFAULTS, **raw}
    validate_required(config, REQUIRED_KEYS)
    return config
```
