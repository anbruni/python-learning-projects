# WEEK 1, DAY 6-8: Mutability & Memory
# Exercise 1.7 - Mutability Gotchas

# CONCEPTS:
# - Mutable (list, dict, set) vs Immutable (int, str, tuple)
# - Assignment vs copy (references)
# - Shallow copy vs deep copy
# - Function side effects
# - Default argument trap

# WHY THIS MATTERS:
# Understanding mutability is CRITICAL to avoid bugs!
# - References can cause unexpected behavior
# - Side effects can break your code
# - Default arguments with mutables = classic Python bug
# This is one of the most common sources of bugs for beginners.

# ============================================================================
# 📚 KNOWLEDGE: Mutability Basics
# ============================================================================

"""
WHAT IS MUTABILITY?

IMMUTABLE ❄️ = Cannot modify the object after creation
- int, float, str, tuple, bool, frozenset, None
- Every "change" creates a NEW object in memory

MUTABLE 🔥 = Can modify the object in place
- list, dict, set
- The object stays the same in memory, content changes

EXAMPLE - IMMUTABLE (str):

name = "Alice"
print(id(name))  # 140234567890

name = name.upper()
print(id(name))  # 140234567999 ← DIFFERENT! New object!

EXAMPLE - MUTABLE (list):

numbers = [1, 2, 3]
print(id(numbers))  # 140234580000

numbers.append(4)
print(id(numbers))  # 140234580000 ← SAME! Modified in place!

KEY INSIGHT:
With mutables, assignment creates REFERENCES, not copies!

list2 = list1  # ❌ NOT a copy! Same object!
list2 = list1.copy()  # ✅ Real copy!
"""

# ============================================================================
# 📚 KNOWLEDGE: The Reference Problem
# ============================================================================

"""
THE REFERENCE PROBLEM:

# With immutables (SAFE):
a = 10
b = a
a = 20
print(b)  # 10 ← unchanged ✅

# With mutables (DANGEROUS):
list1 = [1, 2, 3]
list2 = list1  # Reference to SAME object!
list1.append(4)
print(list2)  # [1, 2, 3, 4] ← changed! ⚠️

VISUALIZATION:
list1 → [1, 2, 3] ← address: 140234580000
list2 → [1, 2, 3] ← address: 140234580000 (SAME!)

After list1.append(4):
list1 → [1, 2, 3, 4] ← address: 140234580000
list2 → [1, 2, 3, 4] ← address: 140234580000 (still SAME!)

SOLUTION - Make a copy:
list2 = list1.copy()  # Different objects now!
"""

# ============================================================================
# 📚 KNOWLEDGE: Shallow vs Deep Copy
# ============================================================================

"""
SHALLOW COPY - Copies only first level:

list1 = [[1, 2], [3, 4]]
list2 = list1.copy()

list1[0].append(99)
print(list1)  # [[1, 2, 99], [3, 4]]
print(list2)  # [[1, 2, 99], [3, 4]] ← changed! ⚠️

Why? Shallow copy copies references to nested objects.

DEEP COPY - Copies everything:

import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)

list1[0].append(99)
print(list1)  # [[1, 2, 99], [3, 4]]
print(list2)  # [[1, 2], [3, 4]] ← unchanged! ✅
"""

# ============================================================================
# PART 1: Understanding Mutability
# ============================================================================


def demonstrate_immutable_behavior():
    """
    Demonstrate that strings are immutable.
    Create a string "hello", change it to uppercase,
    return a tuple (original_id, new_id, are_same).

    Returns:
        tuple: (id before, id after, are they same)

    Example output:
        (140234567890, 140234567999, False)

    Hint: Use id() to get memory address
    """
    string1 = "hello"
    original_id = id(string1)
    string2 = string1.upper()
    new_id = id(string2)
    are_same = original_id == new_id
    return (original_id, new_id, are_same)


def demonstrate_mutable_behavior():
    """
    Demonstrate that lists are mutable.
    Create a list [1, 2, 3], append 4,
    return a tuple (original_id, new_id, are_same).

    Returns:
        tuple: (id before, id after, are they same)

    Example output:
        (140234580000, 140234580000, True)

    Hint: Use id() before and after append
    """
    new_list = [1, 2, 3]
    original_id = id(new_list)
    new_list.append(4)
    new_id = id(new_list)
    are_same = original_id == new_id
    return (original_id, new_id, are_same)


