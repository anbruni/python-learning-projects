"""
Exercise 2.4 - JSON read/write
================================

LEARNING GOALS:
- json.load    → leggere JSON da file → Python dict/list
- json.loads   → parsare una stringa JSON → Python dict/list
- json.dump    → scrivere Python dict/list in file JSON
- json.dumps   → serializzare Python dict/list → stringa JSON
- Nested JSON  → accedere a dati annidati (liste e dict dentro dict)

DATA FILE: data/movies.json   (film con dati annidati: cast, awards, streaming)
OUTPUT:    data/              (le tue funzioni creeranno file qui)

STRUCTURE:
- Part 1: Concept  — JSON vs CSV, quando usare cosa, mapping tipi Python ↔ JSON
- Part 2: json.load / json.loads  → leggere JSON
- Part 3: json.dump / json.dumps  → scrivere JSON
- Part 4: Nested JSON             → accedere a cast[], awards{}, streaming[]
- Part 5: Cinema task             → creare watchlist personale e salvarla
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "movies.json")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "data")


# =============================================================================
# PART 1 - CONCEPT: JSON vs CSV, mapping tipi
# =============================================================================
"""
QUANDO USARE JSON vs CSV:

    CSV:
        - Dati tabulari (righe + colonne) — come un foglio Excel
        - Tutti i valori sono stringhe (devi convertire int/float manualmente)
        - No strutture annidate possibili
        - Ottimo per dataset semplici e compatibilità con Excel/pandas

    JSON:
        - Strutture arbitrarie: dict dentro dict, liste di oggetti, valori misti
        - Tipi preservati: int, float, bool, null, str, list, dict
        - Standard universale per API REST (quello che ricevi da fetch/axios)
        - Ottimo per config, API responses, dati con strutture variabili

MAPPING TIPI Python ↔ JSON:

    Python          JSON
    ─────────────────────
    dict        →   {}  (object)
    list        →   []  (array)
    str         →   "stringa"
    int / float →   42 / 3.14
    True/False  →   true/false
    None        →   null

LE 4 FUNZIONI:

    json.load(f)         → legge da file object    → Python object
    json.loads(s)        → legge da stringa        → Python object
    json.dump(obj, f)    → scrive su file object   → (nessun return)
    json.dumps(obj)      → scrive su stringa       → str

    MNEMONICO: load/dump = file, loads/dumps = string
               la 's' finale sta per 'string'

JS COMPARISON:
    // In JS usi JSON.parse() e JSON.stringify()
    const movies = JSON.parse(jsonString)      ≈  json.loads(json_str)
    const str    = JSON.stringify(movies, null, 2)  ≈  json.dumps(movies, indent=2)
    // Per file in Node.js usi fs.readFileSync + JSON.parse
    // In Python json.load() legge direttamente dal file object — più comodo
"""


# =============================================================================
# PART 2 - json.load e json.loads: leggere JSON
# =============================================================================


def load_movies(filepath: str) -> list[dict]:
    """
    YOUR TASK:
    Apri il file JSON e caricalo con json.load().
    Ritorna la lista di film (già come list[dict], tipi preservati).

    HINT:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    EXPECTED: lista di 12 dizionari, es:
        [{'title': 'The Godfather', 'year': 1972, 'rating': 9.2,
          'cast': ['Marlon Brando', 'Al Pacino', 'James Caan'],
          'awards': {'oscars': 3, 'nominations': 11}, ...}, ...]
        Nota: year è già int, rating è già float — nessuna conversione necessaria!
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_movie_json(json_str: str) -> dict:
    """
    YOUR TASK:
    Parsa la stringa JSON `json_str` con json.loads().
    Ritorna il dizionario risultante.

    HINT: json.loads(json_str)

    EXAMPLE INPUT:
        '{"title": "Inception", "year": 2010, "rating": 8.8}'

    EXPECTED OUTPUT:
        {'title': 'Inception', 'year': 2010, 'rating': 8.8}
        Nota: year è int e rating è float, non stringhe — JSON preserva i tipi.
    """
    return json.loads(json_str)


# =============================================================================
# PART 3 - json.dump e json.dumps: scrivere JSON
# =============================================================================


