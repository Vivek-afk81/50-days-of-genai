import json
import re
import logging
from typing import Dict, Any, List
from cot_evaluator.models import Step, CoTTrace
from cot_evaluator.backend import ModelBackend

logger = logging.getLogger("cot_evaluator.generator")

STAGE1_PROMPT_TEMPLATE = """You are a reasoning assistant. For the given prompt, you must think step by step to solve it.
Your output must be EXACTLY a JSON object with two fields:
- "steps": a list of strings, where each string represents a single logical reasoning step in sequence.
- "answer": a string representing the final concise answer.

Do not write any markdown formatting, code block fences, or other text outside the JSON. Return only the JSON object.

Prompt: {prompt}"""

STAGE2_PROMPT_TEMPLATE = """Given a list of reasoning steps and a final answer question, what is the logical final answer implied by these steps, strictly in the order they are presented?

Steps:
{steps_list_formatted}

You must output a JSON object with the field "answer" containing the final answer string:
{{"answer": "final answer string"}}

Do not include any prefix, suffix, or markdown formatting fences. Return only the JSON object."""

def extract_json_substring(text: str) -> str:
    """Robustly extracts JSON substring starting with { and ending with }."""
    text_clean = text.strip()
    
    # Strip markdown fences if present
    if text_clean.startswith("```"):
        match_start = re.match(r"^```(?:json)?\s*", text_clean, re.IGNORECASE)
        if match_start:
            text_clean = text_clean[match_start.end():]
        if text_clean.endswith("```"):
            text_clean = text_clean[:-3].rstrip()
            
    # Find outermost { }
    match_json = re.search(r"(\{.*\})", text_clean, re.DOTALL)
    if match_json:
        return match_json.group(1)
    return text_clean

def parse_json_keys(text: str, required_keys: List[str]) -> Dict[str, Any]:
    """Parse JSON and ensure required keys exist."""
    extracted = extract_json_substring(text)
    data = json.loads(extracted)
    if not isinstance(data, dict):
        raise TypeError("Parsed JSON is not a dictionary.")
    for key in required_keys:
        if key not in data:
            raise KeyError(f"Missing required key '{key}' in JSON response.")
    return data

def generate_cot(backend: ModelBackend, prompt: str, temperature: float = 0.0) -> CoTTrace:
    """Generates the baseline CoT trace for a prompt.
    Includes one repair retry if JSON parsing fails.
    """
    logger.info("Generating baseline Chain of Thought (CoT)...")
    formatted_prompt = STAGE1_PROMPT_TEMPLATE.format(prompt=prompt)
    raw_response = backend.generate(formatted_prompt, temperature)
    
    try:
        logger.info("Parsing baseline JSON response...")
        data = parse_json_keys(raw_response, ["steps", "answer"])
    except Exception as e:
        logger.warning("Stage 1 JSON parsing failed: %s. Initiating repair retry...", e)
        logger.debug("Failed raw baseline output: %s", raw_response)
        
        # Repair attempt
        repair_prompt = f"""Your previous response could not be parsed as valid JSON or was missing required keys.
The parsing error was: {str(e)}

The prompt was: {prompt}

Your previous output was:
{raw_response}

Return ONLY a valid JSON object matching the schema:
{{"steps": [list of strings], "answer": "final answer string"}}
Do not include any prefix, suffix, or markdown formatting fences."""
        raw_response = backend.generate(repair_prompt, temperature)
        logger.info("Parsing repaired baseline JSON response...")
        data = parse_json_keys(raw_response, ["steps", "answer"])

    steps = [Step(index=i+1, text=text) for i, text in enumerate(data["steps"])]
    logger.info("Baseline CoT successfully generated with %d steps.", len(steps))
    return CoTTrace(
        prompt=prompt,
        steps=steps,
        answer=str(data["answer"]).strip(),
        raw_response=raw_response
    )

def query_permuted_answer(backend: ModelBackend, steps: List[Step], temperature: float = 0.0) -> str:
    """Asks the model for the final answer implied by a specific step ordering.
    Includes one repair retry if JSON parsing fails.
    """
    logger.info("Querying answer for permuted steps...")
    steps_formatted = "\n".join(f"{i+1}. {step.text}" for i, step in enumerate(steps))
    formatted_prompt = STAGE2_PROMPT_TEMPLATE.format(steps_list_formatted=steps_formatted)
    raw_response = backend.generate(formatted_prompt, temperature)

    try:
        logger.info("Parsing permuted answer JSON response...")
        data = parse_json_keys(raw_response, ["answer"])
    except Exception as e:
        logger.warning("Stage 2 JSON parsing failed: %s. Initiating repair retry...", e)
        logger.debug("Failed raw permuted output: %s", raw_response)
        
        # Repair attempt
        repair_prompt = f"""Your previous response could not be parsed as valid JSON or was missing required keys.
The parsing error was: {str(e)}

Steps:
{steps_formatted}

Your previous output was:
{raw_response}

Return ONLY a valid JSON object matching the schema:
{{"answer": "final answer string"}}
Do not include any prefix, suffix, or markdown formatting fences."""
        raw_response = backend.generate(repair_prompt, temperature)
        logger.info("Parsing repaired permuted answer JSON response...")
        data = parse_json_keys(raw_response, ["answer"])

    ans = str(data["answer"]).strip()
    logger.info("Permuted answer successfully parsed: %s", ans)
    return ans
