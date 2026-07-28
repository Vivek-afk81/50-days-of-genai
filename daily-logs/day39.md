# Day 39 — Fixing Answer Normalization & Revalidating Experimental Results

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## What I built / learned
Discovered and fixed a bug in my answer normalization pipeline that incorrectly treated values like `2.00` and `2` as different answers, creating false negatives across multiple experiments. Applied the fix directly to all stored result files with automatic backups, then re-scored every saved experiment for Llama, Mistral, and Qwen without making any new API calls. Re-ran the complete H1 statistical analysis, confirming that the corrected numbers changed slightly but the overall hypothesis and significance conclusions remained unchanged. Also identified a potential integrity issue in the H2 analysis pipeline, since manually annotated "wrong" cases may now include records that are actually correct after the parser fix.

## Key insight
A seemingly minor parser bug can propagate through an entire research pipeline. Correcting the data is only the first step—every downstream analysis, statistical test, and manually annotated dataset must be revalidated before the results can be considered final.


Implemented the normalization fix (`18_apply_normalizer_fix.py`), re-ran the statistical analysis (`04_analysis.py`), and flagged the H2 integrity check for verification before finalizing the paper.