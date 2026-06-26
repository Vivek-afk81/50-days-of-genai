# Day 14 / 50 — RAG Chatbot: Chunk Mode + Semantic Search

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## What I Added

Two new features to the Day 12 PDF RAG chatbot — no UI, pure functionality:

- **`chunk` command** — switch chunk size at runtime, FAISS index rebuilds instantly
- **`search` command** — pure semantic search mode to inspect retrieved chunks before the LLM sees them

---

## The Experiment That Made It Real

Same question, same PDF, same model — three chunk sizes:

```
Ask: How did Eunice find her way back during the blizzard?

small  (300 chars,  315 chunks) → "I cannot find that information in the document."
medium (1000 chars,  99 chunks) → "Eunice found her way back by following the sound of a chicken." ✅
large  (2000 chars,  47 chunks) → "I cannot find that information in the document."
```

**Why small failed:** the story was split mid-sentence across chunk boundaries — the relevant passage never appeared in any single retrieved chunk.

**Why large failed:** the relevant passage got buried inside a 2000-char chunk alongside unrelated content — retrieval ranked other chunks higher.

**Why medium worked:** the passage fit cleanly within one chunk, retrieved as the top result.

---

## Chunk Size Comparison

| Mode | chunk_size | Chunks | Avg chars |
|---|---|---|---|
| small | 300 | 315 | 300 |
| medium | 1000 | 99 | 993 |
| large | 2000 | 47 | 1968 |

PDF: `book-of-short-stories.pdf` — 78,711 characters extracted via PyMuPDF.

---

## Key Additions to main.py

```python
# Runtime chunk switching
if question.lower() == "chunk":
    # show options, rebuild FAISS index with new chunk size
    pass

# Semantic search mode
if question.lower() == "search":
    # embed query, retrieve top-k, print raw chunks (no LLM)
    pass
```

The `search` command is a debugging tool — see exactly what context the LLM is working with before you blame the model for a bad answer.

---

## What I Learned

- Chunk size is not a config detail — it determines whether retrieval works at all
- `search` mode revealed that small chunks retrieved partial sentences with high similarity scores but zero useful context
- Runtime index rebuilding (re-encode + re-add to FAISS) is fast enough for a dev tool — ~2s for 315 chunks on CPU
- The right chunk size depends on the document structure — short stories need medium; dense technical docs may need large

---

## Connection to the Roadmap

- **Day 12** → built the base RAG chatbot (1000-char fixed chunks, cosine similarity, Qwen 2.5 7B)
- **Day 14** → chunk mode + semantic search added
- **Day 17** → chunking strategies deep dive (fixed vs sentence vs semantic)

---

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*