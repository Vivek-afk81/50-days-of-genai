<p align="center">
  <h1 align="center"> 50 Days of Generative AI</h1>
  <p align="center">
    Building GenAI systems from fundamentals to original research — one day at a time.
  </p>
  <p align="center">
    <a href="https://linkedin.com/in/vivek-chauhan-500396340"><img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white" alt="LinkedIn"></a>
    <a href="https://github.com/Vivek-afk81"><img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white" alt="GitHub"></a>
    <img src="https://img.shields.io/badge/Days_Logged-49%2F50-blueviolet" alt="Progress">
    <img src="https://img.shields.io/badge/Notebooks-17-orange" alt="Notebooks">
  </p>
</p>

---

## What This Is

A 50-day public learning challenge documenting my journey through Generative AI — from attention mechanisms and embeddings to RAG pipelines, fine-tuning, LLM evaluation, and an **original Chain-of-Thought robustness research experiment** tested across multiple model families.

Every day has a log. Many days have runnable notebooks. The later half of the challenge evolves into a full research study on whether **the order of reasoning steps affects LLM accuracy**, with results across Llama 3.1, Mistral, and Qwen models.

---

## Repository Structure

```
50-Days-of-GENAI/
├── 50-days-of-genai/
│   ├── daily-logs/          # 49 daily markdown logs (day1.md – day49.md)
│   ├── notebooks/           # 17 Jupyter notebooks with runnable experiments
│   ├── datasets/            # Benchmark data (hallucination_benchmark.json, book-of-short-stories.pdf)
│   └── images/              # Assets used in multimodal experiments
├── advance builds/
│   ├── COT-EVALUATOR/       # Modular CoT permutation evaluation framework (CLI + backend)
│   └── PROMPT-MUTATION/     # Prompt mutation tooling
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Daily Log Index

### Phase 1 — Foundations (Days 1–10)

| Day | Topic |
|-----|-------|
| 1 | What is Generative AI + Causal & Multi-Head Attention |
| 2 | Tokens, Embeddings, and Word2Vec Arithmetic |
| 3 | Transformer Attention Explorer (interactive DistilBERT visualization) |
| 4 | Zero-Shot vs Few-Shot vs Chain-of-Thought Prompting |
| 5 | Tokenization, Decoding Strategies, and Sentiment Models |
| 6 | LLM Evaluation & Hallucination Analysis |
| 7 | What is RAG and Why it Matters |
| 8 | FAISS vs ChromaDB: Vector Database Benchmark |
| 9 | LangChain Basics: Prompt Templates |
| 10 | Phase 1 Recap |

### Phase 2 — Intermediate Systems (Days 11–20)

| Day | Topic |
|-----|-------|
| 11 | Structured Outputs and Output Parsers |
| 12 | RAG Chatbot over a PDF |
| 13 | BLEU, ROUGE, and BERTScore |
| 14 | RAG Chatbot: Chunk Mode + Semantic Search |
| 15 | RAG Chatbot: Gradio UI |
| 16 | ReAct: Reasoning + Acting |
| 17 | LangChain Agent with DuckDuckGo Search + Custom Math Tool |
| 18 | *(log placeholder)* |
| 19 | Fine-Tuning vs RAG: Decision Framework |
| 20 | Recap: Days 11–19 |

### Phase 3 — Fine-Tuning & Security (Days 21–27)

| Day | Topic |
|-----|-------|
| 21 | Fine-Tuning LLMs: LoRA, Quantization & QLoRA |
| 22 | Fine-Tuning Llama 3.2 with Unsloth + LoRA on R1 Distillation Data |
| 23 | Prompt Injection: What It Is and What Actually Works |
| 24 | Adding Conversational Memory to My RAG Chatbot |
| 25 | Semantic Search vs Keyword Search vs Hybrid Search |
| 26 | RAG Guardrails: Input Filter Confirmed, Output Filter Unproven |
| 27 | Chain-of-Thought Prompting |

### Phase 4 — CoT Robustness Research Experiment (Days 28–49)

| Day | Topic |
|-----|-------|
| 28 | CoT Robustness Experiment: Stage 1 Baseline |
| 29 | Step order actually matters (just not how I expected) |
| 30 | Stage 2 analysis complete (and a bug almost fooled me) |
| 31 | Two-Trial Replication Check + Bonferroni Correction |
| 32 | H2 Self-Report Experiment: Divergence Position Analysis |
| 33 | Manual Annotation — when the only real check is doing it by hand |
| 34 | I asked the model to explain its own mistakes |
| 35 | Rule-based H2 taxonomy, significance testing, careful annotation |
| 36 | Cross-model selection saga + explicit H3 scoping decision |
| 37 | Cross-model bypass finding — Mistral block closed early |
| 38 | Investigating Reasoning Order Robustness in a 27B LLM |
| 39 | Fixing Answer Normalization & Revalidating Experimental Results |
| 40 | Wrapping Up the Research & Beginning the Paper |
| 41 | Comparing Reasoning Recovery Strategies Across Three LLMs |
| 42 | Measuring LLM Consistency Beyond Final Accuracy |
| 43 | Week 6 Recap: From Experiments to Research Insights |
| 44 | From Research Scripts to a Reusable Evaluation Framework |
| 45 | Exploring Vision-Language Models with CLIP |
| 46 | Verifying Recovery Rate with a Full Manual Audit |
| 47 | Bringing H3 Offline with Local LLM Inference |
| 48 | When "Robust" Doesn't Mean Robust |
| 49 | When a Failed Hypothesis Becomes the Result |

---

## 📓 Notebooks

| Notebook | Day | Topic |
|----------|-----|-------|
| `Day2_vector embeddings.ipynb` | 2 | Word2Vec embeddings & vector arithmetic |
| `Day3_Transformer Attention Explorer.ipynb` | 3 | Interactive attention head visualization |
| `Day4_zeroshot Fewshot COT.ipynb` | 4 | Prompting strategy comparison |
| `Day5_huggingFace_tansformers.ipynb` | 5 | Decoding strategies & sentiment analysis |
| `Day6_LLM Evaluation & Hallucination Analysis.ipynb` | 6 | Hallucination detection & custom benchmarks |
| `Day7_RAG.ipynb` | 7 | Full RAG pipeline (FAISS + FLAN-T5) |
| `day8_FAISSvsCHROMADB.ipynb` | 8 | Vector DB benchmark |
| `day9_langchain_prompts.ipynb` | 9 | LangChain prompt templates |
| `Day11LLMs_responses and parsing.ipynb` | 11 | Structured output parsing |
| `day13_evaluation_metrics.ipynb` | 13 | BLEU, ROUGE, BERTScore |
| `day17_langchain_agent.ipynb` | 17 | LangChain agent with tools |
| `Day21_finetuningLLMs.ipynb` | 21 | LoRA & QLoRA fine-tuning |
| `day22_finetuning_part2.ipynb` | 22 | Llama 3.2 fine-tuning with Unsloth |
| `day23_prompt_injection.ipynb` | 23 | Prompt injection attacks & defenses |
| `day25_semanticSearch_vs_keywordSearch.ipynb` | 25 | Semantic vs keyword vs hybrid search |
| `Day42_llm_consistency_scorer.ipynb` | 42 | LLM consistency scoring |
| `day45_multimodalGenAI_img_text.ipynb` | 45 | Vision-language models (CLIP) |

---

## 🔬 The Research Experiment

Starting Day 28, this project transitions from a learning challenge into an **original research study**:

> **Research Question:** Does the order of Chain-of-Thought reasoning steps affect LLM accuracy on grade-school math (GSM8K)?

### Hypotheses Tested

| ID | Hypothesis | Status |
|----|-----------|--------|
| **H1** | Permuting CoT step order reduces LLM accuracy |  Directional support (Llama 3.1 8B) |
| **H2** | The model's self-reported divergence point differs from human annotation |  Confirmed — model self-reports systematically later than actual break |
| **H3** | Smaller models show larger step-order sensitivity |  Open — free-tier model access constraints prevented testing |

### Key Findings

- **Step order matters**, but inconsistently — reversed and shuffled conditions reduce accuracy, though the effect didn't survive Bonferroni correction at n=89
- **Models detect errors but don't self-correct** — 50% of failures are "SELF-BREAK": the model flags an inconsistency, then continues with degraded reasoning anyway
- **Capable models bypass the experiment entirely** — Mistral (8B) produced character-identical responses regardless of step order in 94% of cases, solving problems from scratch rather than following the provided steps
- **Self-report is directionally biased** — human annotation locates reasoning divergence earlier (Steps 1–2) than the model reports (Step 3)

### Models Tested

| Model | Source | Role |
|-------|--------|------|
| Llama 3.1 8B Instant | Groq API | Primary experimental model |
| ministral-8b-2512 | Mistral AI API | Cross-family generalization check |
| Qwen 2.5 27B | HuggingFace Inference | Scale comparison |
| Phi-3 Mini / Qwen 2.5 3B | Local inference | H3 feasibility testing |

> Full experiment code and data: [cot-robustness-experiment](https://github.com/Vivek-afk81/cot-robustness-experiment)

---

## Advance Builds

### COT-EVALUATOR

A modular, CLI-driven framework for running CoT permutation evaluations at scale. Built with a clean backend separation (`cot_evaluator/` package), YAML config, logging, and tests.

### PROMPT-MUTATION

Tooling for systematic prompt mutation experiments.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Vivek-afk81/50-days-of-genai.git
cd 50-days-of-genai

# Install dependencies
pip install -r requirements.txt

# Set up your API key
echo "GROQ_API_KEY=your_key_here" > .env
```

