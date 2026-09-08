import unittest
from cot_evaluator.models import Step
from cot_evaluator.permute import reverse, shuffle, partial_shuffle

class TestCoTEvaluator(unittest.TestCase):
    def setUp(self):
        self.steps = [
            Step(1, "Step 1 text"),
            Step(2, "Step 2 text"),
            Step(3, "Step 3 text"),
            Step(4, "Step 4 text"),
            Step(5, "Step 5 text"),
        ]

    def test_reverse(self):
        reversed_steps = reverse(self.steps)
        self.assertEqual(len(reversed_steps), 5)
        self.assertEqual([s.index for s in reversed_steps], [5, 4, 3, 2, 1])
        # Ensure original was not mutated
        self.assertEqual([s.index for s in self.steps], [1, 2, 3, 4, 5])

    def test_shuffle(self):
        # With seed, shuffle should be reproducible
        shuffled1 = shuffle(self.steps, seed=42)
        shuffled2 = shuffle(self.steps, seed=42)
        self.assertEqual([s.index for s in shuffled1], [s.index for s in shuffled2])
        # Check that shuffle actually permuted
        self.assertNotEqual([s.index for s in shuffled1], [1, 2, 3, 4, 5])
        self.assertEqual(set(s.index for s in shuffled1), {1, 2, 3, 4, 5})

    def test_partial_shuffle(self):
        # With seed, partial shuffle should be reproducible
        partial1 = partial_shuffle(self.steps, k=2, seed=10)
        partial2 = partial_shuffle(self.steps, k=2, seed=10)
        self.assertEqual([s.index for s in partial1], [s.index for s in partial2])
        self.assertEqual(set(s.index for s in partial1), {1, 2, 3, 4, 5})

        # Test empty/short list
        short = [Step(1, "Only one")]
        self.assertEqual(partial_shuffle(short, k=2), short)
        self.assertEqual(partial_shuffle([], k=2), [])

    def test_generator_success(self):
        from cot_evaluator.backend import MockBackend
        from cot_evaluator.generator import generate_cot

        mock_response = '{"steps": ["Step 1 text", "Step 2 text"], "answer": "42"}'
        backend = MockBackend(mock_response)
        trace = generate_cot(backend, "What is the meaning of life?")
        
        self.assertEqual(trace.answer, "42")
        self.assertEqual(len(trace.steps), 2)
        self.assertEqual(trace.steps[0].text, "Step 1 text")
        self.assertEqual(trace.steps[1].text, "Step 2 text")
        self.assertEqual(backend.call_count, 1)

    def test_generator_repair_success(self):
        from cot_evaluator.backend import MockBackend
        from cot_evaluator.generator import generate_cot

        # First returns malformed JSON, second returns corrected JSON
        responses = [
            "This is not JSON at all!",
            '{"steps": ["Step A", "Step B"], "answer": "success"}'
        ]
        backend = MockBackend(responses)
        trace = generate_cot(backend, "Test prompt")

        self.assertEqual(trace.answer, "success")
        self.assertEqual(len(trace.steps), 2)
        self.assertEqual(backend.call_count, 2)

    def test_query_permuted_answer_success(self):
        from cot_evaluator.backend import MockBackend
        from cot_evaluator.generator import query_permuted_answer
        from cot_evaluator.models import Step

        backend = MockBackend('{"answer": "99"}')
        steps = [Step(1, "S1"), Step(2, "S2")]
        ans = query_permuted_answer(backend, steps)
        self.assertEqual(ans, "99")
        self.assertEqual(backend.call_count, 1)

    def test_query_permuted_answer_repair_success(self):
        from cot_evaluator.backend import MockBackend
        from cot_evaluator.generator import query_permuted_answer
        from cot_evaluator.models import Step

        responses = [
            '{"wrong_key": "oops"}',
            '{"answer": "100"}'
        ]
        backend = MockBackend(responses)
        steps = [Step(1, "S1")]
        ans = query_permuted_answer(backend, steps)
        self.assertEqual(ans, "100")
        self.assertEqual(backend.call_count, 2)

    def test_runner_mock_evaluation(self):
        from cot_evaluator.backend import MockBackend
        from cot_evaluator.runner import run_evaluation

        # Mock responses
        responses = [
            '{"steps": ["S1", "S2"], "answer": "42"}', # Baseline
            '{"answer": "42"}', # Reversed
            '{"answer": "42"}', # Shuffled T1
            '{"answer": "41"}', # Shuffled T2
            '{"answer": "42"}', # Partial T1
            '{"answer": "42"}', # Partial T2
        ]
        backend = MockBackend(responses)
        report = run_evaluation(
            backend=backend,
            prompt="Dummy math",
            shuffle_trials=2,
            partial_shuffle_trials=2,
            partial_k=1
        )
        self.assertEqual(report.baseline.answer, "42")
        self.assertEqual(len(report.results), 5) # 1 reversed + 2 shuffled + 2 partial
        
        matches = [r.matches_baseline for r in report.results]
        self.assertEqual(matches, [True, True, False, True, True])

if __name__ == '__main__':
    unittest.main()
