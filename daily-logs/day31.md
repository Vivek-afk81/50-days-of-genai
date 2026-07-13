# Day 31/50 — Two-Trial Replication Check + Bonferroni Correction

## What I built / learned
Ran a second independent trial of the corrected (bug-fixed) Stage 2 pipeline
at temperature=0.0, then updated `04_analysis.py` to run McNemar's exact test
across both trials and compare per-problem flip rates between them.

Trial 1 vs Trial 2 results:
- Baseline-control: 85/89 (95.51%) both trials — 0% flip rate
- Reversed: 76/89 (85.39%) both trials — 2.2% flip rate (1 flip each direction, net 0)
- Shuffled: 79/89 (88.76%) both trials — 6.7% flip rate (3 each direction, net 0)
- Partial (non-degenerate, n=51): 80.39% → 84.31% — 4.5% flip rate, net +2
  (this is the only condition where the AGGREGATE number moved, not just
  individual problems trading places)

McNemar's exact test (Bonferroni-corrected for 6 comparisons, α=0.05/6≈0.0083):
- Baseline vs. Reversed: p=0.0352 in both trials — raw-significant, not
  Bonferroni-significant, but the most consistent result I have
- Baseline vs. Partial (non-degenerate): raw-significant in trial 1
  (p=0.0391), NOT significant in trial 2 (p=0.1250) — did not replicate
- All other pairwise comparisons: not significant in either trial

## Key insight
Temperature=0.0 does not mean deterministic across separate API calls —
already knew this in principle, but seeing it concretely (net-zero flip
rates masking real underlying instability) made it click. More importantly:
Partial permutation isn't just the worst-performing condition, it's also the
LEAST stable one across repeated trials. That's a second, unplanned finding
sitting next to my original research question — the model seems to be in a
less confident/more variable regime specifically under partial reordering,
possibly because it's the most structurally unusual condition (correct
endpoints, scrambled middle) rather than a clean reversal or full shuffle.

Overall honest status: every perturbed condition is directionally below
baseline in both trials. Nothing survives multiple-comparison correction yet.
This is a real, replicated, honestly-reported null-leaning result — not a
failure, a legitimate pilot-study finding.

GitHub: [cot-robustness-experiment](https://github.com/Vivek-afk81/cot-robustness-experiment)

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*