# 🎯 Project 3: Movie Recommendation API

> FastAPI backend with AI-powered movie recommendations

## 📋 Overview

A production-ready REST API that provides personalized movie recommendations using LLM integration. Built with FastAPI, SQLAlchemy, and OpenAI/Anthropic APIs, demonstrating modern backend development practices including database design, testing, and deployment.

## 🎯 Learning Goals

- FastAPI framework and REST principles
- Database design and ORM (SQLAlchemy)
- API authentication and security
- LLM integration (OpenAI/Anthropic)
- Unit and integration testing (pytest)
- Docker containerization
- API deployment (Render/Railway)

## 🛠️ Tech Stack

- **Python 3.12**
- **FastAPI** - Modern web framework
- **SQLAlchemy** - ORM
- **SQLite** - Database
- **OpenAI/Anthropic API** - AI recommendations
- **pytest** - Testing
- **Docker** - Containerization
- **Pydantic** - Data validation

## ✨ Features

- [ ] RESTful API endpoints (CRUD operations)
- [ ] User preferences management
- [ ] Movie database with ratings
- [ ] AI-powered personalized recommendations
- [ ] Search and filter capabilities
- [ ] Authentication and authorization
- [ ] Rate limiting
- [ ] API documentation (auto-generated)
- [ ] Comprehensive test suite
- [ ] Dockerized deployment

## 📁 Structure

```
03-movie-recommendation-api/
├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── routers/
│   │   ├── movies.py
│   │   ├── users.py
│   │   └── recommendations.py
│   └── services/
│       ├── recommendation_engine.py
│       └── llm_client.py
└── tests/
    ├── test_movies.py
    ├── test_recommendations.py
    └── test_integration.py
```

## 🔌 API Endpoints (Coming Soon)

```
GET    /movies              # List all movies
GET    /movies/{id}         # Get movie details
POST   /movies              # Add new movie
GET    /recommendations     # Get personalized recommendations
POST   /users/preferences   # Set user preferences
GET    /search              # Search movies
```

## 🚀 Usage (Coming Soon)

```bash
# Local development
uvicorn app.main:app --reload

# Run tests
pytest tests/

# Docker deployment
docker-compose up
```

## 🧠 Recommendation Engine

Uses LLM (OpenAI/Anthropic) to analyze:
- User viewing history
- Genre preferences
- Rating patterns
- Similar user behaviors

Returns context-aware recommendations with explanations.

## 📝 Status

**Week 7-8** - Coming Soon

---

*Part of the 8-week Python learning roadmap*
