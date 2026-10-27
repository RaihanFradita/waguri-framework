from waguri.adapters.base import ModelAdapter
from waguri.models import ClaimResult, WaguriResult
from waguri.validation.evidence import check_evidence

class WaguriClient:
    def __init__(self, model: ModelAdapter):
        self.model = model

    def answer(
        self,
        question: str,
        context: list[str] | None = None,
    ) -> WaguriResult:
        if not question.strip():
            raise ValueError("Question must not be empty.")

        evidence = context or []

        prompt = (
            "Answer concisely. Use only the supplied context. "
            "If information is insufficient, say so.\n\n"
            f"Question: {question}\n"
            f"Context:\n" + "\n".join(evidence)
        )

        answer = self.model.generate(prompt).strip()

        if not answer:
            return WaguriResult(
                answer="",
                status="rejected",
            )

        check = check_evidence(answer, evidence)

        claim = ClaimResult(
            text=answer,
            status=check.status,
            evidence_ids=(
                [str(evidence.index(check.matched_evidence))]
                if check.matched_evidence is not None
                else []
            ),
            reason=check.reason,
        )

        return WaguriResult(
            answer=answer,
            status="needs_review",
            claims=[claim],
            metrics={
                "evidence_match": int(check.status == "supported"),
            },
        )