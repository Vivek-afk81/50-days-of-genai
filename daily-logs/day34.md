# Day 34 — I asked the model to explain its own mistakes

Picking up the CoT order-sensitivity experiment where the accuracy numbers left off —
today was about a different question: not just *does* the model fail when its reasoning
gets scrambled, but *where* does it fail.

## What I did today

The original hypothesis (H2) guessed that when the model's reasoning steps get shuffled,
its answer breaks specifically at the 2nd step in the order it's shown. Checking that by
hand across every wrong answer would mean reading dozens of full model responses myself.
So I tried a shortcut first: asking the model to look back at its own wrong answer and
self-report where its reasoning first went off track.

## What I found

Across 35 wrong answers, the self-reported failure point clustered hardest at the **3rd**
step — not the 2nd, which is what I'd guessed going in. That's already a real, measurable
pattern, and not the one I expected.

## The part I'm not trusting yet

A model confidently explaining its own mistake doesn't mean the explanation is true. I've
already caught one case where the self-report cited something that sounded like a real
reason but didn't actually match what the response had done. So before I write this up as
a finding, I'm manually checking a sample myself — reading the actual response, deciding
for myself where I think it broke, without looking at the model's own answer first, then
comparing.


## Honest state of things

The Step-3 pattern is real in the self-report data. Whether it's real in *reality* is
still open. Not writing that up as a conclusion until the check is finished — real numbers
once it's done, not before.



GitHub: [cot-robustness-experiment](https://github.com/Vivek-afk81/cot-robustness-experiment)

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*