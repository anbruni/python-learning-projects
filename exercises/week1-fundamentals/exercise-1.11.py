"""
Exercise 1.11 - Lambda Functions & Pure Functions
==================================================

KNOWLEDGE REFERENCE: /knowledge/functions.md (Lambda & Best Practices sections)

LEARNING GOALS:
- Master lambda syntax for simple operations
- Know when to use lambda (sort, filter, map) vs regular functions
- Understand pure vs impure functions
- Write testable, predictable code

STRUCTURE:
- Part 1: Lambda functions (6 functions)
- Part 2: Pure vs Impure functions (6 functions)
"""

from typing import List, Dict, Callable

# =============================================================================
# PART 1 - LAMBDA FUNCTIONS
# =============================================================================
"""
CONCEPTS:
- Lambda syntax: lambda x: expression
- Use cases: sort key, filter, map
- When NOT to use: complex logic, multiple lines
"""


def sort_by_age(users: List[Dict]) -> List[Dict]:
    """
    Sort users by age using lambda.

    Common pattern: sort with custom key.

    Args:
        users: List of user dicts with 'age' key

    Returns:
        List[Dict]: Sorted users

    Example:
        >>> users = [{"name": "Andrea", "age": 30}, {"name": "Maria", "age": 25}]
        >>> sort_by_age(users)
        [{'name': 'Maria', 'age': 25}, {'name': 'Andrea', 'age': 30}]
    """
    sorted_users = sorted(users, key=lambda u: u["age"])
    return sorted_users


def filter_adults(users: List[Dict]) -> List[Dict]:
    """
    Filter users 18+ using lambda and filter().

    Args:
        users: List of user dicts with 'age' key

    Returns:
        List[Dict]: Users 18+

    Example:
        >>> users = [{"name": "Kid", "age": 10}, {"name": "Adult", "age": 25}]
        >>> filter_adults(users)
        [{'name': 'Adult', 'age': 25}]
    """
    # filtered_users = list(filter(lambda u: u["name"] == "Adult", users))
    # return filtered_users
    filtered_users = list(filter(lambda u: u["age"] >= 18, users))
    return filtered_users


def double_prices(prices: List[float]) -> List[float]:
    """
    Double all prices using lambda and map().

    Args:
        prices: List of prices

    Returns:
        List[float]: Doubled prices

    Example:
        >>> double_prices([10, 20, 30])
        [20.0, 40.0, 60.0]
    """
    doubled_items = list(map(lambda x: x * 2, prices))
    return doubled_items


def sort_movies_by_rating(movies: List[Dict]) -> List[Dict]:
    """
    Sort movies by rating (descending) using lambda.

    Args:
        movies: List of movie dicts with 'rating' key

    Returns:
        List[Dict]: Movies sorted by rating (highest first)

    Example:
        >>> movies = [
        ...     {"title": "Movie A", "rating": 7.5},
        ...     {"title": "Movie B", "rating": 9.0}
        ... ]
        >>> sort_movies_by_rating(movies)
        [{'title': 'Movie B', 'rating': 9.0}, {'title': 'Movie A', 'rating': 7.5}]
    """
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return sorted_movies


def create_multiplier(factor: int) -> Callable:
    """
    Create a multiplier function using lambda.

    Factory pattern with lambda.

    Args:
        factor: Multiplication factor

    Returns:
        Callable: Lambda function that multiplies by factor

    Example:
        >>> double = create_multiplier(2)
        >>> double(5)
        10
        >>> triple = create_multiplier(3)
        >>> triple(5)
        15
    """
    return lambda x: x * factor


def when_not_to_use_lambda():
    """
    Demonstrate when lambda is BAD.

    Return a regular function instead of complex lambda.

    Returns:
        Callable: Function that validates and transforms data

    Example:
        >>> validator = when_not_to_use_lambda()
        >>> validator("hello")
        'HELLO'
        >>> validator("")
        None
    """
    # ❌ BAD: Complex lambda (don't do this!)
    # bad = lambda x: x.upper() if x and len(x) > 0 else None

    # ✅ GOOD: Regular function with name
    def validate_and_transform(text: str):
        if text and len(text) > 0:
            return text.upper()
        return None

    return validate_and_transform


