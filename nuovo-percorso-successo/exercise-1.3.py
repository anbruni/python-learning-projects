# WEEK 1, DAY 3-5: Data Structures
# Exercise 1.3 - Lists Deep Dive

# CONCEPTS:
# - List methods (append, extend, insert, pop, remove, sort, reverse)
# - Slicing [start:end:step]
# - List operations (concatenation, repetition, membership)
# - Nesting (list of lists)
# - List vs Reference vs Copy

# WHY THIS MATTERS:
# Lists are THE most used data structure in Python. You'll use them daily.
# Understanding methods, slicing, and references is critical.

# ============================================================================
# 📚 KNOWLEDGE: List Methods
# ============================================================================

"""
LIST METHODS REFERENCE:

ADDING ELEMENTS:
- append(item)     → Add ONE item to end
- extend(iterable) → Add ALL items from iterable to end
- insert(i, item)  → Insert item at index i

REMOVING ELEMENTS:
- remove(item)     → Remove FIRST occurrence of item (ValueError if not found)
- pop()            → Remove and return LAST item
- pop(i)           → Remove and return item at index i
- clear()          → Remove all items

ORDERING:
- sort()           → Sort in place (modifies original)
- reverse()        → Reverse in place (modifies original)
- sorted(list)     → Return NEW sorted list (original unchanged)
- reversed(list)   → Return iterator (need list() to convert)

SEARCHING:
- index(item)      → Return index of first occurrence (ValueError if not found)
- count(item)      → Count occurrences of item

OTHER:
- copy()           → Shallow copy of list
- len(list)        → Number of items
- list[i]          → Access item at index i
- list[i] = value  → Set item at index i

COMPARISON WITH JAVASCRIPT:
Python              JavaScript
------              ----------
append(x)          push(x)
extend([x, y])     push(x, y) or concat([x, y])
pop()              pop()
remove(x)          splice(indexOf(x), 1)
insert(i, x)       splice(i, 0, x)
sort()             sort() (but different behavior!)
"""

# ============================================================================
# 📚 KNOWLEDGE: List Slicing
# ============================================================================

"""
SLICING SYNTAX: list[start:end:step]

- start: index to start (inclusive), default 0
- end: index to stop (exclusive), default len(list)
- step: increment, default 1

EXAMPLES:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[2:5]      → [2, 3, 4]           # From index 2 to 5 (exclusive)
numbers[:5]       → [0, 1, 2, 3, 4]     # From start to 5
numbers[5:]       → [5, 6, 7, 8, 9]     # From 5 to end
numbers[:]        → [0, 1, ..., 9]      # Copy entire list
numbers[1:8:2]    → [1, 3, 5, 7]        # Every 2nd item from 1 to 8
numbers[::2]      → [0, 2, 4, 6, 8]     # Every 2nd item
numbers[::-1]     → [9, 8, 7, ..., 0]   # Reverse (step -1)
numbers[-3:]      → [7, 8, 9]           # Last 3 items
numbers[:-3]      → [0, 1, ..., 6]      # All except last 3

NEGATIVE INDICES:
numbers[-1]       → 9                    # Last item
numbers[-2]       → 8                    # Second to last
numbers[-3:-1]    → [7, 8]               # From -3 to -1 (exclusive)

COMPARISON WITH JAVASCRIPT:
Python              JavaScript
------              ----------
list[1:4]          list.slice(1, 4)
list[::2]          list.filter((_, i) => i % 2 === 0)
list[::-1]         list.reverse() (mutates!) or [...list].reverse()
"""

# ============================================================================
# PART 1: List Methods Practice
# ============================================================================


