# Day 3 / 50 — Transformer Attention Explorer
 
> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)
 
## What I Built
 
An interactive tool to visualize attention weights inside DistilBERT — explore all 6 layers and 12 attention heads in real time using sliders.
 
Instead of just reading about attention, you can **watch** which tokens the model focuses on, layer by layer.
 
---
 
## Demo
 
> Input sentence: *"When it rains look for Rainbow, when it's dark look for stars"*
 
Slide through layers and heads to see how attention patterns shift:
- **Early layers (0–1):** broad, chaotic — almost every token attends to everything
- **Later layers (4–5):** surgical — specific tokens lock onto semantically related ones
The repeated words (`when`, `it`, `look`, `for`) create fascinating symmetric patterns in later layers.
 
---
 
## How It Works
 
```
Input Text
    ↓
Tokenizer → [CLS, when, it, rains, look, for, rainbow, ...]
    ↓
DistilBERT (output_attentions=True)
    ↓
attentions[layer][batch, head, token, token]
    ↓
Plotly Heatmap → Gradio UI
```
 
**Attention tensor shape:** `[1, 12, 17, 17]`
- 1 → batch size
- 12 → attention heads
- 17 × 17 → each token attending to every other token
---
 
## Tech Stack
 
| Tool | Purpose |
|---|---|
| `distilbert-base-uncased` | Pretrained transformer model |
| Hugging Face Transformers | Model loading + attention extraction |
| Plotly | Interactive heatmap visualization |
| Gradio | Live UI with layer/head sliders |
| PyTorch | Tensor operations |
 
---
 
## Key Code
 
**Extract attention weights:**
```python
def extract_attention(text, layer_idx, head_idx):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=64)
    with torch.no_grad():
        outputs = model(**inputs)
 
    attention = outputs.attentions[layer_idx]
    attention = attention[0, head_idx]  # [tokens, tokens]
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
 
    return tokens, attention.cpu().numpy()
```
 
**Sanity check — rows must sum to 1.0:**
```python
tokens, attn = extract_attention("your sentence", layer_idx=0, head_idx=0)
print(attn.sum(axis=1))  # Every value should be ~1.0
```
 
---
 
## What I Learned
 
- Attention weights per row always sum to 1.0 (softmax property) — easy way to verify correctness
- `[CLS]` and `[SEP]` tokens attract disproportionate attention in early layers — this is normal BERT behavior
- Different heads specialize in different patterns — some track syntax, some semantics
- DistilBERT has 6 layers × 12 heads = **72 different views** of the same sentence
---
 
## Run It Yourself
 
```bash
pip install transformers torch gradio plotly pandas
```
 
Open `day3_attention_explorer.ipynb` in Colab and run all cells.
 
---
 
## Connection to the Research Experiment
 
Starting Day 26, I'll run an original experiment on **Chain-of-Thought reasoning order** — asking whether permuting reasoning steps affects LLM accuracy. Understanding attention behavior (today) is foundational to interpreting *why* step order might matter.
 
---
 
*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*