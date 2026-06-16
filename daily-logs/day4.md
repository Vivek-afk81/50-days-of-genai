# Day 4 — Zero-Shot vs Few-Shot vs Chain-of-Thought Prompting
 
## What I built / learned
Ran two different reasoning questions through three prompting strategies
— zero-shot, few-shot, and chain-of-thought — using Llama 3.1 8B via
Groq API. Compared outputs to test whether prompt structure changes
reasoning quality and correctness.
 
## Key insight
The two questions told completely different stories.
 
On a simple arithmetic question (juggler/golf balls), all three
strategies produced near-identical correct reasoning. The task was
too easy to differentiate the methods — prompting strategy didn't
matter when the model could solve it without help.
 
On an ambiguous "odd one out" question (couch, rug, table, chair),
the three strategies actually disagreed:
- Zero-shot confidently answered "couch" with a fabricated justification
- Few-shot answered "table," matching the reasoning style of its examples
- Chain-of-Thought visibly reversed itself multiple times mid-generation
  before settling on "rug"
The lesson: prompting strategy matters most exactly when the question
is genuinely ambiguous, not when it's easy. Zero-shot's confident wrong
answer was the most concerning result — it gave no signal that it was
guessing.

 
