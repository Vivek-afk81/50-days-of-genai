# Day 47 — Bringing H3 Offline with Local LLM Inference

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## The Problem

H3 was originally designed as a **cross-model robustness experiment**, requiring a smaller open-weight instruction model alongside Llama 3.1 8B.

After evaluating multiple free inference providers, I found that none consistently exposed suitable **2–3B instruction models**. Rather than changing the experiment itself, I changed the inference backend.

The evaluation pipeline, prompts, parsing logic, and statistical methodology all remain identical—only the model execution moved from cloud APIs to local inference.

---

## What I Built

Migrated the H3 pipeline to **local GGUF inference** using `llama-cpp-python`.

Implemented:

- Local CPU inference with `llama-cpp-python`
- Support for loading GGUF models by model name
- Automatic dependency updates via `requirements.txt`
- `.gitignore` rules to exclude multi-GB GGUF files
- Local model launcher (`local_model.py`)
- Feasibility evaluation script (`20_h3_local_feasibility.py`)
- Full baseline evaluation pipeline (`21_h3_local_baseline.py`)

---

## Verification

Before committing to the full benchmark, I performed a five-question feasibility test.

| Metric | Result |
|--------|-------:|
| Problems | 5 |
| Correct | 4 |
| Accuracy | 80% |
| Average parsed CoT steps | 7.2 |
| Parse failures | 0 |

The parser extracted reasoning traces and final answers successfully from every locally generated response, confirming compatibility with the existing evaluation pipeline.

---

## Baseline Results

After validating the local setup, I ran the complete Stage-1 baseline evaluation using **Phi-3 Mini (Q4_K_M GGUF)**.

| Metric | Result |
|--------|-------:|
| Problems | 100 |
| Correct | 72 |
| Accuracy | **72.00%** |

The experiment incrementally stored results in:

`results/h3_local_phi3-mini_stage1_baseline.jsonl`

This establishes the clean baseline before introducing reasoning-order perturbations.

---

## Engineering Notes

During validation I discovered two schema inconsistencies in the newly generated result files:

- `id` was used instead of the existing `problem_id` field.
- `n_parsed_steps` was introduced as an additional metadata field.

Neither issue affects experimental correctness, but they create downstream compatibility problems with the existing analysis scripts. These will be standardized before running the remaining H3 experiments.

---

## Key Takeaway

Today's work wasn't about improving model performance—it was about making the research independent of external inference services. By moving H3 to local inference, the entire experimental pipeline is now reproducible without relying on API availability, while preserving the original methodology and evaluation protocol.