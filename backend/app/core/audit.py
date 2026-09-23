"""
Audit logging skeleton (BRD BR-05, PRD FR-013).

Every material user/model/source/output event must be reconstructable:
actor, case, source/output IDs, model/prompt/config version.

This is a minimal in-process stub for local development. Production
must write to centrally protected, tamper-resistant storage (PRD §9 Audit)
and must not log sensitive prompt/data content (SEC-08).
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

logger = logging.getLogger("audit")


def record_event(
    *,
    actor_id: str,
    action: str,
    case_id: str | None = None,
    source_id: str | None = None,
    output_id: str | None = None,
    model_version: str | None = None,
    config_version: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> None:
    """Record an auditable event. Replace with durable storage before production."""
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "actor_id": actor_id,
        "action": action,
        "case_id": case_id,
        "source_id": source_id,
        "output_id": output_id,
        "model_version": model_version,
        "config_version": config_version,
        "metadata": metadata or {},
    }
    logger.info("audit_event", extra={"audit_event": event})