def save_movies_json(filepath: str, movies: list[dict]) -> None:
    """
    YOUR TASK:
    Scrivi `movies` nel file `filepath` usando json.dump().
    Usa indent=2 per formattazione leggibile (come JSON.stringify(obj, null, 2) in JS).
    Usa ensure_ascii=False per preservare caratteri non-ASCII (es. accenti).

    HINT:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(movies, f, indent=2, ensure_ascii=False)

    EXPECTED: il file risultante è JSON valido, formattato con 2 spazi di indentazione,
              leggibile da json.load() — stessa struttura dell'input.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2, ensure_ascii=False)


def movie_to_json_string(movie: dict) -> str:
    """
    YOUR TASK:
    Serializza SOLO i campi 'title', 'year', 'rating' del film in una stringa JSON.
    Usa indent=2.

    HINT:
        summary = {
            "title":  movie["title"],
            "year":   movie["year"],
            "rating": movie["rating"],
        }
        return json.dumps(summary, indent=2)

    EXAMPLE INPUT:
        {'title': 'Inception', 'year': 2010, 'director': 'Christopher Nolan',
         'rating': 8.8, 'genre': 'Sci-Fi', 'cast': [...], ...}

    EXPECTED OUTPUT (stringa):
        {
          "title": "Inception",
          "year": 2010,
          "rating": 8.8
        }
    """
    summary = {
        "title": movie["title"],
        "year": movie["year"],
        "rating": movie["rating"],
    }
    return json.dumps(summary, indent=2)


# =============================================================================
# PART 4 - Nested JSON: accedere a strutture annidate
# =============================================================================


def get_lead_actors(movies: list[dict]) -> list[dict]:
    """
    YOUR TASK:
    Per ogni film, estrai il primo elemento della lista `cast` (il protagonista).
    Ritorna una lista di dizionari: [{"title": ..., "lead_actor": ...}, ...]
    Ordinata per titolo (sorted).

    HINT:
        # cast è una lista → cast[0] è il primo attore
        result = []
        for movie in movies:
            result.append({
                "title": movie["title"],
                "lead_actor": movie["cast"][0],
            })
        return sorted(result, key=lambda x: x["title"])

    EXPECTED (prime 3 righe):
        [{'title': '2001: A Space Odyssey', 'lead_actor': 'Keir Dullea'},
         {'title': 'Fight Club', 'lead_actor': 'Brad Pitt'},
         {'title': 'Goodfellas', 'lead_actor': 'Ray Liotta'}, ...]
    """
    result = []
    for movie in movies:
        result.append(
            {
                "title": movie["title"],
                "lead_actor": movie["cast"][0],
            }
        )
    return sorted(result, key=lambda x: x["title"])


def total_oscar_nominations(movies: list[dict]) -> int:
    """
    YOUR TASK:
    Calcola il totale di nomination agli Oscar sommando `awards["nominations"]`
    di tutti i film.

    HINT:
        # awards è un dict annidato → movie["awards"]["nominations"]
        total = 0
        for movie in movies:
            total += movie["awards"]["nominations"]
        return total

    EXPECTED: 83
    """
    nom_tot = 0
    for movie in movies:
        nom_tot += movie["awards"]["nominations"]

    return nom_tot


def find_movies_on_platform(movies: list[dict], platform: str) -> list[str]:
    """
    YOUR TASK:
    Ritorna i titoli dei film disponibili sulla piattaforma `platform`
    (case-insensitive), in ordine alfabetico.

    HINT:
        # streaming è una lista → devi controllare se platform è IN quella lista
        # usa str.lower() su entrambi i lati per il confronto
        result = []
        for movie in movies:
            if any(p.lower() == platform.lower() for p in movie["streaming"]):
                result.append(movie["title"])
        return sorted(result)

    EXPECTED con platform="Netflix":
        ['Fight Club', 'Goodfellas', 'Inception', 'The Shawshank Redemption']
    """
    found_plat = []
    for movie in movies:
        if any(p.lower() == platform.lower() for p in movie["streaming"]):
            found_plat.append(movie["title"])
    return sorted(found_plat)


# =============================================================================
# PART 5 - CINEMA TASK: creare e salvare una watchlist
# =============================================================================


def create_watchlist(
    movies: list[dict], min_rating: float, output_filepath: str
) -> int:
    """
    YOUR TASK:
    1. Filtra i film con rating >= min_rating.
    2. Per ogni film filtrato, aggiungi un campo "watched": False.
    3. Salva la lista filtrata+arricchita in `output_filepath` con indent=2.
    4. Ritorna il numero di film salvati.

    NOTA: non modificare i dizionari originali — crea una copia con dict(movie)
          prima di aggiungere il campo "watched".

    HINT:
        watchlist = []
        for movie in movies:
            if movie["rating"] >= min_rating:
                entry = dict(movie)      # copia superficiale
                entry["watched"] = False
                watchlist.append(entry)
        with open(output_filepath, "w", encoding="utf-8") as f:
            json.dump(watchlist, f, indent=2, ensure_ascii=False)
        return len(watchlist)

    EXPECTED con min_rating=8.8:
        Ritorna 8
        Salva in watchlist.json: 8 film, ognuno con "watched": false
        (The Godfather 9.2, Shawshank 9.3, Dark Knight 9.0, Inception 8.8,
         Pulp Fiction 8.9, Schindler's 9.0, Good/Bad/Ugly 8.8, Fight Club 8.8)
        Nota: Goodfellas ha 8.7 → NON incluso perché 8.7 < 8.8
    """
    watchlist = []
    for movie in movies:
        if movie["rating"] >= min_rating:
            entry = dict(movie)
            entry["watched"] = False
            watchlist.append(entry)
    with open(output_filepath, "w", encoding="utf-8") as w:
        json.dump(watchlist, w, indent=2, ensure_ascii=False)
    return len(watchlist)


# =============================================================================
# RUNNER
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("EXERCISE 2.4 — JSON read/write")
    print("=" * 55)

    # Part 2 — json.load
    # print("\n--- Part 2: json.load / json.loads ---")
    movies = load_movies(DATA_FILE)
    # if movies:
    #     print(f"  Caricati {len(movies)} film. Primo: {movies[0]['title']}")
    #     print(
    #         f"  year type: {type(movies[0]['year'])}, rating type: {type(movies[0]['rating'])}"
    #     )
    #     print(f"  cast: {movies[0]['cast']}")
    #     print(f"  awards: {movies[0]['awards']}")
    # else:
    #     print("  load_movies: non ancora implementata.")

    # sample_json = '{"title": "Inception", "year": 2010, "rating": 8.8}'
    # parsed = parse_movie_json(sample_json)
    # if parsed:
    #     print(f"\n  parse_movie_json → {parsed}")
    #     print(f"  year type: {type(parsed['year'])}")
    # else:
    #     print("  parse_movie_json: non ancora implementata.")

    # Part 3 — json.dump / json.dumps
    # print("\n--- Part 3: json.dump / json.dumps ---")
    # if movies:
    #     out_path = os.path.join(OUTPUT_DIR, "movies_copy.json")
    #     save_movies_json(out_path, movies)
    #     if os.path.exists(out_path):
    #         print(f"  movies_copy.json scritto.")
    #         with open(out_path, "r", encoding="utf-8") as f:
    #             lines = f.readlines()
    #         print(f"  Righe totali: {len(lines)} (con indent=2)")
    #     else:
    #         print("  save_movies_json: non ancora implementata.")

    #     first_movie = movies[0]
    #     json_str = movie_to_json_string(first_movie)
    #     if json_str:
    #         print(f"\n  movie_to_json_string({first_movie['title']}):")
    #         print(f"  {json_str}")
    #     else:
    #         print("  movie_to_json_string: non ancora implementata.")

    # Part 4 — Nested JSON
    # print("\n--- Part 4: Nested JSON ---")
    # if movies:
    #     leads = get_lead_actors(movies)
    #     if leads:
    #         print(f"  Lead actors (prime 3): {leads[:3]}")
    #     else:
    #         print("  get_lead_actors: non ancora implementata.")

    #     total = total_oscar_nominations(movies)
    #     if total:
    #         print(f"  Totale nomination Oscar: {total}  (atteso: 83)")
    #     else:
    #         print("  total_oscar_nominations: non ancora implementata.")

    #     netflix = find_movies_on_platform(movies, "Netflix")
    #     if netflix:
    #         print(f"  Film su Netflix: {netflix}")
    #     else:
    #         print("  find_movies_on_platform: non ancora implementata.")

    # # Part 5 — Cinema task
    print("\n--- Part 5: Watchlist ---")
    if movies:
        watchlist_path = os.path.join(OUTPUT_DIR, "watchlist.json")
        count = create_watchlist(movies, 8.8, watchlist_path)
        if count:
            print(f"  {count} film salvati in watchlist.json  (atteso: 8)")
            with open(watchlist_path, "r", encoding="utf-8") as f:
                watchlist = json.load(f)
            print(
                f"  Primo elemento: {watchlist[0]['title']} | watched: {watchlist[0]['watched']}"
            )
        else:
            print("  create_watchlist: non ancora implementata.")
