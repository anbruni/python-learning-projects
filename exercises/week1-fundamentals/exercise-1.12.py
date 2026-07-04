"""
Exercise 1.12 - List, Dict & Set Comprehensions
===============================================

LEARNING GOALS:
- Master list comprehensions (basic, with filter, nested)
- Use dict comprehensions for data transformation
- Use set comprehensions for unique values
- Understand when comprehensions beat loops

STRUCTURE:
- Part 1: List comprehensions (6 functions)
- Part 2: Dict & set comprehensions (6 functions)
"""

from typing import List, Dict, Set

# =============================================================================
# PART 1 - LIST COMPREHENSIONS
# =============================================================================
"""
CONCEPTS:
- Basic: [expr for item in iterable]
- With filter: [expr for item in iterable if condition]
- Nested: [expr for x in iter1 for y in iter2]
- Transform + filter in one line
"""


def double_numbers(numbers: List[int]) -> List[int]:
    """
    Double all numbers using list comprehension.

    Args:
        numbers: List of integers

    Returns:
        List[int]: Doubled numbers

    Example:
        >>> double_numbers([1, 2, 3, 4, 5])
        [2, 4, 6, 8, 10]
        >>> double_numbers(range(5))
        [0, 2, 4, 6, 8]
    """
    return [x * 2 for x in numbers]


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filter even numbers using list comprehension.

    Args:
        numbers: List of integers

    Returns:
        List[int]: Only even numbers

    Example:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        >>> filter_even_numbers(range(10))
        [0, 2, 4, 6, 8]
    """
    return [x for x in numbers if x % 2 == 0]


def transform_and_filter(numbers: List[int], threshold: int = 10) -> List[int]:
    """
    Square numbers and keep only those above threshold.

    Args:
        numbers: List of integers
        threshold: Minimum value to keep

    Returns:
        List[int]: Squared numbers above threshold

    Example:
        >>> transform_and_filter([1, 2, 3, 4, 5])
        [16, 25]
        >>> transform_and_filter([1, 2, 3, 4, 5], threshold=5)
        [9, 16, 25]
    """
    return [x**2 for x in numbers if x**2 > threshold]


def extract_movie_titles(movies: List[dict], min_rating: float = 0.0) -> List[str]:
    """
    Extract titles from movies with rating filter.

    Args:
        movies: List of movie dicts
        min_rating: Minimum rating filter

    Returns:
        List[str]: Filtered movie titles

    Example:
        >>> movies = [
        ...     {'title': 'Great Movie', 'rating': 9.0},
        ...     {'title': 'Bad Movie', 'rating': 5.0},
        ...     {'title': 'Good Movie', 'rating': 7.5}
        ... ]
        >>> extract_movie_titles(movies, 7.0)
        ['Great Movie', 'Good Movie']
    """
    return [m["title"] for m in movies if m["rating"] > min_rating]


def nested_combinations(range1: int, range2: int) -> List[tuple]:
    """
    Create all combinations of two ranges using nested comprehension.

    Args:
        range1: First range size
        range2: Second range size

    Returns:
        List[tuple]: All (x, y) combinations

    Example:
        >>> nested_combinations(2, 3)
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
        >>> nested_combinations(3, 2)
        [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
    """
    return [(x, y) for x in range(range1) for y in range(range2) if x + y == 3]


def flatten_nested_list(nested: List[List[int]]) -> List[int]:
    """
    Flatten 2D list using nested comprehension.

    Args:
        nested: List of lists

    Returns:
        List[int]: Flattened list

    Example:
        >>> flatten_nested_list([[1, 2], [3, 4], [5]])
        [1, 2, 3, 4, 5]
        >>> flatten_nested_list([[1, 2, 3], [4, 5]])
        [1, 2, 3, 4, 5]
    """
    return [item for row in nested for item in row]


# =============================================================================
# PART 2 - DICT & SET COMPREHENSIONS
# =============================================================================
"""
CONCEPTS:
- Dict comprehension: {key: value for item in iterable}
- Set comprehension: {expr for item in iterable}
- Transform datasets (list of dicts → dict, etc.)
"""


def create_squares_dict(n: int) -> Dict[int, int]:
    """
    Create dict of numbers to their squares.

    Args:
        n: Range limit (0 to n-1)

    Returns:
        Dict[int, int]: {number: square}

    Example:
        >>> create_squares_dict(5)
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
        >>> create_squares_dict(3)
        {0: 0, 1: 1, 2: 4}
    """
    return {v: v**2 for v in range(n)}


def invert_dict(data: Dict[str, int]) -> Dict[int, str]:
    """
    Swap keys and values using dict comprehension.

    Args:
        data: Original dictionary

    Returns:
        Dict: Inverted dictionary

    Example:
        >>> invert_dict({'a': 1, 'b': 2, 'c': 3})
        {1: 'a', 2: 'b', 3: 'c'}
        >>> invert_dict({'US': 100, 'EU': 200})
        {100: 'US', 200: 'EU'}
    """
    return {v: k for k, v in data.items()}


def movies_by_id(movies: List[dict]) -> Dict[int, dict]:
    """
    Create lookup dict: id -> movie.

    Args:
        movies: List of movie dicts with 'id' key

    Returns:
        Dict[int, dict]: Lookup table

    Example:
        >>> movies = [
        ...     {'id': 1, 'title': 'Inception', 'year': 2010},
        ...     {'id': 2, 'title': 'Interstellar', 'year': 2014}
        ... ]
        >>> lookup = movies_by_id(movies)
        >>> lookup[1]['title']
        'Inception'
    """
    return {m["id"]: m for m in movies}


def filter_dict_by_value(data: Dict[str, int], threshold: int) -> Dict[str, int]:
    """
    Filter dict keeping only values above threshold.

    Args:
        data: Dictionary to filter
        threshold: Minimum value

    Returns:
        Dict: Filtered dictionary

    Example:
        >>> scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
        >>> filter_dict_by_value(scores, 80)
        {'Alice': 85, 'Bob': 92, 'Diana': 95}
    """
    return {k: v for k, v in data.items() if v > threshold}


def extract_unique_genres(movies: List[dict]) -> Set[str]:
    """
    Extract unique genres using set comprehension.

    Args:
        movies: List of movie dicts with 'genre' key

    Returns:
        Set[str]: Unique genres

    Example:
        >>> movies = [
        ...     {'title': 'Movie A', 'genre': 'Action'},
        ...     {'title': 'Movie B', 'genre': 'Drama'},
        ...     {'title': 'Movie C', 'genre': 'Action'}
        ... ]
        >>> sorted(extract_unique_genres(movies))
        ['Action', 'Drama']
    """
    return set({m["genre"] for m in movies})


def unique_lengths(words: List[str]) -> Set[int]:
    """
    Get unique word lengths using set comprehension.

    Args:
        words: List of strings

    Returns:
        Set[int]: Unique lengths

    Example:
        >>> words = ['cat', 'dog', 'elephant', 'ant', 'tiger']
        >>> sorted(unique_lengths(words))
        [3, 5, 8]
        >>> sorted(unique_lengths(['a', 'bb', 'ccc', 'dd']))
        [1, 2, 3]
    """
    return {len(word) for word in words}


# =============================================================================
# TESTS
# =============================================================================


if __name__ == "__main__":
    # print("=" * 70)
    # print("PART 1 - LIST COMPREHENSIONS")
    # print("=" * 70)

    # print("\n1. Double numbers:")
    # print(f"[1,2,3,4,5] doubled: {double_numbers([1, 2, 3, 4, 5])}")
    # print(f"range(5) doubled: {double_numbers(list(range(5)))}")

    # print("\n2. Filter even numbers:")
    # print(f"Even from [1-6]: {filter_even_numbers([1, 2, 3, 4, 5, 6])}")
    # print(f"Even from range(10): {filter_even_numbers(list(range(10)))}")

    # print("\n3. Transform and filter:")
    # print(f"Squares > 10 from [1-5]: {transform_and_filter([1, 2, 3, 4, 5])}")
    # print(f"Squares > 5 from [1-5]: {transform_and_filter([1, 2, 3, 4, 5], 5)}")

    # print("\n4. Extract movie titles:")
    # movies = [
    #     {"title": "Great Movie", "rating": 9.0},
    #     {"title": "Bad Movie", "rating": 5.0},
    #     {"title": "Good Movie", "rating": 7.5},
    # ]
    # print(f"Movies with rating >= 7.0:")
    # print(f"  {extract_movie_titles(movies, 7.0)}")

    # print("\n5. Nested combinations:")
    # print(f"Combinations (2,3): {nested_combinations(2, 3)}")

    # print("\n6. Flatten nested list:")
    # nested = [[1, 2], [3, 4], [5]]
    # print(f"Nested: {nested}")
    # print(f"Flat: {flatten_nested_list(nested)}")

    # print("\n" + "=" * 70)
    # print("PART 2 - DICT & SET COMPREHENSIONS")
    # print("=" * 70)

    # print("\n1. Create squares dict:")
    # print(f"Squares 0-4: {create_squares_dict(5)}")

    # print("\n2. Invert dict:")
    # original = {"a": 1, "b": 2, "c": 3}
    # inverted = invert_dict(original)
    # print(f"Original: {original}")
    # print(f"Inverted: {inverted}")

    # print("\n3. Movies by ID:")
    # movies_data = [
    #     {"id": 1, "title": "Inception", "year": 2010},
    #     {"id": 2, "title": "Interstellar", "year": 2014},
    # ]
    # lookup = movies_by_id(movies_data)
    # print(f"Movie with id=1: {lookup[1]['title']}")
    # print(f"Movie with id=2: {lookup[2]['title']}")

    # print("\n4. Filter dict by value:")
    # scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
    # print(f"Original scores: {scores}")
    # print(f"Scores > 80: {filter_dict_by_value(scores, 80)}")

    # print("\n5. Extract unique genres:")
    # movies_genres = [
    #     {"title": "Movie A", "genre": "Action"},
    #     {"title": "Movie B", "genre": "Drama"},
    #     {"title": "Movie C", "genre": "Action"},
    #     {"title": "Movie D", "genre": "Comedy"},
    # ]
    # genres = sorted(extract_unique_genres(movies_genres))
    # print(f"Unique genres: {genres}")

    print("\n6. Unique word lengths:")
    words = ["cat", "dog", "elephant", "ant", "tiger"]
    lengths = sorted(unique_lengths(words))
    print(f"Words: {words}")
    print(f"Unique lengths: {lengths}")

# print("\n" + "=" * 70)
# print("✅ Exercise 1.12 Complete!")
# print("=" * 70)
# print("\nKEY TAKEAWAYS:")
# print("- List comprehension: cleaner than for loops for transform/filter")
# print("- Syntax: [expr for item in iterable if condition]")
# print("- Nested: [x for sublist in nested for x in sublist]")
# print("- Dict comprehension: {k: v for item in data}")
# print("- Set comprehension: {expr for item in data} - auto removes duplicates")
# print("- Use comprehensions for readability, loops for complex logic")
