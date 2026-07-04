"""
Exercise 1.17 - String Manipulation
====================================

LEARNING GOALS:
- Master string methods (split, join, replace, strip, lower, upper)
- Use f-strings for formatting
- Parse and extract data from strings
- Understand string immutability

STRUCTURE:
- Part 1: String methods (5 functions)
- Part 2: f-strings & parsing (5 functions)
"""

from typing import List, Dict, Tuple

# =============================================================================
# PART 1 - STRING METHODS
# =============================================================================
"""
CONCEPTS:
- Strings are IMMUTABLE - methods return NEW strings
- split() - string to list
- join() - list to string
- replace() - substitute text
- strip() - remove whitespace
- lower()/upper() - case conversion
"""


def clean_movie_title(title: str) -> str:
    """
    Clean movie title: strip whitespace and title case.

    Args:
        title: Raw movie title

    Returns:
        str: Cleaned title

    Example:
        >>> clean_movie_title("  inception  ")
        'Inception'
        >>> clean_movie_title("the DARK knight")
        'The Dark Knight'
    """
    return title.strip()


def normalize_genre(genre: str) -> str:
    """
    Normalize genre to lowercase without spaces.

    Args:
        genre: Genre string (may have spaces, mixed case)

    Returns:
        str: Normalized genre

    Example:
        >>> normalize_genre("Sci-Fi Action")
        'sci-fi-action'
        >>> normalize_genre("  Horror  ")
        'horror'
    """
    return genre.strip().lower()


def extract_words(text: str) -> List[str]:
    """
    Split text into words (by spaces).

    Args:
        text: Text string

    Returns:
        List[str]: List of words

    Example:
        >>> extract_words("The quick brown fox")
        ['The', 'quick', 'brown', 'fox']
        >>> extract_words("one,two,three")
        ['one,two,three']
    """
    return text.split(" ")


def join_with_separator(words: List[str], separator: str = ", ") -> str:
    """
    Join list of words with separator.

    Args:
        words: List of strings
        separator: Separator string (default ", ")

    Returns:
        str: Joined string

    Example:
        >>> join_with_separator(["apple", "banana", "cherry"])
        'apple, banana, cherry'
        >>> join_with_separator(["2024", "05", "26"], separator="-")
        '2024-05-26'
    """
    return separator.join(words)


def replace_spaces_with_dash(text: str) -> str:
    """
    Replace all spaces with dashes.

    Args:
        text: Text with spaces

    Returns:
        str: Text with dashes instead of spaces

    Example:
        >>> replace_spaces_with_dash("hello world")
        'hello-world'
        >>> replace_spaces_with_dash("The Dark Knight")
        'The-Dark-Knight'
    """
    return text.replace(" ", "-")


# =============================================================================
# PART 2 - F-STRINGS & PARSING
# =============================================================================
"""
CONCEPTS:
- f-strings: f"Hello {name}" - modern string formatting
- Format expressions: f"{value:.2f}" - number formatting
- Parsing: extract data from structured strings
- String slicing: text[start:end]
"""


def format_movie_info(title: str, year: int, rating: float) -> str:
    """
    Format movie info using f-string.

    Args:
        title: Movie title
        year: Release year
        rating: Rating (0-10)

    Returns:
        str: Formatted string

    Example:
        >>> format_movie_info("Inception", 2010, 8.8)
        'Inception (2010) - Rating: 8.8/10'
        >>> format_movie_info("Interstellar", 2014, 8.6)
        'Interstellar (2014) - Rating: 8.6/10'
    """
    return f"{title} ({year}) - Rating: {rating}/10"


def format_price_with_decimals(price: float) -> str:
    """
    Format price with 2 decimal places using f-string.

    Args:
        price: Price value

    Returns:
        str: Formatted price string

    Example:
        >>> format_price_with_decimals(19.5)
        '$19.50'
        >>> format_price_with_decimals(100)
        '$100.00'
    """
    return f"${price:.2f}"


def parse_movie_string(movie_str: str) -> Dict[str, any]:
    """
    Parse movie string in format "Title (Year) - Rating".

    Args:
        movie_str: String like "Inception (2010) - 8.8"

    Returns:
        Dict: {'title': str, 'year': int, 'rating': float}

    Example:
        >>> parse_movie_string("Inception (2010) - 8.8")
        {'title': 'Inception', 'year': 2010, 'rating': 8.8}
        >>> parse_movie_string("The Matrix (1999) - 8.7")
        {'title': 'The Matrix', 'year': 1999, 'rating': 8.7}
    """
    # Split by " - " per separare title+year da rating
    parts = movie_str.split(" - ")
    title_year = parts[0]  # "Inception (2010)"
    rating = parts[1]  # "8.8"

    # Split title_year per estrarre title e year
    title = title_year[: title_year.index("(")].strip()
    year_str = title_year[title_year.index("(") + 1 : title_year.index(")")]

    return {"title": title, "year": int(year_str), "rating": float(rating)}


def extract_domain_from_email(email: str) -> str:
    """
    Extract domain from email address.

    Args:
        email: Email address

    Returns:
        str: Domain part

    Example:
        >>> extract_domain_from_email("user@example.com")
        'example.com'
        >>> extract_domain_from_email("andrea@gmail.com")
        'gmail.com'
    """
    return email.split("@")[1]


