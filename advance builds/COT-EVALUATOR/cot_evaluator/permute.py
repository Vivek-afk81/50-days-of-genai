import random
from typing import List
from cot_evaluator.models import Step

def reverse(steps: List[Step]) -> List[Step]:
    """Returns a new list of steps in reversed order."""
    return list(reversed(steps))

def shuffle(steps: List[Step], seed: int = None) -> List[Step]:
    """Returns a new list of steps completely shuffled.
    Uses target seed if provided to ensure reproducibility."""
    shuffled_steps = list(steps)
    if seed is not None:
        random.seed(seed)
    random.shuffle(shuffled_steps)
    return shuffled_steps

def partial_shuffle(steps: List[Step], k: int, seed: int = None) -> List[Step]:
    """Returns a new list of steps with `k` random random pairwise swaps.
    If the list has fewer than 2 elements, returns a copy of the list.
    Uses target seed if provided to ensure reproducibility."""
    shuffled_steps = list(steps)
    n = len(shuffled_steps)
    if n < 2 or k <= 0:
        return shuffled_steps

    if seed is not None:
        random.seed(seed)

    for _ in range(k):
        idx1 = random.randint(0, n - 1)
        idx2 = random.randint(0, n - 1)
        shuffled_steps[idx1], shuffled_steps[idx2] = shuffled_steps[idx2], shuffled_steps[idx1]

    return shuffled_steps
