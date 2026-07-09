# Day 26 — Chain-of-Thought Prompting

## What I built / learned

Today I explored **Chain-of-Thought (CoT) prompting**, a prompting technique that encourages an LLM to generate intermediate reasoning steps before producing the final answer.

Unlike standard prompting, which asks directly for the answer, CoT makes the reasoning process explicit. This has been shown to improve performance on many multi-step reasoning tasks such as arithmetic, logical reasoning, and question answering.

Example:

**Question**

Janet has 16 eggs. She uses 7 for baking. She sells the rest at \$2 each. How much does she make?

**Direct Prompt**

Answer: **\$18**

**Chain-of-Thought**

1. Janet has 16 eggs.
2. She uses 7, so 16 − 7 = 9 remain.
3. She sells 9 eggs at \$2 each.
4. 9 × 2 = \$18.
5. Answer: **\$18**

Both approaches produce the correct answer.

The key difference is that CoT exposes a reasoning trace that can be inspected and analyzed.

## Key Insight

Most research asks whether Chain-of-Thought improves reasoning.

A question that receives much less attention is:

> **Does the order of the reasoning steps actually matter?**

If the reasoning steps are shuffled or reversed while containing the same information, will the model still reach the correct answer?

This question will be the focus of my upcoming multi-day experiment using the GSM8K benchmark.

## Technologies Used

- Python
- Groq API
- Llama 3.1 8B Instant
- Prompt Engineering

## Next Steps

Beginning tomorrow, I'll evaluate the model on GSM8K under multiple reasoning conditions:

- Original Chain-of-Thought
- Reversed Chain-of-Thought
- Shuffled Chain-of-Thought
- Randomized reasoning order

The goal is to understand whether LLMs truly follow the logical dependency between reasoning steps or rely primarily on pattern recognition.

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*