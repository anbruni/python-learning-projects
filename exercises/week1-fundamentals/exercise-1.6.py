# WEEK 1, DAY 3-5: Data Structures
# Exercise 1.6 - Sets Operations

# CONCEPTS:
# - Set creation (literal, set(), set comprehension)
# - Uniqueness (automatic duplicate removal)
# - Set operations: union, intersection, difference, symmetric difference
# - Membership testing (O(1) performance)
# - Set methods: add, remove, discard, pop, clear
# - frozenset (immutable set)

# WHY THIS MATTERS:
# Sets are incredibly useful for:
# - Removing duplicates from lists
# - Fast membership testing (O(1) vs O(n) for lists)
# - Mathematical set operations (union, intersection)
# - Tracking "seen" items in algorithms
# You'll use sets in data processing, algorithms, and optimization.

# ============================================================================
# 📚 KNOWLEDGE: Set Basics
# ============================================================================

"""
WHAT IS A SET?

- Unordered collection of UNIQUE elements
- Automatically removes duplicates
- Fast membership testing O(1)
- Elements must be immutable (hashable)
- NO indexing, NO slicing

CREATING SETS:

# Literal syntax
fruits = {"apple", "banana", "cherry"}

# From list (removes duplicates!)
numbers = set([1, 2, 2, 3, 3, 3])
print(numbers)  # {1, 2, 3}

# Empty set (CAREFUL!)
empty = set()  # ✅ Correct
# empty = {}   # ❌ This creates an empty DICT!

# Set comprehension
squares = {x**2 for x in range(5)}
# {0, 1, 4, 9, 16}

COMPARISON WITH JAVASCRIPT:

// JavaScript
const mySet = new Set([1, 2, 2, 3]);
console.log(mySet);  // Set {1, 2, 3}
mySet.add(4);
mySet.has(3);  // true
mySet.size;    // 4

# Python
my_set = {1, 2, 2, 3}
print(my_set)  # {1, 2, 3}
my_set.add(4)
3 in my_set    # True
len(my_set)    # 4
"""

# ============================================================================
# 📚 KNOWLEDGE: Set Operations (Mathematical)
# ============================================================================

"""
SET OPERATIONS:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

UNION (|) - All elements from both sets:
a | b                → {1, 2, 3, 4, 5, 6}
a.union(b)           → {1, 2, 3, 4, 5, 6}

INTERSECTION (&) - Only common elements:
a & b                → {3, 4}
a.intersection(b)    → {3, 4}

DIFFERENCE (-) - Elements in first but not in second:
a - b                → {1, 2}
a.difference(b)      → {1, 2}

SYMMETRIC DIFFERENCE (^) - Elements in either set, but not both:
a ^ b                → {1, 2, 5, 6}
a.symmetric_difference(b) → {1, 2, 5, 6}

VISUAL EXAMPLE:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A | B  → {1, 2, 3, 4, 5, 6}  (everything)
A & B  → {3, 4}              (only common)
A - B  → {1, 2}              (only in A)
B - A  → {5, 6}              (only in B)
A ^ B  → {1, 2, 5, 6}        (not common)
"""

# ============================================================================
# 📚 KNOWLEDGE: Performance - Why Sets Are Fast
# ============================================================================

"""
MEMBERSHIP TESTING PERFORMANCE:

# With List: O(n) - checks every element
my_list = [1, 2, 3, 4, 5, ..., 1000000]
if 999999 in my_list:  # Slow! Checks all elements
    pass

# With Set: O(1) - instant lookup using hash
my_set = {1, 2, 3, 4, 5, ..., 1000000}
if 999999 in my_set:   # Fast! Direct lookup
    pass

PERFORMANCE COMPARISON:
List with 1M elements: ~0.015s to find last element
Set with 1M elements:  ~0.000001s (15,000x faster!)

WHEN TO USE SETS:
✅ Need to check "is this item in collection?" many times
✅ Need to remove duplicates
✅ Don't care about order
✅ Don't need to access by index
✅ Need mathematical set operations
"""

