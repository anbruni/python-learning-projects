"""
Exercise 2.3 - CSV Handling Manuale
=====================================

LEARNING GOALS:
- Capire perché split(",") da solo non basta per i CSV reali
- Usare csv.reader per leggere righe come liste
- Usare csv.writer per scrivere CSV correttamente (gestisce le virgolette per te)
- Usare csv.DictReader per leggere righe come dizionari
- Usare csv.DictWriter per scrivere da dizionari

DATA FILE: data/movies.csv   (ha header + edge cases con virgole nei titoli)
OUTPUT:    data/             (le tue funzioni creeranno file qui)

STRUCTURE:
- Part 1: Concept — csv module vs split() manuale, edge cases
- Part 2: csv.reader       → leggere righe come liste
- Part 3: csv.writer       → scrivere CSV correttamente
- Part 4: csv.DictReader   → leggere righe come dizionari (più comodo)
- Part 5: csv.DictWriter   → scrivere da dizionari
- Part 6: Cinema task      → filtrare per genere e salvare CSV
"""

import csv
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "movies.csv")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "data")


# =============================================================================
# PART 1 - CONCEPT: perché il modulo csv e non split()
# =============================================================================
"""
IL PROBLEMA CON split(","):

    line = '"The Good, the Bad and the Ugly",1966,Sergio Leone,8.8,Western'
    parts = line.split(",")
    # → ['"The Good', ' the Bad and the Ugly"', '1966', 'Sergio Leone', '8.8', 'Western']
    #   SBAGLIATO — ha spezzato il titolo in due!

IL CSV STANDARD (RFC 4180) gestisce questo con le virgolette:
    - Un campo con virgole al suo interno viene racchiuso tra "..."
    - Un campo con virgolette al suo interno usa "" per escape:  He said ""hello""
    - Le newlines dentro un campo sono permesse se il campo è quotato

IL MODULO csv RISOLVE TUTTO QUESTO:

    import csv
    with open("movies.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    # → ['The Good, the Bad and the Ugly', '1966', 'Sergio Leone', '8.8', 'Western']
    #   CORRETTO — il titolo è un unico campo

QUANDO USARE COSA:
    - split(",")    → solo per dati semplici e controllati che non avranno mai virgole
    - csv module    → per qualsiasi CSV reale (la scelta giusta quasi sempre)
    - pandas        → per analisi dati su CSV grandi (lo userai nelle settimane successive)

JS COMPARISON:
    // In Node.js non c'è un csv built-in, si usa una libreria (csv-parse, papaparse)
    // In Python csv è nella standard library — zero installazioni
"""


# =============================================================================
# PART 2 - csv.reader: leggere righe come liste
# =============================================================================


def read_all_movies(filepath: str) -> list[list[str]]:
    """
    YOUR TASK:
    Leggi il file CSV con csv.reader.
    Salta la prima riga (header) con next(reader).
    Ritorna una lista di righe — ogni riga è una lista di stringhe.

    HINT:
        with open(filepath, ...) as f:
            reader = csv.reader(f)
            next(reader)              # salta l'header
            for row in reader:
                rows.append(row)

    EXPECTED: lista di 12 liste, es:
        [['The Godfather', '1972', 'Francis Ford Coppola', '9.2', 'Crime'], ...]
        Nota: anche 'The Good, the Bad and the Ugly' deve essere UN solo campo.
    """
    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            rows.append(row)
    return rows


def get_header(filepath: str) -> list[str]:
    """
    YOUR TASK:
    Leggi SOLO la prima riga (l'header) del CSV.
    Ritorna quella riga come lista di stringhe.

    HINT: apri il file, crea il reader, chiama next(reader) una volta sola.

    EXPECTED: ['title', 'year', 'director', 'rating', 'genre']
    """
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(next(reader))


# =============================================================================
# PART 3 - csv.writer: scrivere CSV correttamente
# =============================================================================


