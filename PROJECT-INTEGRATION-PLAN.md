# 🎬 Cinema Mood Recommender - Full-Stack Integration Plan

> **Obiettivo:** Integrare un AI movie recommender nel sito personale React + FastAPI backend Python

---

## 🎯 Vision del Progetto

**Cosa fa:**
Un recommender di film AI-powered integrato nella sezione "Interessi" del tuo sito personale. L'utente inserisce:
- Genere preferito
- Mood attuale (es: "mind-bending", "relaxing", "thrilling")
- Film che gli è piaciuto (opzionale)

Il sistema risponde con **5 film personalizzati + spiegazione AI** del perché sono stati scelti.

**Perché è potente per colloqui:**
- ✅ Full-stack (React + Python)
- ✅ AI integration (LLM per recommendations)
- ✅ Real APIs (TMDB)
- ✅ Live demo sul tuo sito
- ✅ Mostra personalità + skills tecnici
- ✅ Storytelling: "Amo il cinema, ho costruito questo..."

---

## 🏗️ Architettura

```
cinema-mood-recommender/
│
├── 📁 backend/                    # FastAPI Python
│   ├── main.py                    # FastAPI app
│   ├── routers/
│   │   └── recommendations.py     # POST /api/recommend
│   ├── services/
│   │   ├── tmdb_service.py        # TMDB API client
│   │   └── llm_service.py         # OpenAI/Anthropic client
│   ├── models.py                  # SQLAlchemy models
│   ├── schemas.py                 # Pydantic schemas
│   ├── database.py                # DB connection
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
└── 📁 frontend/                   # Il tuo sito React
    └── src/
        ├── pages/
        │   └── Interests.tsx      # Sezione cinema
        └── components/
            └── MovieRecommender/
                ├── MovieRecommender.tsx
                ├── MovieCard.tsx
                └── RecommendationForm.tsx
```

---

## 🔌 API Design

### Endpoint: `POST /api/recommend`

**Request:**
```json
{
  "genre": "Sci-Fi",
  "mood": "mind-bending, philosophical",
  "liked_movie": "Inception",
  "year_min": 2010,
  "year_max": 2024
}
```

**Response:**
```json
{
  "recommendations": [
    {
      "title": "Interstellar",
      "year": 2014,
      "rating": 8.6,
      "poster_url": "https://image.tmdb.org/...",
      "tmdb_id": 157336,
      "reason": "Similar to Inception - Christopher Nolan's masterpiece exploring time dilation and consciousness. Mind-bending narrative structure with philosophical themes about love and sacrifice.",
      "genres": ["Sci-Fi", "Drama"]
    },
    // ... altri 4 film
  ],
  "query_summary": "Based on your love for Inception and your mind-bending mood, here are 5 philosophical sci-fi films from 2010-2024."
}
```

---

## 🧠 LLM Integration Strategy (FREE with Groq)

### Setup Groq (GRATUITO)

