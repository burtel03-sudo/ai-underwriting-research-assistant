# AI Underwriting Research Assistant

Evidence-first research workspace for underwriters. Decision support only —
no autonomous credit-limit decisions (see [BRD](02_BRD_AI_Underwriting_Research_Assistant.docx) BR-01).

Full requirements: [BRD](02_BRD_AI_Underwriting_Research_Assistant.docx) ·
[PRD](<03_PRD_AI_Underwriting_Research_Assistant (1).docx>) ·
project guide for Claude Code: [CLAUDE.md](CLAUDE.md)

## Status

Phase 0/1 scaffold. No production functionality yet — see [PRD §18 open
decisions](<03_PRD_AI_Underwriting_Research_Assistant (1).docx>) before
building further.

## Structure

```
frontend/   Next.js + TypeScript UI
backend/    FastAPI + Pydantic API
infra/      Terraform (production infra — not yet configured)
docs/       Architecture, ADRs, threat model, data dictionary
```

## Local development

Prerequisites: Node 20+, Python 3.12+, Docker.

```powershell
# 1. Copy environment template
copy .env.example .env

# 2. Start Postgres + backend
docker compose up -d

# 3. Backend, for local iteration without Docker
cd backend
pip install -r requirements-dev.txt
uvicorn app.main:app --reload

# 4. Frontend
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:3000 · Backend: http://localhost:8000/healthz

## Workflow

`feature/*` branch → pull request → `main`. No direct pushes to `main`
(see [CLAUDE.md](CLAUDE.md)). CI runs lint/build/test on every PR
(`.github/workflows/ci.yml`).
