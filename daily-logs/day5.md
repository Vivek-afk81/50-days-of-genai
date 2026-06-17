# Day 5 — Tokenization, Decoding Strategies, and Sentiment Models
 
## What I built / learned
Went deeper into Hugging Face Transformers than the original plan called
for. Skipped re-demonstrating "load a model via API" since the Day 4
prompting comparison already covered that with Llama via Groq. Instead
focused on what's happening underneath text generation itself.
 
Covered four things using GPT-2 loaded directly (not just the pipeline
wrapper):
1. Subword tokenization — showed how words like "unbelivable" and
   "pneumonoultramicroscopicsilicovolcanoconiosis" get split into
   subword pieces, not whole words.
2. Manually implemented four decoding strategies from raw logits:
   greedy, top-k sampling, top-p (nucleus) sampling, and temperature
   sampling — without relying on `model.generate()`.
3. Visualized next-token probability distributions — looked at the
   top 10 candidate tokens and their softmax probabilities for a given
   input.
4. Ran sentiment analysis with two different fine-tuned models —
   DistilBERT (general-purpose) and FinBERT (finance-domain) — on the
   IMDB dataset and custom finance sentences, to see how domain-specific
   fine-tuning changes model behavior on the same task.
## Key insight
The same logits produce five different next words depending purely on
the decoding strategy: greedy picked "am", top-k picked "was", top-p
picked "left", temperature sampling picked "would", and pure random
sampling picked "had" — all from the exact same probability
distribution over the vocabulary. The model's "knowledge" doesn't
change; only the rule for choosing from what it already knows changes.
This is the part most tutorials skip — they call `.generate()` and
never show what's happening inside it.
 
The domain-specific FinBERT vs general DistilBERT comparison also
made it concrete why "off-the-shelf" sentiment models can quietly
fail on specialized text — finance language doesn't map cleanly onto
movie-review sentiment patterns.
 
