import pytest
from waguri import WaguriClient

class FakeModel:
    def __init__(self, response: str):
        self.response = response

    def generate(self, prompt: str) -> str:
        return self.response

def test_answer_includes_evidence_check():
    client = WaguriClient(
        model=FakeModel("Revenue was Rp50 million.")
    )

    result = client.answer(
        question="What is the reported revenue?",
        context=["Revenue was Rp50 million."],
    )

    assert result.answer == "Revenue was Rp50 million."
    assert result.status == "needs_review"
    assert len(result.claims) == 1
    assert result.claims[0].status == "supported"
    assert result.claims[0].evidence_ids == ["0"]

def test_empty_question_is_rejected():
    client = WaguriClient(model=FakeModel("Some answer"))

    with pytest.raises(ValueError, match="Question must not be empty"):
        client.answer(question="   ")

def test_empty_model_response_is_rejected():
    client = WaguriClient(model=FakeModel(""))

    result = client.answer(question="What is the revenue?")

    assert result.status == "rejected"
    assert result.answer == ""

def test_answer_without_matching_evidence_needs_review():
    client = WaguriClient(
        model=FakeModel("Revenue was Rp500 million.")
    )

    result = client.answer(
        question="What is the reported revenue?",
        context=["Revenue was Rp50 million."],
    )

    assert result.status == "needs_review"
    assert result.claims[0].status == "uncertain"
    assert result.claims[0].evidence_ids == []
    assert result.metrics["evidence_match"] == 0