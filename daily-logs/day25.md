# Day 25 — Semantic Search vs Keyword Search vs Hybrid Search

## What I built / learned

Today I compared three popular retrieval approaches used in Retrieval-Augmented Generation (RAG):

- **BM25 (Keyword Search)**
- **Semantic Search** using `all-MiniLM-L6-v2`
- **Hybrid Search** using equal-weight score fusion

The experiment was conducted on the **BEIR FiQA** benchmark, which contains approximately **57,000 financial documents** and **500 evaluation queries**.

To evaluate each retrieval method, I used two common Information Retrieval metrics:

- **Recall@10** – Measures whether the correct document appears in the top 10 retrieved results.
- **MRR (Mean Reciprocal Rank)** – Measures how highly the first relevant document is ranked.

## Results

| Retriever | Recall@10 | MRR |
|------------|----------:|----:|
| BM25 | 0.227 | 0.240 |
| Semantic Search | **0.467** | **0.453** |
| Hybrid Search | 0.396 | 0.384 |

## Key Insight

I expected Hybrid Search to outperform Semantic Search.

Instead, **Semantic Search achieved the highest Recall@10 and MRR** in this experiment.

The takeaway isn't that hybrid retrieval is worse.

Rather, **a simple 50/50 score fusion is not automatically better**. If one retriever is significantly stronger than the other, combining both without tuning can actually reduce retrieval performance.

This experiment reinforced an important lesson:

> **Always evaluate retrieval methods on your own data instead of assuming a more complex approach will perform better.**

## Technologies Used

- Python
- Sentence Transformers
- all-MiniLM-L6-v2
- BM25
- NumPy
- BEIR FiQA Dataset

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*