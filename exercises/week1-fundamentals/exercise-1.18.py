"""
Exercise 1.18 - Error Handling
==============================

LEARNING GOALS:
- Master try/except/finally blocks
- Catch specific exceptions (ValueError, KeyError, ZeroDivisionError, etc.)
- Raise custom exceptions with meaningful messages
- Understand when to catch vs when to let fail
- Handle multiple exception types
- Use finally for cleanup

STRUCTURE:
- Part 1: Basic try/except (5 functions)
- Part 2: Specific exceptions (5 functions)
- Part 3: Raising exceptions (3 functions)
- Part 4: Real-world patterns (3 functions)
"""

from typing import Dict, List, Optional, Any

# =============================================================================
# PART 1 - BASIC TRY/EXCEPT
# =============================================================================
"""
CONCEPTS:
- try/except - catch and handle errors gracefully
- Generic Exception vs specific exceptions
- finally - always runs (cleanup)
- else - runs only if no exception
"""


def safe_divide(a: float, b: float) -> Optional[float]:
    """
    Safely divide two numbers, return None if division by zero.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Optional[float]: Result or None if error

    Example:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(10, 0)
        None
    """
    try:
        result = a / b
        return result
    except:
        return None


def convert_to_int_safe(value: str) -> Optional[int]:
    """
    Convert string to int, return None if invalid.

    Args:
        value: String to convert

    Returns:
        Optional[int]: Integer or None if conversion fails

    Example:
        >>> convert_to_int_safe("42")
        42
        >>> convert_to_int_safe("abc")
        None
        >>> convert_to_int_safe("3.14")
        None
    """
    try:
        return int(value)
    except:
        return None


def get_item_safe(items: List[str], index: int) -> Optional[str]:
    """
    Get item at index, return None if index out of range.

    Args:
        items: List of items
        index: Index to access

    Returns:
        Optional[str]: Item or None if index invalid

    Example:
        >>> get_item_safe(["a", "b", "c"], 1)
        'b'
        >>> get_item_safe(["a", "b", "c"], 10)
        None
        >>> get_item_safe([], 0)
        None
    """
    try:
        return items[index]
    except:
        return None


def parse_rating(rating_str: str) -> float:
    """
    Parse rating string to float.
    If invalid, return 0.0 and print error message.

    Args:
        rating_str: Rating as string

    Returns:
        float: Parsed rating or 0.0 if invalid

    Example:
        >>> parse_rating("8.5")
        8.5
        >>> parse_rating("invalid")
        Error: Invalid rating 'invalid'
        0.0
    """
    try:
        return float(rating_str)
    except:
        print("Error: Invalid rating 'invalid'")
        return float(0.0)


def read_file_lines(filepath: str) -> List[str]:
    """
    Read all lines from file, return empty list if file not found.

    Args:
        filepath: Path to file

    Returns:
        List[str]: Lines from file or empty list

    Example:
        >>> lines = read_file_lines("data.txt")
        >>> lines = read_file_lines("nonexistent.txt")  # Returns []
    """
    pass


# =============================================================================
# PART 2 - SPECIFIC EXCEPTIONS
# =============================================================================
"""
CONCEPTS:
- ValueError - invalid value (e.g., int("abc"))
- KeyError - missing dictionary key
- IndexError - list index out of range
- TypeError - wrong type
- ZeroDivisionError - division by zero
- FileNotFoundError - file doesn't exist

WHY catch specific exceptions?
- More precise error handling
- Different actions for different errors
- Better debugging
"""


def get_movie_rating(movie_data: Dict[str, Any], movie_id: str) -> float:
    """
    Get rating for movie. Handle missing key and invalid rating gracefully.

    Args:
        movie_data: {'movie_id': {'rating': float, ...}}
        movie_id: Movie ID to lookup

    Returns:
        float: Rating or 0.0 if not found/invalid

    Example:
        >>> data = {'tt0111161': {'rating': 9.3}}
        >>> get_movie_rating(data, 'tt0111161')
        9.3
        >>> get_movie_rating(data, 'tt9999999')
        0.0
        >>> data_bad = {'tt0111161': {'rating': 'invalid'}}
        >>> get_movie_rating(data_bad, 'tt0111161')
        0.0
    """

    try:
        rating = movie_data[movie_id]["rating"]
        return float(rating)
    except KeyError:
        return 0.0
    except ValueError:
        return 0.0


