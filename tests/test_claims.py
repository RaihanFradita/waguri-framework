from waguri.validation.claims import split_claims

def test_split_multiple_sentences():
    result = split_claims(
        "Revenue was Rp50 million. Expenses were Rp20 million."
    )

    assert result == [
        "Revenue was Rp50 million.",
        "Expenses were Rp20 million.",
    ]

def test_single_sentence():
    assert split_claims("Revenue was Rp50 million.") == [
        "Revenue was Rp50 million."
    ]

def test_empty_answer():
    assert split_claims("   ") == []

def test_question_marks_split_sentences():
    result = split_claims(
        "What is the revenue? It is Rp50 million."
    )

    assert result == [
        "What is the revenue?",
        "It is Rp50 million.",
    ]