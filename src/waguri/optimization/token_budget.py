def estimate_tokens(text: str) -> int:
    """Estimate token count conservatively using an approximate 4:1 ratio."""
    if not text:
        return 0
    return (len(text) + 3) // 4
