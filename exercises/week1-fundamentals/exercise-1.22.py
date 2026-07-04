"""
Exercise 1.22 - Virtual Environments
======================================

LEARNING GOALS:
- Understand why virtual environments are essential
- Create and activate a venv
- Install packages with pip and pin them in requirements.txt
- Know the difference between global Python and a project venv

STRUCTURE:
- Part 1: Why venv? (concept)
- Part 2: Create & activate (shell commands)
- Part 3: Install packages + requirements.txt
- Part 4: Use an installed package in Python code
"""

# =============================================================================
# PART 1 - WHY VIRTUAL ENVIRONMENTS?
# =============================================================================
"""
PROBLEM WITHOUT VENV:

  Project A needs requests==2.28     # old version
  Project B needs requests==2.31     # new version

  If you install both globally, one project breaks.

SOLUTION — virtual environment:
  Each project gets its own isolated Python + packages.
  Activating a venv makes `python` and `pip` point to that project only.

RULE: one project = one venv. Always.

WHAT A VENV CONTAINS:
  venv/
  ├── bin/           ← python, pip executables (Mac/Linux)
  ├── lib/           ← installed packages live here
  └── pyvenv.cfg     ← points to the base Python interpreter

NOTE: never commit the venv/ folder — add it to .gitignore.
      commit requirements.txt instead so anyone can recreate it.
"""


# =============================================================================
# PART 2 - CREATE & ACTIVATE
# =============================================================================
"""
TASK: run these commands in your terminal (NOT inside Python):

# 1. Create the venv (run once per project)
python -m venv venv

# 2. Activate it (run every time you open a new terminal)
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows

# You'll see the prompt change:
#   (venv) $

# 3. Verify you're using the venv's Python
which python                    # Mac/Linux → .../venv/bin/python
python --version                # should show your Python version

# 4. Deactivate when done
deactivate
"""


# =============================================================================
# PART 3 - INSTALL PACKAGES + requirements.txt
# =============================================================================
"""
TASK: with the venv active, run these commands:

# Install a package
pip install requests

# See what's installed
pip list

# Pin current packages to a file (snapshot of your environment)
pip freeze > requirements.txt

# Recreate the exact same environment on another machine:
pip install -r requirements.txt

WHAT requirements.txt LOOKS LIKE:
  certifi==2024.2.2
  charset-normalizer==3.3.2
  idna==3.7
  requests==2.32.3
  urllib3==2.2.1

IMPORTANT:
  - pip freeze captures ALL installed packages, including sub-dependencies
  - Commit requirements.txt to git (never commit venv/)
  - Add venv/ to .gitignore
"""


# =============================================================================
# PART 4 - USE THE INSTALLED PACKAGE
# =============================================================================
"""
This code uses `requests` — it only works if:
1. You've activated the venv
2. You've run: pip install requests

TASK:
1. Activate the venv
2. pip install requests
3. Run this file: python exercise-1.22.py
"""

import sys


def show_environment_info() -> dict:
    """
    Return info about the current Python environment.

    Returns:
        dict with python path, version, and whether we're in a venv
    """
    in_venv = sys.prefix != sys.base_prefix
    return {
        "python_path": sys.executable,
        "version": sys.version.split()[0],
        "in_venv": in_venv,
        "venv_path": sys.prefix if in_venv else None,
    }


def fetch_movie_from_api(movie_id: int = 550) -> dict:
    """
    Fetch a movie from a public API using requests.
    movie_id 550 = Fight Club on OMDb-style test endpoint.

    Args:
        movie_id: numeric movie id

    Returns:
        dict with title, year, and status_code

    Raises:
        ImportError: if requests is not installed in the active environment
    """
    try:
        import requests
    except ImportError:
        raise ImportError(
            "requests not found. Run: pip install requests\n"
            "Make sure the venv is active first!"
        )

    url = f"https://jsonplaceholder.typicode.com/todos/{movie_id}"
    response = requests.get(url, timeout=5)
    return {
        "status_code": response.status_code,
        "data": response.json(),
    }


if __name__ == "__main__":
    print("=" * 55)
    print("EXERCISE 1.22 — Virtual Environments")
    print("=" * 55)

    info = show_environment_info()
    print(f"\nPython:   {info['version']}")
    print(f"Path:     {info['python_path']}")
    print(f"In venv:  {info['in_venv']}")
    if info["in_venv"]:
        print(f"Venv:     {info['venv_path']}")
    else:
        print("\nWARNING: not inside a venv. Activate it first:")
        print("  source venv/bin/activate")

    print("\n--- Testing requests (Part 4) ---")
    try:
        result = fetch_movie_from_api(1)
        print(f"HTTP status: {result['status_code']}")
        print(f"Response:    {result['data']}")
        print("\n✅ requests is installed and working!")
    except ImportError as e:
        print(f"✗  {e}")

    print("\nKEY TAKEAWAYS:")
    print("- python -m venv venv        → create isolated environment")
    print("- source venv/bin/activate   → activate it")
    print("- pip install <package>      → install inside the venv")
    print("- pip freeze > requirements.txt → pin dependencies")
    print("- never commit venv/ — commit requirements.txt instead")
