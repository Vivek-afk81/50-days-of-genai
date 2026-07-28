# Day 42 — Measuring LLM Consistency Beyond Final Accuracy

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## What I built / learned
Built a reusable LLM consistency evaluation pipeline that measures response stability across multiple generations using three complementary metrics: semantic similarity (embedding-based), structural consistency (response length variation and final-answer agreement), and lexical diversity. Evaluated Llama 3.1 8B (Groq, temperature = 0.7) on a multi-step reasoning problem over 10 independent runs. While the model achieved a high semantic consistency score (0.914), the final-answer agreement was only 50%, demonstrating that highly similar reasoning traces can still produce inconsistent conclusions.

## Key insight
Semantic consistency and answer consistency measure different properties. A model can generate responses that appear nearly identical in wording and reasoning while still disagreeing with itself on the final answer, making embedding similarity alone an incomplete measure of reliability.

Implemented a reusable LLM consistency scorer that reports semantic similarity, structural consistency, lexical diversity, and final-answer agreement across multiple sampled generations.