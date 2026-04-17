# RAG Guardrails and Safety Layer

## Overview
This project enhances a Retrieval-Augmented Generation (RAG) system by adding guardrails to control responses based on confidence and query validation.

## Features
- Rejects low-confidence queries
- Handles out-of-scope questions
- Prevents hallucinated responses
- Adds fallback responses

## How It Works
Query → Retrieval → Confidence Check → Guardrail Decision → Final Response

## Tech Stack
- Python
- numpy
- pandas
