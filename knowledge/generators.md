# Generators & Iterators in Python

> Lazy evaluation for memory-efficient data processing

## Table of Contents
1. [yield vs return](#yield-vs-return)
2. [Generator Functions](#generator-functions)
3. [Generator Expressions](#generator-expressions)
4. [When to Use Generators](#when-to-use-generators)
5. [Interview: list vs generator](#interview-list-vs-generator)
6. [Real-World Patterns](#real-world-patterns)

---

## yield vs return

```python
# return → builds and returns the WHOLE list at once
def get_numbers_list(n):
    return [i for i in range(n)]  # all n items in memory

# yield → produces ONE value at a time, pauses, resumes on next()
def get_numbers_gen(n):
    for i in range(n):
        yield i  # pauses here, resumes next time
```

| | `return` | `yield` |
|---|---|---|
| Returns | The full value immediately | A generator object |
| Memory | All items at once | One item at a time |
| Can be resumed | No | Yes |
| Infinite sequences | No | Yes |

---

## Generator Functions

```python
from typing import Generator

def fibonacci(limit: int) -> Generator[int, None, None]:
    a, b = 0, 1
    while a <= limit:
        yield a          # pause, return a
        a, b = b, a + b  # resume here on next()

# Usage
for n in fibonacci(20):
    print(n)  # 0 1 1 2 3 5 8 13

# Or collect into a list
nums = list(fibonacci(20))  # [0, 1, 1, 2, 3, 5, 8, 13]
```

### next() — manual stepping

```python
gen = fibonacci(10)
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 1
# StopIteration raised when exhausted
```

### Infinite generators

```python
def infinite_counter(start=0):
    n = start
    while True:
        yield n
        n += 1

counter = infinite_counter(5)
print(next(counter))  # 5
print(next(counter))  # 6
# use break or itertools.islice to stop
```

---

## Generator Expressions

Syntax: `(expression for item in iterable [if condition])`

```python
# List comprehension → builds entire list in memory
squares_list = [x ** 2 for x in range(1000)]   # 1000 items NOW

# Generator expression → lazy, one item at a time
squares_gen  = (x ** 2 for x in range(1000))   # nothing computed yet

# Both work with sum(), max(), min(), list()
total = sum(x ** 2 for x in range(1000))        # no list created at all!
```

### With conditions

```python
even_squares = (x ** 2 for x in range(20) if x % 2 == 0)
print(list(even_squares))  # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
```

---

## When to Use Generators

| Use case | Why generator wins |
|---|---|
| Large files | Read line by line, don't load all into RAM |
| Large datasets | Stream instead of loading 1M rows at once |
| Infinite sequences | Can't represent infinity as a list |
| Data pipelines | Chain generators — each step processes one item |
| Batch processing | Yield fixed-size chunks from a large list |

---

## Interview: list vs generator

**Question:** "What is the difference between a list and a generator in Python?"

```python
# LIST
nums_list = [x for x in range(1_000_000)]
# → all 1M integers allocated in memory immediately
# → you can index: nums_list[42]
# → you can iterate multiple times

# GENERATOR
nums_gen = (x for x in range(1_000_000))
# → NO memory allocated upfront
# → cannot index: nums_gen[42] → TypeError
# → single-use: once exhausted, it's done
```

**Answer template:**
> A list stores all values in memory at once. A generator is lazy — it computes
> values on demand one at a time, using almost no memory. Use generators when
> the dataset is large, the sequence is infinite, or you only need to iterate once.

---

## Real-World Patterns

### Reading large files

```python
def read_large_file(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()  # one line at a time, file stays open until done

# vs loading all lines → for tiny files fine, for 10GB logs → crash
lines = open("huge.log").readlines()  # loads entire file!
```

### Batch processor

```python
def batch(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]

for chunk in batch(range(100), 10):
    # process 10 items at a time (e.g., bulk DB insert, API call)
    insert_to_db(chunk)
```

### Pipeline (chaining generators)

```python
def read_lines(filepath):
    with open(filepath) as f:
        yield from f  # delegates to another iterable

def filter_non_empty(lines):
    return (line.strip() for line in lines if line.strip())

def parse_csv(lines):
    return (line.split(",") for line in lines)

# Pipeline: nothing is computed until you iterate
pipeline = parse_csv(filter_non_empty(read_lines("data.csv")))
for row in pipeline:
    process(row)
```

---

## Type Hints

```python
from typing import Generator, Iterator

# Generator[YieldType, SendType, ReturnType]
# SendType and ReturnType are usually None for simple generators
def count_up(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i

# Iterator is simpler when you only yield
def count_up(n: int) -> Iterator[int]:
    for i in range(n):
        yield i
```