# ============================================================================
# PART 1: Set Creation and Basic Operations
# ============================================================================


def create_set_from_list(items):
    """
    Create a set from a list, removing duplicates.

    Args:
        items (list): List of items (may contain duplicates)

    Returns:
        set: Set with unique items

    Example:
        create_set_from_list([1, 2, 2, 3, 3, 3]) → {1, 2, 3}
        create_set_from_list(["a", "b", "a", "c"]) → {"a", "b", "c"}
    """
    return set(items)


def count_unique_elements(items):
    """
    Count how many unique elements are in a list.

    Args:
        items (list): List of items

    Returns:
        int: Number of unique elements

    Example:
        count_unique_elements([1, 2, 2, 3, 3, 3]) → 3
        count_unique_elements(["a", "a", "a"]) → 1

    Hint: len(set(items))
    """
    return len(set(items))


def has_duplicates(items):
    """
    Check if a list has duplicate elements.

    Args:
        items (list): List to check

    Returns:
        bool: True if duplicates exist, False otherwise

    Example:
        has_duplicates([1, 2, 3]) → False
        has_duplicates([1, 2, 2, 3]) → True

    Hint: Compare len(items) with len(set(items))
    """
    return len(items) > len(set(items))


def add_to_set(my_set, element):
    """
    Add an element to a set and return the set.

    Args:
        my_set (set): The set to modify
        element: Element to add

    Returns:
        set: Modified set

    Example:
        add_to_set({1, 2, 3}, 4) → {1, 2, 3, 4}
        add_to_set({1, 2, 3}, 2) → {1, 2, 3} (duplicate ignored)

    Hint: set.add()
    """
    my_set.add(element)
    return my_set


# ============================================================================
# PART 2: Set Operations (Union, Intersection, Difference)
# ============================================================================


def get_union(set1, set2):
    """
    Return union of two sets (all elements from both).

    Args:
        set1 (set): First set
        set2 (set): Second set

    Returns:
        set: Union of both sets

    Example:
        get_union({1, 2, 3}, {3, 4, 5}) → {1, 2, 3, 4, 5}

    Hint: Use | operator or .union()
    """
    return set1 | set2


def get_intersection(set1, set2):
    """
    Return intersection of two sets (only common elements).

    Args:
        set1 (set): First set
        set2 (set): Second set

    Returns:
        set: Intersection of both sets

    Example:
        get_intersection({1, 2, 3}, {2, 3, 4}) → {2, 3}
        get_intersection({1, 2}, {3, 4}) → set() (empty)

    Hint: Use & operator or .intersection()
    """
    return set1 & set2


def get_difference(set1, set2):
    """
    Return difference of two sets (elements in set1 but not in set2).

    Args:
        set1 (set): First set
        set2 (set): Second set

    Returns:
        set: Elements in set1 that are not in set2

    Example:
        get_difference({1, 2, 3, 4}, {3, 4, 5}) → {1, 2}
        get_difference({1, 2}, {1, 2, 3}) → set()

    Hint: Use - operator or .difference()
    """
    return set1 - set2


def get_symmetric_difference(set1, set2):
    """
    Return symmetric difference (elements in either set, but not both).

    Args:
        set1 (set): First set
        set2 (set): Second set

    Returns:
        set: Elements that are in either set but not in both

    Example:
        get_symmetric_difference({1, 2, 3}, {3, 4, 5}) → {1, 2, 4, 5}

    Hint: Use ^ operator or .symmetric_difference()
    """
    return set1 ^ set2


# ============================================================================
# PART 3: Real-World Applications
# ============================================================================


def find_common_elements(list1, list2):
    """
    Find elements that appear in both lists.

    Args:
        list1 (list): First list
        list2 (list): Second list

    Returns:
        list: Elements that appear in both lists (no duplicates)

    Example:
        find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) → [3, 4]
        find_common_elements(["a", "b"], ["c", "d"]) → []

    Hint: Convert to sets, use intersection, convert back to list
    """

    return list((set(list1) & set(list2)))


