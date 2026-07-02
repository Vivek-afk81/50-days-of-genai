# Day 20 — Recap: Days 11–19
 
## Daily Log
 
### What this recap covers
Days 11–19 of the #50DaysOfGenAI challenge. This phase moved from
foundations (Days 1–10) into actual building — a deployed RAG chatbot,
an LLM agent, evaluation metrics, chunking experiments, and a decision
framework for fine-tuning vs RAG.
 
### What was shipped in Days 11–19
 
| Day | What shipped |
|---|---|
| 11 | Structured LLM outputs — TypedDict, Pydantic, JSON Schema |
| 12 | PDF RAG chatbot — PyMuPDF + FAISS cosine similarity + Qwen 2.5 7B |
| 13 | BLEU/ROUGE/BERTScore comparison — 6 test cases, original data |
| 14 | Runtime chunking experiment — small/medium/large, blizzard example |
| 15 | Gradio UI — source citations, search mode, chunk switching |
| 16 | ReAct concept — Yao et al. ICLR 2023 paper |
| 17 | LangChain ReAct agent — 1/3 queries clean, 2 documented failures |
| 18 | 3 chunking strategies — fixed/sentence/semantic on same document |
| 19 | Fine-tuning vs RAG decision framework — concept day |
 
### The single most important finding across Days 11–19
Semantic chunking produced 982 chunks averaging 79 characters from the
same document that fixed chunking handled in 99 chunks. More chunks
destroyed retrieval quality — each chunk lost the surrounding context
needed to actually answer. This directly contradicts the intuition that
more granular = better retrieval.

---
*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*