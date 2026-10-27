import re

def split_claims(answer: str) -> list[str]:
    """
    Split an answer into sentence-like claims.

    This is a lightweight baseline, not semantic claim extraction.
    """
    if not answer or not answer.strip():
        return []

    parts = re.split(r"(?<=[.!?])\s+", answer.strip())
    return [part.strip() for part in parts if part.strip()]