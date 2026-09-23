"""
Case management endpoints (PRD FR-003, FR-002).

TODO before this is usable:
- Wire real authentication (FR-001: enterprise SSO) and extract the caller's
  identity/role instead of the placeholder below.
- Enforce RBAC + case/data scope checks on every route (FR-002) — do not
  rely on the UI to hide unauthorized cases.
- Replace the in-memory store with PostgreSQL persistence.
- Call app.core.audit.record_event on every create/update/archive (BR-05).
"""
from __future__ import annotations

import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, status

from app.core.audit import record_event
from app.schemas.case import CaseCreate, CaseRead, CaseStatus

router = APIRouter()

# Placeholder store — replace with a real repository/DB session (PRD §12: PostgreSQL).
_CASES: dict[str, CaseRead] = {}


@router.post("", response_model=CaseRead, status_code=status.HTTP_201_CREATED)
def create_case(payload: CaseCreate) -> CaseRead:
    now = datetime.now(timezone.utc)
    case = CaseRead(
        id=str(uuid.uuid4()),
        company_name=payload.company_name,
        owner_id=payload.owner_id,
        status=CaseStatus.draft,
        version=1,
        created_at=now,
        updated_at=now,
    )
    _CASES[case.id] = case
    record_event(actor_id=payload.owner_id, action="case.create", case_id=case.id)
    return case


@router.get("/{case_id}", response_model=CaseRead)
def get_case(case_id: str) -> CaseRead:
    case = _CASES.get(case_id)
    if case is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
    return case


@router.get("", response_model=list[CaseRead])
def list_cases() -> list[CaseRead]:
    return list(_CASES.values())
