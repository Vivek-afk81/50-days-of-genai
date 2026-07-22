Day 36: cross-model model-selection saga + explicit H3 scoping decision

**Decision, logged explicitly:** the cross-model block is being split into
two separate, clearly labeled things in the paper, not conflated:

1. **Cross-family generalization check (what we're actually running):**
   does the step-order-sensitivity effect (H1's core finding) replicate
   with a different model family at comparable parameter scale? This is
   what ministral-8b-2512 (via Mistral AI's own API) vs. Llama-3.1-8B-
   Instant (via Groq) actually tests. Both are ~8B dense models. Report
   this as its own labeled result — "cross-family replication at matched
   scale" — not as an H3 test.

2. **H3 (smaller/weaker model shows a larger accuracy drop):** remains
   **open and untested**. None of the models trialed this week satisfy
   H3's premise of being genuinely smaller than Llama-3.1-8B-Instant.
   Explicitly flagged as a **future-work item**, not silently dropped or
   quietly reframed as answered by the ministral run.

**Why this distinction matters for the paper:** conflating "a different
model also shows the effect" with "H3 is confirmed" would be a scoping
error — same mistake in spirit as the Step-3 self-report issue from
Day 34 (a real-looking pattern getting overclaimed past what the data
actually supports). Keeping the two claims separate protects both: the
generalization result stands on its own merits, and H3 stays honestly
marked as not yet tested rather than either confirmed or refuted by proxy.

---

**Model-selection history (for Methods section):**

| Attempt | Model | Source | Outcome |
|---|---|---|---|
| 1 | Gemini 3.1 Flash-Lite | Google AI Studio (free tier) | Ran full Stage 1 (98/100, 98%) — too strong vs. Llama's 90%, defeats size-comparison premise. Abandoned. |
| 2 | google/gemma-2-2b-it | HF Inference Providers | Failed feasibility test — "not deployed by any Inference Provider." Never ran. |
| 3 | microsoft/Phi-3.5-mini-instruct | HF Inference Providers | Failed feasibility test — same reason. Never ran. |
| 4 | Qwen/Qwen2.5-3B-Instruct | HF Inference Providers (featherless-ai) | Passed feasibility test (single call, correct answer, clean parse). HF free-tier rate limits judged too restrictive for a full 189-call run. Abandoned before full Stage 1. |
| 5 | **ministral-8b-2512** | **Mistral AI API (direct)** | **Selected and run.** Stage 1 result: **95/100 (95%)**. Sits between Llama's 90% and the abandoned Gemini's 98%. Generous published rate limits (625,000 TPM, 3.13 RPS) comfortably cleared the run with a 0.5s sleep and zero errors. ~8B scale — comparable to, not smaller than, Llama-3.1-8B. |

**Implementation note:** the `mistralai` Python SDK raised an unresolvable
`ImportError` ("cannot import name 'Mistral' from 'mistralai' (unknown
location)") in this project's environment — likely a stray local
file/folder shadowing the package, or a stale v0.x install still on the
old import path. Rather than debug the SDK further, `utils_mistral.py`
calls Mistral's REST endpoint directly via `requests` (already manually
confirmed working). No functional difference in what's being tested — the
model, prompt, and scoring are identical either way.

---

**Day 36 Stage 1 result (confirmed):**

| Model | Accuracy |
|---|---|
| Llama-3.1-8B-Instant (Groq) | 90/100 (90%) |
| Gemini 3.1 Flash-Lite (abandoned) | 98/100 (98%) |
| **ministral-8b-2512 (Mistral AI)** | **95/100 (95%)** |

ministral-8b-2512 sits between the two — not lower than Llama's baseline,
which is worth noting plainly: at matched Stage-1 accuracy this close
(90% vs. 95%), a Stage 2 accuracy-drop comparison between the two models
should still be interpretable, since neither model is so much stronger at
the base task that a difference in perturbed-condition accuracy would just
reflect "one model is generally better at GSM8K" rather than "one model is
more sensitive to step-order disruption." Day 37 (eligibility filtering +
Stage 2 Baseline-control vs. Reversed) is the next actionable step.



> A genuinely smaller model was not available within this study's
> free/low-cost tier constraints at the time of writing: candidates in
> the 2–4B range either lacked any active Inference Provider deployment
> (gemma-2-2b-it, Phi-3.5-mini-instruct) or were feasible but rate-limited
> below what a full experimental run required (Qwen2.5-3B-Instruct via
> HF). H3 (smaller models show larger step-order sensitivity) therefore
> remains an open hypothesis, not evaluated in this study, and is flagged
> as a natural extension for future work with access to a broader range of
> model sizes.

GitHub: [cot-robustness-experiment](https://github.com/Vivek-afk81/cot-robustness-experiment)

*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*