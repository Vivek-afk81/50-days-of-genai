# Day 21 / 50 — Fine-Tuning LLMs: LoRA, Quantization & QLoRA


## What I Built / Learned

**Topic:** Fine-tuning large language models on limited hardware — covering LoRA, int-8 quantization from scratch, and QLoRA.

### RAG vs Fine-Tuning — The Decision Framework

Before touching any training code, I mapped out when to use each:

| Dimension | RAG | Fine-Tuning |
|---|---|---|
| Knowledge updates | Easy — update the database | Requires retraining |
| Hardware | Minimal | Requires GPUs |
| Hallucination | Reduced (grounded in docs) | Can still hallucinate |
| Consistency | Depends on retrieval | More consistent |
| Best for | Chatbots, Q&A, enterprise search | Classification, summarization, domain assistants |

### LoRA — How It Works

Full fine-tuning on a 1B+ parameter model is expensive: more GPU memory, slower training, huge storage. LoRA solves this:

1. Load a pretrained model (e.g. MT0-large, 1.23B params)
2. Freeze all original weights
3. Inject small trainable adapter matrices at key layers
4. Train only those adapters

Result: only **0.19% of parameters** are trained — 2.3M instead of 1.23B — with performance close to full fine-tuning.

This is the setup and config — not the training loop — but understanding how LoRA wraps a model is the prerequisite to everything that comes next.

```python
from transformers import AutoModelForSeq2SeqLM
from peft import get_peft_model, LoraConfig, TaskType

peft_config = LoraConfig(
    task_type=TaskType.SEQ_2_SEQ_LM,
    inference_mode=False,
    r=8,
    lora_alpha=32,
    lora_dropout=0.1
)

model = AutoModelForSeq2SeqLM.from_pretrained("bigscience/mt0-large")
model = get_peft_model(model, peft_config)
model.print_trainable_parameters()
# trainable params: 2,359,296 || all params: 1,231,940,608 || trainable%: 0.19%
```

### Quantization — Built From Scratch

Quantization reduces weight precision: float32 → int8 (or even 4-bit). I implemented symmetric int-8 quantization manually with NumPy to understand what's actually happening:

```python
# Quantize float weights to int8
scale = (max_x - min_x) / (qmax - qmin)   # step size
q = np.round((x - zero_point) / scale).astype(int)
q = np.clip(q, -128, 127)

# Dequantize back to float for comparison
x_hat = scale * (q - zero_point)
```

Plotted original vs dequantized values — the staircase effect (quantization error) is visible but small at int8 precision.

### QLoRA — Combining Both

QLoRA combines 4-bit quantization + LoRA adapters. Key innovations from the original paper:

- **NF4 (Normal Float 4):** A 4-bit format designed specifically for neural network weights — preserves quality better than standard int4
- **Double Quantization:** Quantizes the quantization constants themselves, saving an additional ~0.37 bits per parameter
- **Paged Optimizers:** Handles GPU memory spikes during training

Result: fine-tune a 65B model on a single 48GB GPU.

```python
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    "bigscience/mt0-large",
    quantization_config=bnb_config,
    device_map="auto",
)
model = get_peft_model(model, peft_config)
```

---

## Key Insight

> Fine-tuning isn't one thing — it's a spectrum. Full fine-tuning is at one end (expensive, powerful). LoRA cuts trainable parameters to <1%. QLoRA compresses the base model weights too, making large models runnable on consumer hardware. Each step trades a little quality for a lot of practicality.

The quantization implementation from scratch was the most clarifying part — seeing the staircase effect in the plot makes the quality vs. compression tradeoff concrete, not abstract.

---

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*