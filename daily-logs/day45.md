# Day 45 — Exploring Vision-Language Models with CLIP

> **#50DaysOfGenAI** · [LinkedIn](https://linkedin.com/in/vivek-chauhan-500396340) · [GitHub](https://github.com/Vivek-afk81)

## Overview

Today's focus was on **Multimodal Generative AI**, specifically understanding how Vision-Language Models connect images and text through a shared embedding space. I explored the architecture and capabilities of **CLIP (Contrastive Language–Image Pretraining)** and compared its contrastive learning approach with modern multimodal LLMs such as LLaVA.

Rather than only studying the theory, I built a notebook containing practical experiments to understand how multimodal models represent visual and textual information.

## What I Built

- Implemented zero-shot image classification using CLIP.
- Measured image-text similarity using cosine similarity between embeddings.
- Visualized image embeddings using PCA to observe semantic clustering.
- Performed prompt sensitivity experiments by describing the same image with multiple prompts.
- Compared CLIP's contrastive learning objective with generative vision-language models.

## Key Findings

The prompt sensitivity experiment was the most interesting part of today's work.

Even though the image remained identical, changing the wording of the text prompt produced different similarity scores because CLIP compares **embeddings**, not object labels.

For example:

- "rasmalai"
- "a photo of rasmalai"
- "an Indian dessert called rasmalai"
- "a picture of rasmalai on a plate"

All describe the same object, yet each generates a different text embedding and therefore a different alignment score with the image.

This demonstrates why prompt engineering matters for multimodal systems just as much as it does for language models.

## Key Insight

CLIP is designed to **understand relationships** between images and text through a shared embedding space, whereas models like LLaVA are designed to **generate language** from visual inputs. Although both are multimodal models, they solve fundamentally different problems.

## Notebook

Built a hands-on notebook covering:

- Zero-shot image classification
- Image-text similarity
- Embedding visualization (PCA)
- Prompt sensitivity analysis
- CLIP architecture and multimodal learning concepts