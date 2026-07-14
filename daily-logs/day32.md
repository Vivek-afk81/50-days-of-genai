# Day 32 — H2 Self-Report Experiment: Divergence Position Analysis

## What I built / learned
Designed and ran a follow-up self-report prompt (`05_h2_self_report.py`) to
test H2: does the model's first reasoning error cluster at a specific step
position when steps are reordered?

Design choices:
- Ground truth answer deliberately withheld from the follow-up prompt — if
  shown the correct answer, the model could work backward and confabulate a
  plausible-sounding step number rather than genuinely introspecting.
- Model is shown its own prior response + the exact permuted step list it
  saw the first time (numbered in the order it was given, not original
  correct order), and asked to name a step number where it first went off
  track, or "none."
- Only run on records where `correct == False` (35 total: 13 reversed, 10
  shuffled, 12 partial) — no divergence to find on records the model got
  right.
- Tracked divergence in BOTH permuted-position and original-position terms,
  using the saved step-pairing from the Stage 2 permutation files, since
  these are genuinely different questions and conflating them would be an
  analysis error.

Ran `analyze_h2_distribution.py` (read-only, no API calls) on the resulting
`results/h2_self_report_trial1.jsonl` to get exact counts rather than
eyeballing the terminal log.

## Key insight
**Permuted-position divergence distribution:**
Step 1: 7, Step 2: 4, Step 3: 12, Step 4: 6, Step 6: 2, Step 7: 3,
unparsed: 1 (problem 48, reversed)

**Original-position divergence distribution (same 35 records, mapped back):**
Step 1: 2, Step 2: 6, Step 3: 7, Step 4: 1, Step 5: 9, Step 6: 4, Step 7: 3,
Step 9: 1, Step 12: 1

Step 3 (in permuted order) is the clear mode — 34% of all self-reported
divergences — holding up as the mode or tied-for-mode within each of the
three conditions individually, not driven by one condition alone. My
original H2 prediction (Step 2) was one of the smallest buckets (11%).

The important confirmation is the CONTRAST between the two views: permuted-
position clusters sharply, original-position is flat and spread out to
position 12. That's evidence this is a real positional effect (something
about being 3 steps into whatever sequence the model is handed, regardless
of what content lives there) rather than certain reasoning content just
being inherently fragile no matter where it sits. If it were a content
effect, both distributions should cluster the same way — they don't.

Revised, honest framing: H2 as originally stated (divergence clusters at
Step 2) is not confirmed. A more specific, real finding replaces it:
divergence clusters at Step 3 by sequence position, and the position-vs-
content contrast supports this being genuine rather than coincidental.

One unresolved item: problem 48 (reversed) produced an unparseable
self-report — flagged for follow-up (parsing miss vs. genuine "can't
identify a divergence" outcome, not yet determined).

Built (not yet run): `06_manual_spotcheck.py` — blind manual annotation
tool, stratified ~18-case sample across the three conditions, reveals the
model's self-report only after my own judgment is locked in, to avoid
anchoring. This is the step that actually determines whether the Step-3
clustering finding can be trusted or whether it's confident pattern-matching
from the model.

GitHub: [cot-robustness-experiment](https://github.com/Vivek-afk81/cot-robustness-experiment)

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*