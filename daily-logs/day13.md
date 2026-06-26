# Day 13 — BLEU, ROUGE, and BERTScore

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## What I built / learned
Implemented and compared three LLM evaluation metrics (BLEU, ROUGE-1,
ROUGE-L, BERTScore) on six deliberately designed test cases, each built
to expose a specific blind spot in one or more metrics. 

Test cases covered: paraphrase, meaning reversal, real RAG
chatbot output, partial coverage, hallucination via false addition, and
irrelevant padding.


## Results

| TC | Test Case                          | BLEU-1 | ROUGE-L F | BERTScore F1 |
|----|------------------------------------|--------|-----------|--------------|
| 1  | Paraphrase                         | 0.6667 | 0.5714    | 0.9494       |
| 2  | Wrong meaning — high word overlap  | 1.0    | 0.6000    | 0.9767       |
| 3  | RAG chatbot output                 | 0.9500 | 0.9577    | 0.9885       |
| 4  | Partial coverage                   | 0.0767 | 0.4138    | 0.8661       |
| 5  | Hallucination (false addition)     | 0.6154 | 0.7368    | 0.9664       |
| 6  | Irrelevant extra info              | 0.3750 | 0.5556    | 0.9244       |

## Key insights from actual results

**TC 2 — Wrong meaning scored BLEU-1: 1.0, ROUGE-1 P: 1.0, ROUGE-1 R: 1.0**
Every single lexical metric gave a perfect score to a sentence that
means the exact opposite of the reference. "The man bit the dog" vs
"The dog bit the man" — 100% word overlap, completely wrong meaning.
This is the clearest possible proof that lexical metrics cannot detect
semantic contradiction.

**TC 5 — Hallucination scored ROUGE-1 R: 1.0, BERTScore F1: 0.9664**
The model output contained the correct fact ("Eiffel Tower is in Paris")
plus a fabricated fact ("built in 2015"). ROUGE recall hit 1.0 because
every word in the reference appeared in the generated text. BERTScore
F1 was 0.9664 — nearly perfect. None of the three metrics flagged the
hallucination at all. This is exactly the gap RAGAS is built to fill
(Day 42).

**TC 1 — Paraphrase: BLEU-1: 0.6667 vs BERTScore F1: 0.9494**
This gap (0.33 difference) is the clearest demonstration of why
BERTScore exists. Same meaning, different words — BLEU penalizes it,
BERTScore correctly rewards it.

**TC 4 — Partial coverage: BLEU-1: 0.0767, BERTScore F1: 0.8661**
BLEU collapsed completely (0.0767) when the model only covered a small
fraction of a complex reference. BERTScore stayed at 0.8661 — because
the words the model did use ("attention mechanisms", "process data")
are semantically close to terms in the reference. ROUGE-L (0.4138)
sits in between — a reasonable middle ground.

**TC 6 — Irrelevant padding: ROUGE-1 P: 0.3846, ROUGE-1 R: 1.0**
This is the precision vs recall split most clearly. Recall hit 1.0
because the reference content ("Python is a programming language")
appeared in the generated text. Precision dropped to 0.3846 because
most of the generated tokens were irrelevant. F1 alone (0.5556) would
have masked this — always look at P and R separately.

## Connection back to Day 6
On Day 6, cosine similarity was used to score model outputs against
ground truth. That was essentially a sentence-level BERTScore — fast,
interpretable, good for short factual answers. Today's results confirm
that approach was reasonable for Category A/B questions (short facts)
but would have missed the hallucination in TC 5 just as badly as
BERTScore did. 

## Reference
Mansuy, R. (2023, September 20). Evaluating NLP Models: A Comprehensive
Guide to ROUGE, BLEU, METEOR, and BERTScore Metrics.


*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*