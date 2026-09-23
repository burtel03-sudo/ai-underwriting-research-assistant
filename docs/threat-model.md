# Threat model / security matrix

Status: placeholder. Owner: security (update on architecture/tool/data change, per PRD §15).

Required coverage per SEC-01: users, APIs, data stores, model endpoints,
retrieval, tools, and CI/CD.

TODO before Phase 1 build start (PRD §13 phase gate "MVP build start"
requires this to be approved):
- Enumerate trust boundaries and data flows.
- Apply STRIDE (or equivalent) per component.
- Cover AI-specific risks: prompt injection (SEC-07, AI-03), tool misuse
  (AI-06), data leakage to the LLM provider (AI-09).
- Map each identified risk to a control and an owner.
