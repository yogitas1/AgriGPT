# 🌾 AgriGPT - Intelligent Farming Advisory System

An Agentic RAG (Retrieval Augmented Generation) system that helps farmers get quick, accurate answers about citrus crop diseases and government agricultural schemes.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Intent Detection & Routing Logic](#intent-detection--routing-logic)
- [Vector Database Design](#vector-database-design)
- [Chunking Strategy](#chunking-strategy)
- [Deployment](#deployment)
- [Testing](#testing)
- [Challenges & Solutions](#challenges--solutions)
- [Future Improvements](#future-improvements)

## Overview

AgriGPT is an intelligent chatbot designed for farmers who need information about:

- **Citrus crop diseases**: Symptoms, identification, treatment, and prevention
- **Government schemes**: Subsidies, financial assistance, eligibility, and application processes
- **Combined queries**: How government schemes can help manage specific diseases

The system uses advanced NLP techniques to understand farmer intent, route queries to the appropriate knowledge base, and generate helpful, context-aware responses.

## Features

- 🧠 **Intelligent Intent Detection**: Automatically classifies queries as Disease, Scheme, or Hybrid
- 🔀 **Dynamic Query Routing**: Routes to appropriate knowledge base(s) using LangGraph
- 📚 **Dual Knowledge Bases**: Separate vector stores for diseases and government schemes
- 🎯 **Semantic Search**: Retrieves most relevant information using embeddings
- 💬 **Farmer-Friendly Responses**: Generates clear, actionable advice
- 📖 **Source Citations**: Includes references to source documents
- ⚡ **Fast API**: RESTful endpoint for easy integration

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              FastAPI Backend                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐                                                           │
│  │  POST /query │                                                           │
│  │   Endpoint   │                                                           │
│  └──────┬───────┘                                                           │
│         │                                                                   │
│         ▼                                                                   │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                    LangGraph State Machine                            │   │
│  │                                                                       │   │
│  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────────────────┐   │   │
│  │  │   START     │───▶│  Classify   │───▶│     Route by Intent     │   │   │
│  │  │             │    │   Intent    │    │                         │   │   │
│  │  └─────────────┘    └─────────────┘    └───────────┬─────────────┘   │   │
│  │                                                    │                 │   │
│  │                    ┌───────────────────────────────┼────────────┐    │   │
│  │                    │                               │            │    │   │
│  │                    ▼                               ▼            ▼    │   │
│  │         ┌──────────────────┐           ┌────────────────┐  ┌──────┐ │   │
│  │         │ Retrieve Disease │           │Retrieve Scheme │  │ Both │ │   │
│  │         │       KB         │           │      KB        │  │      │ │   │
│  │         └────────┬─────────┘           └───────┬────────┘  └──┬───┘ │   │
│  │                  │                             │              │     │   │
│  │                  └─────────────┬───────────────┴──────────────┘     │   │
│  │                                ▼                                     │   │
│  │                    ┌─────────────────────┐                          │   │
│  │                    │ Generate Response   │                          │   │
│  │                    │    (OpenAI GPT)     │                          │   │
│  │                    └──────────┬──────────┘                          │   │
│  │                               │                                      │   │
│  │                               ▼                                      │   │
│  │                    ┌─────────────────────┐                          │   │
│  │                    │        END          │                          │   │
│  │                    └─────────────────────┘                          │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                           Vector Databases (ChromaDB)                        │
│                                                                             │
│  ┌─────────────────────────────┐    ┌─────────────────────────────┐        │
│  │     disease_collection      │    │     scheme_collection       │        │
│  │                             │    │                             │        │
│  │  • Citrus diseases          │    │  • Government subsidies     │        │
│  │  • Pest management          │    │  • Financial assistance     │        │
│  │  • Treatment methods        │    │  • Eligibility criteria     │        │
│  │  • Prevention strategies    │    │  • Application processes    │        │
│  │                             │    │                             │        │
│  └─────────────────────────────┘    └─────────────────────────────┘        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend Framework** | FastAPI | REST API with automatic OpenAPI docs |
| **LLM** | OpenAI GPT-4 / GPT-3.5-turbo | Intent classification & response generation |
| **Embeddings** | OpenAI text-embedding-3-small | Document vectorization |
| **Vector Database** | ChromaDB | Local persistent vector storage |
| **Orchestration** | LangChain + LangGraph | Agent workflows & state management |
| **PDF Processing** | PyPDF | Document loading |
| **Language** | Python 3.9+ | Primary language |

## Prerequisites

Before you begin, ensure you have:

1. **Python 3.9 or higher**
   ```bash
   python --version  # Should be 3.9+
   ```

2. **OpenAI API Key**
   - Sign up at [platform.openai.com](https://platform.openai.com)
   - Create an API key
   - You'll need ~$2-5 for the hackathon

3. **Git** (for version control)
   ```bash
   git --version
   ```

4. **The PDF Documents**
   - `CitrusPlantPestsAndDiseases.pdf`
   - `GovernmentSchemes.pdf`

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/agrigpt.git
   cd agrigpt
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

5. **Add PDF documents**
   ```bash
   # Place your PDFs in the data/ directory
   mkdir -p data
   # Copy CitrusPlantPestsAndDiseases.pdf to data/
   # Copy GovernmentSchemes.pdf to data/
   ```

6. **Initialize the vector database**
   ```bash
   python scripts/ingest_documents.py
   ```

## Project Structure

```
agrigpt/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── config.py               # Configuration management
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py          # Pydantic models for request/response
│   ├── services/
│   │   ├── __init__.py
│   │   ├── intent_classifier.py    # Intent detection logic
│   │   ├── retriever.py            # Vector store retrieval
│   │   └── response_generator.py   # LLM response generation
│   ├── agents/
│   │   ├── __init__.py
│   │   └── query_router.py     # LangGraph workflow
│   └── utils/
│       ├── __init__.py
│       └── helpers.py          # Utility functions
├── scripts/
│   └── ingest_documents.py     # Document processing script
├── data/
│   ├── CitrusPlantPestsAndDiseases.pdf
│   └── GovernmentSchemes.pdf
├── chroma_data/                # Vector database storage
│   ├── disease_collection/
│   └── scheme_collection/
├── tests/
│   ├── __init__.py
│   ├── test_intent.py
│   ├── test_retrieval.py
│   └── test_api.py
├── .env.example
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── PROMPTS.md
└── render.yaml                 # Render deployment config
```

## Configuration

### Environment Variables

Create a `.env` file with the following:

```bash
# Required
OPENAI_API_KEY=sk-your-openai-api-key-here

# Optional - LangSmith tracing
LANGCHAIN_API_KEY=your-langsmith-key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=agrigpt

# Application settings
ENVIRONMENT=development
LOG_LEVEL=INFO
CHUNK_SIZE=800
CHUNK_OVERLAP=200
TOP_K_RESULTS=5
```

### Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | Required | Your OpenAI API key |
| `CHUNK_SIZE` | 800 | Number of tokens per document chunk |
| `CHUNK_OVERLAP` | 200 | Overlap between chunks |
| `TOP_K_RESULTS` | 5 | Number of similar documents to retrieve |

## Running the Application

### Development Mode

```bash
# Start the server with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Documentation

### POST /query

Main endpoint for farmer queries.

**Request:**
```json
{
  "question": "My citrus leaves are showing yellow blotchy patches. What could this be?"
}
```

**Response:**
```json
{
  "success": true,
  "intent": "disease",
  "answer": "The yellow blotchy patches on your citrus leaves could indicate Huanglongbing (HLB) or Citrus Greening disease...",
  "sources": [
    {
      "document": "CitrusPlantPestsAndDiseases.pdf",
      "page": 12
    }
  ]
}
```

### GET /health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

### Intent Types

| Intent | Description | Knowledge Base |
|--------|-------------|----------------|
| `disease` | Questions about pests, diseases, symptoms, treatment | Citrus Pests & Diseases |
| `scheme` | Questions about government programs, subsidies, eligibility | Government Schemes |
| `hybrid` | Questions combining both topics | Both knowledge bases |

## Intent Detection & Routing Logic

### How Intent Detection Works

The system uses an LLM-based classifier to analyze the user's query:

```python
# Intent classification prompt
INTENT_PROMPT = """
Analyze the following farmer's query and classify it into one of three categories:

1. DISEASE - Questions about plant diseases, pests, symptoms, treatment, prevention
2. SCHEME - Questions about government programs, subsidies, financial assistance
3. HYBRID - Questions that combine both (e.g., "What schemes help with disease X?")

Query: {query}

Respond with only one word: DISEASE, SCHEME, or HYBRID
"""
```

### Routing Logic (LangGraph)

```
START
  │
  ▼
┌─────────────────┐
│ classify_intent │ ──── Analyzes query using LLM
└────────┬────────┘
         │
         ▼
    ┌────┴────┐
    │  Route  │
    └────┬────┘
         │
    ┌────┼────┬────────────┐
    │    │    │            │
    ▼    ▼    ▼            ▼
DISEASE SCHEME HYBRID    ERROR
    │    │    │            │
    ▼    ▼    ▼            │
retrieve retrieve retrieve  │
disease  scheme   both     │
    │    │    │            │
    └────┴────┴────────────┘
              │
              ▼
       generate_response
              │
              ▼
            END
```

## Vector Database Design

### Why ChromaDB?

1. **Zero configuration** - Just install and use
2. **Persistent storage** - Survives application restarts
3. **LangChain integration** - Native support
4. **Fast for small datasets** - Perfect for ~100 pages of PDFs

### Collection Structure

**Disease Collection:**
```python
{
    "collection_name": "disease_kb",
    "embedding_function": OpenAIEmbeddings(model="text-embedding-3-small"),
    "metadata": {
        "source": "CitrusPlantPestsAndDiseases.pdf",
        "page": int,
        "chunk_id": str
    }
}
```

**Scheme Collection:**
```python
{
    "collection_name": "scheme_kb", 
    "embedding_function": OpenAIEmbeddings(model="text-embedding-3-small"),
    "metadata": {
        "source": "GovernmentSchemes.pdf",
        "page": int,
        "chunk_id": str
    }
}
```

## Chunking Strategy

### Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Chunk Size | 800 tokens | Balance between context and precision |
| Chunk Overlap | 200 tokens | Preserves context across chunk boundaries |
| Separator | Paragraph breaks | Maintains semantic coherence |

### Why These Values?

- **800 tokens**: Large enough to contain complete concepts (disease symptoms, scheme eligibility), small enough for precise retrieval
- **200 token overlap**: Ensures important information at chunk boundaries isn't lost
- **Paragraph-based splitting**: Keeps related information together

### Implementation

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=200,
    length_function=len,
    separators=["\n\n", "\n", ". ", " ", ""]
)
```

## Deployment

### Deploy to Render

1. **Create render.yaml** in project root:
   ```yaml
   services:
     - type: web
       name: agrigpt
       env: python
       buildCommand: pip install -r requirements.txt && python scripts/ingest_documents.py
       startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
       envVars:
         - key: OPENAI_API_KEY
           sync: false
         - key: PYTHON_VERSION
           value: 3.11.0
   ```

2. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

3. **Connect to Render**
   - Go to [render.com](https://render.com)
   - New → Web Service
   - Connect your GitHub repo
   - Add environment variables
   - Deploy!

### Live API URL

After deployment, your API will be available at:
```
https://agrigpt.onrender.com
```

## Testing

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_intent.py -v
```

### Manual Testing with cURL

```bash
# Health check
curl http://localhost:8000/health

# Disease query
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the symptoms of citrus canker?"}'

# Scheme query
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What subsidies are available for drip irrigation?"}'

# Hybrid query
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What government support is available for managing citrus greening disease?"}'
```

## Challenges & Solutions

### Challenge 1: Intent Ambiguity
**Problem:** Some queries could be interpreted as multiple intents.
**Solution:** Default to `hybrid` for ambiguous cases and retrieve from both knowledge bases.

### Challenge 2: Colloquial Language
**Problem:** Farmers may use local terms or misspellings.
**Solution:** Use semantic search which understands meaning, not just keywords.

### Challenge 3: Context Assembly
**Problem:** Retrieved chunks may have overlapping or contradictory information.
**Solution:** Include source citations and let the LLM synthesize coherent responses.

### Challenge 4: Response Length
**Problem:** Balancing comprehensive answers with readability.
**Solution:** Structure responses with numbered lists and clear sections for hybrid queries.

## Future Improvements

1. **Multi-language Support**: Add Hindi, Telugu, and other regional languages
2. **Voice Interface**: Allow farmers to speak queries
3. **Image Recognition**: Identify diseases from photos of affected plants
4. **Conversation Memory**: Multi-turn conversations with context retention
5. **Offline Mode**: Cache common queries for areas with poor connectivity
6. **Scheme Eligibility Calculator**: Interactive tool to check scheme eligibility
7. **Weather Integration**: Combine disease advice with local weather data
8. **Push Notifications**: Alert farmers about disease outbreaks in their region

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Anthropic for the hackathon opportunity
- OpenAI for the LLM and embedding APIs
- LangChain team for the excellent framework
- ChromaDB for the vector database

---

**Built with ❤️ for farmers**
