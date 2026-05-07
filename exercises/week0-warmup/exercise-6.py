# Write a function `nested_sum(data)` that takes a nested dictionary/list structure
# and returns the SUM of all numeric values (int or float) found at any depth.
# Ignore all non-numeric values (strings, bools, None, etc.)
#
# Hint: Use isinstance() to check types:
#   - isinstance(x, dict) → is it a dictionary?
#   - isinstance(x, list) → is it a list?
#   - isinstance(x, (int, float)) → is it a number?
#   - isinstance(x, bool) → is it a bool? (IMPORTANT: bool counts as int in Python!)
#
# Examples:
# nested_sum({"a": 1, "b": {"c": 2, "d": 3}})  → 6
# nested_sum([1, [2, {"x": 3}], 4])  → 10
# nested_sum({"a": 1, "b": "ignore", "c": [2, True, 3]})  → 6 (True is bool, not counted)
# nested_sum({})  → 0
# nested_sum({"a": [1, [2, [3, {"nested": 4}]]]})  → 10

def nested_sum(data):
    values = 0
    if isinstance(data, bool):
        pass
    elif isinstance(data, str):
        pass
    elif isinstance(data, dict):
        for value in data.values():
            values += nested_sum(value)
    elif isinstance(data, list):
        for element in data:
            values += nested_sum(element)
    elif isinstance(data, (int, float)):
        values += data
    return values

# --- Tests ---
print(nested_sum({"a": 1, "b": {"c": 2, "d": 3}}))
# Expected: 6

print(nested_sum([1, [2, {"x": 3}], 4]))
# # Expected: 10

print(nested_sum({"a": 1, "b": "ignore", "c": [2, True, 3]}))
# # Expected: 6

print(nested_sum({}))
# # Expected: 0

print(nested_sum({"a": [1, [2, [3, {"nested": 4}]]]}))
# # Expected: 10

print(nested_sum({"x": 5, "y": False, "z": [10, None, 20]}))
# Expected: 35