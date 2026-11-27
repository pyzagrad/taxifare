FROM python:3.12-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
ENV UV_NO_DEV=1 \
    UV_FROZEN=1
COPY src src
COPY api api
COPY models models
COPY pyproject.toml uv.lock README.md ./
RUN uv sync
CMD ["sh", "-c", "uv run uvicorn api.fast:app --host 0.0.0.0 --port ${PORT:-8080}"]
