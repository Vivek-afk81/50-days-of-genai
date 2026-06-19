# Day 2 — Tokens, Embeddings, and Word2Vec Arithmetic

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## What I built / learned
Explored how text becomes geometry. Covered the pipeline from raw text
to tokens to token IDs to embeddings, and why semantic similarity shows
up as spatial distance in embedding space. Used Gensim's pretrained
Word2Vec to run two experiments: measuring vector distances between
word pairs of varying semantic closeness, and the classic
king - man + woman = queen analogy.

## Key insight
Embeddings encode meaning as geometry, not as explicit rules. Vector
distance between "hi" and "hello" (2.64) and "man" and "woman" (1.73)
is much smaller than between "semiconductor" and "earthworm" (5.67) —
proving that semantically related words cluster together in embedding
space purely as a result of training, with no hand-coded relationships.
The same geometric property is what allows vector arithmetic
(king - man + woman ≈ queen) to surface relationships the model was
never explicitly taught.

