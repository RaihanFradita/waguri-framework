from waguri.validation.evidence import check_evidence

def test_claim_found_in_evidence():
    result = check_evidence(
        claim="Revenue was Rp50 million.",
        evidence=["The report says revenue was Rp50 million."],
    )

    assert result.status == "supported"
    assert result.matched_evidence is not None

def test_different_amount_is_uncertain():
    result = check_evidence(
        claim="Revenue was Rp500 million.",
        evidence=["The report says revenue was Rp50 million."],
    )

    assert result.status == "uncertain"
    assert result.matched_evidence is None

def test_empty_claim_is_uncertain():
    result = check_evidence(
        claim="   ",
        evidence=["Revenue was Rp50 million."],
    )

    assert result.status == "uncertain"
    assert result.reason == "Claim is empty."

def test_matching_ignores_case_and_extra_whitespace():
    result = check_evidence(
        claim="REVENUE WAS Rp50 MILLION.",
        evidence=["The report says Revenue   was Rp50 million."],
    )

    assert result.status == "supported"
    assert result.matched_evidence is not None

def test_negated_evidence_is_not_marked_supported():
    result = check_evidence(
        claim="Revenue was Rp50 million.",
        evidence=["Revenue was not Rp50 million."],
    )

    assert result.status == "uncertain"

def test_missing_evidence_is_uncertain():
    result = check_evidence(
        claim="Revenue was Rp50 million.",
        evidence=[],
    )

    assert result.status == "uncertain"

def test_blank_evidence_is_uncertain():
    result = check_evidence(
        claim="Revenue was Rp50 million.",
        evidence=["  "],
    )

    assert result.status == "uncertain"