"""
Exercise 1.8 - Shallow vs Deep Copy
===================================

KNOWLEDGE REFERENCE: /knowledge/mutability.md (Shallow vs Deep Copy section)

LEARNING GOALS:
- Understand difference between shallow and deep copy
- Know when each copy method is needed
- Handle nested data structures correctly

STRUCTURE:
- Part 1: Basic shallow vs deep copy (5 functions)
- Part 2: Practical nested structures (5 functions)
"""

import copy

# =============================================================================
# PART 1 - BASIC SHALLOW VS DEEP COPY
# =============================================================================
"""
CONCEPTS:
- shallow copy: copy.copy() or list.copy() - copies first level only
- deep copy: copy.deepcopy() - recursively copies everything
- nested structures: lists containing lists, dicts containing dicts
"""


def demonstrate_shallow_copy():
    """
    Demonstrates shallow copy behavior with nested list.

    Creates nested list, makes shallow copy, modifies inner list.
    Shows both original and copy are affected.

    Returns:
        tuple: (original_list, copied_list, are_inner_lists_same)

    Example:
        >>> original, copied, same = demonstrate_shallow_copy()
        >>> original
        [[1, 2, 999], [4, 5, 6]]
        >>> copied
        [[1, 2, 999], [4, 5, 6]]
        >>> same
        True
    """
    original = [[1, 2, 3], [4, 5, 6]]
    copied = original.copy()  # shallow copy
    copied[0].append(999)  # modify inner list
    are_inner_lists_same = original[0] == copied[0]  # True
    return (original, copied, are_inner_lists_same)


def demonstrate_deep_copy():
    """
    Demonstrates deep copy behavior with nested list.

    Creates nested list, makes deep copy, modifies inner list.
    Shows only original is affected.

    Returns:
        tuple: (original_list, copied_list, are_inner_lists_same)

    Example:
        >>> original, copied, same = demonstrate_deep_copy()
        >>> original
        [[1, 2, 999], [4, 5, 6]]
        >>> copied
        [[1, 2, 3], [4, 5, 6]]
        >>> same
        False
    """
    original = [[1, 2, 3], [4, 5, 6]]
    copied = copy.deepcopy(original)  # deep copy
    copied[0].append(999)  # modify inner list
    are_inner_lists_same = original[0] == copied[0]  # False
    return (original, copied, are_inner_lists_same)


def safe_copy_nested_list(nested_list):
    """
    Creates a safe copy of nested list that won't affect original.

    Args:
        nested_list: List containing other lists

    Returns:
        list: Deep copy of nested_list

    Example:
        >>> original = [[1, 2], [3, 4]]
        >>> copied = safe_copy_nested_list(original)
        >>> copied[0].append(999)
        >>> original
        [[1, 2], [3, 4]]
        >>> copied
        [[1, 2, 999], [3, 4]]
    """
    return copy.deepcopy(nested_list)


def compare_copy_methods(nested_data):
    """
    Compares assignment, shallow copy, and deep copy.

    Creates 3 copies using:
    - assignment (reference)
    - shallow copy (.copy())
    - deep copy (copy.deepcopy())

    Modifies nested element and shows which copies are affected.

    Args:
        nested_data: Nested list like [[1, 2], [3, 4]]

    Returns:
        dict: {
            'reference': reference_copy,
            'shallow': shallow_copy,
            'deep': deep_copy
        }

    Example:
        >>> data = [[1, 2], [3, 4]]
        >>> result = compare_copy_methods(data)
        # After modifying data[0][0] = 999:
        >>> result['reference'][0][0]  # affected
        999
        >>> result['shallow'][0][0]    # affected
        999
        >>> result['deep'][0][0]       # NOT affected
        1
    """
    reference = nested_data
    shallow = nested_data.copy()
    deep = copy.deepcopy(nested_data)
    return {"reference": reference, "shallow": shallow, "deep": deep}


def when_shallow_is_enough(flat_list):
    """
    Demonstrates when shallow copy is sufficient.

    For flat lists (no nesting), shallow copy works fine.

    Args:
        flat_list: List of primitives like [1, 2, 3]

    Returns:
        list: Shallow copy that behaves independently

    Example:
        >>> original = [1, 2, 3]
        >>> copied = when_shallow_is_enough(original)
        >>> copied.append(4)
        >>> original
        [1, 2, 3]
        >>> copied
        [1, 2, 3, 4]
    """
    shallow = flat_list.copy()
    return shallow


# =============================================================================
# PART 2 - PRACTICAL NESTED STRUCTURES
# =============================================================================
"""
REAL-WORLD SCENARIOS:
- User data with addresses
- Configuration objects
- Game states
- API response caching
"""


def copy_user_profile(user):
    """
    Creates independent copy of user profile dict.

    User profile contains nested dicts (address, preferences).
    Must use deep copy to avoid shared references.

    Args:
        user: Dict like {
            'name': 'Andrea',
            'address': {'city': 'Milan', 'country': 'Italy'},
            'preferences': {'theme': 'dark'}
        }

    Returns:
        dict: Deep copy of user profile

    Example:
        >>> user = {
        ...     'name': 'Andrea',
        ...     'address': {'city': 'Milan'}
        ... }
        >>> backup = copy_user_profile(user)
        >>> user['address']['city'] = 'Rome'
        >>> backup['address']['city']
        'Milan'
    """
    deep_copy = copy.deepcopy(user)
    return deep_copy


