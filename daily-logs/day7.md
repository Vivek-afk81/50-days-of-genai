# Day 7 / 50 — What is RAG and Why it Matters

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## The Problem (see Day 6)

Yesterday I built a custom dataset and proved FLAN-T5 fabricates confident answers for things that don't exist. Today I built the fix.

But first — without RAG, this is what the model thought about One Piece:

> **"What is the One Piece treasure?"** → *"a samurai sword"*
> **"Who are the Straw Hat Pirates?"** → *"Scottish pirates"*

Confident. Specific. Completely wrong. This is exactly the failure mode RAG is designed to solve.

---

## What is RAG?

**Retrieval-Augmented Generation (RAG)** is the process of giving an LLM access to an external knowledge source at query time — before it generates an answer — instead of relying purely on what it memorized during training.

The analogy that makes it click:
> *"Imagine asking ChatGPT about One Piece, but it hasn't read the manga in years. It remembers some things, forgets others, and fills the gaps with confident nonsense. RAG lets it open the relevant chapter notes before answering."*

**LLMs have amnesia. RAG gives them a cheat sheet.**

---

## Why RAG Matters

| Problem | RAG Solution |
|---|---|
| LLMs hallucinate / fabricate | Answers grounded in retrieved real documents |
| Training data goes stale | Retrieval source can be updated anytime |
| Retraining is expensive | No retraining needed — just update the knowledge base |
| Private data can't be baked into public models | RAG works with any document, including proprietary ones |

---

## What I Built

A simple complete RAG pipeline over the One Piece Wikipedia article using FAISS + sentence-transformers + FLAN-T5.

### RAG Workflow

```
User Question
    ↓
Embed question → 384-dimensional vector
    ↓
FAISS similarity search over 87 chunk embeddings
    ↓
Retrieve top-3 most relevant chunks
    ↓
Build grounded prompt: "Use only the context below to answer..."
    ↓
FLAN-T5 generates answer from context
    ↓
Grounded Answer
```

---

## Implementation

### 1. Scrape + Chunk the Knowledge Base

```python
import wikipedia

wikipedia.set_lang("en")
page = wikipedia.page("One Piece", auto_suggest=False)
text = page.content

def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks

chunks = chunk_text(text)
print("Total chunks:", len(chunks))  # 87
```

### 2. Embed + Index with FAISS

```python
from sentence_transformers import SentenceTransformer
import faiss

embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
chunk_embeddings = embedding_model.encode(chunks, convert_to_numpy=True)
# Shape: (87, 384)

index = faiss.IndexFlatL2(chunk_embeddings.shape[1])
index.add(chunk_embeddings)
```

### 3. Retrieve Relevant Chunks

```python
def retrieve(query, k=3):
    query_embedding = embedding_model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, k)
    return [chunks[i] for i in indices[0]]
```

### 4. Generate Grounded Answer

```python
prompt = f"""
Use only the context below to answer the question.
Context  : {context}
Question : {question}
Answer   :
"""

rag_answer = generate_answer(prompt)
```

---

## Before vs After RAG

| Question | Without RAG | With RAG |
|---|---|---|
| What is the One Piece treasure? | a samurai sword (wrong) | Grounded answer from Wikipedia  |
| Who are the Straw Hat Pirates? | Scottish pirates (wrong) | Correct context retrieved  |

The key instruction that makes RAG work:
> *"Use only the context below to answer the question."*

That single line forces the model to answer from retrieved knowledge instead of fabricated memory.

---

## Numbers

- Wikipedia article → **87 chunks** of 500 characters each
- Embedding model: `all-MiniLM-L6-v2` → **384-dimensional vectors**
- Vector store: **FAISS IndexFlatL2**
- Generator: **google/flan-t5-base**
- Retrieval: top-**3** most similar chunks per query

---

## Tech Stack

| Tool | Purpose |
|---|---|
| `wikipedia` | Knowledge source scraping |
| `sentence-transformers` | Chunk + query embedding |
| `FAISS` | Fast vector similarity search |
| `google/flan-t5-base` | Answer generation |

---

## What I Learned

- The chunking strategy matters more than it seems — 500-char fixed chunks are fast to implement but can split mid-sentence, losing semantic context. Day 17 will go deeper on chunking strategies.
- The prompt instruction "Use **only** the context below" is doing heavy lifting — without it, the model mixes retrieved context with its own (wrong) prior knowledge.
- FAISS `IndexFlatL2` does exact nearest-neighbor search — fine for 87 chunks, but won't scale to millions. Day 8 will compare FAISS vs ChromaDB for larger corpora.
- RAG doesn't eliminate hallucination — if the retrieved chunks don't contain the answer, the model can still fabricate. Retrieval quality is the bottleneck.

---

## Connection to the Research Experiment

Day 6 showed the fabrication problem. Day 7 shows the standard fix. Starting Day 26, the experiment asks: even when you give an LLM a structured reasoning chain (CoT), does the *order* of those reasoning steps affect whether it stays grounded — or drifts back into fabrication?

---

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*