def list_operations_demo():
    """
    Demonstrate difference between append, extend, insert.
    Return a dict with results of each operation.

    Start with: [1, 2, 3]

    Return dict with keys:
    - "after_append": result after append([4, 5])
    - "after_extend": result after extend([4, 5]) on fresh list
    - "after_insert": result after insert(1, 99) on fresh list

    Example return:
    {
        "after_append": [1, 2, 3, [4, 5]],
        "after_extend": [1, 2, 3, 4, 5],
        "after_insert": [1, 99, 2, 3]
    }
    """
    operations = {}
    after_append = [1, 2, 3]
    after_extend = [1, 2, 3]
    after_insert = [1, 2, 3]
    after_append.append([4, 5])
    after_extend.extend([4, 5])
    after_insert.insert(1, 99)

    operations["after_append"] = after_append
    operations["after_extend"] = after_extend
    operations["after_insert"] = after_insert

    return operations


def remove_duplicates_keep_order(items):
    """
    Remove duplicates from list while maintaining original order.
    Don't use set() - it would lose order.

    Example:
        remove_duplicates_keep_order([1, 2, 2, 3, 1, 4]) → [1, 2, 3, 4]
        remove_duplicates_keep_order(["a", "b", "a", "c"]) → ["a", "b", "c"]

    Hint: Keep a list of seen items, check before appending
    """
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def rotate_list_left(items, n):
    """
    Rotate list to the left by n positions.
    Use slicing!

    Example:
        rotate_list_left([1, 2, 3, 4, 5], 2) → [3, 4, 5, 1, 2]
        rotate_list_left(['a', 'b', 'c'], 1) → ['b', 'c', 'a']

    Hint: items[n:] + items[:n]
    """
    return items[n:] + items[:n]


# ============================================================================
# PART 2: Slicing Mastery
# ============================================================================


def get_every_nth(items, n):
    """
    Return every nth item from list using slicing.

    Example:
        get_every_nth([1, 2, 3, 4, 5, 6, 7, 8], 2) → [1, 3, 5, 7]
        get_every_nth([1, 2, 3, 4, 5, 6, 7, 8], 3) → [1, 4, 7]

    Use slicing with step parameter!
    """
    return items[::n]


def reverse_words_in_sentence(sentence):
    """
    Reverse the order of words in a sentence.
    Use string split() and list slicing.

    Example:
        reverse_words_in_sentence("Hello World Python") → "Python World Hello"
        reverse_words_in_sentence("I love coding") → "coding love I"

    Hint: sentence.split() gives list of words, then slice [::-1], then " ".join()
    """
    return " ".join(sentence.split()[::-1])


def extract_middle_portion(items):
    """
    Extract the middle 50% of a list.
    If list has odd length, favor keeping more items.

    Example:
        extract_middle_portion([1, 2, 3, 4, 5, 6, 7, 8]) → [3, 4, 5, 6]
        extract_middle_portion([1, 2, 3, 4, 5]) → [2, 3, 4]

    Hint: Calculate start = len//4, end = len - len//4
    """
    items_len = len(items)
    start = items_len // 4
    end = items_len - items_len // 4

    return items[start:end]


def is_palindrome_list(items):
    """
    Check if list is a palindrome (same forwards and backwards).
    Use slicing!

    Example:
        is_palindrome_list([1, 2, 3, 2, 1]) → True
        is_palindrome_list([1, 2, 3, 4]) → False
        is_palindrome_list(['a', 'b', 'a']) → True

    Hint: Compare items with items[::-1]
    """
    return items == items[::-1]


# ============================================================================
# PART 3: Nested Lists (List of Lists)
# ============================================================================


def flatten_2d_list(matrix):
    """
    Flatten a 2D list (list of lists) into 1D list.

    Example:
        flatten_2d_list([[1, 2], [3, 4], [5, 6]]) → [1, 2, 3, 4, 5, 6]
        flatten_2d_list([[1], [2, 3], [4, 5, 6]]) → [1, 2, 3, 4, 5, 6]

    Hint: Use nested loop or list comprehension
    """
    flattened = [item for row in matrix for item in row]
    return flattened