def calculate_average(numbers: List[float]) -> Optional[float]:
    """
    Calculate average of numbers. Handle empty list and division by zero.

    Args:
        numbers: List of numbers

    Returns:
        Optional[float]: Average or None if empty list

    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([])
        None
        >>> calculate_average([10.5, 20.5])
        15.5
    """
    try:
        total = sum(numbers)
        return total / len(numbers)
    except IndexError:
        return None
    except ZeroDivisionError:
        return None


def parse_year_from_string(text: str) -> Optional[int]:
    """
    Extract year from text like "Released in 2010".
    Try to parse the last 4-digit number.

    Args:
        text: Text containing year

    Returns:
        Optional[int]: Year or None if not found/invalid

    Example:
        >>> parse_year_from_string("Released in 2010")
        2010
        >>> parse_year_from_string("No year here")
        None
        >>> parse_year_from_string("Made in 1999")
        1999
    """
    values = text.split()
    for value in reversed(values):
        try:
            year = int(value)
            if len(value) == 4:
                return year
        except ValueError:
            continue
    return None


def access_nested_value(data: Dict, keys: List[str]) -> Any:
    """
    Safely access nested dictionary value.
    Return None if any key is missing.

    Args:
        data: Nested dictionary
        keys: List of keys to traverse

    Returns:
        Any: Value or None if path doesn't exist

    Example:
        >>> data = {'user': {'profile': {'name': 'Alice'}}}
        >>> access_nested_value(data, ['user', 'profile', 'name'])
        'Alice'
        >>> access_nested_value(data, ['user', 'missing', 'key'])
        None
    """
    new_data = data
    try:
        for key in keys:
            new_data = new_data[key]
        return new_data
    except (KeyError, TypeError):
        return None


def convert_and_multiply(value: str, multiplier: int) -> Optional[int]:
    """
    Convert string to int and multiply.
    Handle both ValueError (invalid string) and TypeError (wrong multiplier type).

    Args:
        value: String number
        multiplier: Multiplier

    Returns:
        Optional[int]: Result or None if error

    Example:
        >>> convert_and_multiply("5", 3)
        15
        >>> convert_and_multiply("abc", 3)
        None
        >>> convert_and_multiply("5", "3")
        None
    """
    try:
        total = int(value) * multiplier
        return total
    except (ValueError, TypeError):
        return None


# =============================================================================
# PART 3 - RAISING EXCEPTIONS
# =============================================================================
"""
CONCEPTS:
- raise Exception("message") - throw error
- When to raise vs when to return None
- Custom error messages

WHEN TO RAISE:
- Invalid input that MUST be fixed (e.g., negative age)
- Programming errors (wrong function usage)
- Contract violations

WHEN TO RETURN None/default:
- Expected failures (e.g., file not found might be OK)
- Optional values
- Graceful degradation
"""


def validate_rating(rating: float) -> None:
    """
    Validate rating is between 0 and 10.
    Raise ValueError if invalid.

    Args:
        rating: Rating value

    Raises:
        ValueError: If rating not in [0, 10]

    Example:
        >>> validate_rating(8.5)  # OK
        >>> validate_rating(15)   # Raises ValueError
        Traceback (most recent call last):
        ValueError: Rating must be between 0 and 10, got 15
    """
    if not (0 <= rating <= 10):
        raise ValueError(f"Rating must be between 0 and 10, got {rating}")


def create_movie_dict(title: str, year: int, rating: float) -> Dict[str, Any]:
    """
    Create movie dictionary with validation.
    Raise ValueError if any field is invalid.

    Validation rules:
    - title: non-empty string
    - year: between 1888 and 2030
    - rating: between 0 and 10

    Args:
        title: Movie title
        year: Release year
        rating: Rating

    Returns:
        Dict: Movie data

    Raises:
        ValueError: If any field invalid

    Example:
        >>> create_movie_dict("Inception", 2010, 8.8)
        {'title': 'Inception', 'year': 2010, 'rating': 8.8}
        >>> create_movie_dict("", 2010, 8.8)
        Traceback (most recent call last):
        ValueError: Title cannot be empty
    """
    if not title:
        raise ValueError("Title cannot be empty")
    if not (1888 <= year <= 2030):
        raise ValueError(f"Year must be between 1888 and 2030, got {year}")
    if not (0 <= rating <= 10):
        raise ValueError(f"Rating must be between 0 and 10, got {rating}")
    return {"title": title, "year": year, "rating": rating}


