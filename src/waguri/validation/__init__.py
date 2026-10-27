import re
from dataclasses import dataclass

@dataclass(frozen=True)
class EvidenceCheck:
    supported: bool
    matched_evidence: str | None
    reason: str

def normalize_text(text: str) -> str:
    """Normalize text for basic, deterministic comparison."""
    text = text.casefold()
    return re.sub(r"\s+", " ", text).strip()

def check_evidence(
    claim: str,
    evidence: list[str],
) -> EvidenceCheck:
    """
    Check whether the normalized claim appears in supplied evidence.

    This is a strict text-match baseline, not semantic verification.
    """
    normalized_claim = normalize_text(claim)

    if not normalized_claim:
        return EvidenceCheck(
            supported=False,
            matched_evidence=None,
            reason="Claim is empty.",
        )

    for item in evidence:
        normalized_evidence = normalize_text(item)

        if normalized_claim in normalized_evidence:
            return EvidenceCheck(
                supported=True,
                matched_evidence=item,
                reason="Exact normalized text match found.",
            )

    return EvidenceCheck(
        supported=False,
        matched_evidence=None,
        reason="No exact normalized text match found.",
    )