from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class BenchmarkCase:
    prompt: str
    expected: str


@dataclass(frozen=True)
class BenchmarkResult:
    total: int
    passed: int

    @property
    def accuracy(self) -> float:
        return self.passed / self.total if self.total else 0.0


def evaluate(
    cases: Sequence[BenchmarkCase],
    responses: Sequence[str],
) -> BenchmarkResult:
    if len(cases) != len(responses):
        raise ValueError("The number of responses must match the number of cases.")

    passed = sum(
        case.expected.strip().casefold() == response.strip().casefold()
        for case, response in zip(cases, responses)
    )
    return BenchmarkResult(total=len(cases), passed=passed)