def write_movies_csv(filepath: str, rows: list[list]) -> None:
    """
    YOUR TASK:
    Scrivi `rows` in un file CSV usando csv.writer.
    La prima riga deve essere l'header: ['title', 'year', 'director', 'rating', 'genre']
    Poi scrivi tutte le righe di `rows`.

    HINT:
        with open(filepath, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(['title', 'year', 'director', 'rating', 'genre'])
            writer.writerows(rows)

    NOTA: newline="" è NECESSARIO su Windows per evitare righe vuote doppie.
          Su Mac non cambia nulla ma è buona pratica metterlo sempre.

    EXPECTED: il file CSV risultante è leggibile da csv.reader,
              e i titoli con virgole sono automaticamente quotati.
    """
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "year", "director", "rating", "genre"])
        writer.writerows(rows)


# =============================================================================
# PART 4 - csv.DictReader: leggere come dizionari
# =============================================================================


def read_movies_as_dicts(filepath: str) -> list[dict]:
    """
    YOUR TASK:
    Leggi il CSV con csv.DictReader.
    Ritorna una lista di dizionari — ogni dict usa i nomi dell'header come chiavi.
    Converti 'year' in int e 'rating' in float prima di aggiungere al risultato.

    HINT:
        reader = csv.DictReader(f)
        # DictReader legge l'header automaticamente — non serve next()
        for row in reader:
            # row è un dict: {'title': 'The Godfather', 'year': '1972', ...}
            # i valori sono tutti stringhe — converti quelli numerici
            movie = dict(row)
            movie['year'] = int(movie['year'])
            movie['rating'] = float(movie['rating'])
            ...

    EXPECTED: lista di 12 dizionari, es:
        [{'title': 'The Godfather', 'year': 1972, 'director': 'Francis Ford Coppola',
          'rating': 9.2, 'genre': 'Crime'}, ...]
    """
    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie = dict(row)
            movie["year"] = int(movie["year"])
            movie["rating"] = float(movie["rating"])
            rows.append(movie)
    return rows


def get_directors(filepath: str) -> list[str]:
    """
    YOUR TASK:
    Usa DictReader per leggere il file.
    Ritorna una lista dei nomi dei registi, senza duplicati, in ordine alfabetico.

    HINT: usa un set() per eliminare i duplicati, poi sorted() per ordinare.

    EXPECTED: ['Christopher Nolan', 'David Fincher', 'Francis Ford Coppola',
               'Frank Darabont', 'Lana Wachowski', 'Martin Scorsese',
               'Quentin Tarantino', 'Sergio Leone', 'Stanley Kubrick',
               'Steven Spielberg']
    """
    # --- scrivi il tuo codice qui sotto ---
    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row["director"])
    return sorted(set(rows))


# =============================================================================
# PART 5 - csv.DictWriter: scrivere da dizionari
# =============================================================================


def write_movies_from_dicts(filepath: str, movies: list[dict]) -> None:
    """
    YOUR TASK:
    Scrivi `movies` (lista di dict) in un CSV usando csv.DictWriter.
    L'ordine delle colonne deve essere: title, year, director, rating, genre

    HINT:
        fieldnames = ['title', 'year', 'director', 'rating', 'genre']
        with open(filepath, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()        # scrive la riga header
            writer.writerows(movies)    # scrive tutti i dict

    EXPECTED: il file CSV ha l'header corretto e una riga per ogni dict in `movies`.
    """
    fieldnames = ["title", "year", "director", "rating", "genre"]
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(movies)


# =============================================================================
# PART 6 - CINEMA TASK: filtrare per regista e salvare CSV
# =============================================================================


