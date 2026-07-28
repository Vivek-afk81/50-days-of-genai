# Day 38 — Investigating Reasoning Order Robustness in a 27B LLM

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## What I built / learned
Extended my reasoning-order robustness experiments to a larger 27B language model after observing another near-perfect accuracy score under reversed reasoning steps. Instead of bypassing the evaluation by solving problems from scratch, the model appeared to internally reconstruct the correct logical sequence while preserving the externally provided step labels. Analyzed individual responses, identified a potential evaluation confound related to the placement of the final answer, and documented the need for a more controlled experiment to isolate this behavior.

## Key insight
High accuracy alone is not evidence of reasoning robustness. A model may achieve the same score through fundamentally different strategies, making qualitative response analysis essential before drawing conclusions.

## Notebook
Experiment conducted using the CoT robustness evaluation pipeline in the project repository:
github.com/Vivek-afk81/GenAI-Research