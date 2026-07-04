"""
Exercise 1.21 - Import & Modules
==================================

LEARNING GOALS:
- Use import, from...import, import...as
- Understand the standard library (math, random, datetime, collections)
- Create and import your own module (cinema_utils.py)
- Understand if __name__ == "__main__"

STRUCTURE:
- Part 1: Standard library imports
- Part 2: from...import and import...as
- Part 3: Importing from your own module (cinema_utils.py)
- Part 4: if __name__ == "__main__"
"""

# =============================================================================
# PART 1 - STANDARD LIBRARY: import module
# =============================================================================
"""
CONCEPTS:
- Python ships with hundreds of built-in modules (the "standard library")
- import math → access everything via math.something
- No installation needed — always available

COMMON STANDARD LIBRARY MODULES:
- math       → sqrt, floor, ceil, pi, log
- random     → random(), randint(), choice(), shuffle()
- datetime   → date, time, datetime, timedelta
- os         → file paths, env variables, directory listing
- json       → loads(), dumps() — parse and create JSON
- collections→ Counter, defaultdict, deque
"""

import math
import random
import datetime


def get_movie_stats(ratings: list) -> dict:
    """
    Return basic stats for a list of ratings using math module.

    Args:
        ratings: List of float ratings

    Returns:
        dict: {'min': float, 'max': float, 'avg': float, 'rounded_avg': float}

    Example:
        >>> get_movie_stats([7.5, 8.0, 9.3, 6.1])
        {'min': 6.1, 'max': 9.3, 'avg': 7.725, 'rounded_avg': 8.0}
    """
    avg = sum(ratings) / len(ratings)  # sum(), min(), max() sono built-in, non math.*
    return {
        "min": min(ratings),
        "max": max(ratings),
        "avg": avg,
        "rounded_avg": float(round(avg)),  # round() senza decimali → intero più vicino
    }


def pick_random_movie(movies: list) -> str:
    """
    Return a random movie title from the list using random module.

    Args:
        movies: List of movie title strings

    Returns:
        str: One random title

    Example:
        >>> pick_random_movie(["Inception", "Matrix", "Interstellar"])
        'Matrix'   # (result varies)
    """
    return random.choice(movies)


def days_since_release(release_year: int) -> int:
    """
    Return approximate number of days since a movie's release year
    (calculated from Jan 1 of that year to today).

    Args:
        release_year: Year the movie was released

    Returns:
        int: Number of days

    Example:
        >>> days_since_release(2010) > 0
        True
    """
    release_date = datetime.datetime(release_year, 1, 1)
    today = datetime.datetime.now()
    delta = today - release_date
    return delta.days


# =============================================================================
# PART 2 - from...import AND import...as
# =============================================================================
"""
CONCEPTS:

    import math
    math.sqrt(16)          # must use module name as prefix

    from math import sqrt
    sqrt(16)               # no prefix needed

    import math as m
    m.sqrt(16)             # shorter alias

    from math import sqrt as sq
    sq(16)                 # alias for the function directly

WHEN TO USE WHICH:
- import module          → when you use many things from it
- from module import fn  → when you only need one or two things
- import module as alias → long names (numpy as np, pandas as pd)
"""

from math import floor, ceil
from random import choice, shuffle
from datetime import datetime as dt
from collections import Counter


def normalize_rating(rating: float) -> dict:
    """
    Return floor and ceil of a rating using the imported floor/ceil functions
    (not math.floor / math.ceil — imported directly).

    Args:
        rating: Float rating

    Returns:
        dict: {'floor': int, 'ceil': int}

    Example:
        >>> normalize_rating(7.3)
        {'floor': 7, 'ceil': 8}
        >>> normalize_rating(8.0)
        {'floor': 8, 'ceil': 8}
    """
    return {
        "floor": floor(rating),
        "ceil": ceil(rating),
    }


def most_common_genres(genre_list: list) -> list:
    """
    Return the 3 most common genres using Counter.

    Args:
        genre_list: List of genre strings (may repeat)

    Returns:
        list: [(genre, count), ...] — top 3

    Example:
        >>> genres = ["Drama", "Action", "Drama", "Sci-Fi", "Action", "Drama"]
        >>> most_common_genres(genres)
        [('Drama', 3), ('Action', 2), ('Sci-Fi', 1)]
    """
    return Counter(genre_list).most_common(3)


def current_timestamp() -> str:
    """
    Return current date and time as formatted string using dt alias.
    Format: "YYYY-MM-DD HH:MM"

    Returns:
        str: Formatted timestamp

    Example:
        >>> current_timestamp()
        '2026-06-03 14:30'  # (varies)
    """
    return dt.now().strftime("%Y-%m-%d %H:%M")


