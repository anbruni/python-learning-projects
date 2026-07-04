"""
Week 2 Checkpoint — Self-Assessment
=====================================

Mescola TUTTO quello che hai imparato nelle settimane 1-2.
Se riesci a completare queste 4 parti senza guardare indietro, sei pronto per la Week 3.

CONCETTI USATI:
- Data structures (list, dict, set, tuple)
- Comprehensions (list, dict, set)
- Functions (*args, **kwargs, default params, pure functions)
- Error handling (try/except, raise)
- Generators (yield, memory efficiency)
- Collections (Counter, defaultdict)
- Strings (f-strings, methods)
- Mutability & copy
- Imports (datetime, copy)

STRUTTURA:
- Part 1: Movie catalog builder (structures + comprehensions + strings)
- Part 2: Flexible filter engine (functions + error handling)
- Part 3: Genre statistics (generators + Counter + defaultdict)
- Part 4: Data pipeline (mutability + sets + datetime)
"""

import copy
from collections import Counter, defaultdict
from datetime import datetime
from typing import Generator

# ── dati di test ──────────────────────────────────────────────────────────────
MOVIES = [
    {
        "title": "Inception",
        "year": 2010,
        "rating": 8.8,
        "genres": ["Sci-Fi", "Thriller"],
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "genres": ["Action", "Drama"],
    },
    {
        "title": "Interstellar",
        "year": 2014,
        "rating": 8.6,
        "genres": ["Sci-Fi", "Drama"],
    },
    {"title": "Parasite", "year": 2019, "rating": 8.5, "genres": ["Drama", "Thriller"]},
    {"title": "Dune", "year": 2021, "rating": 8.0, "genres": ["Sci-Fi", "Drama"]},
    {"title": "Morbius", "year": 2022, "rating": 5.2, "genres": ["Action"]},
    {"title": "The Room", "year": 2003, "rating": 3.7, "genres": ["Drama"]},
    {
        "title": "Mad Max: Fury Road",
        "year": 2015,
        "rating": 8.1,
        "genres": ["Action", "Sci-Fi"],
    },
]


# =============================================================================
# PART 1 — MOVIE CATALOG BUILDER
# Concetti: dict, list, set, tuple, comprehensions, f-strings, string methods
# =============================================================================
"""
TASK: costruisci funzioni che trasformano MOVIES in strutture utili.
"""


def build_title_index(movies: list) -> dict:
    """
    Build a dict mapping lowercase title → full movie dict.
    Useful for fast lookups by title.

    Args:
        movies: List of movie dicts

    Returns:
        dict: {'inception': {...}, 'dune': {...}, ...}

    Example:
        >>> idx = build_title_index(MOVIES)
        >>> idx["inception"]["rating"]
        8.8
        >>> idx["dune"]["year"]
        2021
    """
    # YOUR CODE HERE — usa una dict comprehension
    # hint: lower() sul titolo come chiave
    return {m["title"].lower(): m for m in movies}


def format_movie_label(movie: dict) -> str:
    """
    Return a formatted string: "Title (Year) ★ Rating"

    Args:
        movie: Dict with 'title', 'year', 'rating'

    Returns:
        str: Formatted label

    Example:
        >>> format_movie_label({"title": "Inception", "year": 2010, "rating": 8.8})
        'Inception (2010) ★ 8.8'
    """
    return f"{movie["title"]} ({movie["year"]}) ★ {movie["rating"]}"


def movies_above_rating(movies: list, threshold: float) -> list:
    """
    Return a list of formatted labels for movies with rating >= threshold.
    Use format_movie_label and a list comprehension.

    Args:
        movies: List of movie dicts
        threshold: Minimum rating

    Returns:
        list: Formatted labels sorted alphabetically by title

    Example:
        >>> movies_above_rating(MOVIES, 8.5)
        ['Inception (2010) ★ 8.8', 'Interstellar (2014) ★ 8.6', ...]
    """
    # YOUR CODE HERE — list comprehension + sorted()
    return sorted([format_movie_label(m) for m in movies if m["rating"] >= threshold])


