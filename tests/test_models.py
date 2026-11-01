from waguri.models import ClaimResult, WaguriResult

def test_claim_result_accepts_supported_status():
    claim = ClaimResult(
        text="Revenue was Rp50 million.",
        status="supported",
        evidence_ids=["0"],
        reason="Exact text match found.",
    )

    assert claim.status == "supported"
    assert claim.evidence_ids == ["0"]

def test_claim_result_accepts_uncertain_status():
    claim = ClaimResult(
        text="Revenue was Rp500 million.",
        status="uncertain",
        evidence_ids=[],
        reason="No exact text match.",
    )

    assert claim.status == "uncertain"

def test_waguri_result_defaults_to_empty_claims():
    result = WaguriResult(
        answer="Insufficient information.",
        status="needs_review",
    )

    assert result.claims == []
    assert result.retries == 0