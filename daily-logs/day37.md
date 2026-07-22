Day 37-38 Cross-model block: bypass finding, Mistral block closed early

**Result that looked like a finding, but isn't one:** ministral-8b-2512
scored 89/89 (100%) on BOTH baseline-control and Reversed conditions --
Robustness_tau = 1.000 exactly.

**Investigated via manual spot-check (09_spotcheck_mistral_bypass.py,
full 89-problem pass, not just the 8-case sample):**

| Category | n | % |
|---|---|---|
| Char-for-char IDENTICAL response, baseline vs. reversed | 84 | 94.4% |
| Near-identical (trivial formatting diff only, e.g. trailing `%`) | 1 | 1.1% |
| "Substantively different" text | 4 | 4.5% |

**The 4 "substantively different" cases do NOT rescue a robustness
claim.** On inspection (problems 15, 56, 97 and one more): baseline-control
produced a terse one-line answer, Reversed produced a full verbose
re-derivation -- but the verbose version is a FRESH solve of the original
question, not an engagement with the given (reversed) step content or
order. Different verbosity, same underlying bypass. Effectively **89/89
(100%) show no evidence the model used the provided step list as input at
all**, regardless of which of the two literal-similarity buckets they
landed in.

**Conclusion: tau=1.000 must NOT be reported as a robustness finding.**
The correct interpretation is a construct-validity limitation: Mistral is
apparently confident enough to solve GSM8K problems directly from the
question text, and does so regardless of what step list (correct-order or
reversed) it's handed in the Stage 2 prompt. The prompt's "use these exact
steps, do not reorder" instruction does not behaviorally constrain this
model the way it constrains Llama-3.1-8B-Instant (90% Stage 1 accuracy,
vs. Mistral's 95% -- only a 5-point gap in raw capability, but apparently
enough to cross a threshold where the model stops needing the scaffolded
input).

**McNemar's test is not being run for this pair.** With zero discordant
pairs (b=0, c=0 -- baseline-control and Reversed agree on literally every
problem), the test is undefined / trivially p=1.0. This is not "no
significant difference from reordering" in the H1 sense -- it's a symptom
of the bypass, and reporting a p-value here without this context would be
misleading.

**Decision: closing the Mistral cross-model block here, not expanding to
Shuffled + Partial.** Running the remaining two conditions would almost
certainly reproduce the identical bypass pattern (both are equally
"not the correct order" from the model's perspective) -- more API calls
on a contaminated condition adds no information. Day 38/39's originally
planned scope (decide whether to expand conditions based on directional
match with Llama) is superseded by this finding: there is no meaningful
directional comparison to make when the denominator condition itself
isn't testing what it's supposed to test.

**Reframed contribution to the paper:** this becomes a documented
methodological limitation/finding in its own right, not a null result to
bury. Candidate framing for Discussion/Limitations:

> A Stage-2 prompt design that scaffolds reasoning via a provided step
> list implicitly assumes the model needs and uses that scaffold. For a
> sufficiently capable model, this assumption can silently fail: rather
> than following (or being disrupted by) the given step order, the model
> may bypass the provided steps entirely and re-derive the answer from the
> original question, producing near-identical outputs regardless of step
> order or content. This was observed in 89/89 (100%) of eligible cases for
> ministral-8b-2512, evidenced by character-for-character identical
> responses between the baseline-control (correct order) and Reversed
> conditions in the large majority of cases, and by verbosity-only
> differences (not content-order engagement) in the remainder. This
### suggests that step-order-sensitivity experiments of this design are only
> informative for models operating below their own solve-from-scratch
> confidence threshold on the target task, and that apparent perfect
> robustness (tau=1.000) should be verified qualitatively before being
> reported as a substantive finding -- a purely quantitative accuracy
> comparison would have missed this entirely.

**Open item flagged for future work, not resolved here:** a cleaner
Stage 2 prompt design might mitigate bypass (e.g. withholding the original
question and showing ONLY the step list, forcing the model to work
strictly from the given steps rather than allowing a fallback re-derivation
path) -- worth considering for any follow-up study, but out of scope for
the current pipeline/timeline.


---

### [Follow-up] — Steps-only prompt test: bypass persists, block closed

**Tested whether withholding the original question (forcing the model to
work ONLY from the given step list) would eliminate the bypass, before
committing to a full re-run.** Ran on a random 15-problem sample
(10_test_noquestion_prompt_mistral.py), both baseline-control and Reversed
conditions, using a hardened prompt that explicitly states the question is
not provided and instructs the model not to reinterpret or re-derive
outside the given steps.

**Result: 14/15 (93.3%) still produced character-identical responses
between baseline-control and Reversed.** The fix did not work. This
narrows down the mechanism: it's not simply that the model has the
original question as a fallback -- ministral-8b-2512 is apparently capable
of reconstructing enough problem context from the step list's own content
(the numbers and phrasing embedded in the steps themselves) to solve the
problem independently of what order those steps are shown in. Removing
the question removed one bypass route; the model used another.

**One exception, flagged but not over-interpreted (n=1):** problem 71 --
baseline-control answered incorrectly (0.25), Reversed answered correctly
(25). This is the only case across both the original 89-problem run and
this 15-problem follow-up where order appeared to matter at all for this
model. With a single data point, this is consistent with ordinary noise
and should not be read as evidence of partial order-sensitivity without
further investigation (out of scope for now, given the block is closing).

**Decision: cross-model block (ministral-8b-2512) is closed.** No further
prompt-hardening attempts planned -- diminishing returns, and the finding
itself (capable models bypass artificial reasoning-order manipulations via
multiple independent routes) is now well-evidenced across two separate
tests. This strengthens, not weakens, the paper's methodological
contribution: it's not a one-off prompt quirk, it's a robust bypass
behavior that survived a deliberate attempt to close the most obvious
escape hatch.

**Updated framing for paper's Discussion/Limitations section:**

> Two independent attempts to constrain a capable model
> (ministral-8b-2512) to genuinely engage with a provided, potentially
> reordered reasoning chain both failed to prevent bypass: providing the
> original question alongside the steps, and withholding the question
> entirely, both resulted in over 90% character-identical responses
> between correct-order and reversed-order conditions. This suggests the
> bypass is not attributable to a single fixable prompt weakness, but to
> the model's general capability exceeding what the experimental
> manipulation requires it to rely on -- it can reconstruct sufficient
> problem context from the steps' own content regardless of the
> scaffolding's completeness. Step-order-sensitivity designs of this kind
> are therefore only informative below some model-specific capability
> threshold, and confirming genuine engagement (not just comparing
> accuracy numbers) is a necessary check, not an optional one, before
> reporting a robustness result.

**Status: H3 remains untested (unchanged). Cross-family generalization
check is now this two-part bypass finding, not an accuracy-drop
comparison, and is closed as of this entry.**

---

GitHub: [cot-robustness-experiment](https://github.com/Vivek-afk81/cot-robustness-experiment)

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*