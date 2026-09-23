# Architecture

Status: placeholder. Owner: architecture/engineering (update on every architectural decision, per PRD §15).

See PRD §11 (Logical architecture) and §12 (Recommended stack) for the current baseline:

```
Browser UI (Next.js)
  -> API gateway / backend (FastAPI)
    -> authorization/policy layer
      -> case service
      -> document service
      -> retrieval service
      -> AI orchestration service
        -> PostgreSQL / object storage / vector index (pgvector)
        -> approved external/internal data connectors
        -> approved LLM provider (thin adapter)

Cross-cutting: identity, secrets, feature flags, audit logging, telemetry,
evaluation service, CI/CD.
```

TODO: add a real diagram (`docs/architecture.png` or Mermaid) and record decisions as ADRs under `docs/adrs/`.
