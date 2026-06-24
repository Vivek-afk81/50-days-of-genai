# Day 12 / 50 — RAG Chatbot over a PDF
 
> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)
 
## What I Built
 
A terminal RAG chatbot that reads any PDF and answers questions about it — and explicitly says "I cannot find that information in the document" when the answer isn't there.
 
---
 
## Upgrades Over Day 7's RAG
 
| Feature | Day 7 | Day 12 |
|---|---|---|
| Knowledge source | Wikipedia scrape | Real PDF (PyMuPDF) |
| Chunking | Fixed 500 chars, no overlap | 1000 chars, 200 char overlap |
| Similarity metric | L2 distance (IndexFlatL2) | Cosine similarity (IndexFlatIP + normalized) |
| LLM | FLAN-T5 base (250M) | Qwen 2.5 7B via HF Inference API |
| Hallucination guard | None | Explicit fallback instruction |
| Interface | One-shot Q&A | Multi-turn chat loop |
 
---
 
## Architecture
 
```
PDF
  ↓
PyMuPDF → raw text
  ↓
Overlap chunking (1000 chars, 200 overlap)
  ↓
all-MiniLM-L6-v2 → normalized embeddings
  ↓
FAISS IndexFlatIP (cosine similarity)
  ↓
User query → embed → search top-5 chunks
  ↓
Context + question → Qwen 2.5 7B
  ↓
Grounded answer (or honest "I don't know")
```
 
---
 
## Key Implementation Details
 
### Overlap Chunking
```python
def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks
```
The 200-char overlap ensures context isn't cut mid-sentence at chunk boundaries — a common failure mode in basic RAG pipelines.
 
### Cosine Similarity via FAISS
```python
# Normalize embeddings first
embeddings = embedding_model.encode(chunks, normalize_embeddings=True)
 
# IndexFlatIP on normalized vectors = cosine similarity
index = faiss.IndexFlatIP(dimension)
index.add(vectors)
```
L2 distance (Day 7) measures geometric distance. Cosine similarity measures directional alignment — better for semantic matching where magnitude doesn't matter.
 
### Hallucination Guard
```python
prompt = f"""
Answer ONLY using the provided context.
 
If the answer is not present in the context, reply exactly:
"I cannot find that information in the document."
 
Context: {context}
Question: {question}
"""
```
That single instruction is what separates a RAG chatbot from a hallucination machine.
 
---
 
## Tech Stack
 
| Tool | Purpose |
|---|---|
| `pymupdf` | PDF text extraction |
| `sentence-transformers` | Chunk + query embedding |
| `faiss-cpu` | Cosine similarity vector search |
| `huggingface-hub` InferenceClient | Qwen 2.5 7B answer generation |
| `python-dotenv` | API key management |
 
---
 
## What I Learned
 
- Overlap chunking is a small change with noticeable impact — questions that would have hit a chunk boundary now retrieve proper context
- Cosine similarity via IndexFlatIP requires normalized embeddings — forget to normalize and the results are wrong with no error thrown
- The fallback prompt instruction is non-negotiable for production — without it the model fills gaps with confident hallucinations (see Day 6)
- Qwen 2.5 7B via HF Inference API is free and significantly better than FLAN-T5 for instruction-following tasks
---
 
## Connection to the Roadmap
 
- **Day 7** → Basic RAG with Wikipedia + FAISS L2 + FLAN-T5
- **Day 12** → Production-grade RAG with PDF + cosine similarity + Qwen 2.5 7B
- **Day 14** → Streamlit UI wrapping this same pipeline
- **Day 17** → Chunking strategies deep dive (fixed vs semantic vs sentence)
---
 
*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*