from collections.abc import Sequence

from waguri.optimization.token_budget import estimate_tokens


def fit_context(context: Sequence[str], max_tokens: int) -> list[str]:
    """Keep the longest source-order prefix that fits the approximate token budget."""
    if max_tokens < 0:
        raise ValueError("max_tokens must not be negative.")

    selected: list[str] = []
    tokens_used = 0
    for item in context:
        item_tokens = estimate_tokens(item)
        if tokens_used + item_tokens > max_tokens:
            break
        selected.append(item)
        tokens_used += item_tokens
    return selected
