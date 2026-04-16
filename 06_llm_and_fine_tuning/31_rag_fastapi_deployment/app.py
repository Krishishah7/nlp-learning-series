from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
from sentence_transformers import util
import uvicorn

# -----------------------------
# Initialize App
# -----------------------------
app = FastAPI()

# -----------------------------
# Data
# -----------------------------
documents = [
    "Elon Musk founded SpaceX.",
    "SpaceX works on rockets and space exploration.",
    "Tesla builds electric cars.",
    "Elon Musk is CEO of Tesla."
]

df = pd.DataFrame({"text": documents})

# -----------------------------
# Model Loader (Lazy Loading)
# -----------------------------
model = None

def get_model():
    global model
    if model is None:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

# -----------------------------
# Memory
# -----------------------------
feedback_memory = []

# -----------------------------
# Request Schema
# -----------------------------
class QueryRequest(BaseModel):
    query: str

# -----------------------------
# Retrieval
# -----------------------------
def retrieve(query, k=2):
    model = get_model()

    doc_embeddings = model.encode(df["text"].tolist())
    query_embedding = model.encode(query)

    scores = util.cos_sim(query_embedding, doc_embeddings)[0]
    scores = scores.cpu().numpy() if hasattr(scores, "cpu") else np.array(scores)

    top_idx = np.argsort(-scores)[:k]
    return df.iloc[top_idx], scores[top_idx]

# -----------------------------
# Answer Extraction
# -----------------------------
def extract_answer(query):
    model = get_model()

    answers = ["Elon Musk", "SpaceX", "Tesla"]
    answer_embeddings = model.encode(answers)

    query_embedding = model.encode(query)
    scores = util.cos_sim(query_embedding, answer_embeddings)[0]
    scores = scores.cpu().numpy() if hasattr(scores, "cpu") else np.array(scores)

    return answers[np.argmax(scores)]

# -----------------------------
# Confidence
# -----------------------------
def get_confidence(scores):
    score = float(scores[0])

    if score > 0.7:
        return "High", score
    elif score > 0.5:
        return "Medium", score
    else:
        return "Low", score

# -----------------------------
# Tool
# -----------------------------
def needs_calculation(query):
    return any(op in query for op in ["+", "-", "*", "/"])

def calculator(expr):
    try:
        return str(eval(expr))
    except:
        return None

# -----------------------------
# Feedback
# -----------------------------
def check_feedback(query):
    for q, ans in feedback_memory:
        if q.lower() == query.lower():
            return ans
    return None

# -----------------------------
# API Endpoint
# -----------------------------
@app.post("/ask")
def ask_question(request: QueryRequest):
    query = request.query

    # Feedback
    learned = check_feedback(query)
    if learned:
        return {"answer": learned, "confidence": "High"}

    # Tool
    tool_output = None
    if needs_calculation(query):
        expr = "".join([c for c in query if c in "0123456789+-*/"])
        tool_output = calculator(expr)

    # Retrieval
    docs, scores = retrieve(query)

    # Answer
    answer = extract_answer(query)

    # Confidence
    conf, score = get_confidence(scores)

    # Combine answers
    final_answer = answer
    if tool_output:
        final_answer = f"Calculation result: {tool_output}, Answer: {answer}"

    return {
        "query": query,
        "answer": final_answer,
        "confidence": conf,
        "score": score,
        "tool_output": tool_output
    }

# -----------------------------
# Run (for Render)
# -----------------------------
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=10000)