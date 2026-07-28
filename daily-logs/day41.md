# Day 41 — Comparing Reasoning Recovery Strategies Across Three LLMs

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## What I built / learned
Compared how three language models responded to the same reasoning-order perturbation instead of evaluating them by accuracy alone. Analyzed response traces and identified three distinct behaviors: Llama-8B explicitly detected and repaired broken reasoning sequences, Ministral-8B ignored the provided steps and solved problems independently, and Qwen-27B silently reconstructed the correct logical order while preserving the original step labels. Also refined the recovery-language detection methodology after discovering that the initial keyword set significantly underestimated Llama's successful recovery attempts.

## Key insight
Identical accuracy scores can conceal fundamentally different reasoning strategies. Inspecting response behavior—not just final answers—is essential for understanding how models actually process disrupted reasoning.

Behavioral analysis performed on the completed CoT robustness experiments by comparing response patterns from Llama-8B, Ministral-8B, and Qwen-27B under reasoning-order perturbations.