# WEEK 1, DAY 1-2: Data Types & Control Flow
# Exercise 1.2 - Control Flow Challenges

# CONCEPTS:
# - if/elif/else chains
# - for loops with break/continue
# - while loops
# - Ternary operators (inline if/else)
# - Nested loops
# - Loop control (break, continue, pass)

# WHY THIS MATTERS:
# Control flow is the foundation of all programming. You need to master
# loops and conditionals to build any real application.

# ============================================================================
# PART 1: FizzBuzz Variations
# ============================================================================


def fizzbuzz_classic(n):
    """
    Classic FizzBuzz from 1 to n.

    Rules:
    - If number divisible by 3: "Fizz"
    - If number divisible by 5: "Buzz"
    - If divisible by both 3 and 5: "FizzBuzz"
    - Otherwise: the number itself

    Return a list of results.

    Example:
        fizzbuzz_classic(15) → [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8,
                                 "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
    """
    result = [
        (
            num
            if num % 3 != 0 and num % 5 != 0
            else (
                "FizzBuzz"
                if (num % 3 == 0 and num % 5 == 0)
                else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else num
            )
        )
        for num in range(1, n + 1)
    ]
    return result


def fizzbuzz_custom(n, divisor1, word1, divisor2, word2):
    """
    Generalized FizzBuzz with custom divisors and words.

    Example:
        fizzbuzz_custom(10, 2, "Even", 3, "Three") →
        [1, "Even", "Three", "Even", 5, "EvenThree", 7, "Even", "Three", "Even"]

    Note: When divisible by both, concatenate words (word1 + word2)
    """
    return [
        (
            word1 + word2
            if num % divisor1 == 0 and num % divisor2 == 0
            else word1 if num % divisor1 == 0 else word2 if num % divisor2 == 0 else num
        )
        for num in range(1, n + 1)
    ]


# ============================================================================
# PART 2: Loop Control (break/continue)
# ============================================================================


def find_first_negative(numbers):
    """
    Find the first negative number in a list.
    Use a loop with 'break' to stop as soon as you find it.
    Return None if no negative found.

    Example:
        find_first_negative([1, 5, -3, 8, -1]) → -3
        find_first_negative([1, 2, 3]) → None
    """
    for num in numbers:
        if num < 0:
            break
    return None if num >= 0 else num


def sum_until_negative(numbers):
    """
    Sum numbers in list until you hit a negative number.
    Stop immediately when you see a negative (don't include it).

    Example:
        sum_until_negative([1, 2, 3, -5, 10]) → 6
        sum_until_negative([5, 5, 5]) → 15
        sum_until_negative([-1, 2, 3]) → 0
    """
    sum = 0
    for num in numbers:
        if num < 0:
            break
        sum += num
    return 0 if sum <= 0 else sum


def skip_multiples_of_three(n):
    """
    Return list of numbers from 1 to n, but skip multiples of 3.
    Use 'continue' in your loop.

    Example:
        skip_multiples_of_three(10) → [1, 2, 4, 5, 7, 8, 10]
    """
    result = []
    for num in range(1, n + 1):
        if num % 3 == 0:
            pass
        else:
            result.append(num)
    return result


# ============================================================================
# PART 3: Nested Loops
# ============================================================================


def multiplication_table(n):
    """
    Generate a multiplication table from 1 to n.
    Return as list of lists (matrix).

    Example:
        multiplication_table(3) → [
            [1, 2, 3],
            [2, 4, 6],
            [3, 6, 9]
        ]
    """
    outer = []
    for i in range(1, n + 1):
        inner = []
        for j in range(1, n + 1):
            inner.append(j * i)
        outer.append(inner)
    return outer


def find_pairs_sum_to_target(numbers, target):
    """
    Find all pairs of numbers that add up to target.
    Return list of tuples. Avoid duplicate pairs.

    Example:
        find_pairs_sum_to_target([1, 2, 3, 4, 5], 6) → [(1, 5), (2, 4)]
        find_pairs_sum_to_target([1, 1, 2, 3], 4) → [(1, 3)]

    Rules:
    - Use nested loops
    - Don't include same element twice: (2, 2) not allowed unless two 2s exist
    - Avoid duplicates: if you have (1, 5), don't also add (5, 1)

    Hint: Keep track of indices to avoid using same element twice
    """
    seen = set()
    result = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pair = (numbers[i], numbers[j])
                if pair not in seen:
                    seen.add(pair)
                    result.append(pair)

    return result


