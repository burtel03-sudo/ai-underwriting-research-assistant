"""
Application entrypoint.

Logical architecture (PRD §11):
Browser UI -> API gateway/backend -> authorization/policy layer ->
case service + document service + retrieval service + AI orchestration service
-> PostgreSQL / object storage / vector index -> approved connectors + LLM provider.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import cases, health
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title="AI Underwriting Research Assistant API",
    version="0.1.0",
    description=(
        "Evidence-first underwriting research workspace. "
        "Decision support only — see BRD BR-01: no autonomous credit decisions."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["health"])
app.include_router(cases.router, prefix="/api/v1/cases", tags=["cases"])
