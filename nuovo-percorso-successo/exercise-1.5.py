# WEEK 1, DAY 3-5: Data Structures
# Exercise 1.5 - Dictionaries Mastery

# CONCEPTS:
# - Dictionary creation (literal, dict(), dict comprehension)
# - Access: [] vs .get()
# - Methods: keys(), values(), items()
# - Adding, updating, removing items
# - Nested dicts (JSON-like structures)
# - Common patterns: counting, grouping, lookup

# WHY THIS MATTERS:
# Dicts are Python's most powerful data structure. Used for:
# - JSON data (APIs, config files)
# - Counting/grouping (word frequency, user analytics)
# - Fast lookups (O(1) access by key)
# - Caching, memoization
# You'll use dicts in EVERY Python project.

# ============================================================================
# 📚 KNOWLEDGE: Dictionary Basics
# ============================================================================

"""
WHAT IS A DICTIONARY?

- Collection of KEY-VALUE pairs
- Unordered (before Python 3.7) / Ordered (Python 3.7+)
- Keys must be IMMUTABLE (strings, numbers, tuples)
# Values can be anything
- FAST lookup by key (O(1))

CREATING DICTS:

# Literal syntax
person = {"name": "Alice", "age": 25}

# Constructor
person = dict(name="Alice", age=25)

# From list of tuples
person = dict([("name", "Alice"), ("age", 25)])

# Empty dict
empty = {}
empty = dict()

# Dict comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

ACCESSING VALUES:

person = {"name": "Alice", "age": 25}

# With [] (KeyError if missing)
print(person["name"])  # "Alice"
# print(person["job"])   # KeyError!

# With .get() (returns None if missing)
print(person.get("name"))  # "Alice"
print(person.get("job"))   # None
print(person.get("job", "Unknown"))  # "Unknown" (default)

COMPARISON WITH JAVASCRIPT:

// JavaScript
const person = { name: "Alice", age: 25 };
console.log(person.name);        // "Alice"
console.log(person["name"]);     // "Alice"
console.log(person.job);         // undefined
console.log(person.job || "Unknown");  // "Unknown"

# Python
person = {"name": "Alice", "age": 25}
print(person["name"])         # "Alice"
# print(person["job"])        # KeyError!
print(person.get("job"))      # None
print(person.get("job", "Unknown"))  # "Unknown"
"""

# ============================================================================
# 📚 KNOWLEDGE: Dict Methods
# ============================================================================

"""
DICT METHODS REFERENCE:

ACCESSING:
- dict[key]           → Get value (KeyError if missing)
- dict.get(key)       → Get value (None if missing)
- dict.get(key, def)  → Get value (default if missing)
- key in dict         → Check if key exists

ADDING/UPDATING:
- dict[key] = value   → Set/update value
- dict.update(other)  → Merge another dict
- dict.setdefault(k, v) → Set if key doesn't exist

REMOVING:
- del dict[key]       → Delete key (KeyError if missing)
- dict.pop(key)       → Remove and return value
- dict.popitem()      → Remove and return last (key, value)
- dict.clear()        → Remove all items

VIEWING:
- dict.keys()         → View of all keys
- dict.values()       → View of all values
- dict.items()        → View of (key, value) tuples

OTHER:
- len(dict)           → Number of items
- dict.copy()         → Shallow copy

EXAMPLES:

person = {"name": "Alice", "age": 25}

# Add/update
person["job"] = "Engineer"
person.update({"city": "NYC", "age": 26})

# Check existence
if "name" in person:
    print(person["name"])

# Iterate
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")

# Remove
age = person.pop("age")  # Returns 26
del person["city"]
person.clear()  # {}

COMPARISON WITH JAVASCRIPT:

Python                  JavaScript
------                  ----------
dict[key]              obj.key or obj[key]
dict.get(key)          obj[key] (undefined if missing)
dict.keys()            Object.keys(obj)
dict.values()          Object.values(obj)
dict.items()           Object.entries(obj)
key in dict            key in obj or obj.hasOwnProperty(key)
del dict[key]          delete obj[key]
"""

# ============================================================================
# PART 1: Basic Dict Operations
# ============================================================================


def create_user_dict(name, age, email):
    """
    Create and return a dictionary with user information.

    Args:
        name (str): User's name
        age (int): User's age
        email (str): User's email

    Returns:
        dict: {"name": name, "age": age, "email": email}

    Example:
        create_user_dict("Alice", 25, "alice@example.com")
        → {"name": "Alice", "age": 25, "email": "alice@example.com"}
    """
    person = {"name": name, "age": age, "email": email}
    return person


def get_value_safely(data, key, default="N/A"):
    """
    Get value from dict using .get() with default.

    Args:
        data (dict): Dictionary to search
        key: Key to look for
        default: Default value if key not found

    Returns:
        Value if found, else default

    Example:
        get_value_safely({"name": "Alice"}, "name") → "Alice"
        get_value_safely({"name": "Alice"}, "age") → "N/A"
        get_value_safely({"name": "Alice"}, "age", 0) → 0

    Hint: Use dict.get(key, default)
    """
    return data.get(key, default)