def transpose_matrix(matrix):
    """
    Transpose a matrix (swap rows and columns).

    Example:
        transpose_matrix([[1, 2, 3], [4, 5, 6]]) → [[1, 4], [2, 5], [3, 6]]

        Visual:
        [1, 2, 3]    →    [1, 4]
        [4, 5, 6]         [2, 5]
                          [3, 6]

    Hint: result[j][i] = matrix[i][j]
    Or use: [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    """
    result = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[j][i] = matrix[i][j]
    return result


def find_max_in_2d(matrix):
    """
    Find maximum value in a 2D list.

    Example:
        find_max_in_2d([[1, 5, 3], [9, 2, 8], [4, 7, 6]]) → 9
        find_max_in_2d([[10], [20, 30], [5]]) → 30

    Hint: Flatten first, then max(), or nested loop
    """
    flatten = [item for row in matrix for item in row]
    max_num = max(flatten)
    return max_num


# ============================================================================
# 📚 KNOWLEDGE: List vs Reference vs Copy
# ============================================================================

"""
CRITICAL CONCEPT: Lists are MUTABLE and passed by REFERENCE

# Reference (same object):
a = [1, 2, 3]
b = a           # b points to SAME list
b.append(4)
print(a)        # [1, 2, 3, 4] ← a changed too!

# Shallow copy (new list, same items):
a = [1, 2, 3]
b = a.copy()    # or list(a) or a[:]
b.append(4)
print(a)        # [1, 2, 3] ← a unchanged

# Deep copy (for nested lists):
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)
print(a)        # [[1, 2], [3, 4]] ← a unchanged

COMPARISON WITH JAVASCRIPT:
Python              JavaScript
------              ----------
b = a               b = a (same reference)
b = a.copy()        b = [...a] or a.slice()
b = a[:]            b = [...a]
deepcopy(a)         structuredClone(a) or JSON.parse(JSON.stringify(a))
"""

# ============================================================================
# PART 4: Reference vs Copy Challenge
# ============================================================================


def demonstrate_reference_issue():
    """
    Show the problem with list references.

    Create a list [1, 2, 3]
    Assign it to another variable
    Modify the new variable (append 4)

    Return tuple: (original_list, new_list)

    Expected: Both should be [1, 2, 3, 4] (showing reference issue)
    """
    list_a = [1, 2, 3]
    list_b = list_a
    list_b.append(4)

    return (list_a, list_b)


def safe_modify_list(original, item_to_add):
    """
    Add item to list WITHOUT modifying original.
    Return the new list.

    Example:
        original = [1, 2, 3]
        result = safe_modify_list(original, 4)
        print(result)   # [1, 2, 3, 4]
        print(original) # [1, 2, 3] ← unchanged!

    Hint: Make a copy first!
    """
    list_b = original.copy()
    list_b.append(item_to_add)

    return list_b


def merge_without_duplicates(list1, list2):
    """
    Merge two lists, removing duplicates, maintaining order.
    Don't modify original lists.

    Example:
        merge_without_duplicates([1, 2, 3], [2, 3, 4, 5]) → [1, 2, 3, 4, 5]
        merge_without_duplicates(['a', 'b'], ['b', 'c']) → ['a', 'b', 'c']

    Hint: Copy first list, then iterate second and add if not present
    """
    copy_list1 = list1.copy()
    for item in list2:
        if item not in copy_list1:
            copy_list1.append(item)

    return copy_list1


# ============================================================================
# PART 5: Advanced List Manipulation
# ============================================================================


def chunk_list(items, chunk_size):
    """
    Split list into chunks of given size.

    Example:
        chunk_list([1, 2, 3, 4, 5, 6, 7], 3) → [[1, 2, 3], [4, 5, 6], [7]]
        chunk_list([1, 2, 3, 4], 2) → [[1, 2], [3, 4]]

    Hint: Use slicing in a loop: items[i:i+chunk_size]
    """
    new_list = []
    for i in range(0, len(items), chunk_size):
        chunk = items[i : i + chunk_size]
        new_list.append(chunk)
    return new_list


