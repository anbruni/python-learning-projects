# WEEK 1, DAY 1-2: Data Types & Control Flow
# Exercise 1.1 - Type Conversions & None

# CONCEPTS:
# - Basic types: int, float, str, bool, None
# - Type conversion (casting): int(), float(), str(), bool()
# - Type checking: type(), isinstance()
# - None handling (common gotcha)

# WHY THIS MATTERS:
# In real projects, you'll receive data in wrong formats (strings from APIs,
# user input, CSV files). You need to convert safely without crashing.

# ============================================================================
# PART 1: Safe Type Conversions
# ============================================================================


def safe_int(value):
    """
    Convert value to int. If impossible, return None.

    Examples:
        safe_int("42") → 42
        safe_int("3.14") → None (not a valid int)
        safe_int("hello") → None
        safe_int(None) → None
        safe_int(42) → 42
    """
    if isinstance(value, bool):
        return None  # Skip booleans

    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def safe_float(value):
    """
    Convert value to float. If impossible, return None.

    Examples:
        safe_float("3.14") → 3.14
        safe_float("42") → 42.0
        safe_float("hello") → None
        safe_float(None) → None
    """
    if isinstance(value, bool):
        return None  # Skip booleans

    try:
        return float(value)
    except (ValueError, TypeError):
        return None


# ============================================================================
# PART 2: Type Checking & None Handling
# ============================================================================


def describe_type(value):
    """
    Return a string describing the value's type.

    Rules:
    - If None: return "none"
    - If int: return "integer"
    - If float: return "decimal"
    - If str: return "text"
    - If bool: return "boolean" (IMPORTANT: check bool BEFORE int!)
    - Otherwise: return "unknown"

    Examples:
        describe_type(42) → "integer"
        describe_type(3.14) → "decimal"
        describe_type("hello") → "text"
        describe_type(True) → "boolean"
        describe_type(None) → "none"

    GOTCHA: In Python, bool is a subclass of int!
            isinstance(True, int) → True
            So you MUST check isinstance(value, bool) before isinstance(value, int)
    """
    if isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value, float):
        return "decimal"
    elif isinstance(value, str):
        return "text"
    elif value is None:
        return "none"
    else:
        return "unknown"


# ============================================================================
# PART 3: Clean Mixed Data
# ============================================================================


def clean_numbers(data):
    result = []

    for value in data:
        # Skip booleans
        if isinstance(value, bool):
            continue

        # If already a number, keep it
        if isinstance(value, (int, float)):
            result.append(value)
            continue

        # If string, try converting
        if isinstance(value, str):
            num = safe_int(value)
            if num is not None:
                result.append(num)
                continue

            num = safe_float(value)
            if num is not None:
                result.append(num)
                continue

        # Everything else (None, lists, etc) is skipped

    return result


# ============================================================================
# PART 4: None vs Empty vs Zero (important distinction!)
# ============================================================================


def categorize_value(value):
    """
    Categorize a value based on what it is.

    Return one of:
    - "none" if value is None
    - "empty_string" if value is "" (empty string)
    - "zero" if value is 0 (int) or 0.0 (float)
    - "false" if value is False (bool)
    - "truthy" for anything else

    Examples:
        categorize_value(None) → "none"
        categorize_value("") → "empty_string"
        categorize_value(0) → "zero"
        categorize_value(0.0) → "zero"
        categorize_value(False) → "false"
        categorize_value("hello") → "truthy"
        categorize_value(42) → "truthy"
        categorize_value([]) → "truthy" (yes, empty list is not None!)

    WHY: In real code, None, 0, "", and False are all "falsy" but mean
    different things. None = "no value", 0 = "value is zero", etc.
    """
    if value is None:
        return "none"
    elif value is False:
        return "false"
    elif value is True:  # Explicit
        return "truthy"
    elif isinstance(value, str):
        if len(value) > 0:
            return "truthy"
        else:
            return "empty_string"
    elif isinstance(value, (int, float)):
        if value == 0:
            return "zero"
        else:
            return "truthy"
    elif isinstance(value, list):
        return "truthy"
    else:
        return "truthy"


# ============================================================================
# TESTS
# ============================================================================

# Test Part 1: safe_int
# print("=== Testing safe_int ===")
# print(safe_int("42"))        # Expected: 42
# print(safe_int("3.14"))      # Expected: None
# print(safe_int("hello"))     # Expected: None
# print(safe_int(None))        # Expected: None
# print(safe_int(42))          # Expected: 42
# print()

# # Test Part 1: safe_float
# print("=== Testing safe_float ===")
# print(safe_float("3.14"))    # Expected: 3.14
# print(safe_float("42"))      # Expected: 42.0
# print(safe_float("hello"))   # Expected: None
# print(safe_float(None))      # Expected: None
# print()

# # Test Part 2: describe_type
# print("=== Testing describe_type ===")
# print(describe_type(42))     # Expected: "integer"
# print(describe_type(3.14))   # Expected: "decimal"
# print(describe_type("hi"))   # Expected: "text"
# print(describe_type(True))   # Expected: "boolean" (NOT "integer"!)
# print(describe_type(None))   # Expected: "none"
# print()

# Test Part 3: clean_numbers
# print("=== Testing clean_numbers ===")
# data = [42, "3.14", "hello", None, True, "99", 2.5, ""]
# print(clean_numbers(data))   # Expected: [42, 3.14, 99, 2.5]
# print()

# Test Part 4: categorize_value
# print("=== Testing categorize_value ===")
print(categorize_value(None))  # Expected: "none"
print(categorize_value(""))  # Expected: "empty_string"
print(categorize_value(0))  # Expected: "zero"
print(categorize_value(0.0))  # Expected: "zero"
print(categorize_value(False))  # Expected: "false"
print(categorize_value("hello"))  # Expected: "truthy"
print(categorize_value(42))  # Expected: "truthy"
print(categorize_value([]))  # Expected: "truthy"
