"""
Exercise 1.9 - Functions: Basics, Parameters & Type Hints
==========================================================

KNOWLEDGE REFERENCE: /knowledge/functions.md

LEARNING GOALS:
- Define and call functions with different parameter types
- Use type hints (modern Python, essential for FastAPI)
- Master *args and **kwargs for flexible functions
- Understand default parameters and keyword arguments

STRUCTURE:
- Part 1: Function basics & type hints (6 functions)
- Part 2: *args, **kwargs & flexible parameters (6 functions)
"""

from typing import List, Dict, Optional, Union

# =============================================================================
# PART 1 - FUNCTION BASICS & TYPE HINTS
# =============================================================================
"""
CONCEPTS:
- def keyword, return values
- Type hints: int, str, float, List, Dict, Optional
- Default parameters
- Positional vs keyword arguments
"""


def calculate_tax(price: float, tax_rate: float = 0.22) -> float:
    """
    Calculate price with tax.

    Args:
        price: Base price
        tax_rate: Tax rate (default 22%)

    Returns:
        float: Total price with tax

    Example:
        >>> calculate_tax(100)
        122.0
        >>> calculate_tax(100, 0.10)
        110.0
    """
    return price * (1 + tax_rate)


def format_user_info(name: str, age: int, city: str = "Unknown") -> str:
    """
    Format user information as string.

    Args:
        name: User's name
        age: User's age
        city: User's city (optional, default "Unknown")

    Returns:
        str: Formatted string like "Andrea, 30 from Milan"

    Example:
        >>> format_user_info("Andrea", 30, "Milan")
        'Andrea, 30 from Milan'
        >>> format_user_info("Maria", 25)
        'Maria, 25 from Unknown'
    """
    return f"{name}, {age} from {city}"


def get_first_element(items: List[any]) -> Optional[any]:
    """
    Get first element from list, or None if empty.

    Args:
        items: List of any type

    Returns:
        Optional[any]: First element or None

    Example:
        >>> get_first_element([1, 2, 3])
        1
        >>> get_first_element([])
        None
    """
    if items:
        return items[0]
    return None


def create_movie_dict(
    title: str, year: int, rating: float
) -> Dict[str, Union[str, int, float]]:
    """
    Create movie dictionary with type-safe structure.

    Args:
        title: Movie title
        year: Release year
        rating: IMDB rating (0-10)

    Returns:
        Dict: Movie data

    Example:
        >>> create_movie_dict("Inception", 2010, 8.8)
        {'title': 'Inception', 'year': 2010, 'rating': 8.8}
    """
    return {"title": title, "year": year, "rating": rating}


def safe_divide(a: float, b: float) -> Optional[float]:
    """
    Divide two numbers, return None if division by zero.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Optional[float]: Result or None if b is 0

    Example:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(10, 0)
        None
    """
    if b == 0:
        return None
    return a / b


def greet_user(name: str, formal: bool = False) -> str:
    """
    Greet user formally or informally.

    Args:
        name: User's name
        formal: Use formal greeting (default False)

    Returns:
        str: Greeting message

    Example:
        >>> greet_user("Andrea")
        'Hey Andrea!'
        >>> greet_user("Andrea", formal=True)
        'Good day, Andrea.'
    """
    if formal:
        return f"Good day, {name}."
    return f"Hey {name}!"


# =============================================================================
# PART 2 - *ARGS, **KWARGS & FLEXIBLE PARAMETERS
# =============================================================================
"""
CONCEPTS:
- *args: variable positional arguments (tuple)
- **kwargs: variable keyword arguments (dict)
- Combining different parameter types
- Real-world API/data processing patterns
"""


def calculate_average(*numbers: float) -> float:
    """
    Calculate average of any number of values.

    Args:
        *numbers: Variable number of values

    Returns:
        float: Average value

    Example:
        >>> calculate_average(10, 20, 30)
        20.0
        >>> calculate_average(5, 15)
        10.0
        >>> calculate_average(100)
        100.0
    """
    return sum(numbers) / len(numbers)


def build_url(base: str, *paths: str, **params: any) -> str:
    """
    Build URL with paths and query parameters.

    Args:
        base: Base URL
        *paths: Path segments
        **params: Query parameters

    Returns:
        str: Complete URL

    Example:
        >>> build_url("https://api.example.com", "users", "123", active=True, limit=10)
        'https://api.example.com/users/123?active=True&limit=10'
        >>> build_url("https://api.example.com", format="json")
        'https://api.example.com?format=json'
    """
    # Build URL with paths
    url = base
    if paths:
        url += "/" + "/".join(paths)

    # Add query parameters
    if params:
        query = "&".join(f"{key}={value}" for key, value in params.items())
        url += "?" + query

    return url


