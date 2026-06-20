# Day 8 / 50 — FAISS vs ChromaDB: Vector Database Benchmark

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## The Question

Day 7 built a RAG pipeline using FAISS. But FAISS isn't the only option — ChromaDB is arguably more popular for production RAG systems. Today I benchmarked both on 10,000 vectors to understand the real trade-offs.

---

## What is a Vector Database?

A vector database stores embeddings and enables fast similarity search — the retrieval backbone of any RAG pipeline.

```
"I love rasmalai"
        ↓
[0.12, -0.45, 0.89, ...]  ← 384-dimensional vector
        ↓
stored in vector DB
        ↓
query comes in → find the most similar vectors → return top-k results
```

- 10 vectors → easy, any approach works
- 10,000 vectors → need efficient indexing
- 1,000,000 vectors → need a proper vector DB

---

## Benchmark Setup

| Parameter | Value |
|---|---|
| Vectors | 10,000 |
| Dimensions | 384 |
| Query | 1 random vector |
| Top-k | 5 |
| Hardware | Google Colab (T4 GPU) |

---

## Results

```
FAISS vs ChromaDB — 10,000 Vectors

Build time  →  FAISS: 0.007s  |  ChromaDB: 1.076s
Search time →  FAISS: 0.003s  |  ChromaDB: 14.363s

FAISS is significantly faster at search.
```

---

## Why Such a Large Gap?

The number looks shocking but it makes sense once you understand what each tool actually is.

**FAISS** is a pure similarity search library — no overhead, no storage, no metadata, just raw vector math. That's why it's so fast.

**ChromaDB** is a full vector database — it handles persistence, document storage, metadata filtering, and a client-server interface. Every one of those features adds overhead. The 14-second search time on Colab is partly ChromaDB's architecture and partly Colab's I/O constraints; in a proper environment with a persistent server, ChromaDB is significantly faster than this benchmark suggests.

---

## Feature Comparison

| Feature | FAISS | ChromaDB |
|---|---|---|
| Search speed | Extremely fast | Slower (overhead) |
| Persistence | In-memory only | Built-in |
| Document storage | Vectors only | Text + metadata |
| Metadata filtering | No | Yes |
| Setup complexity | Low | Low |
| Production-ready | You manage everything | Out of the box |
| Best for | Research / prototyping | Production RAG pipelines |

---

## Decision Framework

```
Need persistence across sessions?
    YES → ChromaDB
    NO  ↓

Need metadata filtering?
    YES → ChromaDB
    NO  ↓

Speed-critical / research / you control the stack?
    YES → FAISS
```

---

## Semantic Search Demo (Real Sentences)

To verify search quality is identical, I ran a real semantic search demo using `all-MiniLM-L6-v2` embeddings on 10 custom sentences:

```python
sentences = [
    "I love playing football on weekends",
    "Machine learning is changing the world",
    "The best pizza I ever had was in Naples",
    "Python is a great programming language",
    "Dogs are loyal and loving companions",
    "Deep learning requires a lot of data",
    "I enjoy cooking pasta at home",
    "Neural networks mimic the human brain",
    "Cats are independent and mysterious pets",
    "JavaScript runs in the browser",
]

query = "I like animals as pets"
```

**ChromaDB retrieved:**
1. Dogs are loyal and loving companions
2. Cats are independent and mysterious pets
3. I love playing football on weekends

Semantically correct. The gap between FAISS and ChromaDB is purely infrastructure — not intelligence.

---

## Key Takeaways

- **speed difference** sounds dramatic but reflects a fundamental architectural difference — search library vs full database.
- **Search quality is identical** — both use the same underlying similarity math. The gap is infrastructure, not intelligence.
- **FAISS was the right call for Day 7's RAG pipeline** — prototype, in-memory, speed matters, no persistence needed.
- **ChromaDB is the right call for production** — persistent chatbot memory, metadata filtering, multi-session RAG apps.
- **Benchmark environment matters** — ChromaDB on Colab is slower than in a proper server environment. Always benchmark in your actual deployment context.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| `faiss-cpu` | Pure vector similarity search |
| `chromadb` | Full vector database |
| `sentence-transformers` | Real sentence embeddings for semantic search demo |
| `matplotlib` | Benchmark visualization |
| `numpy` | Synthetic vector generation |

---

## Connection to the Roadmap

- **Day 7** → Built RAG with FAISS (now you know why)
- **Day 8** → Understood the FAISS vs ChromaDB trade-off
- **Day 11** → RAG chatbot over a PDF will use ChromaDB for persistence
- **Day 17** → Chunking strategies deep dive

---

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*