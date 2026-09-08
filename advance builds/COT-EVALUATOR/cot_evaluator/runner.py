import logging
from typing import List
from cot_evaluator.models import Step, CoTTrace, EvalResult, EvalReport
from cot_evaluator.backend import ModelBackend
from cot_evaluator.generator import generate_cot, query_permuted_answer
from cot_evaluator import permute

logger = logging.getLogger("cot_evaluator.runner")

def run_evaluation(
    backend: ModelBackend,
    prompt: str,
    shuffle_trials: int = 5,
    partial_shuffle_trials: int = 5,
    partial_k: int = 2,
    temperature: float = 0.0
) -> EvalReport:
    """Ties generation -> permutation -> re-run -> collection together.
    Returns an EvalReport.
    """
    logger.info("Starting CoT evaluation run on prompt.")
    # 1. Generate baseline CoT
    baseline = generate_cot(backend, prompt, temperature)
    results = []

    # 2. Permutation: Reverse (1 trial)
    logger.info("Running reversed permutation trial...")
    reversed_steps = permute.reverse(baseline.steps)
    reversed_order = [s.index for s in reversed_steps]
    reversed_ans = query_permuted_answer(backend, reversed_steps, temperature)
    results.append(EvalResult(
        permutation_type="reversed",
        trial=1,
        order=reversed_order,
        answer=reversed_ans,
        matches_baseline=(reversed_ans == baseline.answer)
    ))
    logger.info("Reversed trial completed. Match baseline: %s", reversed_ans == baseline.answer)

    # 3. Permutation: Shuffle (shuffle_trials)
    logger.info("Running shuffled permutation (%d trials)...", shuffle_trials)
    for t in range(1, shuffle_trials + 1):
        logger.info("Running shuffled trial %d/%d...", t, shuffle_trials)
        shuffled_steps = permute.shuffle(baseline.steps, seed=t)
        shuffled_order = [s.index for s in shuffled_steps]
        shuffled_ans = query_permuted_answer(backend, shuffled_steps, temperature)
        results.append(EvalResult(
            permutation_type="shuffled",
            trial=t,
            order=shuffled_order,
            answer=shuffled_ans,
            matches_baseline=(shuffled_ans == baseline.answer)
        ))
        logger.info("Shuffled trial %d completed. Match baseline: %s", t, shuffled_ans == baseline.answer)

    # 4. Permutation: Partial Shuffle (partial_shuffle_trials)
    logger.info("Running partial shuffled permutation (%d trials, k=%d)...", partial_shuffle_trials, partial_k)
    for t in range(1, partial_shuffle_trials + 1):
        logger.info("Running partial shuffled trial %d/%d...", t, partial_shuffle_trials)
        partial_steps = permute.partial_shuffle(baseline.steps, k=partial_k, seed=t + 100)
        partial_order = [s.index for s in partial_steps]
        partial_ans = query_permuted_answer(backend, partial_steps, temperature)
        results.append(EvalResult(
            permutation_type="partial",
            trial=t,
            order=partial_order,
            answer=partial_ans,
            matches_baseline=(partial_ans == baseline.answer)
        ))
        logger.info("Partial trial %d completed. Match baseline: %s", t, partial_ans == baseline.answer)

    logger.info("CoT evaluation run completed. Total results collected: %d", len(results))
    return EvalReport(prompt=prompt, baseline=baseline, results=results)