def check_mutability(obj):
    """
    Check if an object's type is mutable or immutable.

    Args:
        obj: Any Python object

    Returns:
        str: "mutable" or "immutable"

    Example:
        check_mutability([1, 2, 3]) → "mutable"
        check_mutability("hello") → "immutable"
        check_mutability((1, 2)) → "immutable"
        check_mutability({1, 2}) → "mutable"

    Hint: Check type with isinstance()
    """
    # Mutable types: list, dict, set
    if isinstance(obj, (list, dict, set)):
        return "mutable"
    # Immutable types: int, float, str, tuple, bool, frozenset
    elif isinstance(obj, (int, float, str, tuple, bool, frozenset, type(None))):
        return "immutable"
    else:
        return "immutable"  # Default for other types


def modify_immutable_attempt(text):
    """
    Try to "modify" an immutable string by making it uppercase.
    Return both original and modified, along with whether they're same object.

    Args:
        text (str): Original text

    Returns:
        tuple: (original, modified, are_same_object)

    Example:
        modify_immutable_attempt("hello") → ("hello", "HELLO", False)

    Hint: Use id() to check if same object
    """
    original_str = text
    original_str_id = id(original_str)
    original_upper = original_str.upper()
    original_upper_id = id(original_upper)
    are_same = original_str_id == original_upper_id
    return (original_str_id, original_upper_id, are_same)


# ============================================================================
# PART 2: Assignment vs Copy
# ============================================================================


def test_reference_vs_copy():
    """
    Create a list [1, 2, 3].
    Create reference (assignment) and copy.
    Modify original list by appending 4.
    Return (original, reference, copy).

    Returns:
        tuple: (original list, referenced list, copied list)

    Example output:
        ([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3])
        Notice: reference changed, copy didn't!

    Hint: reference = original, copy = original.copy()
    """
    original = [1, 2, 3]
    reference = original
    copy = original.copy()
    original.append(4)

    return (original, reference, copy)


def safe_list_append(original_list, item):
    """
    Append item to a list WITHOUT modifying the original.
    Return the new list.

    Args:
        original_list (list): Original list
        item: Item to append

    Returns:
        list: New list with item appended

    Example:
        original = [1, 2, 3]
        result = safe_list_append(original, 4)
        print(result)    # [1, 2, 3, 4]
        print(original)  # [1, 2, 3] ← unchanged!

    Hint: Make a copy first!
    """
    copy = original_list.copy()
    copy.append(item)
    return copy


def test_shallow_copy_problem():
    """
    Demonstrate the shallow copy problem with nested lists.

    Create nested list [[1, 2], [3, 4]].
    Make a shallow copy.
    Modify the first nested list by appending 99.
    Return (original, shallow_copy).

    Returns:
        tuple: Both lists (will be the same due to shallow copy!)

    Example output:
        ([[1, 2, 99], [3, 4]], [[1, 2, 99], [3, 4]])

    Hint: Use .copy() for shallow copy
    """
    orig_list = [[1, 2], [3, 4]]
    new_list = orig_list.copy()
    orig_list[0].append(99)
    return (orig_list, new_list)


import copy


def safe_nested_list_copy(nested_list):
    """
    Make a TRUE deep copy of a nested list.

    Args:
        nested_list (list): Nested list

    Returns:
        list: Deep copy

    Example:
        original = [[1, 2], [3, 4]]
        deep = safe_nested_list_copy(original)
        original[0].append(99)
        print(original)  # [[1, 2, 99], [3, 4]]
        print(deep)      # [[1, 2], [3, 4]] ← unchanged!

    Hint: import copy, use copy.deepcopy()
    """
    return copy.deepcopy(nested_list)


# ============================================================================
# PART 3: Function Side Effects
# ============================================================================


def bad_append(my_list, item):
    """
    BAD EXAMPLE: Function that modifies the original list (side effect).

    Args:
        my_list (list): List to modify
        item: Item to append

    Returns:
        list: The modified list

    Example:
        original = [1, 2, 3]
        result = bad_append(original, 4)
        print(original)  # [1, 2, 3, 4] ← CHANGED! Side effect!

    Note: This is intentionally bad to demonstrate side effects.
    """
    my_list.append(item)
    return my_list


def good_append(my_list, item):
    """
    GOOD EXAMPLE: Function without side effects (pure function).
    Does NOT modify the original list.

    Args:
        my_list (list): Original list
        item: Item to append

    Returns:
        list: New list with item appended

    Example:
        original = [1, 2, 3]
        result = good_append(original, 4)
        print(result)    # [1, 2, 3, 4]
        print(original)  # [1, 2, 3] ← UNCHANGED! No side effect!

    Hint: Make a copy first!
    """
    result = my_list.copy()
    result.append(item)
    return result


