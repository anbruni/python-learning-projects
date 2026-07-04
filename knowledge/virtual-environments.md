# Virtual Environments in Python

> Isola le dipendenze di ogni progetto per evitare conflitti tra versioni

## Table of Contents
1. [Perché servono](#perché-servono)
2. [Creare e attivare](#creare-e-attivare)
3. [pip — installare pacchetti](#pip--installare-pacchetti)
4. [requirements.txt](#requirementstxt)
5. [Flusso di lavoro standard](#flusso-di-lavoro-standard)
6. [Cosa NON committare](#cosa-non-committare)

---

## Perché servono

Senza venv, tutti i pacchetti vengono installati **globalmente** — lo stesso Python per tutti i progetti. Questo crea conflitti:

```
Progetto A  →  requests==2.28   (richiede versione vecchia)
Progetto B  →  requests==2.31   (richiede versione nuova)
```

Con un virtual environment ogni progetto ha il **suo Python + i suoi pacchetti**, completamente isolati.

---

## Creare e attivare

```bash
# 1. Crea il venv (una volta sola per progetto)
python -m venv venv

# 2. Attiva (ogni volta che apri un nuovo terminale)
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows

# Il prompt cambia:
# (venv) $  ← sei dentro

# 3. Verifica
which python                    # .../venv/bin/python
python --version

# 4. Disattiva quando hai finito
deactivate
```

### Struttura interna del venv

```
venv/
├── bin/           ← python e pip del venv (Mac/Linux)
├── lib/           ← pacchetti installati
└── pyvenv.cfg     ← punta all'interprete Python base
```

---

## pip — installare pacchetti

```bash
# Installare
pip install requests
pip install requests==2.31.0   # versione specifica

# Vedere cosa è installato
pip list
pip show requests               # dettagli su un pacchetto

# Disinstallare
pip uninstall requests

# Aggiornare
pip install --upgrade requests
```

---

## requirements.txt

Il file che **congela** le dipendenze del progetto. Permette a chiunque di ricreare l'ambiente esatto.

```bash
# Genera il file (snapshot dell'ambiente corrente)
pip freeze > requirements.txt

# Installa da requirements.txt (su un'altra macchina o dopo aver clonato il repo)
pip install -r requirements.txt
```

Esempio di `requirements.txt`:
```
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.7
requests==2.32.3
urllib3==2.2.1
```

> `pip freeze` cattura **tutti** i pacchetti incluse le sotto-dipendenze. È una snapshot esatta.

---

## Flusso di lavoro standard

Ogni volta che inizi un nuovo progetto:

```bash
# 1. Crea il progetto
mkdir my-project && cd my-project

# 2. Crea il venv
python -m venv venv

# 3. Attiva
source venv/bin/activate

# 4. Installa le dipendenze
pip install requests pandas

# 5. Salva le dipendenze
pip freeze > requirements.txt

# 6. Aggiungi venv/ al .gitignore
echo "venv/" >> .gitignore

# 7. Committa solo requirements.txt (non il venv)
git add requirements.txt .gitignore
```

Quando qualcuno clona il repo:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt   # ripristina l'ambiente esatto
```

---

## Cosa NON committare

```gitignore
# .gitignore
venv/          # mai committare il venv — è riproducibile da requirements.txt
__pycache__/
*.pyc
.env           # secrets — mai committare
```

| Cosa | Commit? | Perché |
|------|---------|--------|
| `venv/` | ❌ No | Pesante, riproducibile, path-dipendente |
| `requirements.txt` | ✅ Sì | Permette di ricreare l'ambiente |
| `.env` | ❌ No | Contiene segreti/chiavi API |
| `.env.example` | ✅ Sì | Mostra le variabili necessarie senza i valori reali |

---

## Verificare se sei in un venv

```python
import sys

in_venv = sys.prefix != sys.base_prefix
print(f"In venv: {in_venv}")
print(f"Python:  {sys.executable}")
```

Se `in_venv` è `False`, il tuo codice sta usando il Python globale — attiva il venv prima di installare pacchetti.
