# Day 9 / 50 — LangChain Basics: Prompt Templates

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## What I Covered/learned

Before chains, before agents, before any API calls — every LangChain app starts with Prompt Templates. Today I covered all four levels of prompt structure in LangChain, with no LLM calls needed to understand them.

---

## The Four Levels of Prompt Structure

### 1. Static Prompt — hardcoded, no variables

```python
from langchain_core.prompts import PromptTemplate

static_prompt = PromptTemplate(
    input_variables=[],
    template="Write a short fun fact"
)

prompt_text = static_prompt.format()
print(prompt_text)
# Output: Write a short fun fact
```

Useful for fixed, repeatable tasks. Zero flexibility — same prompt every time.

---

### 2. Dynamic Prompt — variables as placeholders

```python
dynamic_prompt = PromptTemplate(
    template="Write a short fun fact about {topic} in {style} style",
    input_variables=["topic", "style"],
)

prompt_text = dynamic_prompt.format(topic="One Piece", style="humorous")
# Output: Write a short fun fact about One Piece in humorous style

prompt1 = dynamic_prompt.format(topic="rasmalai", style="funny")
# Output: Write a short fun fact about rasmalai in funny style
```

One template, infinite prompts. The foundation of reusable LangChain pipelines.

---

### 3. Chat Prompt — role-separated messages

```python
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "You are a helpful assistant that provides information about {subject}"
    ),
    HumanMessagePromptTemplate.from_template(
        "Can you tell me something interesting about {subject}?"
    )
])

messages = chat_prompt.format_messages(subject="rasmalai")

for i in messages:
    role = i.__class__.__name__.replace("Message", "")
    print(f"[{role}]: {i.content}\n")
```

**Output:**
```
[System]: You are a helpful assistant that provides information about rasmalai

[Human]: Can you tell me something interesting about rasmalai?
```

This is the structure behind every chatbot and agent you've ever used. System sets the persona, Human sends the query — and the LLM generates in that context.

---

### 4. Few-Shot Prompt Template — examples baked in automatically

```python
from langchain_core.prompts import FewShotPromptTemplate

examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall",  "output": "short"},
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input} → Output: {output}"
)

few_shot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Input: {adjective} → Output:",
    input_variables=["adjective"]
)

print(few_shot.format(adjective="fast"))
```

**Output:**
```
Input: happy → Output: sad
Input: tall → Output: short
Input: fast → Output:
```
---

## Key Takeaways

- `PromptTemplate` with `input_variables` is the basic building block — use it for any task with variable inputs
- `ChatPromptTemplate` with System + Human roles is what separates a raw LLM call from a structured chatbot interaction
- `FewShotPromptTemplate` automates what Day 4 showed manually — formatting examples into a consistent structure without string hacks
- None of this requires an API call — prompt templates are pure Python objects you can inspect, test, and debug before connecting to any model

---

## Tech Stack

| Tool | Purpose |
|---|---|
| `langchain-core` | `PromptTemplate`, `ChatPromptTemplate`, `FewShotPromptTemplate` |
| `langchain-community` | Community integrations (used in upcoming days) |

---

## What's Next

Day 10 is a **Week 1 recap** — portfolio of everything built in Days 1–9, GitHub links, and key learnings. After that, Day 11 starts Phase 2: building a full RAG chatbot over a PDF.

---
*Part of [#50DaysOfGenAI](https://github.com/Vivek-afk81/50-days-of-genai) — building GenAI systems from fundamentals to production.*