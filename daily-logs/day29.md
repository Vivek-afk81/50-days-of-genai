# Day 29 — Step order actually matters (just not how I expected)

Picked up right where Day 27 left off — that post planted the seed ("does order
matter?") but today is where I actually got data back.

## What I did today

Finished validating the Stage 1 baseline (100 GSM8K problems, model generates
its own CoT, `llama-3.1-8b-instant` via Groq) — landed at 90% accuracy, which
sits inside the range reported by a recent robustness paper I read as part of
my novelty check. Good sign the pipeline itself is sound.

Then moved into Stage 2: taking the 89 problems the model got right with 3+
reasoning steps, and generating three broken-order versions of each one —
reversed, randomly shuffled, and a "partial" version where I keep the first
and last step in place and only scramble the middle. The idea is simple: the
*content* of the reasoning stays exactly the same, only the *order* changes.
Does the model still land on the right answer?

Fed all three conditions back and scored them.

## What I found

- Reversed: 57.3% accuracy
- Shuffled: 66.3% accuracy
- Partial: 73.0% accuracy (blended — more on this below)

I expected reversed order to be the "gentlest" corruption — it's still a
coherent, logical order, just backwards. I expected fully random shuffling to
be the harshest. That's not what happened. Reversed hurt the model *more*
than pure randomness did.

Still figuring out exactly why, but my working guess is that a full reversal
is close enough to a valid sequence that the model tries to follow it
literally step by step, and that literal following is what causes it to
compound errors. A fully random shuffle might be scrambled enough that the
model falls back on just... reasoning from the problem itself, half-ignoring
the broken step order it was handed. That's a hypothesis, not a conclusion —
need to dig into individual failure cases before I'd stand behind it.

## The part I almost missed

The 73.0% "partial" number looked suspiciously good, so I split it apart —
turns out 38 of those 89 problems had *no real middle to scramble* (3-4 step
chains only have 0-1 middle steps), so I was accidentally measuring "barely
touched the order at all" for nearly half the group. Once I separated that
out: the untouched-order group scored 84.2%, not the ~100% I'd have expected
if order really didn't matter at all.

That gap — 84.2% instead of ~100% — told me something I hadn't accounted for:
just *changing the prompt format* (from "generate your own reasoning" to
"here are some steps, just give me the final answer") costs the model
accuracy on its own, before I've scrambled anything. Which means my Reversed
and Shuffled numbers above are currently tangled up with two effects at once
— the real order effect, and this format-switch effect — and I can't fully
tell them apart yet.

So: building a control condition next (same prompt format, but the *original,
correct* step order) to isolate that. Numbers above are real, but not final.

## Honest state of things

This is genuinely still in progress. The headline finding — reversed order
hurting more than random shuffling — is real and reproducible, but I want the
control run done before I'd post it as a clean causal claim rather than "here's
what I'm seeing so far."

## Next

- Run the baseline-control condition (unpermuted steps, same Stage 2 prompt)
- Use that as the real denominator for a robustness score, not raw Stage 1 accuracy
- Then: full analysis pass, McNemar's test, error position analysis (H2)
- LinkedIn post once the control run confirms whether the reversed/shuffled
  gap survives after removing the format-switch noise

GitHub: [cot-robustness-experiment](https://github.com/Vivek-afk81/cot-robustness-experiment)

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*