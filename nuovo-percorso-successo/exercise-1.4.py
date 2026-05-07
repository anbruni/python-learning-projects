# WEEK 1, DAY 3-5: Data Structures
# Exercise 1.4 - Tuples Deep Dive

# CONCEPTS:
# - Tuple creation and syntax
# - Immutability (cannot modify after creation)
# - Tuple packing/unpacking
# - Multiple return values
# - Named tuples
# - Tuple methods (count, index)
# - Tuple vs List (when to use what)

# WHY THIS MATTERS:
# Tuples are immutable sequences used for fixed data that shouldn't change.
# They're faster than lists, use less memory, and can be used as dict keys.
# Common in function returns, data integrity, and coordinates.

# ============================================================================
# 📚 KNOWLEDGE: Tuple Basics
# ============================================================================

"""
WHAT IS A TUPLE?
- Ordered collection (like list)
- IMMUTABLE (cannot change after creation)
- Can contain mixed types
- Created with parentheses () or just commas
- Faster and more memory-efficient than lists

CREATING TUPLES:

# With parentheses
point = (3, 5)
person = ("Alice", 25, "Engineer")

# Without parentheses (tuple packing)
point = 3, 5
person = "Alice", 25, "Engineer"

# Single element tuple (NEEDS COMMA!)
single = (42,)    # ✅ Tuple with one element
not_tuple = (42)  # ❌ Just an int in parentheses!

# Empty tuple
empty = ()
empty = tuple()

# From other iterables
from_list = tuple([1, 2, 3])
from_string = tuple("abc")  # ('a', 'b', 'c')

TUPLE vs LIST:

Feature              List            Tuple
-------              ----            -----
Syntax               [1, 2, 3]       (1, 2, 3) or 1, 2, 3
Mutable              ✅ Yes          ❌ No
Performance          Slower          Faster
Memory               More            Less
Dict key             ❌ No           ✅ Yes (if elements hashable)
Methods              Many            Few (count, index)
Use case             Dynamic data    Fixed data

IMMUTABILITY:

# List (mutable)
my_list = [1, 2, 3]
my_list[0] = 99      # ✅ Works
my_list.append(4)    # ✅ Works

# Tuple (immutable)
my_tuple = (1, 2, 3)
# my_tuple[0] = 99   # ❌ TypeError!
# my_tuple.append(4) # ❌ AttributeError!

# BUT nested mutable objects CAN be modified
nested = ([1, 2], [3, 4])
nested[0].append(99)  # ✅ Works! List inside tuple can change
print(nested)  # ([1, 2, 99], [3, 4])

COMPARISON WITH JAVASCRIPT:
JavaScript doesn't have tuples. Closest equivalent:
- Frozen arrays (rare): Object.freeze([1, 2, 3])
- Destructuring: const [x, y] = [1, 2]
- Python tuples are native and optimized
"""

# ============================================================================
# 📚 KNOWLEDGE: Tuple Packing/Unpacking
# ============================================================================
#
# TUPLE PACKING (grouping values):
#
# # Implicit packing (no parentheses needed)
# point = 3, 5              # Same as (3, 5)
# person = "Alice", 25      # Same as ("Alice", 25)
#
# TUPLE UNPACKING (extracting values):
#
# # Basic unpacking
# point = (3, 5)
# x, y = point
# print(x)  # 3
# print(y)  # 5
#
# # Multiple return values (common pattern!)
# def get_user():
#     return "Alice", 25, "Engineer"
#
# name, age, job = get_user()  # Unpack tuple
#
# # Swap values (without temp variable!)
# a, b = 10, 20
# a, b = b, a  # Swap!
# print(a, b)  # 20, 10
#
# EXTENDED UNPACKING (*rest):
#
# # Get first and rest
# first, *rest = (1, 2, 3, 4, 5)
# print(first)  # 1
# print(rest)   # [2, 3, 4, 5] ← Note: list!
#
# # Get first, middle, last
# first, *middle, last = (1, 2, 3, 4, 5)
# print(first)   # 1
# print(middle)  # [2, 3, 4]
# print(last)    # 5
#
# # Ignore values with _
# name, _, job = ("Alice", 25, "Engineer")
# print(name, job)  # Alice Engineer
#
# NESTED UNPACKING:
#
# # Nested tuples
# person = ("Alice", (25, "Engineer"))
# name, (age, job) = person
# print(name, age, job)  # Alice 25 Engineer
#
# COMPARISON WITH JAVASCRIPT:
# // JavaScript array destructuring (similar)
# const [x, y] = [3, 5];
# const [first, ...rest] = [1, 2, 3, 4, 5];
# const [a, , c] = [1, 2, 3];  // Skip middle
#
# // Python tuple unpacking (more powerful)
# x, y = 3, 5  # No brackets needed!
# first, *rest = (1, 2, 3, 4, 5)
# a, _, c = (1, 2, 3)  # Use _ for ignored values

