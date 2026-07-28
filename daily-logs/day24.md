# Day 24 — Adding Conversational Memory to My RAG Chatbot

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## Overview

Today's goal was to transform my RAG application from a single-turn question-answering system into a true conversational chatbot by introducing multi-turn memory. Instead of treating every query independently, the chatbot now remembers previous interactions and uses them to interpret follow-up questions.

## Features Implemented

- Maintained conversation history as a list of `{role, content}` message pairs.
- Appended every user query and assistant response to the conversation history before each LLM call.
- Combined retrieved document chunks with the complete conversation history to provide richer context.
- Added a `clear` command to reset conversation memory whenever needed.
- Introduced a `--dev` mode to switch between a clean user interface and a developer mode with debugging options such as chunking strategy and retrieval method selection.

## Validation

The chatbot successfully handled contextual follow-up questions.

**Example conversation:**

**User:** Name two poems in this document.

**Assistant:**
- The Song of the Lark
- The Grand Canyon

**User:** What is the second one about?

Instead of asking for clarification, the chatbot correctly understood that *"the second one"* referred to **The Grand Canyon** from the previous interaction and generated an accurate summary based on the retrieved document.

The hallucination guard also remained effective. When asked about information unrelated to the document (for example, computers or personal preferences), the chatbot correctly responded that the information could not be found in the provided document.

## Key Takeaway

Adding conversational memory required only a small architectural change—a maintained history list—but significantly improved the user experience. The same retrieval pipeline from Day 12 now behaves like an actual chatbot capable of understanding references across multiple turns while still remaining grounded in the source documents.

## Project

Enhanced the existing RAG chatbot by integrating conversation memory, context-aware follow-up handling, memory reset functionality, and developer tooling without compromising hallucination prevention.