def sort_without_side_effect(numbers):
    """
    Sort a list WITHOUT modifying the original.

    Args:
        numbers (list): List of numbers

    Returns:
        list: Sorted list

    Example:
        original = [3, 1, 4, 1, 5]
        sorted_list = sort_without_side_effect(original)
        print(sorted_list)  # [1, 1, 3, 4, 5]
        print(original)     # [3, 1, 4, 1, 5] ← unchanged!

    Hint: Use sorted() NOT .sort()
    """
    return sorted(numbers)


def reverse_without_side_effect(items):
    """
    Reverse a list WITHOUT modifying the original.

    Args:
        items (list): List to reverse

    Returns:
        list: Reversed list

    Example:
        original = [1, 2, 3, 4]
        reversed_list = reverse_without_side_effect(original)
        print(reversed_list)  # [4, 3, 2, 1]
        print(original)       # [1, 2, 3, 4] ← unchanged!

    Hint: Use slicing [::-1] or reversed()
    """
    return items[::-1]


# ============================================================================
# PART 4: Default Argument Trap (THE CLASSIC BUG!)
# ============================================================================


def buggy_function(item, my_list=[]):
    """
    BUGGY! Demonstrates the default argument trap.
    DO NOT FIX THIS - it's intentionally buggy for demonstration.

    Args:
        item: Item to add
        my_list (list): List to add to (DEFAULT [])

    Returns:
        list: The list after adding item

    Example (unexpected behavior!):
        print(buggy_function("a"))  # ["a"]
        print(buggy_function("b"))  # ["a", "b"] ← WTF?!
        print(buggy_function("c"))  # ["a", "b", "c"] ← Growing!

    Why? The [] is created ONCE when function is defined!
    All calls share the SAME list!
    """
    my_list.append(item)
    return my_list


def fixed_function(item, my_list=None):
    """
    FIXED! Correct way to handle default mutable arguments.

    Args:
        item: Item to add
        my_list (list): List to add to (DEFAULT None)

    Returns:
        list: New list with item added

    Example (correct behavior):
        print(fixed_function("a"))  # ["a"]
        print(fixed_function("b"))  # ["b"] ← Correct!
        print(fixed_function("c"))  # ["c"] ← Each call gets new list!

    Hint: Use None as default, create new list inside function
    """
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list


def safe_default_dict(key, value, data=None):
    """
    Safely add key-value to dict with default argument.

    Args:
        key: Dictionary key
        value: Dictionary value
        data (dict): Dictionary to modify (DEFAULT None)

    Returns:
        dict: Dictionary with key-value added

    Example:
        print(safe_default_dict("a", 1))  # {"a": 1}
        print(safe_default_dict("b", 2))  # {"b": 2} ← Separate!

    Hint: Use None as default, create new dict if None
    """
    if data is None:
        data = {}
    data[key] = value
    return data


def append_with_default(item, container=None):
    """
    Append item to container (list) with safe default.

    Args:
        item: Item to append
        container (list): Container list (DEFAULT None)

    Returns:
        list: List with item appended

    Example:
        print(append_with_default(1))     # [1]
        print(append_with_default(2))     # [2]
        print(append_with_default(3, [0])) # [0, 3]

    Hint: Check if container is None, create new list if so
    """
    if container is None:
        container = []
    container.append(item)
    return container


# ============================================================================
# PART 5: Practical Debugging Scenarios
# ============================================================================


def debug_unexpected_list():
    """
    Debug scenario: Create two "separate" lists that are actually the same.

    Create list1 = [1, 2, 3].
    Create list2 = list1.
    Append 4 to list1.
    Return (list1, list2, are_same).

    Returns:
        tuple: (list1, list2, are they same object)

    Expected output:
        ([1, 2, 3, 4], [1, 2, 3, 4], True)

    This demonstrates the reference problem!
    """
    # Your code here
    pass


def fix_unexpected_list():
    """
    Fix the previous scenario by making a real copy.

    Create list1 = [1, 2, 3].
    Create list2 = COPY of list1.
    Append 4 to list1.
    Return (list1, list2, are_same).

    Returns:
        tuple: (list1, list2, are they same object)

    Expected output:
        ([1, 2, 3, 4], [1, 2, 3], False)

    Hint: Use .copy()
    """
    # Your code here
    pass