def find_unique_to_first(list1, list2):
    """
    Find elements that are in list1 but not in list2.

    Args:
        list1 (list): First list
        list2 (list): Second list

    Returns:
        list: Elements only in list1

    Example:
        find_unique_to_first([1, 2, 3, 4], [3, 4, 5]) → [1, 2]
        find_unique_to_first(["a", "b", "c"], ["c", "d"]) → ["a", "b"]

    Hint: Use set difference
    """
    return list((set(list1) - set(list2)))


def merge_without_duplicates(list1, list2):
    """
    Merge two lists and remove all duplicates.

    Args:
        list1 (list): First list
        list2 (list): Second list

    Returns:
        list: Merged list with unique elements

    Example:
        merge_without_duplicates([1, 2, 3], [3, 4, 5]) → [1, 2, 3, 4, 5]

    Hint: Use set union
    """
    return list((set(list1) | set(list2)))


def has_common_elements(list1, list2):
    """
    Check if two lists have any common elements.

    Args:
        list1 (list): First list
        list2 (list): Second list

    Returns:
        bool: True if there are common elements, False otherwise

    Example:
        has_common_elements([1, 2, 3], [3, 4, 5]) → True
        has_common_elements([1, 2], [3, 4]) → False

    Hint: Check if intersection is not empty
    """
    return len(list(set(list1) & set(list2))) > 0


# ============================================================================
# PART 4: Set Comprehension & Advanced Patterns
# ============================================================================


def get_unique_lengths(words):
    """
    Get set of unique word lengths from a list of words.

    Args:
        words (list): List of words

    Returns:
        set: Set of unique lengths

    Example:
        get_unique_lengths(["hi", "hello", "hey", "world"]) → {2, 3, 5}

    Hint: Set comprehension {len(word) for word in words}
    """
    # Your code here
    pass


def get_vowels_in_text(text):
    """
    Get set of unique vowels present in text (lowercase).

    Args:
        text (str): Input text

    Returns:
        set: Set of vowels found in text

    Example:
        get_vowels_in_text("Hello World") → {"e", "o"}
        get_vowels_in_text("Python") → {"o"}

    Hint: Set comprehension with condition, check if char in "aeiou"
    """
    # Your code here
    pass


def remove_seen_items(items, seen):
    """
    Remove items that have been seen before.

    Args:
        items (list): List of items
        seen (set): Set of already seen items

    Returns:
        list: Items that are not in seen set

    Example:
        remove_seen_items([1, 2, 3, 4], {2, 4}) → [1, 3]
        remove_seen_items(["a", "b", "c"], {"b"}) → ["a", "c"]

    Hint: List comprehension with condition
    """
    # Your code here
    pass


def get_all_characters(words):
    """
    Get set of all unique characters from a list of words.

    Args:
        words (list): List of words

    Returns:
        set: Set of all unique characters

    Example:
        get_all_characters(["hello", "world"]) → {"h", "e", "l", "o", "w", "r", "d"}

    Hint: Set comprehension, iterate through words and characters
    """
    # Your code here
    pass


# ============================================================================
# PART 5: Performance & Practical Use Cases
# ============================================================================


def find_duplicates_in_list(items):
    """
    Find all duplicate elements in a list.

    Args:
        items (list): List of items

    Returns:
        set: Set of elements that appear more than once

    Example:
        find_duplicates_in_list([1, 2, 2, 3, 3, 3, 4]) → {2, 3}
        find_duplicates_in_list([1, 2, 3]) → set()

    Hint: Track seen items, check if already seen
    """
    # Your code here
    pass


def is_subset(set1, set2):
    """
    Check if set1 is a subset of set2 (all elements of set1 are in set2).

    Args:
        set1 (set): First set
        set2 (set): Second set

    Returns:
        bool: True if set1 is subset of set2

    Example:
        is_subset({1, 2}, {1, 2, 3, 4}) → True
        is_subset({1, 5}, {1, 2, 3, 4}) → False

    Hint: Use .issubset() or <= operator
    """
    # Your code here
    pass