def interleave_lists(list1, list2):
    """
    Interleave two lists (alternate elements).

    Example:
        interleave_lists([1, 2, 3], ['a', 'b', 'c']) → [1, 'a', 2, 'b', 3, 'c']
        interleave_lists([1, 2], ['a', 'b', 'c']) → [1, 'a', 2, 'b', 'c']

    Hint: Use zip() or manual index tracking
    """
    interleaved = []
    max_len = max(len(list1), len(list2))
    for i in range(max_len):
        if i < len(list1):
            interleaved.append(list1[i])
        if i < len(list2):
            interleaved.append(list2[i])
    return interleaved


def move_zeros_to_end(items):
    """
    Move all zeros to the end, maintaining order of non-zeros.
    Modify in place (change the original list).

    Example:
        nums = [0, 1, 0, 3, 12]
        move_zeros_to_end(nums)
        print(nums)  # [1, 3, 12, 0, 0]

    Hint: Count zeros, remove them, extend with zeros at end
    """
    zero_count = 0
    for item in items[:]:
        if item == 0:
            zero_count += 1
            items.remove(item)

    items.extend([0] * zero_count)


# ============================================================================
# TESTS
# ============================================================================

# print("=== PART 1: List Methods ===")
# print(list_operations_demo())
# Expected: {'after_append': [1, 2, 3, [4, 5]], 'after_extend': [1, 2, 3, 4, 5], 'after_insert': [1, 99, 2, 3]}

# print(remove_duplicates_keep_order([1, 2, 2, 3, 1, 4]))
# print(remove_duplicates_keep_order(["a", "b", "a", "c"]))
# # Expected: [1, 2, 3, 4]

# print(rotate_list_left([1, 2, 3, 4, 5], 2))
# # Expected: [3, 4, 5, 1, 2]
# print()

# print("=== PART 2: Slicing ===")
# print(get_every_nth([1, 2, 3, 4, 5, 6, 7, 8], 2))
# # Expected: [1, 3, 5, 7]

# print(reverse_words_in_sentence("Hello World Python"))
# # Expected: "Python World Hello"

# print(extract_middle_portion([1, 2, 3, 4, 5, 6, 7, 8]))
# # Expected: [3, 4, 5, 6]

# print(is_palindrome_list([1, 2, 3, 2, 1]))
# # Expected: True
# print()

# print("=== PART 3: Nested Lists ===")
# print(flatten_2d_list([[1, 2], [3, 4], [5, 6]]))
# Expected: [1, 2, 3, 4, 5, 6]

# print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))
# Expected: [[1, 4], [2, 5], [3, 6]]

# print(find_max_in_2d([[1, 5, 3], [9, 2, 8], [4, 7, 6]]))
# # Expected: 9
# print()

# print("=== PART 4: Reference vs Copy ===")
# print(demonstrate_reference_issue())
# Expected: ([1, 2, 3, 4], [1, 2, 3, 4])

# original = [1, 2, 3]
# result = safe_modify_list(original, 4)
# print(f"Result: {result}, Original: {original}")
# Expected: Result: [1, 2, 3, 4], Original: [1, 2, 3]

# print(merge_without_duplicates([1, 2, 3], [2, 3, 4, 5]))
# # Expected: [1, 2, 3, 4, 5]
# print()

print("=== PART 5: Advanced ===")
# print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))
# # Expected: [[1, 2, 3], [4, 5, 6], [7]]

# print(interleave_lists([1, 2, 3], ["a", "b", "c"]))
# # Expected: [1, 'a', 2, 'b', 3, 'c']

nums = [0, 1, 0, 3, 12]
move_zeros_to_end(nums)
print(nums)
Expected: [1, 3, 12, 0, 0]
