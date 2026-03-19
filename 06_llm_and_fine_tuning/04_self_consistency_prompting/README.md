# Self-Consistency Prompting

This project demonstrates the Self-Consistency technique for improving reasoning reliability in Large Language Models.

## Overview

Chain-of-Thought prompting generates step-by-step reasoning but may produce inconsistent answers. Self-consistency improves results by generating multiple reasoning paths and selecting the most common final answer.

## Objective

To show how sampling multiple solutions and applying majority voting increases answer stability and accuracy.

## Key Concepts

* Chain-of-Thought Prompting
* Self-Consistency
* Probabilistic Sampling
* Majority Voting

## Libraries Used

* transformers
* torch
* accelerate
* sentencepiece

## Outcome

Demonstrates that aggregating multiple reasoning outputs can yield more reliable final answers than relying on a single model response.