# =============================================================================
# PART 2 - PURE VS IMPURE FUNCTIONS
# =============================================================================
"""
CONCEPTS:
- Pure: same input → same output, no side effects
- Impure: modifies state, I/O, unpredictable
- Benefits: testable, cacheable, parallelizable
"""


# PURE FUNCTIONS (✅ Good for testing)


def calculate_total_pure(prices: List[float], tax_rate: float) -> float:
    """
    Pure function: calculate total with tax.

    Pure because:
    - Same input always gives same output
    - No side effects (doesn't modify prices)
    - Deterministic

    Args:
        prices: List of prices
        tax_rate: Tax rate (e.g., 0.22 for 22%)

    Returns:
        float: Total with tax

    Example:
        >>> calculate_total_pure([100, 200], 0.22)
        366.0
    """
    total_pure = sum(prices) * (1 + tax_rate)
    return total_pure


def filter_expensive_pure(items: List[Dict], min_price: float) -> List[Dict]:
    """
    Pure function: filter expensive items.

    Pure because:
    - Doesn't modify original list
    - Returns NEW list
    - Deterministic

    Args:
        items: List of item dicts with 'price' key
        min_price: Minimum price threshold

    Returns:
        List[Dict]: New list with expensive items

    Example:
        >>> items = [{"name": "A", "price": 10}, {"name": "B", "price": 50}]
        >>> filter_expensive_pure(items, 20)
        [{'name': 'B', 'price': 50}]
        >>> items  # Original unchanged
        [{'name': 'A', 'price': 10}, {'name': 'B', 'price': 50}]
    """
    pass


def merge_users_pure(user1: Dict, user2: Dict) -> Dict:
    """
    Pure function: merge two user dicts.

    Pure because:
    - Doesn't modify original dicts
    - Returns NEW dict
    - Deterministic

    Args:
        user1: First user dict
        user2: Second user dict (overrides user1)

    Returns:
        Dict: New merged dict

    Example:
        >>> u1 = {"name": "Andrea", "age": 30}
        >>> u2 = {"age": 31, "city": "Milan"}
        >>> merge_users_pure(u1, u2)
        {'name': 'Andrea', 'age': 31, 'city': 'Milan'}
        >>> u1  # Original unchanged
        {'name': 'Andrea', 'age': 30}
    """
    pass


# IMPURE FUNCTIONS (❌ Harder to test)

cart_items = []  # Global state


def add_to_cart_impure(item: str):
    """
    Impure function: modifies global state.

    Impure because:
    - Modifies global cart_items
    - Side effect (changes external state)
    - Hard to test (depends on global state)

    Args:
        item: Item to add

    Example:
        >>> add_to_cart_impure("apple")
        >>> cart_items
        ['apple']
    """
    pass


def add_to_cart_pure(cart: List[str], item: str) -> List[str]:
    """
    Pure version: returns new cart.

    Pure because:
    - Doesn't modify input cart
    - Returns NEW list
    - Deterministic
    - Easy to test!

    Args:
        cart: Current cart
        item: Item to add

    Returns:
        List[str]: New cart with item

    Example:
        >>> cart = ["apple"]
        >>> new_cart = add_to_cart_pure(cart, "banana")
        >>> new_cart
        ['apple', 'banana']
        >>> cart  # Original unchanged
        ['apple']
    """
    pass


def compare_pure_vs_impure():
    """
    Demonstrate difference between pure and impure.

    Shows why pure functions are better for testing.

    Returns:
        Dict: Comparison results
    """

    # Pure version - easy to test
    def pure_add(a, b):
        return a + b

    # Impure version - depends on external state
    external_value = 10

    def impure_add(a, b):
        return a + b + external_value  # Uses external state!

    return {
        "pure_result": pure_add(5, 3),  # Always 8
        "impure_result": impure_add(
            5, 3
        ),  # 18 (but changes if external_value changes!)
        "pure_testable": True,  # Pure is easy to test
        "impure_testable": False,  # Impure depends on external state
    }


