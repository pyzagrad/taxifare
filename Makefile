# ── Variables ───────────────────────────────────────
PYTHON   := .venv/bin/python
UVICORN  := .venv/bin/uvicorn
APP      := api.fast:app
HOST     := 0.0.0.0
PORT     := 8000

# ── Public targets ─────────────────────────────────
run-api:  ## Start the FastAPI server (reload on code changes)
	uv run uvicorn api.fast:app
