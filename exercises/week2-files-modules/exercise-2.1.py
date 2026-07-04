"""
Exercise 2.1 - Reading Files
==============================

LEARNING GOALS:
- Open files safely with `with open(...)` (context manager)
- Read entire file with .read()
- Read line by line with .readline() and .readlines()
- Handle encoding correctly with encoding="utf-8"

DATA FILE: data/movies.txt
FORMAT:    title,year,director,rating  (one movie per line)

STRUCTURE:
- Part 1: Concept — why `with open`
- Part 2: read()        → whole file as one string
- Part 3: readlines()   → list of lines
- Part 4: readline()    → one line at a time
- Part 5: Cinema task   → parse movies and find the best rated
"""

# Path to the data file (relative to this script's location)
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "movies.txt")


# =============================================================================
# PART 1 - CONCEPT: with open(...)
# =============================================================================
"""
In Python, files are opened with open() and MUST be closed after use.
The `with` statement (context manager) does this automatically — even if an
error occurs inside the block.

PYTHON:
    with open("file.txt", "r", encoding="utf-8") as f:
        content = f.read()
    # file is automatically closed here ✅

WITHOUT with (don't do this):
    f = open("file.txt", "r")
    content = f.read()
    f.close()   ← easy to forget, leaks file handle on errors

JS COMPARISON:
    // Node.js (sync version)
    const fs = require("fs");
    const content = fs.readFileSync("file.txt", "utf-8");
    // Python's `with open` is roughly equivalent — sync, safe

open() MODES:
    "r"   read (default)
    "w"   write — creates or OVERWRITES the file
    "a"   append — adds to the end
    "x"   create new file, fails if it exists

ENCODING:
    Always pass encoding="utf-8" explicitly.
    Without it, Python uses the OS default (can vary on Windows → bugs with
    accented characters, special symbols, etc.)
"""


# =============================================================================
# PART 2 - read(): whole file as one string
# =============================================================================


def read_whole_file(filepath: str) -> str:
    """
    YOUR TASK:
    Open `filepath` in read mode with utf-8 encoding.
    Return the entire content as a single string.

    EXPECTED: a string with all 10 movies separated by newlines
    """
    # --- write your code below ---
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    return content


# =============================================================================
# PART 3 - readlines(): list of lines
# =============================================================================


def read_as_lines(filepath: str) -> list[str]:
    """
    YOUR TASK:
    Open `filepath` and return a list where each element is one line.
    Strip the trailing newline \\n from each line.

    HINT: readlines() returns lines WITH \\n at the end
          Use .strip() or .rstrip("\\n") to clean them

    EXPECTED: ["The Godfather,1972,...", "The Shawshank...", ...]  (10 items)
    """
    # --- write your code below ---
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    clean = [line.rstrip("\n") for line in lines]
    return clean


# =============================================================================
# PART 4 - readline(): one line at a time
# =============================================================================


def read_first_three_lines(filepath: str) -> list[str]:
    """
    YOUR TASK:
    Open the file and use readline() in a loop to read ONLY the first 3 lines.
    Return them as a list (stripped of \\n).

    HINT: call f.readline() three times, or use a for loop with range(3)

    EXPECTED: the first 3 movies as a list of 3 strings
    """
    # --- write your code below ---
    movies = []
    with open(filepath, "r", encoding="utf-8") as f:
        for i in range(3):
            content = f.readline()
            movies.append(content.strip())
    return movies


# =============================================================================
# PART 5 - CINEMA TASK: parse and find the best rated movie
# =============================================================================


def get_best_rated_movie(filepath: str) -> dict:
    """
    YOUR TASK:
    Read the file, parse each line into a dict with keys:
        title, year, director, rating

    Then return the movie with the highest rating.

    FORMAT of each line:
        The Godfather,1972,Francis Ford Coppola,9.2

    HINTS:
    - Use readlines() or iterate the file directly with `for line in f:`
    - Split each line by comma: line.split(",")
    - Convert year to int, rating to float
    - Track the max rating as you go (or use max() with a key)

    EXPECTED: {"title": "The Shawshank Redemption", "year": 1994,
               "director": "Frank Darabont", "rating": 9.3}
    """
    best_movie = None
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            split_lines = line.split(",")
            movie = {
                "title": split_lines[0],
                "year": int(split_lines[1]),
                "director": split_lines[2],
                "rating": float(split_lines[3]),
            }
            if best_movie is None or movie["rating"] > best_movie["rating"]:
                best_movie = movie

    return best_movie


# =============================================================================
# RUNNER
# =============================================================================

if __name__ == "__main__":
    # print("=" * 55)
    # print("EXERCISE 2.1 — Reading Files")
    # print("=" * 55)

    # Part 2
    # print("\n--- Part 2: read() ---")
    # content = read_whole_file(DATA_FILE)
    # if content:
    #     lines_count = content.count("\n")
    #     print(f"File content ({lines_count} newlines):")
    #     print(content[:120], "...")  # show first 120 chars
    # else:
    #     print("Not implemented yet.")

    # # Part 3
    # print("\n--- Part 3: readlines() ---")
    # lines = read_as_lines(DATA_FILE)
    # if lines:
    #     print(f"Total lines: {len(lines)}")
    #     print(f"First line:  {lines[0]}")
    #     print(f"Last line:   {lines[-1]}")
    # else:
    #     print("Not implemented yet.")

    # # Part 4
    # print("\n--- Part 4: readline() × 3 ---")
    # first_three = read_first_three_lines(DATA_FILE)
    # if first_three:
    #     for i, line in enumerate(first_three, 1):
    #         print(f"  Line {i}: {line}")
    # else:
    #     print("Not implemented yet.")

    # Part 5
    print("\n--- Part 5: best rated movie ---")
    best = get_best_rated_movie(DATA_FILE)
    if best:
        print(f"  Title:    {best['title']}")
        print(f"  Year:     {best['year']}")
        print(f"  Director: {best['director']}")
        print(f"  Rating:   {best['rating']}")
    else:
        print("Not implemented yet.")