def unique_genres(movies: list) -> set:
    """
    Return the set of all unique genres across all movies.

    Args:
        movies: List of movie dicts

    Returns:
        set: All unique genre strings

    Example:
        >>> unique_genres(MOVIES) == {'Sci-Fi', 'Thriller', 'Action', 'Drama'}
        True
    """
    # YOUR CODE HERE — set comprehension oppure set + loop
    # hint: ogni film ha una lista di genres
    genres = set()
    for m in movies:
        for g in m["genres"]:
            genres.add(g)

    return genres


# =============================================================================
# PART 2 — FLEXIBLE FILTER ENGINE
# Concetti: **kwargs, error handling, raise, default params, pure functions
# =============================================================================
"""
TASK: scrivi un filtro flessibile che accetta criteri opzionali via **kwargs.
"""


def filter_movies(movies: list, **criteria) -> list:
    """
    Filter movies by any combination of criteria.
    Supported keys: min_rating, max_rating, min_year, max_year, genre.

    Args:
        movies: List of movie dicts
        **criteria: Filter criteria as keyword arguments

    Returns:
        list: Movies matching ALL criteria

    Raises:
        ValueError: if min_rating or max_rating is outside 0-10
        ValueError: if min_year > max_year

    Examples:
        >>> filter_movies(MOVIES, min_rating=8.5)
        [...]  # movies with rating >= 8.5

        >>> filter_movies(MOVIES, genre="Sci-Fi", min_year=2014)
        [...]  # Sci-Fi movies from 2014 onward

        >>> filter_movies(MOVIES, min_rating=11)
        ValueError: min_rating must be between 0 and 10
    """
    # YOUR CODE HERE
    # 1. Valida i criteri (raise ValueError se non validi)
    # 2. Filtra con un loop o list comprehension
    # hint: 'genre' → controlla se il genere è nella lista movie['genres']
    min_rating = criteria.get("min_rating")
    max_rating = criteria.get("max_rating")
    min_year = criteria.get("min_year")
    max_year = criteria.get("max_year")
    if min_rating is not None and (min_rating < 0 or min_rating > 10):
        raise ValueError("min_rating must be between 0 and 10")
    if max_rating is not None and (max_rating < 0 or max_rating > 10):
        raise ValueError("max_rating must be between 0 and 10")
    if min_year is not None and max_year is not None and min_year > max_year:
        raise ValueError("min_year cannot be greater than max_year")

    return [
        m
        for m in movies
        if (min_rating is None or min_rating <= m["rating"])
        and (max_rating is None or m["rating"] <= max_rating)
        and (min_year is None or min_year <= m["year"])
        and (max_year is None or m["year"] <= max_year)
        and (criteria.get("genre") is None or criteria["genre"] in m["genres"])
    ]


def safe_get_movie(index: dict, title: str) -> dict | None:
    """
    Look up a movie by title (case-insensitive).
    Return None if not found — don't raise.

    Args:
        index: Dict from build_title_index()
        title: Movie title to look up (any case)

    Returns:
        dict | None: Movie dict or None

    Example:
        >>> idx = build_title_index(MOVIES)
        >>> safe_get_movie(idx, "INCEPTION")
        {"title": "Inception", ...}
        >>> safe_get_movie(idx, "Avatar")
        None
    """
    # YOUR CODE HERE — usa .get() sul dict, non try/except
    return index.get(title.lower())


# =============================================================================
# PART 3 — GENRE STATISTICS
# Concetti: generators, Counter, defaultdict
# =============================================================================
"""
TASK: analizza i generi usando strutture efficienti in memoria.
"""


