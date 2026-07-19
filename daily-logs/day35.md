# Day 35

#### 1. Methodology change (record this explicitly in Methods)
 
- Original annotation pass (Day 33/34) used a free-form "gut call" guess
  for divergence step.
- Replaced with a **rule-based taxonomy**, four categories:
  - (a) MISUSE — model misuses/misreads a step it was given
  - (b) INVENTED — model fabricates a transition/content not in the given steps
  - (c) SELF-BREAK — model explicitly flags something as off, then continues
    anyway with degraded reasoning
  - (d) SKIP/IGNORE — model skips or ignores a given step
- `08_h2_careful_analysis.py` is the canonical analysis script going forward.
  Uses `CAREFUL_first_divergence_step_guess` and `CAREFUL_which_rule_applied`
  fields, not the earlier gut-call fields.
- **Why this matters for the paper**: rule-based annotation is more
  defensible than free-form guessing (reviewers can audit against a fixed
  rubric) and it changed the numbers meaningfully vs. the gut-call pass —
  see Section 3 below. Report both passes existed; state the rule-based
  pass as the one used for reported results.
---
 
#### 2. THE CONTRADICTION (headline item — do not lose this)
 
- **Model self-report** (Day 32, `analyze_h2_distribution.py`,
  n=35 wrong answers): divergence clusters at **Step 3** (11/35, ~31%).
- **Careful, rule-based human annotation** (this pass, n=30 non-"none"
  cases): divergence clusters **earlier** — co-modal at **Step 1 and Step 2**
  (8/30 each), median = 2, mean = 3.03, and **73% of divergences occur
  within the first 3 steps**.
- **Interpretation**: this is not just "the self-report is unreliable" (a
  vague claim) — it is a **specific, directional bias**: the model's
  self-reported divergence point is systematically **later** than where a
  blind human annotator locates the actual break. Frame this in the paper
  as a directional finding, not just a reliability caveat.
- Numeric agreement with self-report (careful vs. self-report, n=35):
  - Exact: 10/35 (28.6%)
  - Off-by-one: 11/35 (31.4%)
  - Combined exact+off-1: 21/35 (60.0%)
  - Bigger disagreement: 14/35 (40.0%)
  - (Note: this 60% combined is HIGHER than the earlier gut-call comparison,
    which had given 45.7% combined — the rule-based pass agrees with the
    model somewhat more than the gut-call pass did. Reconcile/mention both
    numbers if the gut-call pass is kept as supplementary material.)
---
 
#### 3. Known bug / caveat to fix before quoting "the mode"
 
- `08_h2_careful_analysis.py`'s summary section calls Step 1 "the modal
  divergence position" using `Counter.most_common(1)`, which silently
  breaks ties by insertion order.
- **Actual data: Step 1 and Step 2 are tied at 8/30 each.** This is a TIE,
  not a clean single mode.
- **Action item**: do not state "modal position was Step 1" verbatim in
  the paper. Correct phrasing: "co-modal at Steps 1–2 (8/30 each)."
- Also worth fixing in the script itself (detect ties, report all tied
  values) before generating any more paper-facing summaries from it.
---
 
#### 4. New finding not in original H2 hypothesis: failure-mode taxonomy
 
- Rule breakdown across 30 classified cases:
  - (a) MISUSE: 0 (0.0%)
  - (b) INVENTED: 6 (20.0%)
  - (c) SELF-BREAK: 15 (50.0%)
  - (d) SKIP/IGNORE: 9 (30.0%)
- **SELF-BREAK is the dominant failure mode (50%)**: the model notices
  something is inconsistent and says so, but continues reasoning anyway
  with degraded output rather than correcting course or stopping.
- **Zero MISUSE cases** — the model never simply misreads a step it was
  given; failures are about what it does *after* noticing a problem, not
  about basic misreading. Worth a sentence in Discussion.
- This taxonomy is an original contribution beyond the original H2
  hypothesis (which only asked "where," not "how"). Consider giving it its
  own subsection in the paper rather than folding it into H2 as a footnote.
---
 
#### 5. Condition-level patterns (n small — report as suggestive, not confirmed)
 
| Condition | n (numeric) | Mean step | Median | Mode | none count |
|---|---|---|---|---|---|
| reversed  | 10 | 2.10 | 2 | 1 | 3 |
| shuffled  | 9  | 2.89 | 2 | 1 | 1 |
| partial   | 11 | 4.00 | 3 | 2 | 1 |
 
- **Reversed** divergences happen earliest (mean 2.1) — consistent with a
  conclusion-first ordering immediately disorienting the model.
- **Partial** divergences happen latest (mean 4.0) — consistent with the
  fixed first/last steps giving the model a stable anchor before things
  break down in the shuffled middle.
- **Reversed has the most "none" cases (3/10)** — i.e., annotator (not just
  model) sometimes couldn't identify one clear divergence point in reversed
  chains. Possible implication: reversed-order reasoning is confusing
  enough that "first divergence" may not be a well-defined concept for
  some of these cases — worth a limitations note.