def merge_dicts(*dicts: dict) -> dict:
    """
    Merge multiple dictionaries into one.
    Later dicts override earlier ones.

    Args:
        *dicts: Variable number of dictionaries

    Returns:
        dict: Merged dictionary

    Example:
        >>> merge_dicts({"a": 1}, {"b": 2}, {"a": 3})
        {'a': 3, 'b': 2}
        >>> merge_dicts({"name": "Andrea"}, {"age": 30, "city": "Milan"})
        {'name': 'Andrea', 'age': 30, 'city': 'Milan'}
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result


def log_event(event_type: str, *args, level: str = "INFO", **kwargs) -> dict:
    """
    Log event with flexible data (real-world pattern).

    Args:
        event_type: Type of event
        *args: Additional positional data
        level: Log level (keyword-only)
        **kwargs: Additional metadata

    Returns:
        dict: Log entry

    Example:
        >>> log_event("USER_LOGIN", "user123", level="INFO", ip="192.168.1.1")
        {'type': 'USER_LOGIN', 'level': 'INFO', 'args': ('user123',), 'meta': {'ip': '192.168.1.1'}}
    """
    return {"type": event_type, "level": level, "args": args, "meta": kwargs}


def create_api_request(endpoint: str, method: str = "GET", **data) -> dict:
    """
    Create API request object (pattern for API clients).

    Args:
        endpoint: API endpoint
        method: HTTP method (default GET)
        **data: Request data (body, query params, headers)

    Returns:
        dict: Request configuration

    Example:
        >>> create_api_request("/users", method="POST", body={"name": "Andrea"}, headers={"Auth": "token"})
        {'endpoint': '/users', 'method': 'POST', 'body': {'name': 'Andrea'}, 'headers': {'Auth': 'token'}}
    """
    return {"endpoint": endpoint, "method": method, **data}


def filter_movies(*movies: dict, **criteria) -> List[dict]:
    print(criteria)
    """
    Filter movies by multiple criteria.

    Args:
        *movies: Variable number of movie dicts
        **criteria: Filter criteria (e.g., min_year=2010, min_rating=8.0)

    Returns:
        List[dict]: Filtered movies

    Example:
        >>> movies = [
        ...     {"title": "Inception", "year": 2010, "rating": 8.8},
        ...     {"title": "Interstellar", "year": 2014, "rating": 8.6},
        ...     {"title": "Old Movie", "year": 1990, "rating": 7.0}
        ... ]
        >>> filter_movies(*movies, min_year=2010, min_rating=8.5)
        [{'title': 'Inception', 'year': 2010, 'rating': 8.8}, {'title': 'Interstellar', 'year': 2014, 'rating': 8.6}]
    """
    filtered = []
    for movie in movies:
        if "min_year" in criteria and movie["year"] < criteria["min_year"]:
            continue
        if "min_rating" in criteria and movie["rating"] < criteria["min_rating"]:
            continue
        filtered.append(movie)
    return filtered


# =============================================================================
# TESTS
# =============================================================================

if __name__ == "__main__":
    # print("=" * 70)
    # print("PART 1 - FUNCTION BASICS & TYPE HINTS")
    # print("=" * 70)

    # print("\n1. Calculate tax:")
    # print(f"100€ with default tax: {calculate_tax(100)}€")
    # print(f"100€ with 10% tax: {calculate_tax(100, 0.10)}€")

    # print("\n2. Format user info:")
    # print(format_user_info("Andrea", 30, "Milan"))
    # print(format_user_info("Maria", 25))

    # print("\n3. Get first element:")
    # print(f"From [1,2,3]: {get_first_element([1, 2, 3])}")
    # print(f"From []: {get_first_element([])}")

    # print("\n4. Create movie dict:")
    # movie = create_movie_dict("Inception", 2010, 8.8)
    # print(movie)

    # print("\n5. Safe divide:")
    # print(f"10 / 2 = {safe_divide(10, 2)}")
    # print(f"10 / 0 = {safe_divide(10, 0)}")

    # print("\n6. Greet user:")
    # print(greet_user("Andrea"))
    # print(greet_user("Andrea", formal=True))

    # print("\n" + "=" * 70)
    # print("PART 2 - *ARGS, **KWARGS & FLEXIBLE PARAMETERS")
    # print("=" * 70)

    # print("\n1. Calculate average:")
    # print(f"Average of 10,20,30: {calculate_average(10, 20, 30)}")
    # print(f"Average of 5,15: {calculate_average(5, 15)}")

    # print("\n2. Build URL:")
    # url1 = build_url(
    #     "https://api.example.com", "users", "123", active=True, limit=10
    # )
    # print(url1)
    # url2 = build_url("https://api.example.com", format="json")
    # print(url2)

    # Remaining tests commented until functions are implemented
    # print("\n3. Merge dicts:")
    # merged = merge_dicts({"a": 1}, {"b": 2}, {"a": 3})
    # print(merged)

    # print("\n4. Log event:")
    # log = log_event("USER_LOGIN", "user123", level="INFO", ip="192.168.1.1")
    # print(log)

    # print("\n5. Create API request:")
    # req = create_api_request(
    #     "/users", method="POST", body={"name": "Andrea"}, headers={"Auth": "token"}
    # )
    # print(req)

    print("\n6. Filter movies:")
    movies = [
        {"title": "Inception", "year": 2010, "rating": 8.8},
        {"title": "Interstellar", "year": 2014, "rating": 8.6},
        {"title": "Old Movie", "year": 1990, "rating": 7.0},
    ]
    filtered = filter_movies(*movies, min_year=2010, min_rating=8.5)
    print(f"Movies from 2010+ with rating 8.5+:")
    for m in filtered:
        print(f"  - {m['title']} ({m['year']}): {m['rating']}")

    print("\n" + "=" * 70)
    print("✅ Exercise 1.9 Complete!")
    print("=" * 70)
