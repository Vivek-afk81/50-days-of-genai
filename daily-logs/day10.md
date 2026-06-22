# Day 10 / 50 — Phase 1 Recap
 
> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)
 
## 10 Days. 9 Builds. 1 Recap.
 
---
 
## Phase 1 — What I Built (Days 1–9)
 
| Day | Topic | Key Result |
|---|---|---|
| 1 | Causal self-attention + multi-head attention from scratch | `masked_fill(-inf)` is the entire secret of autoregressive generation |
| 2 | Word2Vec embeddings + vector arithmetic | king - man + woman = queen (0.71 similarity) |
| 3 | Interactive Transformer Attention Explorer | 72 attention views of one sentence across 6 layers × 12 heads |
| 4 | Zero-shot vs Few-shot vs CoT on Llama 3.1 8B | Prompting strategy only reveals itself on ambiguous questions |
| 5 | Decoding strategies from raw GPT-2 logits | Same distribution → 5 different words depending on the rule |
| 6 | Hallucination benchmark (30 questions, 5 categories) | 26.67% fabrication rate; Mars City population: 87,020 |
| 7 | RAG pipeline over One Piece Wikipedia | Samurai sword → correct answer |
| 8 | FAISS vs ChromaDB benchmark (10k vectors) | 4,776x speed gap — infrastructure difference, not intelligence |
| 9 | LangChain prompt templates (all 4 levels) | Prompt templates are the grammar of LLM communication |
 
---
 
## The Numbers That Mattered
 
- `4,776x` — FAISS search speed advantage over ChromaDB
- `26.67%` — fabrication rate on a 30-question benchmark
- `87,020` — FLAN-T5's confident invented population of Mars City
- `72` — attention pattern views inside one sentence (6 layers × 12 heads)
- `king - man + woman = queen` — geometry of meaning
---
 
## What's Next
 
**Phase 2 (Days 11–21):** RAG chatbot over a PDF,deployment, ReAct agent from scratch, LoRA fine-tuning, evaluation metrics.
 
 ---
 
*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*