# =============================================================================
# TESTS
# =============================================================================

if __name__ == "__main__":
    #     print("=" * 70)
    #     print("PART 1 - LAMBDA FUNCTIONS")
    #     print("=" * 70)

    # print("\n1. Sort by age:")
    # users = [
    #     {"name": "Andrea", "age": 30},
    #     {"name": "Maria", "age": 25},
    #     {"name": "Luca", "age": 35},
    # ]
    # sorted_users = sort_by_age(users)
    # for u in sorted_users:
    #     print(f"  {u['name']}: {u['age']}")

    # print("\n2. Filter adults:")
    # users = [
    #     {"name": "Kid", "age": 10},
    #     {"name": "Teen", "age": 16},
    #     {"name": "Adult", "age": 25},
    # ]
    # adults = filter_adults(users)
    # print(f"  Adults: {[u['name'] for u in adults]}")

    # print("\n3. Double prices:")
    # prices = [10, 20, 30]
    # doubled = double_prices(prices)
    # print(f"  Original: {prices}")
    # print(f"  Doubled: {doubled}")

    # print("\n4. Sort movies by rating:")
    # movies = [
    #     {"title": "Movie A", "rating": 7.5},
    #     {"title": "Movie B", "rating": 9.0},
    #     {"title": "Movie C", "rating": 6.0},
    # ]
    # sorted_movies = sort_movies_by_rating(movies)
    # for m in sorted_movies:
    #     print(f"  {m['title']}: {m['rating']}")

    print("\n5. Create multiplier:")
    double = create_multiplier(2)
    triple = create_multiplier(3)
    print(f"  double(5) = {double(5)}")
    print(f"  triple(5) = {triple(5)}")

# print("\n6. When NOT to use lambda:")
# validator = when_not_to_use_lambda()
# print(f"  validator('hello') = {validator('hello')}")
# print(f"  validator('') = {validator('')}")

# print("\n" + "=" * 70)
# print("PART 2 - PURE VS IMPURE FUNCTIONS")
# print("=" * 70)

# print("\n1. Pure: Calculate total:")
# total = calculate_total_pure([100, 200], 0.22)
# print(f"  Total with tax: {total}")

# print("\n2. Pure: Filter expensive:")
# items = [{"name": "Cheap", "price": 10}, {"name": "Expensive", "price": 50}]
# expensive = filter_expensive_pure(items, 20)
# print(f"  Expensive items: {expensive}")
# print(f"  Original unchanged: {items}")

# print("\n3. Pure: Merge users:")
# u1 = {"name": "Andrea", "age": 30}
# u2 = {"age": 31, "city": "Milan"}
# merged = merge_users_pure(u1, u2)
# print(f"  Merged: {merged}")
# print(f"  u1 unchanged: {u1}")

# print("\n4. Impure: Add to cart (modifies global):")
# global cart_items
# cart_items = []
# add_to_cart_impure("apple")
# add_to_cart_impure("banana")
# print(f"  Global cart: {cart_items}")

# print("\n5. Pure: Add to cart (returns new):")
# cart = ["apple"]
# new_cart = add_to_cart_pure(cart, "banana")
# print(f"  Original cart: {cart}")
# print(f"  New cart: {new_cart}")

# print("\n6. Compare pure vs impure:")
# comparison = compare_pure_vs_impure()
# print(f"  Pure result: {comparison['pure_result']}")
# print(f"  Impure result: {comparison['impure_result']}")
# print(f"  Pure testable: {comparison['pure_testable']}")
# print(f"  Impure testable: {comparison['impure_testable']}")

# print("\n" + "=" * 70)
# print("✅ Exercise 1.11 Complete!")
# print("=" * 70)
