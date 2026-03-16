# Zero-Shot vs Few-Shot Text Classification using LLMs

This project demonstrates how Large Language Models (LLMs) can perform text classification without traditional training by using prompt-based approaches.

## Overview

Two techniques are explored:

### Zero-Shot Learning

The model classifies text using only task instructions, without seeing any examples.

### Few-Shot Learning

The model is provided with a small number of labeled examples in the prompt to guide its predictions.

## Objective

To understand how examples in prompts influence model behavior and improve task performance without retraining the model.

## Key Concepts

* Prompt Engineering
* Zero-shot Learning
* Few-shot Learning
* Transformer-based Language Models
* Instruction Following

## Implementation

The notebook uses pretrained transformer models from Hugging Face to perform classification using both approaches and compares their outputs.

## Libraries Used

* transformers
* torch

## Outcome

Demonstrates the effectiveness of prompt-based learning and highlights the difference between zero-shot and few-shot performance in LLMs.
