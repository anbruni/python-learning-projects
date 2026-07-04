"""
Exercise 2.2 - Writing Files
==============================

LEARNING GOALS:
- Write new files with open("w")  — creates or OVERWRITES
- Append to existing files with open("a")
- Use f.write() for a single string
- Use f.writelines() for a list of strings
- Difference between write() and writelines()

DATA FILE: data/movies.txt   (read source)
OUTPUT:    data/             (your functions will create files here)

STRUCTURE:
- Part 1: Concept — write modes and write vs writelines
- Part 2: write()       → write a string to a file, return char count
- Part 3: writelines()  → write a list of lines at once
- Part 4: append        → add an entry without overwriting
- Part 5: Cinema task   → filter movies and save to a new file
"""

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "movies.txt")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "data")


# =============================================================================
# PART 1 - CONCEPT: write modes and write vs writelines
# =============================================================================
"""
WRITING A FILE:
    with open("file.txt", "w", encoding="utf-8") as f:
        f.write("hello\n")
    # "w" creates the file if missing, or OVERWRITES it entirely

APPENDING TO A FILE:
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write("new line\n")
    # "a" creates the file if missing, adds to the END — never overwrites

write() vs writelines():
    f.write("line one\nline two\n")        # single string, you add \n yourself
    f.writelines(["line one\n", "line two\n"])  # list of strings, same result

    KEY DIFFERENCE: writelines() does NOT add \n between items.
    You must include \n in each string yourself.

JS COMPARISON:
    // Node.js sync equivalent
    const fs = require("fs");
    fs.writeFileSync("file.txt", content, "utf-8");   // like "w"
    fs.appendFileSync("log.txt", line, "utf-8");       // like "a"
"""


# =============================================================================
# PART 2 - write(): write a string to a file
# =============================================================================


def write_summary(filepath: str, content: str) -> int:
    """
    YOUR TASK:
    Write `content` to `filepath` using open("w").
    Return the number of characters written (f.write() returns this for you).

    HINT: f.write(content) returns the number of characters written as an int.

    EXPECTED: the file is created/overwritten with `content`,
              return value is len(content)
    """
    # --- write your code below ---
    with open(filepath, "w", encoding="utf-8") as f:
        write_len = f.write(content)

    return write_len


# =============================================================================
# PART 3 - writelines(): write a list of lines
# =============================================================================


def write_lines(filepath: str, lines: list[str]) -> None:
    """
    YOUR TASK:
    Write the list `lines` to `filepath` using writelines().
    Each string in `lines` already ends with "\n" — don't add more.

    HINT: f.writelines(lines) writes each item in the list with no separator.

    EXPECTED: the file contains exactly the lines in `lines`, one per row.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)


# =============================================================================
# PART 4 - append mode: add an entry without overwriting
# =============================================================================


def log_movie_watched(log_filepath: str, title: str, rating: float) -> None:
    """
    YOUR TASK:
    Append a new entry to `log_filepath` in this format:
        WATCHED: <title> — <rating>/10\n

    Example line:
        WATCHED: Inception — 8.8/10\n

    Use open("a") so previous entries are preserved.

    EXPECTED: each call adds ONE new line to the log file.
              Calling it 3 times → 3 lines in the file.
    """
    with open(log_filepath, "a", encoding="utf-8") as f:
        f.write(f"WATCHED: {title} — {rating}/10\n")


# =============================================================================
# PART 5 - CINEMA TASK: filter movies and save to a new file
# =============================================================================


def save_top_rated(
    source_filepath: str, output_filepath: str, min_rating: float
) -> int:
    """
    YOUR TASK:
    Read all movies from `source_filepath` (same CSV format as exercise 2.1).
    Filter: keep only movies with rating >= min_rating.
    Write the matching lines to `output_filepath` in the SAME CSV format
    (title,year,director,rating — one per line).

    Return the number of movies written.

    HINTS:
    - Parse each line with split(",") and convert rating to float
    - Filter with an if condition
    - Use open("w") to write the output file
    - To write back to CSV: f.write(f"{title},{year},{director},{rating}\n")
    - strip() the line before splitting to avoid trailing \n in the last field

    EXPECTED with min_rating=9.0:
        Writes 3 movies (Godfather 9.2, Shawshank 9.3, Dark Knight 9.0)
        Returns 3
    """
    count = 0
    with open(source_filepath, "r", encoding="utf-8") as r, \
         open(output_filepath, "w", encoding="utf-8") as w:
        for line in r:
            split_line = line.strip().split(",")
            title = split_line[0]
            year = int(split_line[1])
            director = split_line[2]
            rating = float(split_line[3])

            if rating >= min_rating:
                w.write(f"{title},{year},{director},{rating}\n")
                count += 1
    return count


# =============================================================================
# RUNNER
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("EXERCISE 2.2 — Writing Files")
    print("=" * 55)

    # Part 2
    # print("\n--- Part 2: write() ---")
    # summary_file = os.path.join(OUTPUT_DIR, "summary.txt")
    # content = "Cinema Tracker — Top Movies List\nGenerated by exercise 2.2\n"
    # chars = write_summary(summary_file, content)
    # if chars:
    #     print(f"  Written {chars} characters to summary.txt")
    # else:
    #     print("  Not implemented yet.")

    # Part 3
    # print("\n--- Part 3: writelines() ---")
    # lines_file = os.path.join(OUTPUT_DIR, "directors.txt")
    # directors = [
    #     "Francis Ford Coppola\n",
    #     "Frank Darabont\n",
    #     "Christopher Nolan\n",
    # ]
    # write_lines(lines_file, directors)
    # if os.path.exists(lines_file):
    #     with open(lines_file, "r", encoding="utf-8") as f:
    #         result = f.read()
    #     print(f"  directors.txt content:\n{result.strip()}")
    # else:
    #     print("  Not implemented yet.")

    # Part 4
    # print("\n--- Part 4: append ---")
    # log_file = os.path.join(OUTPUT_DIR, "watch_log.txt")
    # log_movie_watched(log_file, "Inception", 8.8)
    # log_movie_watched(log_file, "The Dark Knight", 9.0)
    # log_movie_watched(log_file, "Interstellar", 8.7)
    # if os.path.exists(log_file):
    #     with open(log_file, "r", encoding="utf-8") as f:
    #         entries = f.readlines()
    #     print(f"  {len(entries)} entries in watch_log.txt:")
    #     for entry in entries:
    #         print(f"    {entry.strip()}")
    # else:
    #     print("  Not implemented yet.")

    # # Part 5
    print("\n--- Part 5: save_top_rated ---")
    top_file = os.path.join(OUTPUT_DIR, "top_rated.txt")
    count = save_top_rated(DATA_FILE, top_file, min_rating=9.0)
    if count:
        print(f"  Saved {count} top-rated movies to top_rated.txt:")
        with open(top_file, "r", encoding="utf-8") as f:
            for line in f:
                print(f"    {line.strip()}")
    else:
        print("  Not implemented yet.")
