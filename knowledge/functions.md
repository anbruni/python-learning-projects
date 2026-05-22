# Functions in Python

> Modern, practical guide focused on real-world usage (APIs, data processing, backend development)

## Table of Contents
1. [Function Basics](#function-basics)
2. [Parameters & Arguments](#parameters--arguments)
3. [Type Hints (Modern Python)](#type-hints-modern-python)
4. [*args and **kwargs](#args-and-kwargs)
5. [Scope & Variables](#scope--variables)
6. [Lambda Functions](#lambda-functions)
7. [Higher-Order Functions](#higher-order-functions)
8. [Decorators (Essential for FastAPI)](#decorators-essential-for-fastapi)
9. [Best Practices](#best-practices)
10. [Common Patterns](#common-patterns)

---

## Function Basics

### Definition and Calling

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

result = greet("Andrea")  # "Hello, Andrea!"
```

**JS Comparison:**
```javascript
// JavaScript
function greet(name) {
    return `Hello, ${name}!`;
}

// Python uses 'def', no curly braces, indentation matters
```

### Return Values

```python
# Multiple returns
def get_user_status(age):
    if age < 18:
        return "minor"
    elif age < 65:
        return "adult"
    else:
        return "senior"

# Multiple values (returns tuple)
def get_coordinates():
    return 10, 20  # same as return (10, 20)

x, y = get_coordinates()  # unpacking
```

**Key Point:** Functions without explicit `return` return `None` (like `undefined` in JS).

---

## Parameters & Arguments

### Positional vs Keyword Arguments

```python
def create_user(name, age, city):
    return {"name": name, "age": age, "city": city}

# Positional (order matters)
user1 = create_user("Andrea", 30, "Milan")

# Keyword (order doesn't matter)
user2 = create_user(city="Milan", name="Andrea", age=30)

# Mixed (positional first, then keyword)
user3 = create_user("Andrea", age=30, city="Milan")
```

### Default Parameters

```python
def fetch_data(url, timeout=30, retries=3):
    # timeout and retries have defaults
    pass

fetch_data("https://api.example.com")  # uses defaults
fetch_data("https://api.example.com", timeout=60)  # override one
```

**⚠️ Mutable Default Trap:**
```python
# ❌ BAD - same list reused
def add_item(item, items=[]):
    items.append(item)
    return items

# ✅ GOOD - create new list each time
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## Type Hints (Modern Python)

> Essential for FastAPI, modern codebases, and IDE autocomplete

### Basic Type Hints

```python
def calculate_total(price: float, quantity: int) -> float:
    """Type hints help IDEs and catch bugs early."""
    return price * quantity

# IDE knows the types and can autocomplete
total = calculate_total(19.99, 3)  # float
```

### Complex Types

```python
from typing import List, Dict, Optional, Union

# List of strings
def get_tags() -> List[str]:
    return ["python", "fastapi", "api"]

# Dictionary
def get_user() -> Dict[str, any]:
    return {"name": "Andrea", "age": 30}

# Optional (can be None)
def find_user(user_id: int) -> Optional[Dict]:
    # returns Dict or None
    return None

# Union (multiple types)
def process_id(user_id: Union[int, str]) -> str:
    return str(user_id)
```

### Why Type Hints Matter

```python
# FastAPI automatically validates types!
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int) -> Dict[str, any]:
    # FastAPI converts user_id to int automatically
    # Returns 422 error if not a valid int
    return {"id": user_id, "name": "Andrea"}
```

**Use type hints for:**
- ✅ Function signatures (parameters and return)
- ✅ FastAPI route handlers
- ✅ Data processing pipelines
- ❌ Not needed for quick scripts/prototypes

---

## *args and **kwargs

> Flexible functions that accept variable arguments

### *args - Variable Positional Arguments

```python
def calculate_average(*numbers):
    """Accepts any number of arguments."""
    return sum(numbers) / len(numbers)

avg = calculate_average(10, 20, 30)  # 20.0
avg = calculate_average(5, 15)       # 10.0
```

**What happens:**
- `*numbers` collects all positional arguments into a **tuple**
- Name doesn't have to be "args" (can be `*values`, `*items`, etc.)

**Real-world example:**
```python
def log_message(level: str, *messages):
    """Logger that accepts multiple messages."""
    combined = " ".join(str(msg) for msg in messages)
    print(f"[{level}] {combined}")

log_message("ERROR", "Database", "connection", "failed")
# [ERROR] Database connection failed
```

### **kwargs - Variable Keyword Arguments

```python
def create_api_request(**params):
    """Accepts any keyword arguments."""
    return {"url": "/api/users", "params": params}

req = create_api_request(page=1, limit=10, sort="name")
# {'url': '/api/users', 'params': {'page': 1, 'limit': 10, 'sort': 'name'}}
```

**What happens:**
- `**params` collects all keyword arguments into a **dict**
- Name doesn't have to be "kwargs" (can be `**options`, `**config`, etc.)

**Real-world example (FastAPI pattern):**
```python
def build_query(table: str, **filters):
    """Build SQL WHERE clause from filters."""
    conditions = [f"{key} = '{value}'" for key, value in filters.items()]
    where = " AND ".join(conditions)
    return f"SELECT * FROM {table} WHERE {where}"

query = build_query("users", city="Milan", age=30)
# "SELECT * FROM users WHERE city = 'Milan' AND age = '30'"
```

### Combining All Parameter Types

```python
def api_call(endpoint: str, *ids, method="GET", **params):
    """
    endpoint: required positional
    *ids: optional positional (tuple)
    method: keyword with default
    **params: optional keyword (dict)
    """
    print(f"{method} {endpoint}")
    print(f"IDs: {ids}")
    print(f"Params: {params}")

api_call("/users", 1, 2, 3, method="POST", limit=10, page=1)
# POST /users
# IDs: (1, 2, 3)
# Params: {'limit': 10, 'page': 1}
```

**Order matters:**
1. Positional parameters
2. `*args`
3. Keyword parameters with defaults
4. `**kwargs`

---

## Scope & Variables

### Local vs Global

```python
count = 0  # global variable

def increment():
    count = count + 1  # ❌ ERROR: UnboundLocalError
    return count

# Fix 1: Use 'global' keyword
count = 0
def increment():
    global count
    count = count + 1
    return count

# Fix 2: Return new value (better practice)
def increment(count):
    return count + 1

count = increment(count)  # explicit state change
```

**⚠️ Avoid global variables:**
- Hard to test
- Hard to debug
- Not thread-safe
- Better: pass state as parameters or use classes

### Nonlocal (Nested Functions)

```python
def outer():
    count = 0
    
    def increment():
        nonlocal count  # modifies outer's count
        count += 1
        return count
    
    return increment

counter = outer()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

**When you'll use this:**
- Closures
- Decorators
- Factory functions

**JS Comparison:**
```javascript
// JavaScript has similar closure behavior
function outer() {
    let count = 0;
    return function increment() {
        count++;  // automatically captures count
        return count;
    }
}
```

---

## Lambda Functions

> Anonymous functions for simple operations

### Basic Syntax

```python
# Regular function
def square(x):
    return x ** 2

# Lambda (one-liner)
square = lambda x: x ** 2

result = square(5)  # 25
```

### Practical Use Cases

**1. Sorting with custom key:**
```python
users = [
    {"name": "Andrea", "age": 30},
    {"name": "Maria", "age": 25},
    {"name": "Luca", "age": 35}
]

# Sort by age
sorted_users = sorted(users, key=lambda u: u["age"])
# [{'name': 'Maria', 'age': 25}, ...]
```

**2. Filtering:**
```python
numbers = [1, 2, 3, 4, 5, 6]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]
```

**3. Mapping:**
```python
prices = [10, 20, 30]

# Add tax (22%)
with_tax = list(map(lambda p: p * 1.22, prices))
# [12.2, 24.4, 36.6]
```

### When NOT to Use Lambda

```python
# ❌ BAD - too complex
process = lambda x: x.strip().lower() if x else ""

# ✅ GOOD - use regular function with name
def clean_text(text):
    return text.strip().lower() if text else ""
```

**Rule of thumb:**
- ✅ Lambdas for simple, one-line operations
- ✅ Used as arguments to other functions (sort, filter, map)
- ❌ If you need multiple lines → regular function
- ❌ If logic is complex → regular function with docstring

---

## Higher-Order Functions

> Functions that take other functions as arguments or return functions

### Functions as Arguments

```python
def apply_operation(numbers: List[int], operation):
    """Apply operation to each number."""
    return [operation(n) for n in numbers]

# Use with lambda
doubled = apply_operation([1, 2, 3], lambda x: x * 2)
# [2, 4, 6]

# Use with regular function
def square(x):
    return x ** 2

squared = apply_operation([1, 2, 3], square)
# [1, 4, 9]
```

### Common Built-in Higher-Order Functions

**map() - Transform each element:**
```python
names = ["andrea", "maria", "luca"]
capitalized = list(map(str.capitalize, names))
# ["Andrea", "Maria", "Luca"]

# Same with list comprehension (often preferred)
capitalized = [name.capitalize() for name in names]
```

**filter() - Keep elements that match condition:**
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]

# Same with list comprehension (often preferred)
evens = [x for x in numbers if x % 2 == 0]
```

**sorted() with key:**
```python
users = [
    {"name": "Andrea", "score": 85},
    {"name": "Maria", "score": 92}
]

# Sort by score (descending)
top_users = sorted(users, key=lambda u: u["score"], reverse=True)
```

### Functions Returning Functions (Factory Pattern)

```python
def make_multiplier(factor: int):
    """Factory that creates multiplier functions."""
    def multiply(x: int) -> int:
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

**Real-world example: API client factory:**
```python
def create_api_client(base_url: str, api_key: str):
    """Factory for API client with specific base URL and key."""
    def make_request(endpoint: str, **params):
        url = f"{base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {api_key}"}
        # ... make request
        return {"url": url, "headers": headers, "params": params}
    
    return make_request

# Create specific client
tmdb_client = create_api_client("https://api.themoviedb.org", "abc123")

# Use it
movies = tmdb_client("/movies", page=1, limit=10)
```

---

## Decorators (Essential for FastAPI)

> Functions that modify other functions (you'll use these constantly in FastAPI)

### Basic Decorator

```python
def log_calls(func):
    """Decorator that logs function calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 5)
# Calling add
# add returned 8
```

**What `@log_calls` does:**
```python
# This decorator syntax:
@log_calls
def add(a, b):
    return a + b

# Is equivalent to:
def add(a, b):
    return a + b
add = log_calls(add)  # wrap function
```

### FastAPI Uses Decorators Heavily

```python
from fastapi import FastAPI

app = FastAPI()

# @app.get is a decorator!
@app.get("/")
def home():
    return {"message": "Hello"}

@app.post("/users")
def create_user(user: dict):
    return user
```

### Practical Decorator: Timing

```python
import time

def timer(func):
    """Measure function execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "done"

slow_function()
# slow_function took 2.00s
```

### Decorator with Parameters

```python
def retry(max_attempts: int):
    """Decorator that retries function on failure."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed, retrying...")
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_api_call():
    # might fail occasionally
    pass
```

**You'll use decorators for:**
- ✅ FastAPI routes (`@app.get`, `@app.post`)
- ✅ Authentication/authorization
- ✅ Caching
- ✅ Rate limiting
- ✅ Logging/monitoring

---

## Best Practices

### 1. Use Type Hints (Modern Python)

```python
# ❌ No types
def process_data(data, config):
    pass

# ✅ With types
def process_data(data: List[Dict], config: Dict[str, any]) -> List[Dict]:
    pass
```

### 2. Keep Functions Small & Focused

```python
# ❌ Does too much
def process_and_save_user(data):
    cleaned = clean_data(data)
    validated = validate_data(cleaned)
    user = create_user(validated)
    save_to_db(user)
    send_email(user)
    log_event(user)
    return user

# ✅ Single responsibility
def create_user_from_data(data: dict) -> User:
    cleaned = clean_data(data)
    validated = validate_data(cleaned)
    return create_user(validated)
```

### 3. Pure Functions When Possible

```python
# ❌ Side effects (modifies global state)
total = 0
def add_to_total(value):
    global total
    total += value

# ✅ Pure function (no side effects)
def add_to_total(current_total: int, value: int) -> int:
    return current_total + value

total = add_to_total(total, 10)  # explicit
```

### 4. Descriptive Names

```python
# ❌ Unclear
def process(d):
    return d * 1.22

# ✅ Clear
def calculate_price_with_tax(price: float) -> float:
    TAX_RATE = 0.22
    return price * (1 + TAX_RATE)
```

### 5. Avoid Mutable Defaults

```python
# ❌ BAD
def add_item(item, items=[]):
    items.append(item)
    return items

# ✅ GOOD
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## Common Patterns

### 1. Data Validation

```python
def validate_user(user: dict) -> bool:
    """Validate user data before saving."""
    required = ["name", "email", "age"]
    
    # Check required fields
    if not all(field in user for field in required):
        return False
    
    # Check types
    if not isinstance(user["age"], int) or user["age"] < 0:
        return False
    
    # Check email format
    if "@" not in user["email"]:
        return False
    
    return True
```

### 2. Data Transformation Pipeline

```python
def transform_user_data(raw_data: List[dict]) -> List[dict]:
    """Clean and transform user data."""
    cleaned = [clean_user(u) for u in raw_data]
    validated = [u for u in cleaned if validate_user(u)]
    enriched = [enrich_user(u) for u in validated]
    return enriched
```

### 3. Error Handling

```python
from typing import Optional

def safe_divide(a: float, b: float) -> Optional[float]:
    """Divide with error handling."""
    if b == 0:
        return None
    return a / b

# Or raise specific exception
def divide(a: float, b: float) -> float:
    """Divide or raise ValueError."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### 4. Configuration Functions

```python
def get_database_config(env: str = "development") -> dict:
    """Get database config for environment."""
    configs = {
        "development": {
            "host": "localhost",
            "port": 5432,
            "database": "dev_db"
        },
        "production": {
            "host": "prod-server.com",
            "port": 5432,
            "database": "prod_db"
        }
    }
    return configs.get(env, configs["development"])
```

---

## JavaScript Comparison Summary

| Feature | Python | JavaScript |
|---------|--------|-----------|
| **Definition** | `def func():` | `function func() {}` |
| **Arrow function** | `lambda x: x * 2` | `x => x * 2` |
| **Default params** | `def func(x=10):` | `function func(x = 10) {}` |
| **Rest params** | `def func(*args):` | `function func(...args) {}` |
| **Spread object** | `def func(**kwargs):` | `function func(obj) {}` (no direct equivalent) |
| **Type hints** | `def func(x: int) -> str:` | TypeScript: `function func(x: number): string` |
| **Decorators** | `@decorator` | No native syntax (use HOF) |

---

## Key Takeaways

✅ **Use type hints** - Essential for FastAPI, better IDE support  
✅ **Master *args/**kwargs** - You'll see them everywhere  
✅ **Understand decorators** - FastAPI is built on them  
✅ **Keep functions pure** - Easier to test and debug  
✅ **Avoid mutable defaults** - Common source of bugs  
✅ **Use lambdas sparingly** - Only for simple operations  

**Next:** Practice these concepts in exercises to solidify understanding! 🚀