def divide_or_error(a: float, b: float) -> float:
    """
    Divide a by b. Raise ZeroDivisionError with custom message if b is 0.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        float: Result

    Raises:
        ZeroDivisionError: If b is 0

    Example:
        >>> divide_or_error(10, 2)
        5.0
        >>> divide_or_error(10, 0)
        Traceback (most recent call last):
        ZeroDivisionError: Cannot divide 10 by zero
    """
    if b == 0:
        raise ZeroDivisionError(f"Cannot divide {a} by zero")
    return float(a / b)


# =============================================================================
# PART 4 - REAL-WORLD PATTERNS
# =============================================================================
"""
Real-world error handling patterns from production code
"""


def load_movie_data(filepath: str) -> Dict[str, Any]:
    """
    Load movie data from JSON file with comprehensive error handling.

    Handle:
    - FileNotFoundError → return empty dict, print warning
    - JSONDecodeError → return empty dict, print error
    - Use finally to always print "Load attempt complete"

    Args:
        filepath: Path to JSON file

    Returns:
        Dict: Movie data or empty dict if error

    Example:
        >>> data = load_movie_data("movies.json")
        >>> data = load_movie_data("missing.json")
        Warning: File not found 'missing.json'
        Load attempt complete
        {}
    """
    try:
        with open(filepath) as f:
            import json

            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: File not found '{filepath}'")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file '{filepath}'")
        return {}
    finally:
        print("Load attempt complete")


def batch_convert_ratings(rating_strings: List[str]) -> Dict[str, Any]:
    """
    Convert list of rating strings to floats.
    Track successes and failures.

    Args:
        rating_strings: List of rating strings

    Returns:
        Dict: {
            'successes': [float, ...],
            'failures': [{'value': str, 'error': str}, ...]
        }

    Example:
        >>> batch_convert_ratings(["8.5", "9.0", "invalid", "7.5"])
        {
            'successes': [8.5, 9.0, 7.5],
            'failures': [{'value': 'invalid', 'error': 'ValueError'}]
        }
    """
    movie_dict = {"successes": [], "failures": []}

    for st in rating_strings:
        try:
            new_st = float(st)
            movie_dict["successes"].append(new_st)
        except ValueError:
            movie_dict["failures"].append({"value": st, "error": "ValueError"})
    return movie_dict


def fetch_with_retry(url: str, max_retries: int = 3) -> Optional[Dict]:
    """
    Simulate fetching data with retry logic.
    (Don't actually make HTTP request - just demonstrate the pattern)

    Pattern:
    - Try to fetch
    - On failure, retry up to max_retries times
    - Return None if all retries fail

    Args:
        url: URL to fetch (simulated)
        max_retries: Maximum number of retry attempts

    Returns:
        Optional[Dict]: Data or None if all retries fail

    Example:
        >>> data = fetch_with_retry("https://api.example.com/movie/123")
        Attempt 1: Failed
        Attempt 2: Success
        {'movie': 'Inception'}
    """
    import random

    for attempt in range(1, max_retries + 1):
        try:
            if random.random() < 0.5:
                return {"movie": "Inception"}
            raise Exception("Network Error")
        except:
            print(f"Attempt {attempt} failed")

    return None


# =============================================================================
# TESTS
# =============================================================================

