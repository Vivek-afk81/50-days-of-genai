# Day 16 / 50 — ReAct: Reasoning + Acting

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## Paper

**ReAct: Synergizing Reasoning and Acting in Language Models**
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
ICLR 2023 · [arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)

---

## The Problem ReAct Solves

Before ReAct, reasoning and acting were studied separately:

| Approach | Strength | Weakness |
|---|---|---|
| Chain-of-Thought | Reasons well, decomposes problems | Hallucinates facts, no grounding |
| Action-only (WebGPT) | Can interact with environments | No strategic planning |
| **ReAct** | **Reasons + acts in one loop** | **Best of both** |

---

## The Core Idea

Instead of generating one answer, the model interleaves three steps repeatedly:

```
Thought    → reason about the current state
Action     → call a tool (search, calculator, API)
Observation → read the result
→ repeat until confident
→ Final Answer
```

Each Thought is grounded by the previous Observation. Each Action is justified by the current Thought. The loop continues until the model has enough evidence to answer.

---

## Why It Works

- **Reasoning traces** help the model track progress, decompose tasks, and handle exceptions
- **Actions** let the model retrieve real information instead of relying on memorized (possibly wrong) knowledge
- **Observations** update the model's plan at every step — it self-corrects rather than compounding errors

---

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*