from fastapi import APIRouter

router = APIRouter()


@router.get("/healthz")
def healthz() -> dict[str, str]:
    """Liveness probe."""
    return {"status": "ok"}


@router.get("/readyz")
def readyz() -> dict[str, str]:
    """Readiness probe. Extend to check DB/vector index/LLM provider connectivity."""
    return {"status": "ready"}
