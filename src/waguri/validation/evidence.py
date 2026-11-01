import re
from dataclasses import dataclass
from typing import Literal

EvidenceStatus = Literal["supported", "unsupported", "uncertain"]
_NEGATION_PATTERN = re.compile(
    r"(?<!\w)(not|never|no|without|cannot|can't|isn't|wasn't|doesn't|didn't|don't|won't|aren't|weren't|hardly)(?!\w)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class EvidenceCheck:
    status: EvidenceStatus
    matched_evidence: str | None
    reason: str


def normalize_text(text: str) -> str:
    """Normalize text for basic, deterministic comparison."""
    text = text.casefold()
    return re.sub(r"\s+", " ", text).strip()


def _strip_negation_words(text: str) -> str:
    return _NEGATION_PATTERN.sub("", text)

def check_evidence(
    claim: str,
    evidence: list[str],
) -> EvidenceCheck:
    """
    Check whether a claim is supported by the supplied evidence.

    This is a baseline check, not semantic fact verification; it explicitly
    distinguishes contradicted evidence from unsupported or uncertain results.
    """
    normalized_claim = normalize_text(claim)

    if not normalized_claim:
        return EvidenceCheck(
            status="uncertain",
            matched_evidence=None,
            reason="Claim is empty.",
        )

    usable_evidence = [item for item in evidence if item and item.strip()]
    if not usable_evidence:
        return EvidenceCheck(
            status="uncertain",
            matched_evidence=None,
            reason="No usable evidence was provided.",
        )

    for item in usable_evidence:
        normalized_evidence = normalize_text(item)
        if not normalized_evidence:
            continue

        match_index = normalized_evidence.find(normalized_claim)
        if match_index != -1:
            context = normalized_evidence[max(0, match_index - 32) : match_index + len(normalized_claim) + 32]
            if _NEGATION_PATTERN.search(context):
                return EvidenceCheck(
                    status="unsupported",
                    matched_evidence=item,
                    reason="Claim is contradicted by a negated statement in the evidence.",
                )
            return EvidenceCheck(
                status="supported",
                matched_evidence=item,
                reason="Exact normalized text match found.",
            )

        if normalized_claim in _strip_negation_words(normalized_evidence):
            return EvidenceCheck(
                status="unsupported",
                matched_evidence=item,
                reason="Claim appears only in a negated or contradicted statement.",
            )

    return EvidenceCheck(
        status="uncertain",
        matched_evidence=None,
        reason="No exact text match; semantic support is unknown.",
    )