if __name__ == "__main__":
    # print("=" * 70)
    # print("PART 1 - BASIC TRY/EXCEPT")
    # print("=" * 70)

    # print("\n1. Safe divide:")
    # print(f"10 / 2 = {safe_divide(10, 2)}")
    # print(f"10 / 0 = {safe_divide(10, 0)}")

    # print("\n2. Convert to int safe:")
    # print(f"'42' -> {convert_to_int_safe('42')}")
    # print(f"'abc' -> {convert_to_int_safe('abc')}")

    # print("\n3. Get item safe:")
    # items = ["a", "b", "c"]
    # print(f"items[1] = {get_item_safe(items, 1)}")
    # print(f"items[10] = {get_item_safe(items, 10)}")

    # print("\n4. Parse rating:")
    # print(f"'8.5' -> {parse_rating('8.5')}")
    # print(f"'invalid' -> ", end="")
    # parse_rating("invalid")

    # print("\n" + "=" * 70)
    # print("PART 2 - SPECIFIC EXCEPTIONS")
    # print("=" * 70)

    # print("\n1. Get movie rating:")
    # movie_db = {"tt0111161": {"title": "Shawshank", "rating": 9.3}}
    # print(f"Rating for tt0111161: {get_movie_rating(movie_db, 'tt0111161')}")
    # print(f"Rating for tt9999999: {get_movie_rating(movie_db, 'tt9999999')}")

    # print("\n2. Calculate average:")
    # print(f"Average of [1,2,3,4,5]: {calculate_average([1, 2, 3, 4, 5])}")
    # print(f"Average of []: {calculate_average([])}")

    # print("\n3. Parse year:")
    # print(f"'Released in 2010' -> {parse_year_from_string('Released in 2010')}")
    # print(f"'No year here' -> {parse_year_from_string('No year here')}")

    # print("\n4. Access nested value:")
    # data = {"user": {"profile": {"name": "Alice", "age": 30}}}
    # print(f"name: {access_nested_value(data, ['user', 'profile', 'name'])}")
    # print(f"missing: {access_nested_value(data, ['user', 'missing', 'key'])}")

    # print("\n5. Convert and multiply:")
    # print(f"'5' * 3 = {convert_and_multiply('5', 3)}")
    # print(f"'abc' * 3 = {convert_and_multiply('abc', 3)}")

    print("\n" + "=" * 70)
    print("PART 3 - RAISING EXCEPTIONS")
    print("=" * 70)

    # print("\n1. Validate rating:")
    # try:
    #     validate_rating(8.5)
    #     print("✓ Rating 8.5 is valid")
    # except ValueError as e:
    #     print(f"✗ Error: {e}")

    # try:
    #     validate_rating(15)
    #     print("✓ Rating 15 is valid")
    # except ValueError as e:
    #     print(f"✗ Error: {e}")

    # print("\n2. Create movie dict:")
    # try:
    #     movie = create_movie_dict("Inception", 2010, 8.8)
    #     print(f"✓ Created: {movie}")
    # except ValueError as e:
    #     print(f"✗ Error: {e}")

    # try:
    #     movie = create_movie_dict("", 2010, 8.8)
    #     print(f"✓ Created: {movie}")
    # except ValueError as e:
    #     print(f"✗ Error: {e}")

    # print("\n3. Divide or error:")
    # try:
    #     result = divide_or_error(10, 2)
    #     print(f"✓ 10 / 2 = {result}")
    # except ZeroDivisionError as e:
    #     print(f"✗ Error: {e}")

    # try:
    #     result = divide_or_error(10, 0)
    #     print(f"✓ 10 / 0 = {result}")
    # except ZeroDivisionError as e:
    #     print(f"✗ Error: {e}")

    # print("\n" + "=" * 70)
    # print("PART 4 - REAL-WORLD PATTERNS")
    # print("=" * 70)

    # print("\n1. Load movie data:")
    # data = load_movie_data("nonexistent.json")
    # print(f"Result: {data}")

    # print("\n2. Batch convert ratings:")
    # ratings = ["8.5", "9.0", "invalid", "7.5", "abc"]
    # result = batch_convert_ratings(ratings)
    # print(f"Successes: {result['successes']}")
    # print(f"Failures: {result['failures']}")

    print("\n3. Fetch with retry (simulated):")
    data = fetch_with_retry("https://api.example.com/movie/123")
    print(f"Result: {data}")

    # print("\n" + "=" * 70)
    # print("✅ Exercise 1.18 Complete!")
    # print("=" * 70)
    # print("\nKEY TAKEAWAYS:")
    # print("- try/except - catch errors gracefully, prevent crashes")
    # print("- Catch SPECIFIC exceptions (ValueError, KeyError, etc.) for precise handling")
    # print("- Use finally for cleanup code that ALWAYS runs")
    # print("- raise Exception() - fail fast when input is invalid")
    # print("- Return None/default for expected failures")
    # print("- Raise exceptions for unexpected/invalid states")
    # print("- Real-world: batch processing, retry logic, comprehensive error tracking")
    # print("\nWHEN TO CATCH vs WHEN TO RAISE:")
    # print("- Catch: Expected failures (file not found, network timeout)")
    # print("- Raise: Invalid input, programming errors, contract violations")
