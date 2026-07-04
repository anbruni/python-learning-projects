# Error Handling in Python

> Gestire gli errori in modo graceful: prevenire crash, dare feedback utile, scrivere codice robusto

## Table of Contents
1. [try / except basics](#try--except-basics)
2. [else e finally](#else-e-finally)
3. [Eccezioni specifiche](#eccezioni-specifiche)
4. [Catturare più eccezioni](#catturare-più-eccezioni)
5. [raise — lanciare eccezioni](#raise--lanciare-eccezioni)
6. [Quando catch vs quando raise](#quando-catch-vs-quando-raise)
7. [Pattern reali](#pattern-reali)

---

## try / except basics

```python
try:
    result = 10 / 0         # codice che potrebbe fallire
except:                     # cattura QUALSIASI errore (sconsigliato)
    result = None
```

**Perché `except:` generico è sconsigliato:**
```python
try:
    data = fetch_api()
except:
    pass  # nasconde TUTTI gli errori, anche bug veri!
```

Preferisci sempre eccezioni specifiche (vedi sotto).

---

## else e finally

```python
try:
    result = int("42")
except ValueError:
    print("Conversione fallita")
else:
    print("Successo:", result)   # eseguito SOLO se nessuna eccezione
finally:
    print("Sempre eseguito")     # cleanup: chiudi file, connessioni, log
```

| Blocco | Quando esegue |
|--------|--------------|
| `try` | sempre (finché non c'è errore) |
| `except` | solo se c'è un'eccezione |
| `else` | solo se NON c'è eccezione |
| `finally` | SEMPRE, con o senza errore |

```python
# Esempio reale con finally
f = None
try:
    f = open("data.txt")
    data = f.read()
except FileNotFoundError:
    data = ""
finally:
    if f:
        f.close()  # chiude sempre il file
```

---

## Eccezioni specifiche

Le eccezioni più comuni in Python:

| Eccezione | Quando si verifica |
|-----------|-------------------|
| `ValueError` | valore sbagliato per il tipo: `int("abc")` |
| `KeyError` | chiave non esiste in un dict: `d["missing"]` |
| `IndexError` | indice fuori range: `lista[100]` |
| `TypeError` | tipo sbagliato: `"5" * "3"` |
| `ZeroDivisionError` | divisione per zero: `10 / 0` |
| `FileNotFoundError` | file non esiste: `open("ghost.txt")` |
| `AttributeError` | attributo non esiste: `None.strip()` |
| `ImportError` | modulo non trovato: `import nonexistent` |

```python
# Specifico: sai esattamente cosa è andato storto
try:
    rating = float(movie["rating"])
except KeyError:
    print("Rating non trovato nel dizionario")
    rating = 0.0
except ValueError:
    print("Rating non è un numero valido")
    rating = 0.0
```

---

## Catturare più eccezioni

```python
# Modo 1: blocchi except separati (azioni diverse per errori diversi)
try:
    value = int(user_input) * multiplier
except ValueError:
    return None   # input non convertibile
except TypeError:
    return None   # tipo sbagliato

# Modo 2: tuple (stessa azione per errori diversi)
try:
    value = int(user_input) * multiplier
except (ValueError, TypeError):
    return None

# Modo 3: catturare l'eccezione come variabile
try:
    result = risky_operation()
except ValueError as e:
    print(f"Errore: {e}")   # e contiene il messaggio dell'eccezione
```

---

## raise — lanciare eccezioni

```python
# Lanciare un'eccezione standard
def validate_rating(rating: float) -> None:
    if not 0 <= rating <= 10:
        raise ValueError(f"Rating must be between 0 and 10, got {rating}")

# Lanciare con messaggio personalizzato
def divide_or_error(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError(f"Cannot divide {a} by zero")
    return a / b

# Uso
try:
    validate_rating(15)
except ValueError as e:
    print(e)  # "Rating must be between 0 and 10, got 15"
```

---

## Quando catch vs quando raise

**Catch (gestisci l'errore)** quando il fallimento è **atteso e recuperabile**:
```python
# File non trovato è normale — restituisci default
def load_config(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}   # config di default, non un bug
```

**Raise (lancia l'eccezione)** quando l'input è **invalido e deve essere corretto**:
```python
# Un'età negativa è un bug del chiamante, non un caso normale
def create_user(name: str, age: int):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if not name:
        raise ValueError("Name cannot be empty")
```

| Situazione | Azione |
|-----------|--------|
| File non trovato (potrebbe non esserci) | catch → return default |
| Rete down (retry possibile) | catch → retry o return None |
| Età negativa (bug del chiamante) | raise ValueError |
| Chiave mancante in dict esterno | catch → return default |
| Parametro obbligatorio mancante | raise ValueError |

---

## Pattern reali

### Batch processing con tracking errori

```python
def batch_convert(values: list) -> dict:
    successes = []
    failures = []

    for value in values:
        try:
            successes.append(float(value))
        except ValueError as e:
            failures.append({"value": value, "error": type(e).__name__})

    return {"successes": successes, "failures": failures}

# batch_convert(["8.5", "invalid", "9.0"])
# → {"successes": [8.5, 9.0], "failures": [{"value": "invalid", "error": "ValueError"}]}
```

### Retry logic

```python
def fetch_with_retry(url: str, max_retries: int = 3):
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == max_retries:
                return None
```

### Caricamento JSON con finally

```python
def load_movie_data(filepath: str) -> dict:
    try:
        with open(filepath) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: File not found '{filepath}'")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{filepath}'")
        return {}
    finally:
        print("Load attempt complete")  # eseguito sempre
```

### Accesso sicuro a dict annidati

```python
def get_nested(data: dict, keys: list):
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError):
        return None

# get_nested({"user": {"name": "Alice"}}, ["user", "name"])  → "Alice"
# get_nested({"user": {}}, ["user", "missing"])              → None
```