# ============================================================================
# PART 4: Ternary Operators (Inline if/else)
# ============================================================================


def classify_age(age):
    """
    Classify age using ternary operators.

    Rules:
    - age < 13: "child"
    - age < 18: "teen"
    - age < 65: "adult"
    - age >= 65: "senior"

    Use nested ternary: value1 if condition1 else value2 if condition2 else value3

    Example:
        classify_age(10) → "child"
        classify_age(16) → "teen"
        classify_age(30) → "adult"
        classify_age(70) → "senior"
    """
    result = (
        "child"
        if age < 13
        else "teen" if age < 18 else "adult" if age < 65 else "senior"
    )
    return result


def grade_to_letter(grade):
    """
    Convert numeric grade to letter using ternary operators.

    Rules:
    - >= 90: "A"
    - >= 80: "B"
    - >= 70: "C"
    - >= 60: "D"
    - < 60: "F"

    Use nested ternary operators (one line!)
    """
    return (
        "A"
        if grade >= 90
        else "B" if grade >= 80 else "C" if grade >= 70 else "D" if grade >= 60 else "F"
    )


# ============================================================================
# PART 5: While Loops
# ============================================================================


def countdown(n):
    """
    Return list counting down from n to 1 using while loop.

    Example:
        countdown(5) → [5, 4, 3, 2, 1]
    """
    counter = []
    while n > 0:
        counter.append(n)
        n -= 1

    return counter


def find_power_of_two_greater_than(n):
    """
    Find the smallest power of 2 that is greater than n.
    Use a while loop.

    Example:
        find_power_of_two_greater_than(10) → 16 (because 2^4 = 16 > 10)
        find_power_of_two_greater_than(33) → 64 (because 2^6 = 64 > 33)
    """
    power = 1  # 2^0
    while power <= n:
        power *= 2  # 2, 4, 8, 16, 32...
    return power


# ============================================================================
# TESTS
# ============================================================================

# print("=== PART 1: FizzBuzz ===")
# print(fizzbuzz_classic(15))
# Expected: [
#     1,
#     2,
#     "Fizz",
#     4,
#     "Buzz",
#     "Fizz",
#     7,
#     8,
#     "Fizz",
#     "Buzz",
#     11,
#     "Fizz",
#     13,
#     14,
#     "FizzBuzz",
# ]

# print(fizzbuzz_custom(10, 2, "Even", 3, "Three"))
# # Expected: [1, "Even", "Three", "Even", 5, "EvenThree", 7, "Even", "Three", "Even"]
# print()

# print("=== PART 2: Loop Control ===")
# print(find_first_negative([1, 5, -3, 8, -1]))  # Expected: -3
# print(find_first_negative([1, 2, 3, 5]))  # Expected: None

# print(sum_until_negative([1, 2, 3, -5, 10]))  # Expected: 6
# print(sum_until_negative([5, 5, 5]))  # Expected: 15
# print(sum_until_negative([-1, 2, 3]))  # Expected: 0

# print(skip_multiples_of_three(10))  # Expected: [1, 2, 4, 5, 7, 8, 10]
# print()

# print("=== PART 3: Nested Loops ===")
# print(multiplication_table(3))
# # Expected: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# print(find_pairs_sum_to_target([1, 2, 3, 4, 5], 6))
# # # Expected: [(1, 5), (2, 4)]
# print(find_pairs_sum_to_target([1, 1, 2, 3], 4))
# print()

# print("=== PART 4: Ternary Operators ===")
# print(classify_age(10))  # Expected: "child"
# print(classify_age(16))  # Expected: "teen"
# print(classify_age(30))  # Expected: "adult"
# print(classify_age(70))  # Expected: "senior"

# print(grade_to_letter(95))  # Expected: "A"
# print(grade_to_letter(82))  # Expected: "B"
# print(grade_to_letter(55))  # Expected: "F"
# print()

print("=== PART 5: While Loops ===")
# print(countdown(15))  # Expected: [5, 4, 3, 2, 1]
print(find_power_of_two_greater_than(10))  # Expected: 16
print(find_power_of_two_greater_than(33))  # Expected: 64
