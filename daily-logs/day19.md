# Day 19 — Fine-Tuning vs RAG: Decision Framework

## What I built / learned
No code today. Built a decision framework for choosing between RAG and
fine-tuning based on 6 diagnostic questions. The key insight is that
RAG and fine-tuning fix different failure modes — confusing them leads
to building the wrong system. Produced a decision flowchart and a
real trade-off table.

## Decision FrameWork


START: 

    What is your model getting wrong?
         │
         ├─ It states facts that don't exist → HALLUCINATION
         │       └─ Use RAG
         │
         ├─ It knows the facts but formats/reasons wrong → WRONG BEHAVIOUR
         │       └─ Use Fine-tuning
         │
         ├─ Both → Use RAG + Fine-tuning
         │
         └─ Neither → Fix your prompt first



## Key insight

1. Diagnose the failure mode first, then pick the tool
RAG fixes hallucination. Fine-tuning fixes wrong behaviour. They are not substitutes. Most people pick a technique before diagnosing the problem — that's backwards.
2. The Snorkel AI number
A fine-tuned small model matched GPT-3's performance while being 1,400x smaller and costing 0.1% as much to run. This changes the cost argument completely — fine-tuning isn't just about behaviour, it's also a serious cost optimization at scale.
3. RAG keeps data out of model weights — fine-tuning bakes it in
This is the security/compliance insight most people miss. With RAG you can delete a document from the database and it's gone. With a fine-tuned model, data embedded in weights is nearly impossible to remove. For GDPR or HIPAA compliance, this often decides the choice before anything else.


## References
- MacDonald, L. (n.d.). RAG vs Fine Tuning. Monte Carlo Data.
  montecarlo.ai
  Key additions: Snorkel AI benchmark (fine-tuned model 1,400x smaller
  than GPT-3, same performance), security/compliance angle (RAG keeps
  data out of model weights), hybrid approach legal AI example.

---

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*