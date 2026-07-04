"""
Exercise 1.16 - Iteration Tools
================================

LEARNING GOALS:
- Master enumerate() for index + value iteration
- Use zip() for parallel iteration
- Understand map() and filter() (functional programming)
- Know when to use comprehensions vs map/filter

STRUCTURE:
- Part 1: enumerate & zip (4 functions)
- Part 2: map & filter (4 functions)
"""

from typing import List, Tuple, Dict

# =============================================================================
# PART 1 - ENUMERATE & ZIP
# =============================================================================
"""
CONCEPTS:
- enumerate(iterable, start=0): yields (index, value) tuples
- zip(iter1, iter2, ...): pairs elements from multiple iterables
- Stops at shortest iterable
"""


def add_ranking_enumerate(movies: List[dict]) -> List[dict]:
    """
    Add ranking number to each movie using enumerate.

    Args:
        movies: List of movie dicts (assumed sorted by rating)

    Returns:
        List[dict]: Movies with 'rank' field added (1-indexed)

    Example:
        >>> movies = [
        ...     {'title': 'Great', 'rating': 9.5},
        ...     {'title': 'Good', 'rating': 8.0}
        ... ]
        >>> ranked = add_ranking_enumerate(movies)
        >>> ranked[0]['rank']
        1
        >>> ranked[1]['rank']
        2
    """
    # Create NEW list with rank added (pure function)
    return [
        {**movie, "rank": rank}
        for rank, movie in enumerate(movies, start=1)
    ]


def find_index_of_movie(movies: List[dict], title: str) -> int:
    """
    Find index of movie by title using enumerate.

    Args:
        movies: List of movie dicts
        title: Title to search for

    Returns:
        int: Index of movie, or -1 if not found

    Example:
        >>> movies = [{'title': 'A'}, {'title': 'B'}, {'title': 'C'}]
        >>> find_index_of_movie(movies, 'B')
        1
        >>> find_index_of_movie(movies, 'Z')
        -1
    """
    for index, movie in enumerate(movies):
        if movie["title"] == title:
            return index
    return -1


def merge_movie_data_zip(
    titles: List[str], years: List[int], ratings: List[float]
) -> List[dict]:
    """
    Merge parallel lists into list of dicts using zip.

    Args:
        titles: Movie titles
        years: Release years
        ratings: Ratings

    Returns:
        List[dict]: Movies as dicts

    Example:
        >>> titles = ['Movie A', 'Movie B']
        >>> years = [2010, 2015]
        >>> ratings = [8.5, 9.0]
        >>> movies = merge_movie_data_zip(titles, years, ratings)
        >>> movies[0]
        {'title': 'Movie A', 'year': 2010, 'rating': 8.5}
    """
    return [
        {"title": t, "year": y, "rating": r}
        for t, y, r in zip(titles, years, ratings)
    ]


def compare_two_lists_zip(
    list1: List[any], list2: List[any]
) -> List[Tuple[any, any, bool]]:
    """
    Compare elements from two lists using zip.

    Args:
        list1: First list
        list2: Second list

    Returns:
        List[Tuple]: List of (elem1, elem2, are_equal)

    Example:
        >>> compare_two_lists_zip([1, 2, 3], [1, 5, 3])
        [(1, 1, True), (2, 5, False), (3, 3, True)]
    """
    return [(elem1, elem2, elem1 == elem2) for elem1, elem2 in zip(list1, list2)]


# =============================================================================
# PART 2 - MAP & FILTER
# =============================================================================
"""
CONCEPTS:
- map(function, iterable): applies function to each element
- filter(function, iterable): keeps elements where function returns True
- Returns iterators (need list() to materialize)
- Comprehensions are often more Pythonic
"""


def extract_titles_map(movies: List[dict]) -> List[str]:
    """
    Extract titles using map (compare with comprehension).

    Args:
        movies: List of movie dicts

    Returns:
        List[str]: Movie titles

    Example:
        >>> movies = [{'title': 'A', 'year': 2010}, {'title': 'B', 'year': 2015}]
        >>> extract_titles_map(movies)
        ['A', 'B']
    """
    title = list(map(lambda m: m["title"], movies))
    return title


def double_ratings_map(ratings: List[float]) -> List[float]:
    """
    Double all ratings using map with lambda.

    Args:
        ratings: List of ratings

    Returns:
        List[float]: Doubled ratings

    Example:
        >>> double_ratings_map([7.5, 8.0, 9.0])
        [15.0, 16.0, 18.0]
    """
    doubled = list(map(lambda x: x * 2, ratings))
    return doubled


def filter_high_rated_filter(movies: List[dict], threshold: float) -> List[dict]:
    """
    Filter movies using filter() function.

    Args:
        movies: List of movie dicts
        threshold: Minimum rating

    Returns:
        List[dict]: High-rated movies

    Example:
        >>> movies = [
        ...     {'title': 'Great', 'rating': 9.0},
        ...     {'title': 'Bad', 'rating': 5.0}
        ... ]
        >>> filter_high_rated_filter(movies, 7.0)
        [{'title': 'Great', 'rating': 9.0}]
    """
    # Use FILTER not map! filter keeps elements where lambda returns True
    filtered = list(filter(lambda x: x["rating"] > threshold, movies))
    return filtered


