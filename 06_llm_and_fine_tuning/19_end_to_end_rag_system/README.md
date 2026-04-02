# End-to-End RAG System

This project demonstrates a complete Retrieval-Augmented Generation (RAG) system integrating retrieval, reasoning, and an interactive user interface.

---

## 📌 Overview

The system processes user queries through multiple stages including query rewriting, hybrid retrieval, and answer generation. It also provides a user-friendly interface using Gradio for real-time interaction.

---

## 🧩 Components

### 🔹 RAG Pipeline (`end_to_end_rag_pipeline.ipynb`) 

Implements the core system:

* Query rewriting
* Hybrid retrieval (TF-IDF + embeddings)
* Top-K document selection
* Context-based answer generation

---

### 🔹 Gradio UI (`rag_ui_gradio.ipynb`)

Provides an interactive interface:

* Users can input queries
* System retrieves relevant context
* Generates answers in real-time

---

## 🧠 System Flow

User Query
→ Query Rewriting
→ Hybrid Retrieval
→ Context Selection
→ Answer Generation
→ Display via UI

---

## 🎯 Objective

To build a production-style AI system that combines backend intelligence with a user-facing interface for real-world usability.

---

## ⚙️ Libraries Used

* sentence-transformers
* transformers
* scikit-learn
* gradio
* numpy

---

## 🚀 How to Run

1. Open the notebook in Google Colab
2. Run all cells
3. The Gradio interface will launch automatically
4. Enter a query and view the generated answer

---

## 💡 Notes

* The UI runs using Gradio and generates a temporary public link
* GitHub does not render interactive UI — run locally or in Colab to use it

---

## 🏆 Outcome

A complete AI application demonstrating how modern RAG systems are built with:

* Retrieval
* Generation
* User interaction

This project reflects real-world system design used in production AI applications.
