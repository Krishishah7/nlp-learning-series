# Conversational RAG with Memory

## Overview
This project implements a conversational Retrieval-Augmented Generation (RAG) system that maintains memory of previous interactions to answer follow-up queries more accurately.

## What This Project Does
- Stores conversation history
- Uses past queries and answers for context
- Improves understanding of follow-up questions
- Enables multi-turn interactions

## Problem
Standard RAG systems treat each query independently and fail to understand conversational context.

## Approach
1. Store previous interactions
2. Combine history with current query
3. Perform semantic retrieval
4. Generate context-aware answers

## Tech Stack
- sentence-transformers
- scikit-learn
- pandas
- numpy
