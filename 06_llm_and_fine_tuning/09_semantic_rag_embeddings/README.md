# Semantic Retrieval-Augmented Generation

This project implements a semantic RAG pipeline using sentence embeddings to retrieve context based on meaning rather than keyword matching.

## Overview

Documents and queries are converted into vector representations. Cosine similarity is used to retrieve the most relevant document, which is then supplied to the language model to generate an answer.

## Objective

To demonstrate how semantic search improves retrieval quality and forms the foundation of modern vector-based RAG systems.

## Key Concepts

* Sentence Embeddings
* Semantic Search
* Cosine Similarity
* Retrieval-Augmented Generation

## Libraries Used

* sentence-transformers
* transformers
* scikit-learn
* sentencepiece
* torch

## Outcome

Shows that embedding-based retrieval can find relevant context even when exact keywords differ.
