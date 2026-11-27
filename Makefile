# ── Variables ───────────────────────────────────────
PYTHON   := .venv/bin/python
UVICORN  := .venv/bin/uvicorn
APP      := api.fast:app
HOST     := 0.0.0.0
PORT     := 8000

# ── Public targets ─────────────────────────────────
run-api:  ## Start the FastAPI server (reload on code changes)
	uv run uvicorn api.fast:app

docker_build_local:
	docker build \
		-t ${IMAGE_NAME}:dev .

docker-run:
	docker run \
		-p 8000:8080 ${IMAGE_NAME}:dev
