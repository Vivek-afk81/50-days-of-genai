from collections import defaultdict
from cot_evaluator.models import EvalReport

def print_robustness_report(report: EvalReport):
    """Formats an EvalReport into a robustness table and prints it to stdout."""
    print("-" * 72)
    print("CoT PERMUTATION EVALUATOR REPORT")
    print("-" * 72)
    print(f"Prompt: {report.prompt}")
    print(f"Baseline Answer: {report.baseline.answer}")
    print(f"Number of CoT Steps: {len(report.baseline.steps)}")
    print("-" * 72)
    print("Baseline Steps:")
    for step in report.baseline.steps:
        print(f"  {step.index}. {step.text}")
    print("-" * 72)

    # Group results by permutation type
    by_type = defaultdict(list)
    for result in report.results:
        by_type[result.permutation_type].append(result)

    headers = [
        "Permutation Type",
        "Total Trials",
        "Matches Baseline",
        "Robustness Score"
    ]
    
    # Print table header
    print(f"{headers[0]:<20} | {headers[1]:<12} | {headers[2]:<16} | {headers[3]:<16}")
    print("-" * 72)

    for p_type in ["reversed", "shuffled", "partial"]:
        results = by_type.get(p_type, [])
        if not results:
            continue
        total = len(results)
        matches = sum(1 for r in results if r.matches_baseline)
        score = (matches / total) * 100 if total > 0 else 0.0
        print(f"{p_type:<20} | {total:<12} | {matches:<16} | {score:>14.2f}%")
        
    print("-" * 72)
