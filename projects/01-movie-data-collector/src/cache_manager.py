import os
import json
import time
from dotenv import load_dotenv

ENV_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(ENV_FILE)

_PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
CACHE_DIR = os.path.join(_PROJECT_DIR, os.getenv("CACHE_DIR", "data"))
CACHE_MAX_AGE_HOURS = int(os.getenv("CACHE_MAX_AGE_HOURS", 24))

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR, exist_ok=True)


def _cache_path(key):
    return os.path.join(CACHE_DIR, f"{key}.json")


def is_fresh(key):
    if not os.path.exists(_cache_path(key)):
        return False
    age_hours = (time.time() - os.path.getmtime(_cache_path(key))) / 3600
    return age_hours < CACHE_MAX_AGE_HOURS


def save(key, data):
    with open(_cache_path(key), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_or_fetch(key, fetch_fn):
    if is_fresh(key):
        try:
            with open(_cache_path(key), "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass

    result = fetch_fn()
    if result is None:
        return None
    save(key, result)
    return result