def stream_high_rated(
    movies: list, threshold: float = 7.0
) -> Generator[dict, None, None]:
    """
    Generator that yields movies with rating >= threshold one at a time.
    Memory efficient: doesn't build a list.

    Args:
        movies: List of movie dicts
        threshold: Minimum rating (default 7.0)

    Yields:
        dict: Movie dict

    Example:
        >>> gen = stream_high_rated(MOVIES, 8.5)
        >>> next(gen)["title"]
        'The Dark Knight'
    """
    # YOUR CODE HERE — usa yield
    yield from (m for m in movies if m["rating"] >= threshold)


def genre_counts(movies: list) -> Counter:
    """
    Count how many movies belong to each genre.
    A movie with 2 genres counts once per genre.

    Args:
        movies: List of movie dicts

    Returns:
        Counter: {genre: count, ...} sorted by frequency

    Example:
        >>> gc = genre_counts(MOVIES)
        >>> gc["Drama"]
        5
        >>> gc.most_common(1)
        [('Drama', 5)]
    """
    # YOUR CODE HERE — usa Counter
    # hint: Counter può essere aggiornato con .update()
    counter = Counter()
    counter.update(g for m in movies for g in m["genres"])
    return list(counter.most_common())


def movies_by_genre(movies: list) -> dict:
    """
    Group movie titles by genre using defaultdict.

    Args:
        movies: List of movie dicts

    Returns:
        dict: {genre: [title, title, ...], ...}

    Example:
        >>> mbg = movies_by_genre(MOVIES)
        >>> "Inception" in mbg["Sci-Fi"]
        True
        >>> "Parasite" in mbg["Drama"]
        True
    """
    # YOUR CODE HERE — usa defaultdict(list)
    movie_default = defaultdict(list)
    for m in movies:
        for g in m["genres"]:
            movie_default[g].append(m["title"])

    return movie_default


# =============================================================================
# PART 4 — DATA PIPELINE
# Concetti: mutability, deep copy, sets, datetime import, pure function
# =============================================================================
"""
TASK: dimostra di capire la mutabilità e scrivi una pipeline senza side effects.
"""


def add_timestamp(movie: dict) -> dict:
    """
    Return a NEW dict with a 'fetched_at' key added (current timestamp).
    Do NOT modify the original dict — return a copy with the new field.

    Args:
        movie: Original movie dict

    Returns:
        dict: New dict with 'fetched_at' key added

    Example:
        >>> m = {"title": "Dune", "year": 2021, "rating": 8.0}
        >>> result = add_timestamp(m)
        >>> "fetched_at" in result
        True
        >>> "fetched_at" in m   # original is unchanged
        False
    """
    # YOUR CODE HERE — usa copy.copy() o {**movie}
    # datetime.now().isoformat() per il timestamp
    new_movie = movie.copy()
    new_movie["fetched_at"] = str(datetime.now().isoformat())
    return new_movie


def normalize_movies(movies: list) -> list:
    """
    Return a new list where each movie has:
    - title stripped and title-cased
    - rating rounded to 1 decimal
    - genres sorted alphabetically

    Do NOT modify the originals — return deep-copied, normalized movies.

    Args:
        movies: List of movie dicts

    Returns:
        list: New list of normalized movie dicts (originals unchanged)

    Example:
        >>> raw = [{"title": "  inception ", "year": 2010, "rating": 8.823, "genres": ["Thriller", "Sci-Fi"]}]
        >>> norm = normalize_movies(raw)
        >>> norm[0]["title"]
        'Inception'
        >>> norm[0]["rating"]
        8.8
        >>> norm[0]["genres"]
        ['Sci-Fi', 'Thriller']
        >>> raw[0]["title"]   # original unchanged
        '  inception '
    """
    # YOUR CODE HERE — usa copy.deepcopy per ogni film, poi modifica la copia
    new_movie = []
    for m in movies:
        new_m = copy.deepcopy(m)
        new_m["title"] = new_m["title"].strip().title()
        new_m["rating"] = round(new_m["rating"], 1)
        new_m["genres"] = sorted(new_m["genres"])
        new_movie.append(new_m)
    return new_movie


