"""
cinema_utils.py — Custom module for Exercise 1.21

This is a MODULE: a .py file that contains reusable functions,
constants, and classes that other files can import.

Usage:
    import cinema_utils
    from cinema_utils import format_movie_title
    from cinema_utils import format_movie_title as fmt
"""

# Module-level constants (accessible via cinema_utils.CURRENT_YEAR)
CURRENT_YEAR = 2026
MIN_VALID_YEAR = 1888  # year of the first film ever made
MAX_RATING = 10.0


def format_movie_title(title: str, year: int) -> str:
    """Return formatted title string: 'Inception (2010)'"""
    return f"{title} ({year})"


def is_valid_rating(rating: float) -> bool:
    """Return True if rating is between 0 and 10."""
    return 0 <= rating <= MAX_RATING


def rating_label(rating: float) -> str:
    """Return human-readable label for a rating score."""
    if rating >= 9.0:
        return "Masterpiece"
    elif rating >= 7.5:
        return "Great"
    elif rating >= 6.0:
        return "Good"
    elif rating >= 4.0:
        return "Average"
    else:
        return "Poor"


def filter_by_year(movies: list, min_year: int) -> list:
    """Return movies released from min_year onwards."""
    return [m for m in movies if m.get("year", 0) >= min_year]


if __name__ == "__main__":
    # This block runs ONLY when you execute cinema_utils.py directly,
    # NOT when it's imported by another file.
    print("cinema_utils.py — running as main script (not imported)")
    print(format_movie_title("Inception", 2010))
    print(rating_label(9.3))