# =============================================================================
# PART 3 - YOUR OWN MODULE: cinema_utils.py
# =============================================================================
"""
CONCEPTS:
- Any .py file is a module
- Import it like any other module (must be in the same folder or in sys.path)
- cinema_utils.py contains: format_movie_title, is_valid_rating,
  rating_label, filter_by_year, and constants CURRENT_YEAR / MAX_RATING

Three ways to import it:
    import cinema_utils
    from cinema_utils import format_movie_title
    from cinema_utils import rating_label as label
"""

import cinema_utils
from cinema_utils import format_movie_title
from cinema_utils import rating_label as label

# from cinema_utils import filter_by_year as fil_year
# from cinema_utils import is_valid_rating as val_rat


def display_movie(title: str, year: int, rating: float) -> str:
    """
    Return a display string combining format_movie_title and rating_label.
    Use the imported format_movie_title function (direct import).
    Use the label alias for rating_label.

    Args:
        title: Movie title
        year: Release year
        rating: Float rating

    Returns:
        str: "Inception (2010) — Masterpiece"

    Example:
        >>> display_movie("Inception", 2010, 9.3)
        'Inception (2010) — Masterpiece'
        >>> display_movie("Morbius", 2022, 3.9)
        'Morbius (2022) — Poor'
    """
    return f"{format_movie_title(title, year)} - {label(rating)}"


def validate_and_filter(movies: list, min_year: int) -> list:
    """
    Filter movies by year using cinema_utils.filter_by_year (module prefix).
    Only include movies with a valid rating (use cinema_utils.is_valid_rating).

    Args:
        movies: List of dicts with 'title', 'year', 'rating' keys
        min_year: Minimum year filter

    Returns:
        list: Filtered movies

    Example:
        >>> movies = [
        ...     {"title": "Inception", "year": 2010, "rating": 9.3},
        ...     {"title": "Old Film", "year": 1800, "rating": 7.0},
        ...     {"title": "Bad Rating", "year": 2020, "rating": 15.0},
        ... ]
        >>> validate_and_filter(movies, 2000)
        [{"title": "Inception", "year": 2010, "rating": 9.3}]
    """
    my_movies = cinema_utils.filter_by_year(movies, min_year)
    return [
        movie for movie in my_movies if cinema_utils.is_valid_rating(movie["rating"])
    ]


# =============================================================================
# PART 4 - if __name__ == "__main__"
# =============================================================================
"""
CONCEPTS:
- Every Python file has a __name__ variable
- When run directly:  __name__ == "__main__"
- When imported:      __name__ == "exercise_1_21" (the filename)

WHY IT MATTERS:
- Lets you write test/demo code that only runs when you execute the file
- When another file imports this module, the test code is SKIPPED
- Standard pattern in every Python project

    # This runs when you do: python exercise-1.21.py
    if __name__ == "__main__":
        print("Running tests...")

    # This is SKIPPED when another file does: import exercise_1_21
"""

if __name__ == "__main__":
    # print("=" * 60)
    # print("PART 1 - STANDARD LIBRARY")
    # print("=" * 60)

    # ratings = [7.5, 8.0, 9.3, 6.1, 8.8]
    # print("\n1. Movie stats:", get_movie_stats(ratings))

    # movies = ["Inception", "The Matrix", "Interstellar", "Dune"]
    # print("2. Random pick:", pick_random_movie(movies))

    # print("3. Days since 2010:", days_since_release(2010))

    # print("\n" + "=" * 60)
    # print("PART 2 - FROM...IMPORT AND ALIASES")
    # print("=" * 60)

    # print("\n4. Normalize 7.3:", normalize_rating(7.3))

    # genres = ["Drama", "Action", "Drama", "Sci-Fi", "Action", "Drama", "Action"]
    # print("5. Top genres:", most_common_genres(genres))

    # print("6. Timestamp:", current_timestamp())

    # print("\n" + "=" * 60)
    # print("PART 3 - CUSTOM MODULE cinema_utils")
    # print("=" * 60)

    # print("\n7. CURRENT_YEAR from module:", cinema_utils.CURRENT_YEAR)
    # print("8. display_movie:", display_movie("Inception", 2010, 9.3))
    # print("9. display_movie:", display_movie("Morbius", 2022, 3.9))

    # test_movies = [
    #     {"title": "Inception", "year": 2010, "rating": 9.3},
    #     {"title": "Old Film", "year": 1800, "rating": 7.0},
    #     {"title": "Bad Rating", "year": 2020, "rating": 15.0},
    #     {"title": "Dune", "year": 2021, "rating": 8.0},
    # ]
    # print("10. Filtered movies:", validate_and_filter(test_movies, 2000))

    print("\n✅ Exercise 1.21 - Imports & Modules complete!")
    print("\nKEY TAKEAWAYS:")
    print("- import module         → access via module.something")
    print("- from module import fn → access directly, no prefix")
    print("- import module as m    → shorter alias")
    print("- Any .py file is a module — just import it")
    print("- if __name__ == '__main__' → runs only when executed directly")
