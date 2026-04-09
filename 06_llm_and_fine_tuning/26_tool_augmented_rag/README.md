# Tool-Augmented RAG

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system enhanced with external tools such as a calculator to handle queries requiring computation and reasoning.

## What This Project Does
- Detects when a query requires tool usage
- Uses a calculator for numerical computation
- Performs semantic retrieval for factual information
- Combines tool outputs with retrieved context

## Problem
Standard RAG systems cannot handle:
- Mathematical calculations
- Logical computations
- External reasoning tasks

## Approach
1. Analyze query
2. Trigger tool if required
3. Retrieve relevant documents
4. Combine results
5. Generate final answer

## Tech Stack
- sentence-transformers
- scikit-learn
- pandas
- numpy
