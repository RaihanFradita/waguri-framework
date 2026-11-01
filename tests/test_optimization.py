import pytest

from waguri.optimization import ResponseCache, estimate_tokens, fit_context


def test_estimate_tokens_uses_approximate_four_to_one_ratio():
    assert estimate_tokens("abcdefgh") == 2
    assert estimate_tokens("") == 0


def test_fit_context_preserves_order_and_respects_budget():
    assert fit_context(["1234", "5678", "90"], max_tokens=2) == ["1234", "5678"]


def test_fit_context_rejects_negative_budget():
    with pytest.raises(ValueError, match="must not be negative"):
        fit_context(["context"], max_tokens=-1)


def test_response_cache_evicts_least_recently_used_entry():
    cache = ResponseCache(maxsize=2)
    cache.set("first", "one")
    cache.set("second", "two")
    assert cache.get("first") == "one"
    cache.set("third", "three")

    assert cache.get("first") == "one"
    assert cache.get("second") is None
