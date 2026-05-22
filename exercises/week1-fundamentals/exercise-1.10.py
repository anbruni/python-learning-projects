"""
Exercise 1.10 - Advanced *args and **kwargs
============================================

KNOWLEDGE REFERENCE: /knowledge/functions.md (*args/**kwargs section)

LEARNING GOALS:
- Master *args/**kwargs unpacking in function calls
- Combine all parameter types correctly
- Real-world patterns: decorators, wrappers, forwarding

STRUCTURE:
- Part 1: Unpacking & forwarding (5 functions)
- Part 2: Real-world patterns (5 functions)
"""

from typing import List, Dict, Any, Callable

# =============================================================================
# PART 1 - UNPACKING & FORWARDING
# =============================================================================
"""
CONCEPTS:
- Unpacking: *list_var, **dict_var in function CALLS
- Forwarding: passing *args/**kwargs to other functions
- Order: positional, *args, keyword, **kwargs
"""


def unpack_and_call(numbers: List[int]) -> int:
    """
    Unpack list and pass to max() function.

    Demonstrates * unpacking in function call.

    Args:
        numbers: List of integers

    Returns:
        int: Maximum value

    Example:
        >>> unpack_and_call([5, 2, 8, 1])
        8
    """
    return max(*numbers)


def merge_and_create_user(base_data: dict, extra_data: dict) -> dict:
    """
    Merge two dicts using ** unpacking.

    Create user dict by unpacking both base and extra data.

    Args:
        base_data: Base user info (name, age)
        extra_data: Additional info (city, email)

    Returns:
        dict: Merged user data

    Example:
        >>> merge_and_create_user({"name": "Andrea", "age": 30}, {"city": "Milan"})
        {'name': 'Andrea', 'age': 30, 'city': 'Milan'}
    """
    return {**base_data, **extra_data}


def forward_to_print(*args, **kwargs):
    """
    Forward all arguments to print() function.

    Common pattern: wrapper functions.

    Args:
        *args: Any positional arguments
        **kwargs: Any keyword arguments (sep, end, etc.)

    Example:
        >>> forward_to_print("Hello", "World", sep="-")
        Hello-World
    """
    print(*args, **kwargs)


def call_with_list_and_dict(func: Callable, args_list: list, kwargs_dict: dict) -> Any:
    """
    Call function with unpacked list and dict.

    Pattern: dynamic function calling.

    Args:
        func: Function to call
        args_list: List of positional arguments
        kwargs_dict: Dict of keyword arguments

    Returns:
        Any: Function result

    Example:
        >>> def greet(name, age, city="Unknown"):
        ...     return f"{name}, {age} from {city}"
        >>> call_with_list_and_dict(greet, ["Andrea", 30], {"city": "Milan"})
        'Andrea, 30 from Milan'
    """
    return func(*args_list, **kwargs_dict)


def combine_all_styles(pos1, pos2, *args, default="N/A", **kwargs) -> dict:
    """
    Function with ALL parameter types combined.

    Order matters: positional, *args, keyword with default, **kwargs

    Args:
        pos1: Required positional 1
        pos2: Required positional 2
        *args: Variable positional
        default: Keyword with default
        **kwargs: Variable keyword

    Returns:
        dict: All collected arguments

    Example:
        >>> combine_all_styles("a", "b", "c", "d", default="custom", x=1, y=2)
        {
            'pos': ['a', 'b'],
            'args': ('c', 'd'),
            'default': 'custom',
            'kwargs': {'x': 1, 'y': 2}
        }
    """
    return {
        "pos": [pos1, pos2],
        "args": args,
        "default": default,
        "kwargs": kwargs,
    }


# =============================================================================
# PART 2 - REAL-WORLD PATTERNS
# =============================================================================
"""
PATTERNS:
- Function wrappers (decorators preview)
- API client helpers
- Config builders
- Retry logic
"""


def retry_on_error(func: Callable, max_attempts: int, *args, **kwargs) -> Any:
    """
    Call function with retry logic.

    Forward all args/kwargs to target function.

    Args:
        func: Function to call
        max_attempts: Maximum retry attempts
        *args: Positional args for func
        **kwargs: Keyword args for func

    Returns:
        Any: Function result or None if all attempts fail

    Example:
        >>> def unstable_func(x):
        ...     if x < 5:
        ...         raise ValueError()
        ...     return x * 2
        >>> retry_on_error(unstable_func, 3, 10)
        20
    """
    # Loop da 1 a max_attempts
    for attempt in range(max_attempts):
        try:
            return func(*args, **kwargs)
        except:
            continue

    return None  # Tutti i tentativi falliti


