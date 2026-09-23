"""
Centralized application configuration.

Per PRD SEC-02: no secrets in code. Values are read from environment
variables (see .env.example); never hardcode credentials here.
"""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "development"

    # Database (PostgreSQL + pgvector per PRD §12)
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/underwriting"

    # Auth (OIDC/SAML enterprise SSO per FR-001; unset in dev until an IdP is approved)
    oidc_issuer_url: str | None = None
    oidc_client_id: str | None = None
    oidc_client_secret: str | None = None

    # LLM provider (thin adapter per PRD principle — no provider lock-in)
    llm_provider: str = "unset"
    llm_api_key: str | None = None

    cors_allow_origins: list[str] = ["http://localhost:3000"]


@lru_cache
def get_settings() -> Settings:
    return Settings()