def clone_game_state(game_state):
    """
    Creates independent copy of game state for undo feature.

    Game state contains nested lists (board, players).

    Args:
        game_state: Dict with nested structures like {
            'board': [[' ', 'X'], ['O', ' ']],
            'players': [{'name': 'Alice', 'score': 10}]
        }

    Returns:
        dict: Deep copy for undo stack

    Example:
        >>> state = {
        ...     'board': [[' ', 'X'], ['O', ' ']],
        ...     'turn': 1
        ... }
        >>> backup = clone_game_state(state)
        >>> state['board'][0][0] = 'X'
        >>> backup['board'][0][0]
        ' '
    """
    return copy.deepcopy(game_state)


def update_nested_config(config, key_path, new_value):
    """
    Updates nested config without modifying original.

    Creates deep copy, updates nested value, returns new config.

    Args:
        config: Nested dict
        key_path: List of keys like ['database', 'port']
        new_value: New value to set

    Returns:
        dict: New config with updated value

    Example:
        >>> config = {
        ...     'database': {'host': 'localhost', 'port': 5432},
        ...     'api': {'timeout': 30}
        ... }
        >>> new_config = update_nested_config(config, ['database', 'port'], 3306)
        >>> new_config['database']['port']
        3306
        >>> config['database']['port']
        5432
    """
    pass


def merge_nested_dicts(dict1, dict2):
    """
    Merges two nested dicts without modifying originals.

    Creates deep copies, merges second into first.
    Second dict values override first.

    Args:
        dict1: First nested dict
        dict2: Second nested dict (overrides)

    Returns:
        dict: Merged dict (deep copy)

    Example:
        >>> dict1 = {'user': {'name': 'Andrea', 'age': 30}}
        >>> dict2 = {'user': {'age': 31, 'city': 'Milan'}}
        >>> merged = merge_nested_dicts(dict1, dict2)
        >>> merged
        {'user': {'name': 'Andrea', 'age': 31, 'city': 'Milan'}}
        >>> dict1['user']['age']
        30
    """
    pass


def cache_api_response(response_data):
    """
    Caches API response safely using deep copy.

    API responses often contain nested structures.
    Must deep copy to prevent cache corruption.

    Args:
        response_data: Nested dict from API

    Returns:
        dict: Deep copy safe for caching

    Example:
        >>> response = {
        ...     'users': [
        ...         {'id': 1, 'posts': [{'id': 101}]}
        ...     ]
        ... }
        >>> cached = cache_api_response(response)
        >>> response['users'][0]['posts'].append({'id': 102})
        >>> len(cached['users'][0]['posts'])
        1
    """
    pass


# =============================================================================
# TESTS
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PART 1 - BASIC SHALLOW VS DEEP COPY")
    print("=" * 70)

    print("\n1. Shallow copy behavior:")
    original, copied, same = demonstrate_shallow_copy()
    print(f"Original: {original}")
    print(f"Copied: {copied}")
    print(f"Inner lists same? {same}")

    print("\n2. Deep copy behavior:")
    original, copied, same = demonstrate_deep_copy()
    print(f"Original: {original}")
    print(f"Copied: {copied}")
    print(f"Inner lists same? {same}")

    print("\n3. Safe nested copy:")
    original = [[1, 2], [3, 4]]
    safe = safe_copy_nested_list(original)
    safe[0].append(999)
    print(f"Original: {original}")
    print(f"Safe copy: {safe}")

    print("\n4. Compare copy methods:")
    data = [[1, 2], [3, 4]]
    copies = compare_copy_methods(data)
    data[0][0] = 999
    print(f"Original: {data}")
    print(f"Reference: {copies['reference']}")
    print(f"Shallow: {copies['shallow']}")
    print(f"Deep: {copies['deep']}")

    print("\n5. When shallow is enough:")
    original = [1, 2, 3]
    copied = when_shallow_is_enough(original)
    copied.append(4)
    print(f"Original: {original}")
    print(f"Copied: {copied}")

    print("\n" + "=" * 70)
    print("PART 2 - PRACTICAL NESTED STRUCTURES")
    print("=" * 70)

    print("\n1. Copy user profile:")
    user = {
        "name": "Andrea",
        "address": {"city": "Milan", "country": "Italy"},
        "preferences": {"theme": "dark"},
    }
    backup = copy_user_profile(user)
    user["address"]["city"] = "Rome"
    print(f"User city: {user['address']['city']}")
    print(f"Backup city: {backup['address']['city']}")

    print("\n2. Clone game state:")
    state = {"board": [[" ", "X"], ["O", " "]], "turn": 1}
    backup = clone_game_state(state)
    state["board"][0][0] = "X"
    print(f"Current board: {state['board']}")
    print(f"Backup board: {backup['board']}")

    print("\n3. Update nested config:")
    config = {"database": {"host": "localhost", "port": 5432}, "api": {"timeout": 30}}
    new_config = update_nested_config(config, ["database", "port"], 3306)
    print(f"Original port: {config['database']['port']}")
    print(f"New port: {new_config['database']['port']}")

    print("\n4. Merge nested dicts:")
    dict1 = {"user": {"name": "Andrea", "age": 30}}
    dict2 = {"user": {"age": 31, "city": "Milan"}}
    merged = merge_nested_dicts(dict1, dict2)
    print(f"Original age: {dict1['user']['age']}")
    print(f"Merged: {merged}")

    print("\n5. Cache API response:")
    response = {"users": [{"id": 1, "posts": [{"id": 101}]}]}
    cached = cache_api_response(response)
    response["users"][0]["posts"].append({"id": 102})
    print(f"Response posts: {len(response['users'][0]['posts'])}")
    print(f"Cached posts: {len(cached['users'][0]['posts'])}")

    print("\n" + "=" * 70)
    print("✅ Exercise 1.8 Complete!")
    print("=" * 70)
