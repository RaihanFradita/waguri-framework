import pytest

from waguri.evaluation import BenchmarkCase, evaluate


def test_evaluate_returns_case_insensitive_exact_match_accuracy():
    result = evaluate(
        [BenchmarkCase(prompt="Q1", expected="Answer"), BenchmarkCase("Q2", "No")],
        ["answer", "Different"],
    )

    assert result.total == 2
    assert result.passed == 1
    assert result.accuracy == 0.5


def test_evaluate_rejects_mismatched_response_count():
    with pytest.raises(ValueError, match="must match"):
        evaluate([BenchmarkCase(prompt="Q", expected="A")], [])
