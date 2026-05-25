"""
Exercise 1.13 - Pure vs Impure Functions
=========================================

LEARNING GOALS:
- Understand pure functions (no side effects, deterministic)
- Recognize impure functions (modifies state, I/O, non-deterministic)
- Know when to use each type
- Understand why purity matters for testing and debugging

STRUCTURE:
- Part 1: Pure functions examples (6 functions)
- Part 2: Impure functions & refactoring (6 functions)
"""

from typing import List, Dict
import datetime
import random

# =============================================================================
# PART 1 - PURE FUNCTIONS
# =============================================================================
"""
CONCEPTS:
- Pure function: same input → always same output
- No side effects: doesn't modify external state
- No I/O: no file operations, no API calls, no print
- Deterministic: predictable, testable, cacheable
"""


def add_numbers(a: int, b: int) -> int:
    """
    Pure function: adds two numbers.

    Pure because:
    - Same inputs always return same output
    - No side effects
    - No external state modified

    Args:
        a: First number
        b: Second number

    Returns:
        int: Sum of a and b

    Example:
        >>> add_numbers(2, 3)
        5
        >>> add_numbers(2, 3)  # Always returns 5
        5
    """
    return a + b


def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Pure function: calculate price after discount.

    Args:
        price: Original price
        discount_percent: Discount percentage (0-100)

    Returns:
        float: Price after discount

    Example:
        >>> calculate_discount(100, 20)
        80.0
        >>> calculate_discount(100, 20)  # Deterministic
        80.0
    """
    return float(price * (1 - discount_percent / 100))


def filter_high_rated_pure(movies: List[dict], threshold: float) -> List[dict]:
    """
    Pure function: filter movies without modifying original list.

    Pure because:
    - Returns NEW list
    - Doesn't modify input
    - No external state

    Args:
        movies: List of movie dicts
        threshold: Minimum rating

    Returns:
        List[dict]: NEW list with filtered movies

    Example:
        >>> movies = [{'title': 'A', 'rating': 9.0}, {'title': 'B', 'rating': 6.0}]
        >>> result = filter_high_rated_pure(movies, 7.0)
        >>> len(result)
        1
        >>> len(movies)  # Original unchanged
        2
    """

    return [m for m in movies if m["rating"] > threshold]


def merge_dicts_pure(dict1: dict, dict2: dict) -> dict:
    """
    Pure function: merge two dicts without modifying originals.

    Args:
        dict1: First dictionary
        dict2: Second dictionary (overrides dict1)

    Returns:
        dict: NEW merged dictionary

    Example:
        >>> d1 = {'a': 1, 'b': 2}
        >>> d2 = {'b': 3, 'c': 4}
        >>> result = merge_dicts_pure(d1, d2)
        >>> result
        {'a': 1, 'b': 3, 'c': 4}
        >>> d1  # Original unchanged
        {'a': 1, 'b': 2}
    """
    dict3 = dict1 | dict2
    return dict3


def calculate_total_rating(movies: List[dict]) -> float:
    """
    Pure function: calculate average rating.

    Args:
        movies: List of movie dicts with 'rating' key

    Returns:
        float: Average rating (0 if empty list)

    Example:
        >>> movies = [{'rating': 8.0}, {'rating': 9.0}, {'rating': 7.0}]
        >>> calculate_total_rating(movies)
        8.0
    """
    total = 0
    for m in movies:
        total = total + m["rating"]
    return float(total / len(movies))


def format_movie_title_pure(title: str, year: int) -> str:
    """
    Pure function: format movie title.

    Args:
        title: Movie title
        year: Release year

    Returns:
        str: Formatted string

    Example:
        >>> format_movie_title_pure("Inception", 2010)
        'Inception (2010)'
    """
    return f"{title}, ({year})"


# =============================================================================
# PART 2 - IMPURE FUNCTIONS & REFACTORING
# =============================================================================
"""
CONCEPTS:
- Impure function: may return different outputs for same input
- Side effects: modifies external state, I/O operations
- Non-deterministic: uses random, time, external data
- Harder to test and debug

