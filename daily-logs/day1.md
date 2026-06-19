# Day 1 — What is Generative AI + Causal & Multi-Head Attention

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)
 
## What I built / learned
Kicked off the 50-day challenge. Explained the core distinction between
traditional ML (predicting labels) and Generative AI (creating new data
by learning the underlying distribution). Broke down the three building
blocks of GenAI — tokens, embeddings, and attention — and showed real
PyTorch implementations of CausalSelfAttention and MultiHeadCausalAttention
from my MiniGPT project.
 
## Key insight
The `masked_fill` with `float("-inf")` is what enforces causality in
self-attention. Future positions get set to negative infinity before
softmax, which forces their attention weight to zero. That single line
is what makes autoregressive generation possible — every token can only
"see" what came before it.
 
 
## Notebook
N/A — code shown is from the existing MiniGPT repo:
github.com/Vivek-afk81/mini-gpt-research-framework
 