**Step 1:** Registrati su [groq.com](https://console.groq.com)  
**Step 2:** Prendi API key dalla console  
**Step 3:** Installa SDK:
```bash
pip install groq
```

### Code Example con Groq

```python
# llm_service.py
from groq import Groq
import os
import json

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are a cinema expert who provides personalized movie recommendations.
Given a user's preferences (genre, mood, liked movies), recommend 5 films with thoughtful explanations.

For each recommendation, explain:
- Why it matches their mood
- Connection to movies they liked
- What makes it special

Keep explanations concise (2-3 sentences) and enthusiastic.
Return ONLY valid JSON, no markdown formatting."""

def get_recommendations(genre: str, mood: str, liked_movie: str, candidates: list) -> list:
    """
    Uses Groq (FREE) to select best movies from TMDB candidates.
    Model: llama-3.1-70b-versatile (gratis, velocissimo)
    """
    
    prompt = f"""
User preferences:
- Genre: {genre}
- Mood: {mood}
- Liked movie: {liked_movie}

Here are {len(candidates)} candidate films from TMDB:
{format_candidates(candidates)}

Select the TOP 5 films that best match the user's mood and preferences.
For each film, provide a compelling 2-3 sentence explanation of why it's a great match.

Return as JSON array with this exact structure:
[
  {{"title": "Movie Title", "year": 2020, "reason": "Explanation here..."}},
  ...
]
"""
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",  # FREE model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000,
            response_format={"type": "json_object"}  # Force JSON output
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
        
    except Exception as e:
        # Fallback if Groq fails
        print(f"Groq API error: {e}")
        return []

def format_candidates(candidates: list) -> str:
    """Format TMDB candidates for LLM"""
    formatted = []
    for movie in candidates:
        formatted.append(
            f"- {movie['title']} ({movie['year']}) - Rating: {movie['rating']}/10"
        )
    return "\n".join(formatted)
```

### Groq Limits (Free Tier)

✅ **Limiti generosi per un progetto portfolio:**
- 30 requests/minute
- 14,400 requests/day
- Llama 3.1 70B gratis
- ~300 tokens/second (velocissimo!)

**Sufficiente per:**
- Demo live sul tuo sito
- Testing durante sviluppo
- Mostrare in colloqui
- Primi utenti reali

**Flow:**
1. User input → backend
2. Backend fetches 20-30 candidate movies from TMDB (by genre, year range)
3. Backend calls **Groq** (FREE) con candidates + user preferences
4. Groq ritorna top 5 + spiegazioni (in ~1 secondo!)
5. Backend arricchisce con TMDB data (poster, rating, etc)
6. Frontend mostra i risultati

### Alternative se Groq non ti convince

**Ollama (locale, 100% free):**
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download model (es. Llama 3.1 8B)
ollama pull llama3.1

# Run server
ollama serve

# In Python
from ollama import Client
client = Client(host='http://localhost:11434')
response = client.chat(model='llama3.1', messages=[...])
```

**Pro Ollama**: Zero costi, privacy, offline  
**Con Ollama**: Più lento, serve hardware decente, complesso da deployare

**Consiglio:** Inizia con **Groq** (gratis, veloce, cloud). Se poi vuoi 100% controllo, switch a Ollama.

---

## 🎨 UI/UX nel tuo sito React

### Sezione "Interests" > Cinema

**Layout:**

```
┌─────────────────────────────────────────────┐
│  🎬 Cinema Mood Recommender                 │
│  ──────────────────────────────────────     │
│                                              │
│  "In my free time, I love exploring cinema  │
│   - from classic noir to mind-bending       │
│   sci-fi. I built this AI recommender to    │
│   share that passion."                      │
│                                              │
│  ┌────────────────────────────────────┐     │
│  │ What genre are you in the mood for?│     │
│  │ [Dropdown: Sci-Fi, Thriller, ... ] │     │
│  │                                     │     │
│  │ Describe your mood:                │     │
│  │ [Input: mind-bending, relaxing...] │     │
│  │                                     │     │
│  │ A movie you loved (optional):      │     │
│  │ [Input with autocomplete]          │     │
│  │                                     │     │
│  │ Year range:                         │     │
│  │ [2010] ──────────── [2024]         │     │
│  │                                     │     │
│  │        [Get Recommendations]        │     │
│  └────────────────────────────────────┘     │
│                                              │
│  ✨ Your Recommendations:                   │
│                                              │
│  ┌──────┐  ┌──────┐  ┌──────┐              │
│  │POSTER│  │POSTER│  │POSTER│   ...        │
│  │      │  │      │  │      │              │
│  │Title │  │Title │  │Title │              │
│  │★ 8.6 │  │★ 8.2 │  │★ 9.0 │              │
│  │      │  │      │  │      │              │
│  │"AI explains why..."                      │
│  └──────┘  └──────┘  └──────┘              │
└─────────────────────────────────────────────┘
```

**Animazioni:**
- Smooth fade-in per i risultati
- Hover effect sui poster (scale up)
- Loading state con skeleton cards

---

## 📅 Roadmap di Sviluppo

### Phase 1: Backend MVP (Week 4-5) - 2 settimane
**Goal:** API funzionante che ritorna raccomandazioni

✅ **Step 1.1 - Setup base (2-3 giorni)**
- [ ] FastAPI project structure
- [ ] TMDB API client (`tmdb_service.py`)
  - [ ] Search movies by genre
  - [ ] Get movie details
  - [ ] Get similar movies
- [ ] Environment setup (.env, requirements.txt)
- [ ] Test TMDB integration con Postman/curl

✅ **Step 1.2 - LLM integration (3-4 giorni)**
- [ ] LLM service (`llm_service.py`)
  - [ ] OpenAI/Anthropic client
  - [ ] Prompt engineering per recommendations
  - [ ] Structured output parsing
- [ ] Test LLM recommendations manualmente
- [ ] Error handling (API failures, rate limits)

✅ **Step 1.3 - Endpoint `/api/recommend` (2-3 giorni)**
- [ ] Pydantic schemas (RecommendationRequest, RecommendationResponse)
- [ ] Router per recommendations
- [ ] Flow completo: input → TMDB → LLM → response
- [ ] Logging
- [ ] Basic tests con pytest

**Deliverable Phase 1:** API funzionante, testabile con curl, pronta per il frontend

---

### Phase 2: Frontend Integration (Week 5-6) - 1.5 settimane
**Goal:** UI nel tuo sito React + chiamate al backend

✅ **Step 2.1 - Component MovieRecommender (3-4 giorni)**
- [ ] Form component (genre, mood, liked_movie, year_range)
- [ ] State management (React hooks o Zustand)
- [ ] API client (axios/fetch)
- [ ] Loading & error states
- [ ] Form validation

✅ **Step 2.2 - Results display (2-3 giorni)**
- [ ] MovieCard component (poster, title, rating, reason)
- [ ] Grid layout responsive
- [ ] Animations (fade-in, hover effects)
- [ ] Link to TMDB per ogni film

✅ **Step 2.3 - Integration nella sezione Interests (1-2 giorni)**
- [ ] Aggiungere al tuo sito esistente
- [ ] Styling coerente con il resto del sito
- [ ] Intro text personale ("Why I love cinema...")

**Deliverable Phase 2:** Feature LIVE sul tuo sito

---

### Phase 3: Polish & Deploy (Week 7) - 1 settimana
**Goal:** Production-ready, deployato, documentato

✅ **Step 3.1 - Backend polish (2 giorni)**
- [ ] Caching (Redis o in-memory) per evitare chiamate duplicate
- [ ] Rate limiting
- [ ] CORS setup per il tuo dominio
- [ ] Environment variables per production
- [ ] Logging strutturato

✅ **Step 3.2 - Deploy (2 giorni)**
- [ ] Backend su Render/Railway/Fly.io (free tier)
- [ ] Frontend già deployato col tuo sito
- [ ] Environment variables setup
- [ ] Test end-to-end in production

✅ **Step 3.3 - Documentation (2 giorni)**
- [ ] README backend (setup, API docs, architecture)
- [ ] README frontend (come funziona)
- [ ] Screenshot/GIF della feature
- [ ] Blog post opzionale: "How I built an AI movie recommender"

✅ **Step 3.4 - Testing & refinement (1 giorno)**
- [ ] Test con amici/colleghi
- [ ] Fix edge cases
- [ ] Performance optimization
- [ ] A/B test prompt variations

**Deliverable Phase 3:** Progetto completo, live, documentato

---

## 🎯 Skills Dimostrate (Per CV/Colloqui)

### Backend
- ✅ FastAPI (routing, Pydantic, async)
- ✅ API integration (TMDB)
- ✅ **LLM integration (OpenAI/Anthropic)** ⭐
- ✅ Prompt engineering
- ✅ Error handling & logging
- ✅ Testing (pytest)
- ✅ Environment management

### Frontend
- ✅ React (hooks, state management)
- ✅ TypeScript
- ✅ API consumption (fetch/axios)
- ✅ Responsive design
- ✅ UX (loading states, animations)

### DevOps
- ✅ Deploy (Render/Railway)
- ✅ Environment variables
- ✅ CORS configuration

### Soft Skills
- ✅ Full-stack thinking
- ✅ Product sense (UX decisions)
- ✅ Storytelling (personal project)

---

## 💡 Varianti Avanzate (Post-MVP)

Una volta che il core funziona, puoi aggiungere:

**V2 Features:**
- [ ] User accounts (salvare preferenze)
- [ ] History delle raccomandazioni passate
- [ ] "Watchlist" dove l'utente può salvare film
- [ ] Integrazione con streaming services (dove guardare il film)
- [ ] Social: condividi la tua raccomandazione su Twitter

**V3 Features:**
- [ ] RAG con vector DB (Chroma) - salva tutte le tue note sui film
- [ ] Chat interface: "Dimmi un film come Inception ma più breve"
- [ ] Multi-language (Italiano + English)

---

## 📊 Metrics per Colloqui

Quando presenti il progetto, puoi dire:

> "Ho costruito un AI movie recommender full-stack integrato nel mio sito personale:
> - **Backend**: FastAPI + OpenAI API per recommendations personalizzate
> - **Frontend**: React con UI responsive
> - **API**: TMDB per 500k+ film
> - **Deploy**: Live su [tuo-dominio.com/interests]
> - **Performance**: <2s response time, caching per ridurre API costs
> - **Users**: Testato da 20+ amici, 95% feedback positivo"

---

## 🚀 Next Steps Immediati

**Questa settimana:**
1. ✅ Finisci esercizi 1.13 - 1.22 (ancora ~10 esercizi per completare fundamentals)
2. ✅ Setup TMDB API key (gratis su themoviedb.org)
3. ✅ Setup OpenAI/Anthropic API key

**Week 4:**
1. Inizia Phase 1 - Backend MVP
2. Crea repo GitHub: `cinema-mood-recommender`
3. Setup project structure

**Week 5-6:**
1. Completa backend
2. Integra frontend nel tuo sito
3. Testing

**Week 7:**
1. Deploy
2. Documentation
3. LinkedIn post 🎉

---

## 📝 Domande da Decidere Ora

1. **LLM provider (FREE OPTIONS):**
   
   **⭐ CONSIGLIATO: Groq** (API gratuita + velocissima)
   - **Pro**: API gratuita, 30 req/min, velocissima (300+ tokens/sec), Llama 3.1 70B gratis
   - **Con**: Free tier ha rate limits
   - **Setup**: Registrati su groq.com, prendi API key, 2 minuti
   - **Code**: Compatibile con OpenAI SDK (cambi solo l'endpoint)
   
   **Alternativa 1: Together.ai** (Free tier generoso)
   - Free $25 credits al mese
   - Molti modelli: Llama 3.1, Mixtral, Qwen
   - Buona velocità
   
   **Alternativa 2: Ollama** (100% locale, 0 costi)
   - **Pro**: Zero costi, privacy totale, offline
   - **Con**: Devi hostare tu (serve GPU o CPU potente), più lento
   - **Best for**: Testing locale, poi switch a Groq per production
   
   **Alternativa 3: Hugging Face Inference API** (Free tier)
   - Free tier limitato ma sufficiente per demo
   - Molti modelli disponibili
   
   **❌ Da evitare ora**: OpenAI ($$$), Anthropic ($$$)

2. **Dove deployare backend?**
   - **Render** (facile, free tier generoso) ✅ CONSIGLIATO
   - Railway (simile)
   - Fly.io (più configurabile)

3. **Database:**
   - Per MVP: **SQLite** (semplice, no setup)
   - Per V2: PostgreSQL (se aggiungi user accounts)

4. **Caching:**
   - Per MVP: **in-memory Python dict** (semplice)
   - Per V2: Redis

---

**Pronto a partire? Vuoi che ti aiuti con qualche decisione o vuoi iniziare subito con il setup del backend?** 🚀