def track_function_calls():
    """
    Demonstrate buggy_function behavior by calling it 3 times.

    Call buggy_function() three times with "a", "b", "c".
    Return list of all three results.

    Returns:
        list: [result1, result2, result3]

    Expected output:
        [["a"], ["a", "b"], ["a", "b", "c"]]

    This shows how the default list accumulates!
    """
    # Your code here
    pass


def compare_behaviors():
    """
    Compare buggy_function vs fixed_function.

    Call buggy_function("x") twice.
    Call fixed_function("x") twice.
    Return (buggy_results, fixed_results).

    Returns:
        tuple: ([buggy1, buggy2], [fixed1, fixed2])

    Expected:
        ([["x"], ["x", "x"]], [["x"], ["x"]])
        Notice: buggy accumulates, fixed doesn't!
    """
    # Your code here
    pass


# ============================================================================
# TESTS
# ============================================================================

# print("=== PART 1: Understanding Mutability ===")
# immut = demonstrate_immutable_behavior()
# print(f"String IDs: before={immut[0]}, after={immut[1]}, same={immut[2]}")
# # Expected: same=False

# mut = demonstrate_mutable_behavior()
# print(f"List IDs: before={mut[0]}, after={mut[1]}, same={mut[2]}")
# # Expected: same=True

# print(check_mutability([1, 2, 3]))
# # Expected: "mutable"

# print(check_mutability("hello"))
# # Expected: "immutable"

# print(modify_immutable_attempt("test"))
# # Expected: ("test", "TEST", False)
# print()

# print("=== PART 2: Assignment vs Copy ===")
# # original, ref, copy = test_reference_vs_copy()
# # print(f"Original: {original}, Reference: {ref}, Copy: {copy}")
# # Expected: Original and Reference same, Copy different

# # original = [1, 2, 3]
# # result = safe_list_append(original, 4)
# # print(f"Original: {original}, Result: {result}")
# # Expected: Original unchanged [1, 2, 3], Result [1, 2, 3, 4]

# orig_nested, shallow = test_shallow_copy_problem()
# print(f"Original: {orig_nested}, Shallow: {shallow}")
# # Expected: Both [[1, 2, 99], [3, 4]]
# print()

# print("=== PART 3: Function Side Effects ===")
# # test_list = [1, 2, 3]
# # bad_result = bad_append(test_list, 4)
# # print(f"After bad_append - Original: {test_list}, Result: {bad_result}")
# # Expected: Both [1, 2, 3, 4] (side effect!)

# # test_list2 = [1, 2, 3]
# # good_result = good_append(test_list2, 4)
# # print(f"After good_append - Original: {test_list2}, Result: {good_result}")
# # # Expected: Original [1, 2, 3], Result [1, 2, 3, 4]

# # original_nums = [3, 1, 4, 1, 5]
# # sorted_nums = sort_without_side_effect(original_nums)
# # print(f"Original: {original_nums}, Sorted: {sorted_nums}")
# # Expected: Original unchanged

# reversed_list = reverse_without_side_effect([1, 2, 3, 4])
# print(f"Reversed: {reversed_list}")
# # Expected: [4, 3, 2, 1]
# print()

print("=== PART 4: Default Argument Trap ===")
print("Buggy function (demonstrating the problem):")
print(buggy_function("a"))
# Expected: ["a"]
print(buggy_function("b"))
# Expected: ["a", "b"] ← Accumulates!
print(buggy_function("c"))
# Expected: ["a", "b", "c"] ← Still accumulating!

print("\nFixed function (correct behavior):")
print(fixed_function("a"))
# Expected: ["a"]
print(fixed_function("b"))
# Expected: ["b"] ← Fresh list!
print(fixed_function("c"))
# Expected: ["c"] ← Fresh list!
print()

# print("=== PART 5: Practical Debugging ===")
# list1, list2, same = debug_unexpected_list()
# print(f"Debug: list1={list1}, list2={list2}, same={same}")
# # Expected: Both [1, 2, 3, 4], same=True

# list1, list2, same = fix_unexpected_list()
# print(f"Fixed: list1={list1}, list2={list2}, same={same}")
# # Expected: list1=[1, 2, 3, 4], list2=[1, 2, 3], same=False

# print(track_function_calls())
# # Expected: [["a"], ["a", "b"], ["a", "b", "c"]]

# buggy, fixed = compare_behaviors()
# print(f"Buggy: {buggy}, Fixed: {fixed}")
# # Expected: Buggy accumulates, Fixed doesn't
