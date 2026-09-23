"""
Case schemas (PRD FR-003: create/view/update/archive with owner/status/version).
Validated with Pydantic per AI-04 / API and schema principles (PRD §13).
"""
from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class CaseStatus(str, Enum):
    draft = "draft"
    in_review = "in_review"
    completed = "completed"
    archived = "archived"


class CaseCreate(BaseModel):
    company_name: str = Field(..., min_length=1, max_length=256)
    owner_id: str


class CaseRead(BaseModel):
    id: str
    company_name: str
    owner_id: str
    status: CaseStatus
    version: int
    created_at: datetime
    updated_at: datetime
