from typing import Literal
from pydantic import BaseModel, Field

EvidenceStatus = Literal["supported", "unsupported", "uncertain"]
ResponseStatus = Literal["verified", "needs_review", "rejected"]

class ClaimResult(BaseModel):
    text: str
    status: EvidenceStatus
    evidence_ids: list[str] = Field(default_factory=list)
    reason: str | None = None

class WaguriResult(BaseModel):
    answer: str
    status: ResponseStatus
    claims: list[ClaimResult] = Field(default_factory=list)
    metrics: dict[str, int | float] = Field(default_factory=dict)
    retries: int = 0