def save_director_filmography(
    source_filepath: str, output_filepath: str, director_name: str
) -> int:
    """
    YOUR TASK:
    Leggi il CSV con DictReader.
    Filtra solo i film del regista `director_name` (case-insensitive).
    Scrivi i film trovati in `output_filepath` usando DictWriter
    con le stesse colonne dell'originale.
    Ritorna il numero di film scritti.

    HINT: usa str.lower() su entrambi i lati per il confronto case-insensitive.

    EXPECTED con director_name="Christopher Nolan":
        Ritorna 3
        Scrive: The Dark Knight, Inception, Interstellar
    """
    fieldnames = ["title", "year", "director", "rating", "genre"]
    count = 0
    with (
        open(source_filepath, "r", encoding="utf-8", newline="") as r,
        open(output_filepath, "w", encoding="utf-8", newline="") as w,
    ):
        reader = csv.DictReader(r)
        writer = csv.DictWriter(w, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if row["director"].lower() == director_name.lower():
                writer.writerow(row)
                count += 1
    return count


# =============================================================================
# RUNNER
# =============================================================================

if __name__ == "__main__":
    # print("=" * 55)
    # print("EXERCISE 2.3 — CSV Handling Manuale")
    # print("=" * 55)

    # # Part 2 — csv.reader
    # print("\n--- Part 2: csv.reader ---")
    # header = get_header(DATA_FILE)
    # if header:
    #     print(f"  Header: {header}")
    # else:
    #     print("  get_header: non ancora implementata.")

    rows = read_all_movies(DATA_FILE)
    # if rows:
    #     print(f"  Letti {len(rows)} film. Primo: {rows[0]}")
    #     edge_case = [r for r in rows if "Good" in r[0]]
    #     if edge_case:
    #         print(f"  Edge case OK — titolo con virgola: '{edge_case[0][0]}'")
    # else:
    #     print("  read_all_movies: non ancora implementata.")

    # Part 3 — csv.writer
    # print("\n--- Part 3: csv.writer ---")
    # if rows:
    #     out_writer = os.path.join(OUTPUT_DIR, "movies_copy.csv")
    #     write_movies_csv(out_writer, rows)
    #     if os.path.exists(out_writer):
    #         with open(out_writer, "r", encoding="utf-8") as f:
    #             lines = f.readlines()
    #         print(f"  Scritte {len(lines)} righe (incluso header) in movies_copy.csv")
    #         print(f"  Prima riga dati: {lines[1].strip()}")
    #     else:
    #         print("  write_movies_csv: non ancora implementata.")

    # Part 4 — csv.DictReader
    # print("\n--- Part 4: csv.DictReader ---")
    # movies = read_movies_as_dicts(DATA_FILE)
    # if movies:
    #     print(f"  Letti {len(movies)} film come dizionari.")
    #     print(f"  Primo film: {movies[0]}")
    #     print(
    #         f"  year type: {type(movies[0]['year'])}, rating type: {type(movies[0]['rating'])}"
    #     )
    # else:
    #     print("  read_movies_as_dicts: non ancora implementata.")

    # directors = get_directors(DATA_FILE)
    # if directors:
    #     print(f"  Registi unici ({len(directors)}): {directors}")
    # else:
    #     print("  get_directors: non ancora implementata.")

    # # Part 5 — csv.DictWriter
    # print("\n--- Part 5: csv.DictWriter ---")
    # if movies:
    #     out_dict = os.path.join(OUTPUT_DIR, "movies_dict_copy.csv")
    #     write_movies_from_dicts(out_dict, movies)
    #     if os.path.exists(out_dict):
    #         with open(out_dict, "r", encoding="utf-8") as f:
    #             first_lines = f.readlines()[:3]
    #         print(f"  movies_dict_copy.csv scritto. Prime 2 righe:")
    #         for line in first_lines:
    #             print(f"    {line.strip()}")
    #     else:
    #         print("  write_movies_from_dicts: non ancora implementata.")

    # Part 6 — Cinema task
    print("\n--- Part 6: filmografia regista ---")
    nolan_file = os.path.join(OUTPUT_DIR, "nolan_films.csv")
    count = save_director_filmography(DATA_FILE, nolan_file, "Christopher Nolan")
    if count:
        print(f"  {count} film di Christopher Nolan salvati in nolan_films.csv:")
        with open(nolan_file, "r", encoding="utf-8") as f:
            for line in f:
                print(f"    {line.strip()}")
    else:
        print("  save_director_filmography: non ancora implementata.")
