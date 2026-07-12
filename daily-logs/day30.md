# Day 30/50 — Stage 2 analysis complete (and a bug almost fooled me)
 
Picked up the Stage 2 data from Day 29 and ran the actual statistical analysis
today — McNemar's tests, Bonferroni-corrected for the 6 comparisons. First
pass back gave me a huge effect: Reversed order dropped roughly 30 points
below baseline. That's the kind of number that makes you want to post
immediately.
 
## What I did today
 
Instead of taking that number at face value, I got suspicious and pushed for
a second full trial before calling it — a large, clean-looking effect on a
first run is exactly the kind of thing worth being paranoid about, not
excited about.
 
Good instinct. Tracing back through the parsing pipeline, I found a regex
capture-group bug — `group(1)` instead of `group(2)` — that had been
silently reducing most of the reasoning chains down to bare digits before
they ever got scored. It affected somewhere between 63 and 100 of the 89
eligible records. The step-order "effect" I was seeing wasn't the model
struggling with broken reasoning order — it was partly just broken parsing.
 
Fixed the regex, re-parsed Stage 1 (no new API calls needed, since that data
was already there — just re-extracted correctly), regenerated every
permutation from scratch, and re-ran all of Stage 2 fresh: 267 + 89 calls.
 
## What I found (corrected)
 
- Baseline-control: 95.51%
- Reversed: 85.39%
- Shuffled: 88.76%
- Partial (non-degenerate, 5+ step only): 80.39%
Every perturbed condition still scores below baseline — the direction of
the original finding held. But the magnitude shrank a lot once the parser
bug was gone.
 
Ran McNemar's tests on the pairwise comparisons. Baseline-vs-Reversed
(p=0.0352) and Baseline-vs-Partial (p=0.0391) look significant on their own,
but neither survives Bonferroni correction across the 6 comparisons tested
(corrected α≈0.0083). No comparison between the perturbation types
themselves (Reversed vs Shuffled vs Partial) reached significance at any
threshold.
 
## Honest state of things
 
This is a real, consistent directional trend — step-order disruption
appears to lower CoT accuracy, and that direction replicated across two
independent trials, even though the exact magnitude changed once I fixed
the bug. But it is not statistically confirmed at this sample size (n=89,
n=51 for Partial). H1's predicted ordering between perturbation types is
neither confirmed nor cleanly refuted — the study is underpowered to
distinguish between them right now.
 
H2 (first-error-position analysis) is not implemented yet. It needs its own
annotation or self-report methodology, and I'm not going to fake it with a
shortcut — flagging it honestly as follow-up work instead.
 
Catching this bug before publishing anything is arguably a better
demonstration of actual research practice than the original dramatic number
would have been.
 
## Next
 
- a repeated-trial replication before making any stronger claim
- Implement H2 (first-error-position) with a real methodology, not a shortcut
- Full write-up once statistical power is actually there to support it

GitHub: [cot-robustness-experiment](https://github.com/Vivek-afk81/cot-robustness-experiment)

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*