def are_disjoint(set1, set2):
    """
    Check if two sets have no common elements.

    Args:
        set1 (set): First set
        set2 (set): Second set

    Returns:
        bool: True if sets have no common elements

    Example:
        are_disjoint({1, 2}, {3, 4}) → True
        are_disjoint({1, 2}, {2, 3}) → False

    Hint: Use .isdisjoint()
    """
    # Your code here
    pass


def count_common_interests(user1_interests, user2_interests):
    """
    Count how many interests two users have in common.

    Args:
        user1_interests (set): First user's interests
        user2_interests (set): Second user's interests

    Returns:
        int: Number of common interests

    Example:
        count_common_interests({"python", "ai", "cinema"},
                              {"python", "cinema", "music"}) → 2

    Hint: len(intersection)
    """
    # Your code here
    pass


# ============================================================================
# TESTS
# ============================================================================

# print("=== PART 1: Set Creation ===")
# print(create_set_from_list([1, 2, 2, 3, 3, 3]))
# # Expected: {1, 2, 3}

# print(count_unique_elements([1, 2, 2, 3, 3, 3]))
# # Expected: 3

# print(has_duplicates([1, 2, 3]))
# # Expected: False

# print(has_duplicates([1, 2, 2, 3]))
# # Expected: True

# my_set = {1, 2, 3}
# print(add_to_set(my_set, 4))
# # Expected: {1, 2, 3, 4}
# print()

# print("=== PART 2: Set Operations ===")
# print(get_union({1, 2, 3}, {3, 4, 5}))
# # Expected: {1, 2, 3, 4, 5}

# print(get_intersection({1, 2, 3}, {2, 3, 4}))
# # Expected: {2, 3}

# print(get_difference({1, 2, 3, 4}, {3, 4, 5}))
# # Expected: {1, 2}

# print(get_symmetric_difference({1, 2, 3}, {3, 4, 5}))
# # Expected: {1, 2, 4, 5}
# print()

print("=== PART 3: Real-World Applications ===")
print(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
# Expected: [3, 4] or [4, 3] (order doesn't matter)

print(find_unique_to_first([1, 2, 3, 4], [3, 4, 5]))
# Expected: [1, 2] or [2, 1]

print(merge_without_duplicates([1, 2, 3], [3, 4, 5]))
# Expected: [1, 2, 3, 4, 5] (order may vary)

print(has_common_elements([1, 2, 3], [3, 4, 5]))
# Expected: True

print(has_common_elements([1, 2], [3, 4]))
# Expected: False
print()

# print("=== PART 4: Set Comprehension ===")
# print(get_unique_lengths(["hi", "hello", "hey", "world"]))
# # Expected: {2, 3, 5}

# print(get_vowels_in_text("Hello World"))
# # Expected: {"e", "o"}

# print(remove_seen_items([1, 2, 3, 4], {2, 4}))
# # Expected: [1, 3] or [3, 1]

# print(get_all_characters(["hello", "world"]))
# # Expected: {"h", "e", "l", "o", "w", "r", "d"}
# print()

# print("=== PART 5: Performance & Practical ===")
# print(find_duplicates_in_list([1, 2, 2, 3, 3, 3, 4]))
# # Expected: {2, 3}

# print(is_subset({1, 2}, {1, 2, 3, 4}))
# # Expected: True

# print(is_subset({1, 5}, {1, 2, 3, 4}))
# # Expected: False

# print(are_disjoint({1, 2}, {3, 4}))
# # Expected: True

# print(are_disjoint({1, 2}, {2, 3}))
# # Expected: False

# user1 = {"python", "ai", "cinema"}
# user2 = {"python", "cinema", "music"}
# print(count_common_interests(user1, user2))
# # Expected: 2
