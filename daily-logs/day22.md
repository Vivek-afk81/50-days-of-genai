# Day 22 / 50 — Fine-Tuning Llama 3.2 with Unsloth + LoRA on R1 Distillation Data
---

## What I Built

Fine-tuned `Llama-3.2-3B-Instruct` using Unsloth + LoRA on the `ServiceNow-AI/R1-Distill-SFT` dataset — a 171,647-example dataset containing DeepSeek-R1-style chain-of-thought reasoning traces with `<think>` tags.

**Goal:** Teach the model to reason in a reflective, stream-of-consciousness style before answering, mimicking how R1-class models think out loud.

---

## Setup

**Model:** `unsloth/Llama-3.2-3B-Instruct` (3.2B params, loaded in 4-bit)
**Hardware:** Colab T4 (14.5GB VRAM)
**Trainable params:** 24,313,856 of 3,237,063,680 → **0.75%**

LoRA targeted all 7 key weight matrices:
```python
target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                  "gate_proj", "up_proj", "down_proj"]
```
r=16, lora_alpha=16, no dropout, gradient checkpointing enabled.

---

## Dataset

`ServiceNow-AI/R1-Distill-SFT` — math problems with DeepSeek-R1-distilled reasoning traces. Each example has:
- `problem` — the question
- `reannotated_assistant_content` — `<think>...</think>` reasoning trace
- `solution` — final answer

Prompt template used:
```
You are a reflective assistant engaging in thorough, iterative reasoning...
<problem>
{problem}
</problem>

{thought}
{solution}
```

---

## Training

| Parameter | Value |
|---|---|
| Steps | 60 |
| Batch size | 2 |
| Gradient accumulation | 4 |
| Effective batch size | 8 |
| Learning rate | 2e-4 |
| Optimizer | AdamW 8-bit |
| Runtime | 7m 30s |

**Loss curve:** Started at ~1.01, ended at ~0.43 — consistent downward trend across 60 steps.

**Note:** A `PicklingError` appeared after training completed — this was a checkpoint saving issue caused by a version conflict between `trl` and `unsloth`, not a training failure. The model itself trained successfully and inference worked immediately after.

---

## Inference Test

Tested with: *"How many r's are present in 'strawberry'?"*

The model produced a detailed reflective reasoning trace — exactly the style we trained for — going through the word letter by letter, expressing self-doubt, checking its work. It arrived at "2", which is actually wrong (strawberry has 3 r's: str**a**w**b**e**rr**y → r, r, r), but the **reasoning behavior** was correctly learned. The model thinks out loud now.

This is an important distinction: SFT teaches *style*, not correctness. The model learned to reason reflectively; it didn't learn math facts it didn't already know.

---

## Key Insight

> Fine-tuning with Unsloth + 4-bit quantization makes it feasible to train a 3B model on a free T4 GPU. 0.75% of parameters trained, full reasoning style transferred. The gap between "downloaded a model" and "adapted a model to your use case" is smaller than most people think.

---