- **Rule × Condition** (small n, flag as suggestive only):
  - partial: 4/11 INVENTED vs. reversed 1/10, shuffled 1/9 — partial
    condition may push the model toward *fabricating* a bridging step more
    than reversed/shuffled do. Plausible mechanism: fixed first/last steps
    give the model an anchor to fabricate a plausible-sounding link into,
    whereas reversed/shuffled have no stable anchor to bridge from.
    **Not statistically tested — n too small. State as a hypothesis for
    future work, not a finding.**
---
 
#### 6. Confidence data
 
- Self-rated annotation confidence: mean 4.20/5, N=35.
- Distribution skews high (18/35 rated confidence=5; none rated 1).
- **Caveat for paper**: high self-rated confidence in the human annotator
  does not by itself validate the annotations — worth noting as a
  limitation (annotator confidence is not the same as annotator accuracy,
  and there's no second annotator / inter-rater check yet).
---
 
#### 7. Significance test on positional distribution — RESOLVED (was open)
 
**Status update: this item is no longer open.** Ran a length-aware
significance test on the careful-annotation positional distribution
(n=30 numeric-divergence cases; chain lengths ranged 3–15 steps, e.g.
Counter({5:6, 6:6, 4:5, 7:5, 10:2, 15:2, 8:2, 9:1, 3:1}), max step=15).

**Method:** null hypothesis = divergence position uniform over 1..n_steps
*per individual case* (not a flat uniform over all observed step values —
that would be wrong given varying chain lengths). Expected counts per step
computed accordingly; bins with E<1 merged into an overflow bin before the
chi-square approximation, per standard practice with sparse expected counts.
Cross-checked the analytical result with a 10,000-draw Monte Carlo
permutation test, since several bins still had E<5 even after merging
(chi-square approximation flagged as weak in that regime).

**Result:**
- Chi-square(7) = 6.513, analytical p = 0.4812
- Monte Carlo p = 0.4178 (4,178/10,000 simulated draws met or exceeded the
  observed chi-square)
- **Fail to reject H0 at α=0.05 by both methods.**

**Interpretation — important, do not overstate Section 2's clustering
claim without this context:** the early-clustering pattern described in
Section 2 (co-modal Steps 1–2, 73% within first 3 steps) is visually
consistent but **not statistically distinguishable from a uniform
distribution** once chain-length is properly accounted for. This mirrors
H1's own result (a consistent directional pattern that doesn't survive
correction at this sample size) — report both as the same honest kind of
finding: real-looking pattern, underpowered to confirm at n=30/n=89.
**Do not claim statistically significant positional clustering in the
paper.** The taxonomy finding (Section 4, SELF-BREAK dominant) is
unaffected by this — it's a categorical result, not a positional one.
---
 
#### 8. Single-sentence summary to reuse in the paper draft — REVISED
 
> ~~Rule-based human annotation of 35 Stage-2 failure cases shows reasoning
> divergence concentrated in the first 3 steps (73%, co-modal at Steps 1–2),
> earlier than the position the model itself self-reports (mode Step 3)~~
 
**Revised per item 7 above — the original summary sentence overstates the
positional finding and should not be used as-is.** Corrected version:
 
> Rule-based human annotation of 35 Stage-2 failure cases shows an
> early-leaning divergence pattern (co-modal at Steps 1–2, 73% within the
> first 3 steps) that is directionally earlier than the position the model
> itself self-reports (mode Step 3) — but a length-aware significance test
> (chi-square + Monte Carlo, n=30) fails to distinguish this pattern from a
> uniform distribution, so the positional claim is reported as suggestive,
> not confirmed. The dominant failure mode (50%) is the model explicitly
> flagging an inconsistency and continuing anyway rather than correcting or
> misreading a step outright (0% MISUSE) — this categorical finding is
> unaffected by the positional test.
---

#### 9. Decision: dropped dedicated error-analysis case studies

Originally scoped (Day 33 roadmap) as individual deep-dive write-ups on
problem_ids #6 (Stephen's loan), #67 (Jenna's apples), #69 (Britany's
TikTok time). **Decision: dropped, not carried forward.**

Two of the three (#6, #69) already received qualitative write-ups above
under [10-07-2026], as part of Stage 1 validation — those descriptions
stand and are not being redone. #67 never received individual treatment
and will not now, either.

**Rationale:** the rule-based H2 taxonomy (item 4 above) already
generalizes what three hand-picked anecdotes were meant to illustrate,
across all 30 classified cases rather than 2–3 examples. Given the null
result on positional significance (item 7), effort is better spent on
writeup synthesis than additional qualitative case studies that wouldn't
change the statistical picture. If the paper draft later needs a specific
illustrative quote, pull from the existing 35-case annotation sheet rather
than reopening this as a separate task.

---