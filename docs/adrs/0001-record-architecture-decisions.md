# ADR 0001: Record architecture decisions

## Status
Accepted

## Context
The PRD (§15) requires an architecture diagram plus ADRs, owned by
architecture/engineering and updated on every architectural decision.

## Decision
Use lightweight ADRs (this format) stored under `docs/adrs/`, numbered
sequentially. Each material architectural decision (framework choice,
data model, service boundary, security control) gets its own ADR.

## Consequences
Decisions and their rationale are traceable over time, supporting the
auditability goals in BRD BR-05.