def chain_map_filter(numbers: List[int]) -> List[int]:
    """
    Chain map and filter: square numbers, then keep only > 10.

    Demonstrates functional programming style.

    Args:
        numbers: List of integers

    Returns:
        List[int]: Squared numbers > 10

    Example:
        >>> chain_map_filter([1, 2, 3, 4, 5])
        [16, 25]
    """
    result = list(map(lambda x: x**2, numbers))
    return list(filter(lambda x: x > 10, result))


# =============================================================================
# BONUS - COMPREHENSION VS MAP/FILTER
# =============================================================================
"""
When to use what:
- Comprehensions: More Pythonic, readable for simple cases
- map/filter: Functional style, good with existing functions
- Rule of thumb: Prefer comprehensions unless you have a good reason
"""


def compare_approaches(movies: List[dict]) -> Dict[str, List[str]]:
    """
    Compare comprehension vs map for extracting titles.

    Returns both results to show they're equivalent.

    Args:
        movies: List of movie dicts

    Returns:
        Dict: {'comprehension': [...], 'map': [...]}

    Example:
        >>> movies = [{'title': 'A'}, {'title': 'B'}]
        >>> result = compare_approaches(movies)
        >>> result['comprehension'] == result['map']
        True
    """
    pass


# =============================================================================
# TESTS
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PART 1 - ENUMERATE & ZIP")
    print("=" * 70)

    # print("\n1. Add ranking with enumerate:")
    # movies = [
    #     {"title": "Excellent Movie", "rating": 9.5},
    #     {"title": "Great Movie", "rating": 9.0},
    #     {"title": "Good Movie", "rating": 8.0},
    # ]
    # ranked = add_ranking_enumerate(movies)
    # for movie in ranked:
    #     print(f"  #{movie['rank']}: {movie['title']} ({movie['rating']})")

    # print("\n2. Find index of movie:")
    # movies = [{"title": "A"}, {"title": "B"}, {"title": "C"}]
    # print(f"Index of 'B': {find_index_of_movie(movies, 'B')}")
    # print(f"Index of 'Z': {find_index_of_movie(movies, 'Z')}")

    # print("\n3. Merge data with zip:")
    # titles = ["Inception", "Interstellar", "Dunkirk"]
    # years = [2010, 2014, 2017]
    # ratings = [8.8, 8.6, 7.9]
    # merged = merge_movie_data_zip(titles, years, ratings)
    # print("Merged movies:")
    # for movie in merged:
    #     print(f"  {movie}")

    # print("\n4. Compare lists with zip:")
    # list1 = [1, 2, 3, 4]
    # list2 = [1, 5, 3, 7]
    # comparison = compare_two_lists_zip(list1, list2)
    # print("Comparison:")
    # print(comparison)
    # for elem1, elem2, equal in comparison:
    #     status = "✓" if equal else "✗"
    #     print(f"  {elem1} vs {elem2}: {status}")

    print("\n" + "=" * 70)
    print("PART 2 - MAP & FILTER")
    print("=" * 70)

    # print("\n1. Extract titles with map:")
    # movies = [{"title": "Movie A", "year": 2010}, {"title": "Movie B", "year": 2015}]
    # titles = extract_titles_map(movies)
    # print(f"Titles: {titles}")

    # print("\n2. Double ratings with map:")
    # ratings = [7.5, 8.0, 9.0]
    # doubled = double_ratings_map(ratings)
    # print(f"Original: {ratings}")
    # print(f"Doubled: {doubled}")

    # print("\n3. Filter movies with filter():")
    # movies = [
    #     {"title": "Great Movie", "rating": 9.0},
    #     {"title": "Bad Movie", "rating": 5.0},
    #     {"title": "Good Movie", "rating": 7.5},
    # ]
    # high_rated = filter_high_rated_filter(movies, 7.0)
    # print(f"High-rated (>7.0): {[m['title'] for m in high_rated]}")

    print("\n4. Chain map + filter:")
    numbers = [1, 2, 3, 4, 5]
    result = chain_map_filter(numbers)
    print(f"Numbers: {numbers}")
    print(f"Squared & >10: {result}")

    # print("\n" + "=" * 70)
    # print("BONUS - COMPREHENSION VS MAP/FILTER")
    # print("=" * 70)

    # print("\nCompare approaches:")
    # movies = [{"title": "A"}, {"title": "B"}, {"title": "C"}]
    # result = compare_approaches(movies)
    # print(f"Comprehension: {result['comprehension']}")
    # print(f"Map:           {result['map']}")
    # print(f"Same result? {result['comprehension'] == result['map']}")

    # print("\n" + "=" * 70)
    # print("✅ Exercise 1.16 Complete!")
    # print("=" * 70)
    # print("\nKEY TAKEAWAYS:")
    # print("- enumerate(): get index + value in loops")
    # print("- zip(): iterate multiple lists in parallel")
    # print("- map(): transform elements (returns iterator)")
    # print("- filter(): select elements (returns iterator)")
    # print("- Prefer comprehensions for readability (Pythonic)")
    # print("- Use map/filter when you have existing functions to apply")
