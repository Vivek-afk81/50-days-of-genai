# Day 48 — When "Robust" Doesn't Mean Robust

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## Background

With the local inference pipeline successfully running, I completed the Stage-2 evaluation for **Phi-3 Mini** under the H3 (cross-model robustness) hypothesis. The experiment reused the same methodology developed for previous models, applying reasoning-order perturbations to problems that the model originally solved correctly.

The initial results suggested that Phi-3 Mini was almost completely insensitive to reasoning-step order.

## Stage-2 Results

From the 100 GSM8K problems evaluated during Stage 1, **68** satisfied the eligibility criteria (correct answer and at least three parsed reasoning steps).

The resulting accuracies were:

| Condition | Accuracy |
|-----------|---------:|
| Baseline Control | 100.00% |
| Reversed | 95.59% |
| Shuffled | 98.53% |
| Partial | 98.53% |

At first glance, these values suggested near-perfect robustness across every perturbation condition.

## Bypass Investigation

Following the project's standing rule, I did not interpret the accuracy values directly.

Instead, I performed a bypass analysis by comparing each response against its corresponding baseline output.

The results were:

| Condition | Identical | Near Identical | Different |
|-----------|-----------:|---------------:|-----------:|
| Reversed | 11.8% | 1.5% | 86.8% |
| Shuffled | 32.4% | 0.0% | 67.6% |
| Partial | 80.9% | 0.0% | 19.1% |

The analysis revealed that the **Partial** condition exhibited extensive bypass behavior, with over four-fifths of responses being character-identical to the baseline. This indicates that the reported robustness score is largely an artifact of the model reproducing its original reasoning rather than engaging with the modified reasoning sequence.

The **Reversed** condition behaved differently. Most responses differed from the baseline, and the observed errors appear to reflect genuine reasoning failures rather than bypass.

## Key Insight

This experiment reinforced an important lesson from the project:

A robustness score close to **1.0** is not automatically evidence of robustness.

If a model ignores the supplied reasoning and independently reconstructs the solution, the resulting τ value becomes a measure of bypass behavior rather than reasoning resilience.

Consequently, the H3 hypothesis cannot be fairly evaluated until prompt designs explicitly require the model to engage with the provided reasoning steps instead of silently re-deriving the solution.

## Conclusion

Today's work shifted the focus from comparing model sizes to validating the evaluation itself. Rather than reporting impressive robustness numbers at face value, the bypass analysis demonstrated why response inspection is an essential part of any Chain-of-Thought robustness study.