def genre_overlap(movies_a: list, movies_b: list) -> set:
    """
    Return the set of genres that appear in BOTH lists.
    Use set operations (intersection), not loops.

    Args:
        movies_a: First list of movie dicts
        movies_b: Second list of movie dicts

    Returns:
        set: Common genres

    Example:
        >>> sci_fi = [{"genres": ["Sci-Fi", "Drama"]}]
        >>> action = [{"genres": ["Action", "Drama"]}]
        >>> genre_overlap(sci_fi, action)
        {'Drama'}
    """
    # YOUR CODE HERE — usa set intersection (&)
    # hint: unique_genres() da Part 1 può aiutarti
    return unique_genres(movies_a) & unique_genres(movies_b)


# =============================================================================
# MAIN — esegui per verificare le tue soluzioni
# =============================================================================

if __name__ == "__main__":
    # print("=" * 60)
    # print("WEEK 2 CHECKPOINT — Self Assessment")
    # print("=" * 60)

    # print("\n--- PART 1: Catalog Builder ---")
    # idx = build_title_index(MOVIES)
    # print(idx)
    # if idx:
    #     print("Title index keys:", list(idx.keys())[:3], "...")
    #     print("Lookup 'inception':", idx.get("inception", {}).get("rating"))

    # label = format_movie_label(MOVIES[0])
    # print("Label:", label)

    # top = movies_above_rating(MOVIES, 8.5)
    # print("Above 8.5:", top)

    # genres = unique_genres(MOVIES)
    # print("Unique genres:", genres)

    # print("\n--- PART 2: Filter Engine ---")
    # try:
    #     sci_fi_new = filter_movies(MOVIES, genre="Sci-Fi", min_year=2014)
    #     print("Sci-Fi >= 2014:", [m["title"] for m in sci_fi_new])

    #     filter_movies(MOVIES, min_rating=11)  # should raise
    # except ValueError as e:
    #     print(f"Caught expected error: {e}")

    # found = safe_get_movie(idx or {}, "DUNE")
    # foundandre = safe_get_movie(idx or {}, "DUNEANDRE")
    # print("safe_get DUNE:", found["title"] if found else None)
    # print("safe_get DUNEANDRE:", foundandre["title"] if foundandre else None)

    # print("\n--- PART 3: Genre Statistics ---")
    # gen = stream_high_rated(MOVIES, 8.5)
    # print("stream first title:", next(gen, {}).get("title"))

    # gc = genre_counts(MOVIES)
    # print("Genre counts:", dict(gc))

    # mbg = movies_by_genre(MOVIES)
    # print("Sci-Fi titles:", mbg.get("Sci-Fi", []))

    print("\n--- PART 4: Data Pipeline ---")
    # original = MOVIES[0].copy()
    # stamped = add_timestamp(original)
    # print("Has fetched_at:", "fetched_at" in (stamped or {}))
    # print("Original unchanged:", "fetched_at" not in original)

    raw = [
        {
            "title": "  inception ",
            "year": 2010,
            "rating": 8.823,
            "genres": ["Thriller", "Sci-Fi"],
        }
    ]
    norm = normalize_movies(raw)
    if norm:
        print("Normalized title:", norm[0]["title"])
        print("Normalized rating:", norm[0]["rating"])
        print("Sorted genres:", norm[0]["genres"])
        print("Original title unchanged:", raw[0]["title"])

    # sci_fi_movies = [m for m in MOVIES if "Sci-Fi" in m["genres"]]
    # action_movies = [m for m in MOVIES if "Action" in m["genres"]]
    # print("Genre overlap (Sci-Fi ∩ Action):", genre_overlap(sci_fi_movies, action_movies))

    # print("\n✅ Week 2 Checkpoint complete!")
    # print("Se tutte le funzioni ritornano i valori attesi → sei pronto per Week 3.")