def api_call_builder(endpoint: str, **options) -> dict:
    """
    Build API call config with default + custom options.

    Pattern: merge defaults with user options.

    Args:
        endpoint: API endpoint
        **options: Custom options (override defaults)

    Returns:
        dict: Complete API config

    Example:
        >>> api_call_builder("/users", timeout=60, auth="token123")
        {
            'endpoint': '/users',
            'method': 'GET',
            'timeout': 60,
            'auth': 'token123',
            'retries': 3
        }
    """
    defaults = {"method": "GET", "timeout": 30, "retries": 3}
    return {"endpoint": endpoint, **defaults, **options}


def batch_process(processor: Callable, *items, **config) -> List:
    """
    Process multiple items with same function and config.

    Pattern: batch operations.

    Args:
        processor: Function to apply to each item
        *items: Items to process
        **config: Configuration passed to processor

    Returns:
        List: Processed results

    Example:
        >>> def double(x, multiply_by=2):
        ...     return x * multiply_by
        >>> batch_process(double, 1, 2, 3, multiply_by=3)
        [3, 6, 9]
    """
    result = []
    for item in items:
        result.append(processor(item, **config))
    return result


def compose_functions(*funcs: Callable) -> Callable:
    """
    Compose multiple functions into one.

    Pattern: function composition (advanced).

    Args:
        *funcs: Functions to compose (right to left)

    Returns:
        Callable: Composed function

    Example:
        >>> def add_one(x): return x + 1
        >>> def double(x): return x * 2
        >>> f = compose_functions(double, add_one)
        >>> f(5)  # double(add_one(5)) = double(6) = 12
        12
    """

    def composed(x):
        result = x
        for func in reversed(funcs):
            result = func(result)  # Applica func al risultato attuale
        return result

    return composed


def kwargs_to_query_string(**params) -> str:
    """
    Convert kwargs to URL query string.

    Pattern: URL building.

    Args:
        **params: Query parameters

    Returns:
        str: Query string

    Example:
        >>> kwargs_to_query_string(page=1, limit=10, sort="name")
        'page=1&limit=10&sort=name'
    """
    pass


# =============================================================================
# TESTS
# =============================================================================

if __name__ == "__main__":
    # print("=" * 70)
    # print("PART 1 - UNPACKING & FORWARDING")
    # print("=" * 70)

    # print("\n1. Unpack and call:")
    # result = unpack_and_call([5, 2, 8, 1])
    # print(f"Max of [5, 2, 8, 1]: {result}")

    # print("\n2. Merge and create user:")
    # user = merge_and_create_user({"name": "Andrea", "age": 30}, {"city": "Milan"})
    # print(user)

    # print("\n3. Forward to print:")
    # forward_to_print("Hello", "World", sep=" - ", end="!\n")

    # print("\n4. Call with list and dict:")

    # def greet(name, age, city="Unknown"):
    #     return f"{name}, {age} from {city}"

    # result = call_with_list_and_dict(greet, ["Andrea", 30], {"city": "Milan"})
    # print(result)

    # print("\n5. Combine all styles:")
    # result = combine_all_styles("a", "b", "c", "d", default="custom", x=1, y=2)
    # print(result)

    # print("\n" + "=" * 70)
    # print("PART 2 - REAL-WORLD PATTERNS")
    # print("=" * 70)

    # print("\n1. Retry on error:")

    # def sometimes_fails(x, threshold=5):
    #     if x < threshold:
    #         raise ValueError("Too small")
    #     return x * 2

    # result = retry_on_error(sometimes_fails, 3, 10)
    # print(f"Result: {result}")

    # print("\n2. API call builder:")
    # config = api_call_builder("/users", timeout=60, auth="token123")
    # print(config)

    # print("\n3. Batch process:")

    # def double(x, multiply_by=2):
    #     return x * multiply_by

    # results = batch_process(double, 1, 2, 3, multiply_by=3)
    # print(f"Batch results: {results}")

    print("\n4. Compose functions:")

    def add_one(x):
        return x + 1

    def double(x):
        return x * 2

    f = compose_functions(double, add_one)
    print(f"compose(double, add_one)(5) = {f(5)}")

    # print("\n5. Kwargs to query string:")
    # query = kwargs_to_query_string(page=1, limit=10, sort="name")
    # print(f"Query string: {query}")

    # print("\n" + "=" * 70)
    # print("✅ Exercise 1.10 Complete!")
    # print("=" * 70)
