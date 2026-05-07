# Exercise 2 — Group by Category

# Write your solution in a new file exercise-2.py.

# You're given a list of tuples, where each tuple is (item, category). Build a dictionary that groups items by their category, so each key is a category and its value is a list of items.
items = [
    ("pasta", "food"),
    ("python", "language"),
    ("pizza", "food"),
    ("java", "language"),
    ("water", "drink"),
    ("sushi", "food"),
    ("coffee", "drink"),
    ("rust", "language"),
    ("tea", "drink"),
]

# Your code here:
# Build a dict: category -> list of items
# Then print each category and its items, sorted by category name, like:
#
#   drink: water, coffee, tea
#   food: pasta, pizza, sushi
#   language: python, java, rust
category_items = {}

for item, cat in items:

    if cat not in category_items:
        category_items[cat] = []

    category_items[cat].append(item)

category_items = dict(sorted(category_items.items()))

for cat in category_items:
    formatted = ", ".join(category_items[cat])
    print(f"{cat}: {formatted}")
    