# ============================================================================
# 📚 KNOWLEDGE: Named Tuples
# ============================================================================
#
# NAMED TUPLES (tuples with named fields):
#
# from collections import namedtuple
#
# # Define a named tuple type
# Point = namedtuple('Point', ['x', 'y'])
#
# # Create instances
# p1 = Point(3, 5)
# p2 = Point(x=10, y=20)
#
# # Access by name (readable!)
# print(p1.x)  # 3
# print(p1.y)  # 5
#
# # Or by index (still works)
# print(p1[0])  # 3
# print(p1[1])  # 5
#
# # Unpacking works
# x, y = p1
#
# BENEFITS:
# ✅ More readable than plain tuples
# ✅ Self-documenting code
# ✅ Still immutable
# ✅ Still fast and memory-efficient
# ✅ Can be used as dict keys
#
# EXAMPLE - Person:
#
# Person = namedtuple('Person', ['name', 'age', 'job'])
# alice = Person('Alice', 25, 'Engineer')
#
# # Readable!
# print(alice.name)  # Alice
# print(alice.age)   # 25
#
# # vs regular tuple (what does [1] mean?)
# alice_tuple = ('Alice', 25, 'Engineer')
# print(alice_tuple[1])  # 25 ← What is this?
#
# COMPARISON WITH JAVASCRIPT:
# // JavaScript objects (mutable)
# const point = { x: 3, y: 5 };
# point.x = 10;  // Can modify
#
# // Python namedtuple (immutable)
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(3, 5)
# # p.x = 10  # ❌ AttributeError!

# ============================================================================
# PART 1: Tuple Basics
# ============================================================================


def create_coordinate(x, y):
    """
    Create and return a tuple representing a coordinate.

    Example:
        create_coordinate(3, 5) → (3, 5)
        create_coordinate(-1, 10) → (-1, 10)
    """
    coordinate = (x, y)
    return coordinate


def get_first_and_last(items):
    """
    Return tuple with first and last elements of a sequence.

    Example:
        get_first_and_last([1, 2, 3, 4, 5]) → (1, 5)
        get_first_and_last("hello") → ('h', 'o')

    Hint: (items[0], items[-1])
    """
    my_tuple = (items[0], items[-1])
    return my_tuple


def demonstrate_immutability():
    """
    Demonstrate that tuples are immutable.

    Try to modify a tuple and catch the error.
    Return the error type name as a string.

    Example:
        Try: my_tuple[0] = 99
        Return: "TypeError"

    Hint: Use try/except and return type(e).__name__
    """
    my_tuple = (99, 12, 4, 5)
    try:
        my_tuple[0] = 299
    except TypeError as e:
        return type(e).__name__


# ============================================================================
# PART 2: Tuple Packing/Unpacking
# ============================================================================


def swap_values(a, b):
    """
    Swap two values using tuple unpacking.
    Return tuple with swapped values.

    Example:
        swap_values(10, 20) → (20, 10)
        swap_values("hello", "world") → ("world", "hello")

    Hint: Use a, b = b, a
    """
    a, b = b, a
    return (a, b)


def split_name(full_name):
    """
    Split "First Last" into tuple (first, last).

    Example:
        split_name("John Doe") → ("John", "Doe")
        split_name("Alice Smith") → ("Alice", "Smith")

    Hint: Use split() then tuple() or unpacking
    """
    # my_tuple = tuple((my_name[0], my_name[1]))
    name, surname = full_name.split()
    return (name, surname)


def get_first_and_rest(items):
    """
    Return tuple: (first_item, list_of_rest).
    Use extended unpacking (*rest).

    Example:
        get_first_and_rest([1, 2, 3, 4, 5]) → (1, [2, 3, 4, 5])
        get_first_and_rest(["a", "b", "c"]) → ("a", ["b", "c"])

    Hint: first, *rest = items
    """
    first, *rest = items
    return (first, rest)


def get_min_max_avg(numbers):
    """
    Return tuple: (min, max, average).

    Example:
        get_min_max_avg([1, 2, 3, 4, 5]) → (1, 5, 3.0)
        get_min_max_avg([10, 20, 30]) → (10, 30, 20.0)

    Hint: (min(numbers), max(numbers), sum(numbers)/len(numbers))
    """
    return (min(numbers), max(numbers), sum(numbers) / len(numbers))


# ============================================================================
# PART 3: Tuple Methods & Operations
# ============================================================================


def count_occurrences(items, value):
    """
    Count how many times value appears in tuple.

    Example:
        count_occurrences((1, 2, 3, 2, 1, 2), 2) → 3
        count_occurrences(("a", "b", "a", "c"), "a") → 2

    Hint: Use .count() method
    """
    total = items.count(value)
    return total


