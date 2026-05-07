
# Exercise 5 — Flatten Nested Structure

# Write your solution in exercise-5.py.


# Write a function `flatten(data)` that takes an arbitrarily nested list
# and returns a flat list of all values.
# It must handle ANY depth of nesting.
#
# Hint: use isinstance(item, list) to check if something is a list.
#
# Examples:
# flatten([1, [2, 3], [4, [5, [6, 7]]]]])  → [1, 2, 3, 4, 5, 6, 7]
# flatten([[["a"]], "b", ["c", ["d"]]])     → ["a", "b", "c", "d"]
# flatten([1, 2, 3])                        → [1, 2, 3]
# flatten([])                               → []

def flatten(data):
    # HINTS for recursion:
    #
    # 1. Create an empty result list to collect values
    result = []
    # 2. Loop through each item in data
    for item in data:
        if isinstance(item, list):
            result.extend(flatten(item))  # Recursively flatten and add to result
        else:
            result.append(item)

    return result
    # 3. For each item, ask: "Is this item a list?"
    #    - Use: isinstance(item, list)
    #
    # 4. If it's a list:
    #    - Call flatten(item) recursively to get the flattened version
    #    - Add those results to your result list
    #
    # 5. If it's NOT a list (it's a value):
    #    - Just add it directly to your result list
    #
    # 6. Return the result list
    #
    # Think: flatten([1, [2, 3]]) should:
    #   - See 1 → add 1
    #   - See [2, 3] → call flatten([2, 3]) → returns [2, 3] → add both
    #   - Result: [1, 2, 3]

    pass

# --- Tests ---
print(flatten([1, [2, 3], [4, [5, [6, 7]]]]))
# Expected: [1, 2, 3, 4, 5, 6, 7]

print(flatten([[["a"]], "b", ["c", ["d"]]]))
# Expected: ["a", "b", "c", "d"]

print(flatten([1, 2, 3]))
# Expected: [1, 2, 3]

print(flatten([]))
# Expected: []

print(flatten([[], [[], [1]], []]))
# Expected: [1]