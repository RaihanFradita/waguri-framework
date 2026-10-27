import re
from dataclasses import dataclass
from typing import Literal

EvidenceStatus = Literal["supported", "unsupported", "uncertain"]

@dataclass(frozen=True)
class EvidenceCheck:
    status: EvidenceStatus
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
    Perform strict text matching against supplied evidence.

    This is a baseline check, not semantic fact verification.
    """
    normalized_claim = normalize_text(claim)

    if not normalized_claim:
        return EvidenceCheck(
            status="uncertain",
            matched_evidence=None,
            reason="Claim is empty.",
        )

    if not evidence or not any(item.strip() for item in evidence):
        return EvidenceCheck(
            status="uncertain",
            matched_evidence=None,
            reason="No usable evidence was provided.",
        )

    for item in evidence:
        normalized_evidence = normalize_text(item)

        if normalized_claim in normalized_evidence:
            return EvidenceCheck(
                status="supported",
                matched_evidence=item,
                reason="Exact normalized text match found.",
            )

    return EvidenceCheck(
        status="uncertain",
        matched_evidence=None,
        reason="No exact text match; semantic support is unknown.",
    )