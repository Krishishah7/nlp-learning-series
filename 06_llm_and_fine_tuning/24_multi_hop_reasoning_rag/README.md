# Multi-Hop Reasoning in RAG

## Overview
This project implements a multi-hop reasoning mechanism in a Retrieval-Augmented Generation (RAG) system to answer complex questions that require combining information from multiple documents.

Unlike standard RAG systems, this approach performs iterative retrieval and reasoning across multiple steps.

## What This Project Does
- Performs multi-step retrieval
- Connects information across documents
- Generates follow-up queries
- Produces final answer using combined context

## Problem
Standard RAG fails when answers require:
- Multiple documents
- Logical reasoning
- Step-by-step inference

## Approach
1. Initial Retrieval
2. Extract missing information
3. Generate follow-up query
4. Retrieve additional documents
5. Combine context
6. Generate final answer

## Tech Stack
- sentence-transformers
- transformers
- scikit-learn
- pandas
- numpy
