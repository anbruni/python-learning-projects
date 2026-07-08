import os
import truststore
import requests
import time
from dotenv import load_dotenv

truststore.inject_into_ssl()

ENV_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(ENV_FILE)

API_TOKEN = os.getenv("TMDB_API_TOKEN")
BASE_URL = os.getenv("TMDB_BASE_URL")
if not API_TOKEN or not BASE_URL:
    raise ValueError("TMDB_API_TOKEN e TMDB_BASE_URL sono obbligatori nel .env")


def fetch_trending(max_retries: int = 3, delay: float = 1.0):
    return movies_make_request(
        "/trending/movie/day", max_retries=max_retries, delay=delay
    )


def fetch_search_title(
    title: str, year=None, language=None, max_retries: int = 3, delay: float = 1.0
):
    params = {"query": title}
    if year is not None:
        params["primary_release_year"] = year
    if language is not None:
        params["language"] = language
    return movies_make_request(
        "/search/movie",
        params=params,
        max_retries=max_retries,
        delay=delay,
    )


def fetch_details(movie_id: int, max_retries: int = 3, delay: float = 1.0):
    return movies_make_request(
        f"/movie/{movie_id}", max_retries=max_retries, delay=delay
    )


def movies_make_request(path, params=None, max_retries: int = 3, delay: float = 1.0):
    if not path.startswith("/"):
        path = "/" + path
    url = BASE_URL + path

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(
                url,
                params=params,
                headers={"Authorization": f"Bearer {API_TOKEN}"},
                timeout=10,
            )
            code = response.status_code
            if code == 200:
                return {"status": "ok", "data": response.json()}
            elif 400 <= code < 500:
                return {"status": "client_error", "code": code}
            elif 500 <= code < 600:
                return {"status": "server_error", "code": code}
        except (requests.Timeout, requests.ConnectionError):
            pass
        if attempt < max_retries:
            print(f"Tentativo {attempt}/{max_retries} fallito, riprovo tra {delay}s...")
            time.sleep(delay)
    return None
