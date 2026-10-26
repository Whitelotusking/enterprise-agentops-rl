"""Week 1 API bootstrap. Business endpoints are not implemented yet."""

from fastapi import FastAPI

app = FastAPI(title="Enterprise AgentOps-RL", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Process liveness only; does not claim database readiness."""
    return {"status": "ok", "service": "enterprise-agentops-rl", "phase": "bootstrap"}
