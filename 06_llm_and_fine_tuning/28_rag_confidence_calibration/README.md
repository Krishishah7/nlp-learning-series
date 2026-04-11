# RAG Confidence Calibration

## Overview
This project enhances a Retrieval-Augmented Generation (RAG) system by introducing confidence calibration to measure answer reliability and improve decision-making.

## What This Project Does
- Computes similarity-based confidence scores
- Categorizes answers into high, medium, and low confidence
- Provides explanation for answer reliability

## Problem
Basic confidence thresholds are insufficient and do not provide insight into how reliable an answer is.

## Approach
1. Retrieve documents
2. Compute similarity scores
3. Derive confidence score
4. Categorize confidence levels
5. Provide explanation

## Tech Stack
- sentence-transformers
- numpy
- pandas
- scikit-learn