> **Note:** Individual notebooks may require additional dependencies (transformers, sentence-transformers, faiss-cpu, gradio, etc.) — install instructions are included in each notebook.

---

## Tech Stack

| Category | Tools |
|----------|-------|
| **LLM APIs** | Groq, Mistral AI, HuggingFace Inference |
| **Frameworks** | LangChain, HuggingFace Transformers, Unsloth |
| **Vector Stores** | FAISS, ChromaDB |
| **Models** | Llama 3.1/3.2, Mistral, Qwen, GPT-2, FLAN-T5, DistilBERT, CLIP |
| **Evaluation** | BLEU, ROUGE, BERTScore, McNemar's test, Monte Carlo permutation |
| **UI** | Gradio |
| **Fine-Tuning** | LoRA, QLoRA, Unsloth |

---

## Project Stats

- **49** daily logs written
- **17** runnable Jupyter notebooks
- **4** LLM families tested in the research experiment
- **189+** API calls per experimental condition
- **35** manually annotated failure cases with a rule-based taxonomy

---

## License

This project is for educational and research purposes. Feel free to reference or build upon this work with attribution.

---

## Links

- **Author:** [Vivek Chauhan](https://linkedin.com/in/vivek-chauhan-500396340)
- **GitHub:** [Vivek-afk81](https://github.com/Vivek-afk81)
- **Research Repo:** [cot-robustness-experiment](https://github.com/Vivek-afk81/cot-robustness-experiment)

---

<p align="center">
  <i>Part of <b>#50DaysOfGenAI</b> — building GenAI systems from fundamentals to production.</i>
</p>
