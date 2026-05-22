# --- Data ---
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 25, 30]

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 42},
    {"name": "Charlie", "grade": 90},
    {"name": "Diana", "grade": 55},
    {"name": "Eve", "grade": 73},
    {"name": "Frank", "grade": 38},
]

words = ["hello", "world", "Python", "is", "Awesome", "a", "GREAT", "language"]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# --- Task 1: Fizzbuzz list ---
# Build a list from `numbers` where:
#   - if divisible by both 3 and 5 → "fizzbuzz"
#   - if divisible by 3 only → "fizz"
#   - if divisible by 5 only → "buzz"
#   - otherwise → the number itself
# Expected: [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", "fizzbuzz", "buzz", "buzz", "fizzbuzz"]
fizzbuzz = ["fizzbuzz" if num%3 == 0 and num%5 == 0 else "fizz" if num%3 == 0 else "buzz" if num%5 == 0 else num for num in numbers]

# --- Task 2: Passing students ---
# From `students`, extract the NAMES (just the name string) of students with grade >= 60
# Expected: ["Alice", "Charlie", "Eve"]
passing = [student["name"] for student in students if student["grade"] > 60]

# --- Task 3: Normalize words ---
# From `words`, keep only words longer than 1 character and convert them to lowercase
# Expected: ["hello", "world", "python", "is", "awesome", "great", "language"]
normalized = [word.lower() for word in words if len(word) > 1]

# --- Task 4: Flatten matrix ---
# Flatten `matrix` into a single list of numbers using a nested comprehension
# Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
flat = [v for row in matrix for v in row]

# --- Print results ---
print(f"Fizzbuzz: {fizzbuzz}")
print(f"Passing: {passing}")
print(f"Normalized: {normalized}")
print(f"Flat: {flat}")