def add_or_update(data, key, value):
    """
    Add or update a key-value pair in dictionary.
    Modifies the dict in place and returns it.

    Args:
        data (dict): Dictionary to modify
        key: Key to add/update
        value: Value to set

    Returns:
        dict: Modified dictionary

    Example:
        data = {"name": "Alice"}
        add_or_update(data, "age", 25)
        → {"name": "Alice", "age": 25}
    """
    data[key] = value
    return data


def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries. dict2 values override dict1.
    Don't modify originals, return new dict.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Merged dictionary

    Example:
        merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
        → {"a": 1, "b": 3, "c": 4}

    Hint: Use dict.copy() then update()
    """
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3


# ============================================================================
# PART 2: Iterating Over Dicts
# ============================================================================


def get_all_keys(data):
    """
    Return list of all keys in dictionary.

    Args:
        data (dict): Dictionary

    Returns:
        list: List of keys

    Example:
        get_all_keys({"name": "Alice", "age": 25})
        → ["name", "age"]

    Hint: list(dict.keys())
    """
    return list(data.keys())


def get_all_values(data):
    """
    Return list of all values in dictionary.

    Args:
        data (dict): Dictionary

    Returns:
        list: List of values

    Example:
        get_all_values({"name": "Alice", "age": 25})
        → ["Alice", 25]

    Hint: list(dict.values())
    """
    return list(data.values())


def dict_to_string(data):
    """
    Convert dict to string format: "key1: value1, key2: value2"

    Args:
        data (dict): Dictionary

    Returns:
        str: Formatted string

    Example:
        dict_to_string({"name": "Alice", "age": 25})
        → "name: Alice, age: 25"

    Hint: Use .items() and ", ".join()
    """
    return ", ".join(f"{k}: {v}" for k, v in data.items())


def filter_dict_by_value(data, min_value):
    """
    Return new dict with only values >= min_value.

    Args:
        data (dict): Dictionary with numeric values
        min_value: Minimum value threshold

    Returns:
        dict: Filtered dictionary

    Example:
        filter_dict_by_value({"a": 10, "b": 5, "c": 20}, 10)
        → {"a": 10, "c": 20}

    Hint: Dict comprehension with condition
    """

    new_dict = {key: value for key, value in data.items() if value >= min_value}
    return new_dict


# ============================================================================
# PART 3: Counting and Grouping Patterns
# ============================================================================


def count_characters(text):
    """
    Count frequency of each character in text.

    Args:
        text (str): Input text

    Returns:
        dict: {char: count}

    Example:
        count_characters("hello") → {"h": 1, "e": 1, "l": 2, "o": 1}

    Hint: Loop through text, increment dict[char]
    """
    summary_letter = {}
    for letter in text:
        summary_letter[letter] = summary_letter.get(letter, 0) + 1
    return summary_letter


def word_frequency(text):
    """
    Count frequency of each word in text.
    Case-insensitive, split by spaces.

    Args:
        text (str): Input text

    Returns:
        dict: {word: count}

    Example:
        word_frequency("Hello world hello") → {"hello": 2, "world": 1}

    Hint: text.lower().split(), then count
    """
    summary_word = {}
    for word in text.lower().split():
        summary_word[word] = summary_word.get(word, 0) + 1
    return summary_word


def group_by_first_letter(words):
    """
    Group words by their first letter.

    Args:
        words (list): List of words

    Returns:
        dict: {letter: [words]}

    Example:
        group_by_first_letter(["apple", "banana", "apricot", "cherry"])
        → {"a": ["apple", "apricot"], "b": ["banana"], "c": ["cherry"]}

    Hint: Use setdefault() or check if key in dict
    """
    summary_letter = {}
    for word in words:
        summary_letter.setdefault(word[0], []).append(word)
    return summary_letter


def invert_dict(data):
    """
    Swap keys and values.
    Assume values are unique.

    Args:
        data (dict): Dictionary to invert

    Returns:
        dict: Inverted dictionary

    Example:
        invert_dict({"a": 1, "b": 2}) → {1: "a", 2: "b"}

    Hint: {value: key for key, value in dict.items()}
    """
    inverted_data = {value: key for key, value in data.items()}
    return inverted_data


# ============================================================================
# PART 4: Nested Dictionaries (JSON-like)
# ============================================================================


def create_nested_user():
    """
    Create a nested dictionary representing a user with address.

    Returns:
        dict: Nested user dictionary

    Structure:
    {
        "name": "Alice",
        "age": 25,
        "address": {
            "street": "123 Main St",
            "city": "NYC",
            "zip": "10001"
        }
    }
    """
    address = {
        "name": "Alice",
        "age": 25,
        "address": {"street": "123 Main St", "city": "NYC", "zip": "10001"},
    }
    return address


def get_nested_value(data, *keys):
    """
    Safely get value from nested dict using multiple keys.

    Args:
        data (dict): Nested dictionary
        *keys: Variable number of keys to traverse

    Returns:
        Value if found, else None

    Example:
        user = {"address": {"city": "NYC"}}
        get_nested_value(user, "address", "city") → "NYC"
        get_nested_value(user, "address", "country") → None

    Hint: Loop through keys, use .get() at each level
    """
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
    return data


def flatten_dict(nested_dict, parent_key="", sep="_"):
    """
    Flatten a nested dictionary.

    Args:
        nested_dict (dict): Nested dictionary
        parent_key (str): Prefix for keys
        sep (str): Separator for keys

    Returns:
        dict: Flattened dictionary

    Example:
        flatten_dict({"user": {"name": "Alice", "age": 25}})
        → {"user_name": "Alice", "user_age": 25}

    Hint: Recursion or iterative with queue
    """
    items = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


# ============================================================================
# PART 5: Dict Comprehension & Advanced Patterns
# ============================================================================


def square_dict(n):
    """
    Create dict mapping numbers to their squares.

    Args:
        n (int): Range from 0 to n-1

    Returns:
        dict: {0: 0, 1: 1, 2: 4, 3: 9, ...}

    Example:
        square_dict(5) → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

    Hint: {x: x**2 for x in range(n)}
    """
    result = {x: x**2 for x in range(n)}
    return result


def filter_dict_by_keys(data, keys_to_keep):
    """
    Keep only specified keys in dictionary.

    Args:
        data (dict): Original dictionary
        keys_to_keep (list): Keys to keep

    Returns:
        dict: Filtered dictionary

    Example:
        filter_dict_by_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"])
        → {"a": 1, "c": 3}

    Hint: {k: data[k] for k in keys_to_keep if k in data}
    """

    result = {k: data[k] for k in keys_to_keep if k in data}
    return result


def dict_from_two_lists(keys, values):
    """
    Create dict from two lists (keys and values).

    Args:
        keys (list): List of keys
        values (list): List of values

    Returns:
        dict: Combined dictionary

    Example:
        dict_from_two_lists(["a", "b", "c"], [1, 2, 3])
        → {"a": 1, "b": 2, "c": 3}

    Hint: zip() and dict comprehension or dict(zip())
    """
    return dict(zip(keys, values))


def find_max_value_key(data):
    """
    Find key with maximum value.

    Args:
        data (dict): Dictionary with numeric values

    Returns:
        Key with max value

    Example:
        find_max_value_key({"a": 10, "b": 25, "c": 5}) → "b"

    Hint: max(dict, key=lambda k: dict[k])
    """
    max_value = float("-inf")
    winner = None
    for key, value in data.items():
        if value > max_value:
            winner = key
            max_value = value
    return winner


# ============================================================================
# TESTS
# ============================================================================

# print("=== PART 1: Basic Operations ===")
# print(create_user_dict("Alice", 25, "alice@example.com"))
# # Expected: {"name": "Alice", "age": 25, "email": "alice@example.com"}

# print(get_value_safely({"name": "Alice"}, "name"))
# # Expected: "Alice"

# print(get_value_safely({"name": "Alice"}, "age"))
# # Expected: "N/A"

# data = {"name": "Alice"}
# add_or_update(data, "age", 25)
# print(data)
# # Expected: {"name": "Alice", "age": 25}

# print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))
# # Expected: {"a": 1, "b": 3, "c": 4}
# print()

# print("=== PART 2: Iterating ===")
# # print(get_all_keys({"name": "Alice", "age": 25}))
# # # Expected: ["name", "age"] (or similar)

# # print(get_all_values({"name": "Alice", "age": 25}))
# # # Expected: ["Alice", 25] (or similar)

# # print(dict_to_string({"name": "Alice", "age": 25}))
# # # Expected: "name: Alice, age: 25" (or similar order)

# print(filter_dict_by_value({"a": 10, "b": 5, "c": 20}, 10))
# # Expected: {"a": 10, "c": 20}
# print()

# print("=== PART 3: Counting & Grouping ===")
# # print(count_characters("andreaa"))
# # Expected: {"h": 1, "e": 1, "l": 2, "o": 1}

# # print(word_frequency("Hello world hello andrea"))
# # # Expected: {"hello": 2, "world": 1}

# print(group_by_first_letter(["apple", "banana", "apricot", "cherry"]))
# Expected: {"a": ["apple", "apricot"], "b": ["banana"], "c": ["cherry"]}

# print(invert_dict({"a": 1, "b": 2}))
# # Expected: {1: "a", 2: "b"}
# print()

# print("=== PART 4: Nested Dicts ===")
# user = create_nested_user()
# print(user)
# # # Expected: {"name": "Alice", "age": 25, "address": {...}}

# print(get_nested_value(user, "address", "city"))
# Expected: "NYC"

# print(get_nested_value(user, "address", "country"))
# Expected: None

# print(flatten_dict({"user": {"name": "Alice", "age": 25}}))
# # Expected: {"user_name": "Alice", "user_age": 25}
# print()

print("=== PART 5: Comprehension & Advanced ===")
# # print(square_dict(5))
# # Expected: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# print(filter_dict_by_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
# Expected: {"a": 1, "c": 3}

# print(dict_from_two_lists(["a", "b", "c"], [1, 2, 3]))
# # Expected: {"a": 1, "b": 2, "c": 3}

print(find_max_value_key({"a": 10, "b": 25, "c": 5}))
# Expected: "b"