def build_url_from_parts(protocol: str, domain: str, path: str) -> str:
    """
    Build URL from parts using f-string.

    Args:
        protocol: 'http' or 'https'
        domain: Domain name
        path: Path (with leading /)

    Returns:
        str: Complete URL

    Example:
        >>> build_url_from_parts("https", "api.example.com", "/v1/movies")
        'https://api.example.com/v1/movies'
        >>> build_url_from_parts("http", "localhost:8000", "/health")
        'http://localhost:8000/health'
    """
    return f"{protocol}://{domain}{path}"


# =============================================================================
# BONUS - COMMON STRING PATTERNS
# =============================================================================
"""
Real-world string manipulation patterns
"""


def slugify(text: str) -> str:
    """
    Convert text to URL-friendly slug.

    Steps:
    1. Lowercase
    2. Replace spaces with dashes
    3. Remove special characters (keep letters, numbers, dashes)

    Args:
        text: Text to slugify

    Returns:
        str: URL-friendly slug

    Example:
        >>> slugify("The Dark Knight")
        'the-dark-knight'
        >>> slugify("Movie Title 2024!")
        'movie-title-2024'
    """
    pass


def count_words(text: str) -> int:
    """
    Count words in text (split by spaces).

    Args:
        text: Text string

    Returns:
        int: Number of words

    Example:
        >>> count_words("Hello world")
        2
        >>> count_words("The quick brown fox jumps")
        5
    """
    pass


def truncate_text(text: str, max_length: int = 50) -> str:
    """
    Truncate text to max length, add "..." if truncated.

    Args:
        text: Text to truncate
        max_length: Maximum length (default 50)

    Returns:
        str: Truncated text

    Example:
        >>> truncate_text("This is a short text", 50)
        'This is a short text'
        >>> truncate_text("This is a very long text that needs truncating", 20)
        'This is a very lo...'
    """
    pass


# =============================================================================
# TESTS
# =============================================================================

if __name__ == "__main__":
    # print("=" * 70)
    # print("PART 1 - STRING METHODS")
    # print("=" * 70)

    # print("\n1. Clean movie title:")
    # print(f"'{clean_movie_title('  inception  ')}'")
    # print(f"'{clean_movie_title('the DARK knight')}'")

    # print("\n2. Normalize genre:")
    # print(f"'{normalize_genre('Sci-Fi Action')}'")
    # print(f"'{normalize_genre('  Horror  ')}'")

    # print("\n3. Extract words:")
    # words = extract_words("The quick brown fox")
    # print(f"Words: {words}")

    # print("\n4. Join with separator:")
    # print(f"Comma: {join_with_separator(['apple', 'banana', 'cherry'])}")
    # print(f"Dash: {join_with_separator(['2024', '05', '26'], '-')}")

    # print("\n5. Replace spaces:")
    # print(f"'{replace_spaces_with_dash('hello world')}'")
    # print(f"'{replace_spaces_with_dash('The Dark Knight')}'")

    # print("\n" + "=" * 70)
    # print("PART 2 - F-STRINGS & PARSING")
    # print("=" * 70)

    # print("\n1. Format movie info:")
    # print(format_movie_info("Inception", 2010, 8.8))
    # print(format_movie_info("Interstellar", 2014, 8.6))

    # print("\n2. Format price:")
    # print(format_price_with_decimals(19.5))
    # print(format_price_with_decimals(100))

    print("\n3. Parse movie string:")
    parsed = parse_movie_string("Inception (2010) - 8.8")
    print(f"Parsed: {parsed}")

    # print("\n4. Extract domain:")
    # print(f"Domain: {extract_domain_from_email('user@example.com')}")
    # print(f"Domain: {extract_domain_from_email('andrea@gmail.com')}")

    # print("\n5. Build URL:")
    # url = build_url_from_parts("https", "api.example.com", "/v1/movies")
    # print(f"URL: {url}")

    # print("\n" + "=" * 70)
    # print("BONUS - COMMON PATTERNS")
    # print("=" * 70)

    # print("\n1. Slugify:")
    # print(f"'{slugify('The Dark Knight')}'")
    # print(f"'{slugify('Movie Title 2024!')}'")

    # print("\n2. Count words:")
    # print(f"Words in 'Hello world': {count_words('Hello world')}")

    # print("\n3. Truncate text:")
    # short = "This is short"
    # long = "This is a very long text that needs truncating for display"
    # print(f"Short: '{truncate_text(short, 20)}'")
    # print(f"Long:  '{truncate_text(long, 30)}'")

    # print("\n" + "=" * 70)
    # print("✅ Exercise 1.17 Complete!")
    # print("=" * 70)
    # print("\nKEY TAKEAWAYS:")
    # print("- Strings are IMMUTABLE - methods return NEW strings")
    # print("- split() → list, join() → string")
    # print("- strip() removes whitespace, replace() substitutes text")
    # print("- f-strings: f'Hello {name}' - modern, readable formatting")
    # print("- f'{value:.2f}' - format numbers with precision")
    # print("- Parsing: use split(), slicing, string methods to extract data")
