# Self-Improving RAG with Feedback Loop

## Overview
This project implements a feedback loop in a Retrieval-Augmented Generation (RAG) system, enabling it to learn from incorrect predictions and improve over time.

## What This Project Does
- Stores incorrect predictions and correct answers
- Uses feedback memory to improve future responses
- Overrides incorrect answers based on past mistakes

## Problem
Standard RAG systems do not learn from mistakes and repeat errors.

## Approach
1. Run RAG system
2. Compare with ground truth
3. Store incorrect predictions
4. Use feedback memory for future queries

## Tech Stack
- sentence-transformers
- pandas
- numpy
