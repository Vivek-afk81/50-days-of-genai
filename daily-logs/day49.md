# Day 49 — When a Failed Hypothesis Becomes the Result

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## Background

Today I completed the H3 evaluation by analyzing **Qwen2.5-3B** and comparing its behavior against **Phi-3 Mini**. Although both models initially appeared highly robust based on their τ values, a deeper behavioral analysis revealed that they arrived at those numbers through fundamentally different mechanisms.

Rather than relying solely on aggregate accuracy, I introduced a cross-condition overlap analysis that categorizes each evaluated problem according to how the model behaves across all perturbation conditions.

## Cross-Condition Behavioral Analysis

Each evaluated problem was assigned to one of four categories:

- **Full bypass** — responses remain identical across all perturbations.
- **Reversed-specific disruption** — only reversed reasoning changes the response.
- **Genuinely order-sensitive** — responses differ under every perturbation.
- **Mixed / other** — behavior that does not fit the previous categories.

The comparison produced a striking contrast:

| Behaviour | Phi-3 Mini | Qwen2.5-3B |
|-----------|-----------:|-----------:|
| Full bypass | 4/68 (5.9%) | 66/83 (79.5%) |
| Reversed-specific disruption | 18/68 (26.5%) | 7/83 (8.4%) |
| Genuinely order-sensitive | 13/68 (19.1%) | 4/83 (4.8%) |
| Mixed / Other | 33/68 (48.5%) | 6/83 (7.2%) |

## Interpretation

Although both models reported robustness values close to one, the overlap analysis showed that these scores should not be interpreted the same way.

Qwen2.5-3B exhibited extensive bypass behavior, with nearly eighty percent of evaluated problems producing identical responses regardless of reasoning-step order. This indicates that its high robustness scores are largely driven by re-solving the problem independently rather than engaging with the supplied reasoning.

Phi-3 Mini presented a different profile. Full bypass was uncommon, while a meaningful subset of problems displayed genuine order sensitivity. This makes Phi-3 Mini a much stronger candidate for studying reasoning-order robustness than Qwen2.5-3B, despite its lower overall baseline accuracy.

## Key Insight

This experiment reinforced an important lesson from the project:

A hypothesis failing is not the same as a research project failing.

The original H3 hypothesis predicted that larger models would be more robust than smaller ones. Instead, the experiments revealed that robustness metrics can be dominated by bypass behavior, making direct comparisons misleading unless the evaluation first verifies genuine engagement with the provided reasoning.

## Conclusion

Today's work shifted H3 from a simple model-size comparison into a construct-validity problem. Future experiments should focus on prompt designs that force interaction with the supplied reasoning before robustness across different model sizes can be measured reliably.