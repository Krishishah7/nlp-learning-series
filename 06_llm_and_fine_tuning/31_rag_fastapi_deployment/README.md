# RAG API Deployment using FastAPI

## Overview
This project deploys a production-level Retrieval-Augmented Generation (RAG) system as a FastAPI service.

## Features
- Query-based API endpoint
- Answer generation with confidence scoring
- Tool integration (calculator)
- Feedback learning system

## How to Run

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## API Endpoint

### POST /ask

This endpoint accepts a query and returns an answer with confidence score.

---

### Example Request

```json
{
  "query": "What is 25*4 and which company works on rockets?"
}
