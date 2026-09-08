from dataclasses import dataclass
from typing import List, Optional

@dataclass(frozen=True)
class Step:
    index: int
    text: str

@dataclass(frozen=True)
class CoTTrace:
    prompt: str
    steps: List[Step]
    answer: str
    raw_response: str

@dataclass(frozen=True)
class EvalResult:
    permutation_type: str
    trial: int
    order: List[int]
    answer: str
    matches_baseline: bool
    first_divergence_step: Optional[int] = None

@dataclass(frozen=True)
class EvalReport:
    prompt: str
    baseline: CoTTrace
    results: List[EvalResult]
