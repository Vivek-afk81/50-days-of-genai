# Day 27 — CoT Robustness Experiment: Stage 1 Baseline

## What I built / learned
- Fixed a parsing bug in `parse_response()`: the first version only captured lines
  starting with `"N."` and silently dropped un-numbered continuation lines (sub-calculations
  under a step). Rewrote it as a stateful line-by-line parser that merges continuation
  lines onto the current step, only starting a new step on a new `"N."` line.
- Validated the fix on 2 problems from different step-count buckets (Maggie's oven problem,
  Claire's egg problem) — both parsed cleanly, all sub-calculations correctly merged into
  their parent step.
- Refactored shared logic into `utils.py`: `get_model_response()`, `parse_response()`,
  `normalize_answer()`.
- Wrote `01_generate_baseline.py`: loops over all 100 problems in the stratified GSM8K
  subset, calls `llama-3.1-8b-instant` (temp=0.0) via Groq, parses + normalizes each
  response, writes results incrementally to `data/stage1_baseline.jsonl`
  (2.5s sleep between calls for free-tier rate limits).
- Ran the full 100-problem Stage 1 baseline generation.

## Key result
**90/100 correct — 90.00% baseline accuracy.**

Sanity-checked against two external reference points from papers I read for the novelty
check:
- Fragile Thoughts (Aravindan & Kejriwal, 2026), Llama-3.1-8B-Instruct clean accuracy: ~87–96%
- GSM-Symbolic (Mirzadeh et al., ICLR 2025), Llama3-8b-instruct on their 100-question subset: 74%

90% falls inside the Fragile Thoughts range and comfortably above the GSM-Symbolic anchor —
good sign the Stage 1 pipeline (prompt, parsing, normalization) is sound before I move to
permuting step order in Stage 2.