WHEN TO USE IMPURE:
- File I/O, database operations
- API calls
- User input
- Logging
- Modifying global state when necessary
"""

# Global state (makes functions impure if they modify it)
movie_database = []
request_count = 0


def add_movie_impure(movie: dict) -> None:
    """
    Impure function: modifies global state.

    Impure because:
    - Modifies global variable (movie_database)
    - Side effect visible outside function

    Args:
        movie: Movie dictionary to add

    Returns:
        None (modifies global state)

    Example:
        >>> add_movie_impure({'title': 'Inception', 'rating': 8.8})
        # movie_database is now modified
    """
    movie_database.append(movie)


def add_movie_pure(database: List[dict], movie: dict) -> List[dict]:
    """
    Pure version: returns NEW list instead of modifying global.

    Pure because:
    - Takes database as parameter
    - Returns NEW list
    - No global state modification

    Args:
        database: Current database list
        movie: Movie to add

    Returns:
        List[dict]: NEW database with movie added

    Example:
        >>> db = [{'title': 'Movie A'}]
        >>> new_db = add_movie_pure(db, {'title': 'Movie B'})
        >>> len(new_db)
        2
        >>> len(db)  # Original unchanged
        1
    """
    return database.append("movie")


import random as Random


def get_random_movie_impure(movies: List[dict]) -> dict:
    """
    Impure function: non-deterministic (uses random).

    Impure because:
    - Different output for same input
    - Uses random.choice()

    Args:
        movies: List of movies

    Returns:
        dict: Random movie (different each call)

    Example:
        >>> movies = [{'title': 'A'}, {'title': 'B'}, {'title': 'C'}]
        >>> movie1 = get_random_movie_impure(movies)
        >>> movie2 = get_random_movie_impure(movies)
        # movie1 and movie2 might be different
    """
    return movies[Random.randint(0, len(movies) - 1)]


def get_movie_by_index_pure(movies: List[dict], index: int) -> dict:
    """
    Pure version: deterministic selection.

    Pure because:
    - Same input always returns same output
    - No randomness

    Args:
        movies: List of movies
        index: Index to select

    Returns:
        dict: Movie at index

    Example:
        >>> movies = [{'title': 'A'}, {'title': 'B'}]
        >>> get_movie_by_index_pure(movies, 0)
        {'title': 'A'}
    """
    return movies[index]


import datetime


def log_movie_access_impure(movie_title: str) -> str:
    """
    Impure function: I/O operation (print) + uses current time.

    Impure because:
    - Side effect: prints to console
    - Uses datetime.now() (non-deterministic)
    - Modifies global request_count

    Args:
        movie_title: Title of accessed movie

    Returns:
        str: Log message

    Example:
        >>> log_movie_access_impure("Inception")
        # Prints: "[2024-01-15 10:30:45] Accessed: Inception"
        # Returns: log message string
    """
    return f"{datetime.now()} Accessed: {movie_title}"


def create_log_message_pure(movie_title: str, timestamp: str, count: int) -> str:
    """
    Pure version: takes timestamp and count as parameters.

    Pure because:
    - No side effects (no print)
    - Timestamp provided as parameter
    - Count provided as parameter
    - Same inputs always return same output

    Args:
        movie_title: Title of movie
        timestamp: Timestamp string
        count: Request count

    Returns:
        str: Log message

    Example:
        >>> create_log_message_pure("Inception", "2024-01-15 10:30:45", 5)
        '[2024-01-15 10:30:45] Request #5: Accessed Inception'
    """
    return f"{timestamp} Request #{count}: Accessed: {movie_title}"


def sort_movies_in_place_impure(movies: List[dict]) -> None:
    """
    Impure function: modifies input list.

    Impure because:
    - Modifies the input parameter
    - Side effect: original list is changed

    Args:
        movies: List of movies (will be modified!)

    Returns:
        None (modifies input)

    Example:
        >>> movies = [{'title': 'B', 'rating': 7.0}, {'title': 'A', 'rating': 9.0}]
        >>> sort_movies_in_place_impure(movies)
        >>> movies[0]['title']
        'A'  # List was modified
    """
    return movies.sort(key=lambda m: m["rating"], reverse=True)


def sort_movies_pure(movies: List[dict]) -> List[dict]:
    """
    Pure version: returns NEW sorted list.

    Pure because:
    - Returns NEW list
    - Original list unchanged

    Args:
        movies: List of movies

    Returns:
        List[dict]: NEW sorted list

    Example:
        >>> movies = [{'title': 'B', 'rating': 7.0}, {'title': 'A', 'rating': 9.0}]
        >>> sorted_movies = sort_movies_pure(movies)
        >>> sorted_movies[0]['title']
        'A'
        >>> movies[0]['title']
        'B'  # Original unchanged
    """
    return sorted(movies, key=lambda m: m["rating"], reverse=True)


# =============================================================================
# TESTS
# =============================================================================

if __name__ == "__main__":
    # print("=" * 70)
    # print("PART 1 - PURE FUNCTIONS")
    # print("=" * 70)

    # print("\n1. Add numbers (pure):")
    # print(f"2 + 3 = {add_numbers(2, 3)}")
    # print(f"2 + 3 = {add_numbers(2, 3)} (same result)")

    # print("\n2. Calculate discount (pure):")
    # print(f"$100 with 20% off: ${calculate_discount(100, 20)}")

    # print("\n3. Filter movies (pure - doesn't modify original):")
    # movies = [
    #     {"title": "Great Movie", "rating": 9.0},
    #     {"title": "Bad Movie", "rating": 5.0},
    #     {"title": "Good Movie", "rating": 7.5},
    # ]
    # high_rated = filter_high_rated_pure(movies, 7.0)
    # print(f"High rated: {[m['title'] for m in high_rated]}")
    # print(f"Original list still has {len(movies)} movies")

    # print("\n4. Merge dicts (pure):")
    # d1 = {"a": 1, "b": 2}
    # d2 = {"b": 3, "c": 4}
    # merged = merge_dicts_pure(d1, d2)
    # print(f"Merged: {merged}")
    # print(f"Original d1: {d1} (unchanged)")

    # print("\n5. Calculate average rating (pure):")
    # movies_rating = [{"rating": 8.0}, {"rating": 9.0}, {"rating": 7.0}]
    # avg = calculate_total_rating(movies_rating)
    # print(f"Average rating: {avg}")

    # print("\n6. Format title (pure):")
    # formatted = format_movie_title_pure("Inception", 2010)
    # print(f"Formatted: {formatted}")

    # print("\n" + "=" * 70)
    # print("PART 2 - IMPURE FUNCTIONS & REFACTORING")
    # print("=" * 70)

    # print("\n1. Add movie (impure vs pure):")
    # print("Impure version modifies global state:")
    # movie_database = []
    # add_movie_impure({"title": "Movie A"})
    # print(f"Global database: {movie_database}")

    # print("\nPure version returns new list:")
    # db = []
    # new_db = add_movie_pure(db, {"title": "Movie B"})
    # print(f"New database: {new_db}")
    # print(f"Original: {db} (unchanged)")

    # print("\n2. Random movie (impure vs pure):")
    # movies_random = [{"title": "A"}, {"title": "B"}, {"title": "C"}]
    # print("Impure (random - different each time):")
    # print(f"  Call 1: {get_random_movie_impure(movies_random)['title']}")
    # print(f"  Call 2: {get_random_movie_impure(movies_random)['title']}")

    # print("\nPure (by index - deterministic):")
    # print(f"  Index 0: {get_movie_by_index_pure(movies_random, 0)['title']}")
    # print(f"  Index 0: {get_movie_by_index_pure(movies_random, 0)['title']}")

    # print("\n3. Logging (impure vs pure):")
    # print("Impure (prints + uses current time):")
    # log_movie_access_impure("Inception")

    # print("\nPure (timestamp as parameter, no print):")
    # message = create_log_message_pure("Inception", "2024-01-15 10:30:45", 5)
    # print(f"Message: {message}")

    print("\n4. Sort movies (impure vs pure):")
    movies_sort1 = [
        {"title": "B", "rating": 7.0},
        {"title": "A", "rating": 9.0},
    ]
    print(f"Original: {[m['title'] for m in movies_sort1]}")

    print("\nImpure (modifies original):")
    sort_movies_in_place_impure(movies_sort1)
    print(f"After sort: {[m['title'] for m in movies_sort1]}")

    # movies_sort2 = [
    #     {"title": "B", "rating": 7.0},
    #     {"title": "A", "rating": 9.0},
    # ]
    # print("\nPure (returns new list):")
    # sorted_movies = sort_movies_pure(movies_sort2)
    # print(f"Sorted: {[m['title'] for m in sorted_movies]}")
    # print(f"Original: {[m['title'] for m in movies_sort2]} (unchanged)")

    # print("\n" + "=" * 70)
    # print("✅ Exercise 1.13 Complete!")
    # print("=" * 70)
    # print("\nKEY TAKEAWAYS:")
    # print("- Pure functions: same input → same output, no side effects")
    # print("- Impure functions: side effects, I/O, randomness, modifies state")
    # print("- Pure functions are easier to test, debug, and reason about")
    # print("- Prefer pure when possible, use impure when necessary (I/O, etc)")
    # print("- Refactoring tip: pass external state as parameters instead of using globals")
