# 🎬 Project 1: Movie Data Collector

> CLI tool for fetching and caching TMDB movie data

## 📋 Overview

A command-line application that interacts with the TMDB (The Movie Database) API to fetch, cache, and display movie information. Built with Python fundamentals focusing on API integration, error handling, and file I/O.

## 🎯 Learning Goals

- HTTP requests and API integration
- JSON parsing and data handling
- CLI argument parsing
- Error handling and validation
- File-based caching system
- Environment variables

## 🛠️ Tech Stack

- **Python 3.12**
- **requests** - HTTP library
- **argparse** - CLI interface
- **json** - Data serialization
- **TMDB API** - Movie database

## ✨ Features

- [ ] Search movies by title
- [ ] Fetch movie details (rating, cast, description)
- [ ] Cache results to avoid repeated API calls
- [ ] Display formatted movie information
- [ ] Handle API errors gracefully
- [ ] Support multiple search filters

## 📁 Structure

```
01-movie-data-collector/
├── README.md
├── requirements.txt
├── .env.example
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── api_client.py
│   └── cache_manager.py
└── tests/
    └── test_api_client.py
```

## 🚀 Usage (Coming Soon)

```bash
# Search for a movie
python src/main.py search "Inception"

# Get movie details
python src/main.py details --id 27205

# Clear cache
python src/main.py cache --clear
```

## 📝 Status

**Week 4** - Coming Soon

---

*Part of the 8-week Python learning roadmap*
