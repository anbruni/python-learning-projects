"""
Exercise 1.19 - Generators & Iterators
=======================================

LEARNING GOALS:
- Understand yield vs return
- Create generator functions and generator expressions
- Know when to use generators (large datasets, memory efficiency)
- Interview question: list vs generator

STRUCTURE:
- Part 1: yield basics (3 functions)
- Part 2: Generator expressions (2 exercises)
- Part 3: Real-world use cases (2 functions)
"""

from typing import Generator, Iterator

# =============================================================================
# PART 1 - YIELD BASICS
# =============================================================================
"""
CONCEPTS:
- yield pauses the function and returns a value
- next time the generator is called, it resumes from where it left off
- generators are lazy: they produce values ONE AT A TIME
- a generator function returns a Generator object, not a list

KEY DIFFERENCE:
    def with_return():       def with_yield():
        return [1, 2, 3]         yield 1
                                 yield 2
                                 yield 3

    list() → builds ALL in memory    → produces one at a time
"""


def count_up(n: int) -> Generator[int, None, None]:
    """
    Generate numbers from 0 to n-1 using yield.

    Args:
        n: Upper limit (exclusive)

    Yields:
        int: Numbers from 0 to n-1

    Example:
        >>> list(count_up(5))
        [0, 1, 2, 3, 4]
        >>> for num in count_up(3):
        ...     print(num)
        0
        1
        2
    """
    for num in range(n):
        yield num


def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """
    Generate Fibonacci numbers up to limit.

    Args:
        limit: Maximum value to generate (inclusive)

    Yields:
        int: Fibonacci numbers

    Example:
        >>> list(fibonacci_generator(20))
        [0, 1, 1, 2, 3, 5, 8, 13]
        >>> list(fibonacci_generator(1))
        [0, 1, 1]
    """
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def infinite_counter(start: int = 0) -> Generator[int, None, None]:
    """
    Generate numbers infinitely starting from `start`.
    (Caller decides when to stop with break or islice)

    Args:
        start: Starting value

    Yields:
        int: Incrementing numbers forever

    Example:
        >>> gen = infinite_counter(10)
        >>> next(gen)
        10
        >>> next(gen)
        11
        >>> next(gen)
        12
    """
    num = start
    while True:
        yield num
        num += 1


# =============================================================================
# PART 2 - GENERATOR EXPRESSIONS
# =============================================================================
"""
CONCEPTS:
- Generator expression syntax: (expression for item in iterable)
- Like list comprehension but with () instead of []
- Does NOT compute all values upfront — lazy evaluation
- Memory efficient for large data

COMPARISON:
    list_comp = [x * 2 for x in range(1000)]     # 1000 items in memory NOW
    gen_expr  = (x * 2 for x in range(1000))     # produces one at a time
"""


def sum_large_squares(n: int) -> int:
    """
    Sum of squares from 1 to n using a generator expression (not a list).
    This is memory efficient even for huge n.

    Args:
        n: Upper limit

    Returns:
        int: Sum of 1^2 + 2^2 + ... + n^2

    Example:
        >>> sum_large_squares(5)
        55
        >>> sum_large_squares(3)
        14
    """
    return sum(x**2 for x in range(1, n + 1))


def first_n_even(n: int) -> list:
    """
    Return the first n even numbers using a generator expression + list().
    Even numbers start from 0: 0, 2, 4, 6, ...

    Args:
        n: How many even numbers to return

    Returns:
        list: First n even numbers

    Example:
        >>> first_n_even(5)
        [0, 2, 4, 6, 8]
        >>> first_n_even(3)
        [0, 2, 4]
    """
    return list((x * 2 for x in range(n)))


# =============================================================================
# PART 3 - REAL-WORLD USE CASES
# =============================================================================
"""
WHEN TO USE GENERATORS:
- Reading large files line by line (don't load entire file)
- Processing large datasets (streaming)
- Infinite sequences (pagination, event streams)
- Pipelines (chain generators together)
"""


def read_large_file(filepath: str) -> Generator[str, None, None]:
    """
    Read a large file line by line using a generator.
    This avoids loading the entire file into memory.

    Args:
        filepath: Path to the file

    Yields:
        str: Each line of the file (stripped)

    Example:
        >>> for line in read_large_file("movies.txt"):
        ...     print(line)   # processes one line at a time
    """
    with open(filepath) as f:  # with chiude il file automaticamente, anche in caso di errore
        for line in f:          # un file aperto è iterabile: ogni iterazione = una riga
            yield line.strip()  # strip() rimuove \n e spazi; yield pausa qui fino alla prossima riga richiesta


def batch_processor(items: list, batch_size: int) -> Generator[list, None, None]:
    """
    Yield items in batches of batch_size.
    Useful for bulk API calls or database inserts.

    Args:
        items: Full list of items
        batch_size: Size of each batch

    Yields:
        list: Batch of items

    Example:
        >>> data = [1, 2, 3, 4, 5, 6, 7]
        >>> for batch in batch_processor(data, 3):
        ...     print(batch)
        [1, 2, 3]
        [4, 5, 6]
        [7]
    """
    for i in range(0, len(items), batch_size):  # i salta di batch_size: 0, 3, 6, 9...
        yield items[i : i + batch_size]          # slice: taglia da i fino a i+batch_size (escluso)
                                                 # se i+batch_size supera la lunghezza, Python si ferma alla fine


# =============================================================================
# TESTS
# =============================================================================

if __name__ == "__main__":
    # print("=" * 60)
    # print("PART 1 - YIELD BASICS")
    # print("=" * 60)

    # print("\n1. count_up(5):")
    # print(list(count_up(5)))

    # print("\n2. fibonacci_generator(20):")
    # print(list(fibonacci_generator(20)))

    # print("\n3. infinite_counter — first 5 values:")
    # gen = infinite_counter(10)
    # print([next(gen) for _ in range(5)])

    # print("\n" + "=" * 60)
    # print("PART 2 - GENERATOR EXPRESSIONS")
    # print("=" * 60)

    # print("\n4. sum_large_squares(5):", sum_large_squares(5))
    # print("5. first_n_even(5):", first_n_even(5))

    print("\n" + "=" * 60)
    print("PART 3 - REAL-WORLD")
    print("=" * 60)

    print("\n6. batch_processor([1..7], batch_size=3):")
    for batch in batch_processor(list(range(1, 8)), 3):
        print(" ", batch)

    # print("\n✅ Exercise 1.19 - Generators complete!")
    # print("\nKEY TAKEAWAYS:")
    # print("- yield pauses a function and resumes from that point next time")
    # print("- Generators are LAZY — values produced one at a time")
    # print("- Use generators for large data, infinite sequences, file reading")
    # print("- Generator expression: (x for x in ...) — like list comp but lazy")
    # print("- Interview: list builds all in memory, generator streams values")
