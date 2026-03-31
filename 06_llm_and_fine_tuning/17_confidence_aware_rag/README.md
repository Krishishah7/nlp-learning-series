# Confidence-Aware RAG

This project demonstrates how to incorporate confidence scoring into a Retrieval-Augmented Generation system to decide whether to answer or abstain.

## Overview

A confidence score is computed based on similarity score differences. If confidence is low, the system avoids answering to prevent hallucination.

## Objective

To build safer and more reliable RAG systems by introducing a decision layer before answer generation.

## Key Concepts

* Confidence Scoring
* Answer Validation
* Hallucination Prevention
* Retrieval-Augmented Generation

## Libraries Used

* sentence-transformers
* transformers
* faiss-cpu
* numpy
* scikit-learn

## Outcome

Demonstrates that adding a confidence threshold improves reliability by preventing low-confidence responses.
