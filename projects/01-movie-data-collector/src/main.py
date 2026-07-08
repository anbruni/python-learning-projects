import argparse
import api_client
import cache_manager


def print_movie_list(movies):
    if not movies:
        print("Nessun film trovato.")
        return
    for i, movie in enumerate(movies, start=1):
        title = movie.get("title", "N/A")
        year = movie.get("release_date", "")[:4] or "N/A"
        rating = movie.get("vote_average", 0)
        movie_id = movie.get("id", "")
        print(f"{i:>2}. {title} ({year})  ★ {rating:.1f}  [id: {movie_id}]")


def print_movie_details(movie):
    title = movie.get("title", "N/A")
    year = movie.get("release_date", "")[:4] or "N/A"
    rating = movie.get("vote_average", 0)
    runtime = movie.get("runtime") or "N/A"
    genres = ", ".join(g["name"] for g in movie.get("genres", []))
    overview = movie.get("overview", "N/A")

    print(f"\n{'=' * 50}")
    print(f"  {title} ({year})")
    print(f"{'=' * 50}")
    print(f"  Rating:  ★ {rating:.1f}/10")
    print(f"  Runtime: {runtime} min")
    print(f"  Genres:  {genres or 'N/A'}")
    print(f"\n  {overview}\n")


def handle_fetch(args):
    result = cache_manager.get_or_fetch("trending", api_client.fetch_trending)
    if not result or result.get("status") != "ok":
        print("Errore nel fetch dei film trending.")
        return
    movies = result["data"].get("results", [])
    print(f"\n── Trending today ({len(movies)} films) ──\n")
    print_movie_list(movies)


def handle_search(args):
    key = f"search_{args.title.lower().replace(' ', '_')}"
    if args.year:
        key += f"_{args.year}"
    result = cache_manager.get_or_fetch(
        key, lambda: api_client.fetch_search_title(args.title, args.year, args.language)
    )
    if not result or result.get("status") != "ok":
        print(f"Errore nella ricerca di '{args.title}'.")
        return
    movies = result["data"].get("results", [])
    print(f"\n── Risultati per '{args.title}' ({len(movies)} trovati) ──\n")
    print_movie_list(movies)


def handle_details(args):
    arg = args.movie_id
    key = f"details_{arg}"
    result = cache_manager.get_or_fetch(key, lambda: api_client.fetch_details(arg))
    if not result or result.get("status") != "ok":
        print(f"Errore nel fetch dei dettagli per id {arg}.")
        return
    print_movie_details(result["data"])


parser = argparse.ArgumentParser(
    description="Fetch movie data from TMDB API and cache it locally."
)

subparsers = parser.add_subparsers(dest="command")

fetch_parser = subparsers.add_parser("fetch", help="Fetch trending movies")
fetch_parser.set_defaults(func=handle_fetch)

search_parser = subparsers.add_parser("search", help="Search movies by title")
search_parser.add_argument("title", type=str)
search_parser.add_argument("--year", type=int)
search_parser.add_argument("--language", type=str)
search_parser.set_defaults(func=handle_search)

details_parser = subparsers.add_parser("details", help="Get movie details")
details_parser.add_argument("movie_id", type=int)
details_parser.set_defaults(func=handle_details)

if __name__ == "__main__":
    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
    else:
        args.func(args)