def find_position(items, value):
    """
    Find index of first occurrence of value.
    Return -1 if not found (don't use try/except).

    Example:
        find_position((1, 2, 3, 4, 5), 3) → 2
        find_position(("a", "b", "c"), "d") → -1

    Hint: Check if value in items first, then use .index()
    """
    if value in items:
        return items.index(value)
    return -1


def tuple_to_list_and_back(items):
    """
    Convert tuple to list, add 99, convert back to tuple.
    Return the new tuple.

    Example:
        tuple_to_list_and_back((1, 2, 3)) → (1, 2, 3, 99)

    Hint: list(items), append, tuple()
    """
    new_list = list(items)
    new_list.append(99)
    return tuple(new_list)


# ============================================================================
# PART 4: Named Tuples
# ============================================================================

from collections import namedtuple

# Define Person named tuple
Person = namedtuple("Person", ["name", "age", "city"])


def create_person(name, age, city):
    """
    Create and return a Person named tuple.

    Example:
        create_person("Alice", 25, "NYC") → Person(name='Alice', age=25, city='NYC')
    """
    person = Person(name=name, age=age, city=city)
    return person


def get_person_info(person):
    """
    Extract info from Person named tuple.
    Return string: "name is age years old and lives in city"

    Example:
        p = Person("Alice", 25, "NYC")
        get_person_info(p) → "Alice is 25 years old and lives in NYC"

    Hint: Access person.name, person.age, person.city
    """
    return f"{person.name} is {person.age} years old and lives in {person.city}"


# ============================================================================
# PART 5: Real-World Use Cases
# ============================================================================


def get_user_credentials():
    """
    Simulate returning multiple values from a function.
    Return tuple: (username, password, is_admin)

    Use fixed values: ("admin", "secret123", True)

    This pattern is common for functions that need to return multiple values!
    """
    username, password, is_admin = "admin", "secret123", True
    return username, password, is_admin


def calculate_rectangle(width, height):
    """
    Calculate area and perimeter of rectangle.
    Return tuple: (area, perimeter)

    Example:
        calculate_rectangle(5, 3) → (15, 16)
        calculate_rectangle(10, 20) → (200, 60)

    Hint: area = width * height, perimeter = 2 * (width + height)
    """
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


import re


def parse_rgb_color(color_string):
    """
    Parse "rgb(255, 128, 0)" into tuple (255, 128, 0).

    Example:
        parse_rgb_color("rgb(255, 128, 0)") → (255, 128, 0)
        parse_rgb_color("rgb(100, 200, 50)") → (100, 200, 50)

    Hint: Remove "rgb(" and ")", split by ",", convert to int, return as tuple
    """
    formatted = re.search("^rgb\((\d+), (\d+), (\d+)\)$", color_string)
    if formatted:
        return tuple(map(int, formatted.groups()))
    return None


# ============================================================================
# TESTS
# ============================================================================

print("=== PART 1: Tuple Basics ===")
# print(create_coordinate(3, 5))
# # Expected: (3, 5)

# print(get_first_and_last([1, 2, 3, 4, 5]))
# # Expected: (1, 5)

# print(demonstrate_immutability())
# # Expected: "TypeError"
# print()

print("=== PART 2: Packing/Unpacking ===")
# print(swap_values(10, 20))
# print(swap_values("hello", "world"))
# # Expected: (20, 10)

# print(split_name("John Doe"))
# Expected: ("John", "Doe")

# print(get_first_and_rest([1, 2, 3, 4, 5]))
# Expected: (1, [2, 3, 4, 5])

# print(get_min_max_avg([1, 2, 3, 4, 5]))
# # Expected: (1, 5, 3.0)
# print()

# print("=== PART 3: Methods ===")
# # print(count_occurrences((1, 2, 3, 2, 1, 2), 2))
# # # Expected: 3

# # print(find_position((1, 2, 3, 4, 5), 3))
# # # Expected: 2

# # print(find_position(("a", "b", "c"), "d"))
# # Expected: -1

# print(tuple_to_list_and_back((1, 2, 3)))
# # Expected: (1, 2, 3, 99)
# print()

# print("=== PART 4: Named Tuples ===")
# alice = create_person("Alice", 25, "NYC")
# print(alice)
# # Expected: Person(name='Alice', age=25, city='NYC')

# print(get_person_info(alice))
# # Expected: "Alice is 25 years old and lives in NYC"
# print()

print("=== PART 5: Real-World ===")
# print(get_user_credentials())
# Expected: ("admin", "secret123", True)

# print(calculate_rectangle(5, 3))
# Expected: (15, 16)

print(parse_rgb_color("rgb(255, 128, 0)"))
# # Expected: (255, 128, 0)
