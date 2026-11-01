from waguri.adapters.demo import DemoAdapter
from waguri.adapters.ollama import OllamaAdapter


def test_demo_adapter_returns_revenue_response():
    response = DemoAdapter().generate("What is the revenue?")

    assert response == "The reported revenue is Rp50 million."


def test_demo_adapter_reports_insufficient_information():
    response = DemoAdapter().generate("What is the employee count?")

    assert response == "There is insufficient information to answer."


def test_ollama_adapter_requires_a_model_name():
    import pytest

    with pytest.raises(ValueError, match="Model name must not be empty"):
        OllamaAdapter(model=" ")
