# Day 15 / 50 — RAG Chatbot: Gradio UI

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## What I Built

A full Gradio UI wrapping the terminal RAG pipeline from Days 12 and 14 — PDF upload, live chunk switching, chat + search modes, and source citations on every answer.

---

## UI Features

| Feature | Detail |
|---|---|
| PDF upload | Any PDF, drag and drop, processes instantly |
| Chunk size selector | Small (300) / Medium (1000) / Large (2000) |
| Rebuild index | Re-chunks + re-indexes live without restarting |
| Stats panel | Total chunks, dimensions, chunk size, avg chars |
| Comparison table | All 3 presets shown side by side after upload |
| Chat mode | Q&A with grounded answers from retrieved context |
| Search mode | Pure semantic search — inspect retrieved chunks directly |
| Source citations | Every answer shows which chunk IDs were used |
| Clear chat | One button, resets conversation history |

---

## Source Citations

Every answer includes chunk pill labels:

```
Sources: chunk 276   chunk 439   chunk 275
```

This is non-trivial — without source citations there's no way to distinguish a retrieval-grounded answer from a hallucinated one. Citing sources forces transparency about what the model actually read.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Gradio 6 | UI framework |
| `gr.Chatbot` (messages format) | Multi-turn chat with role dicts |
| `gr.File` (type="filepath") | PDF upload |
| FAISS IndexFlatIP | Cosine similarity vector search |
| `all-MiniLM-L6-v2` | Chunk + query embedding |
| Qwen 2.5 7B (HF Inference API) | Answer generation |
| PyMuPDF | PDF text extraction |

---

## Project Structure

```
RAG_chatbot/
├── app.py              ← Gradio UI (Day 15)
├── main.py             ← Terminal interface (Day 14)
├── rag/
│   ├── loader.py       ← PDF extraction
│   ├── chunker.py      ← Chunking + CHUNK_PRESETS
│   ├── embedder.py     ← FAISS index build + query
│   └── search.py       ← semantic_search + answer_question
├── data/
│   └── book-of-short-stories.pdf
└── .env                ← HF_TOKEN
```

---

## What I Learned

- Gradio 6 uses `{"role": ..., "content": ...}` dicts for chatbot history — older tuple format breaks silently
- `gr.File(type="filepath")` returns the path string directly in Gradio 6 — no `.name` attribute needed
- Separating UI (`app.py`) from logic (`rag/`) made the codebase dramatically cleaner and each module independently testable
- Source citation requires storing chunk text in state and reverse-looking up the index — worth the extra 5 lines

---

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*