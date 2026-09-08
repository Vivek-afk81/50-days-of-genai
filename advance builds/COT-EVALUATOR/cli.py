import argparse
import os
import sys
import yaml
from cot_evaluator.backend import GroqBackend
from cot_evaluator.runner import run_evaluation
from cot_evaluator.report import print_robustness_report

def main():
    parser = argparse.ArgumentParser(description="CoT Permutation Evaluator CLI")
    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="The logic/math prompt to generate CoT and evaluate."
    )
    parser.add_argument(
        "--config",
        type=str,
        default="config.yaml",
        help="Path to the config YAML file (default: config.yaml)."
    )
    args = parser.parse_args()

    # Load config
    config_path = args.config
    current_dir = os.path.dirname(os.path.abspath(__file__))
    actual_config_path = config_path if os.path.isabs(config_path) else os.path.join(current_dir, config_path)
    
    # Configure logging
    logs_dir = os.path.join(current_dir, "logs")
    os.makedirs(logs_dir, exist_ok=True)
    log_file = os.path.join(logs_dir, "evaluator.log")
    
    import logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8")
        ]
    )
    logger = logging.getLogger("cot_evaluator")
    logger.info("=" * 72)
    logger.info("CoT Permutation Evaluator started")
    logger.info("Prompt: %s", args.prompt)
    
    if not os.path.exists(actual_config_path):
        # Allow running even if config.yaml doesn't exist by using defaults
        config = {}
    else:
        with open(actual_config_path, "r") as f:
            config = yaml.safe_load(f) or {}

    model_name = config.get("model_name", "llama-3.1-8b-instant")
    shuffle_trials = config.get("shuffle_trials", 5)
    partial_shuffle_trials = config.get("partial_shuffle_trials", 5)
    partial_k = config.get("partial_k", 2)

    logger.info("Loaded config: model=%s, shuffle_trials=%d, partial_shuffle_trials=%d, partial_k=%d",
                model_name, shuffle_trials, partial_shuffle_trials, partial_k)

    # Initialize backend
    try:
        backend = GroqBackend(model_name=model_name)
    except KeyError as e:
        logger.error("Initialization failed: %s", e)
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Starting CoT Permutation Evaluator using model: {model_name}...")
    print("Generating baseline CoT and running permutations. Please wait...")

    try:
        report = run_evaluation(
            backend=backend,
            prompt=args.prompt,
            shuffle_trials=shuffle_trials,
            partial_shuffle_trials=partial_shuffle_trials,
            partial_k=partial_k
        )
        print_robustness_report(report)
        logger.info("Evaluation completed successfully")
    except Exception as e:
        logger.exception("An error occurred during evaluation: %s", e)
        print(f"\nAn error occurred during evaluation: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
