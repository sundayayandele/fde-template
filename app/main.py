"""FastAPI entry point: health, metrics and a hello endpoint.

Phase repos replace the hello endpoint with their own API and keep the rest.
"""

from __future__ import annotations

import time

from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, make_asgi_app
from pydantic import BaseModel, Field

from fde_service import __version__
from fde_service.config import get_settings

settings = get_settings()
app = FastAPI(title=settings.service_name, version=__version__)
app.mount("/metrics", make_asgi_app())

REQUESTS = Counter(
    "http_requests_total", "HTTP requests handled", ["method", "route", "status"]
)
LATENCY = Histogram(
    "http_request_duration_seconds", "HTTP request duration", ["method", "route"]
)


@app.middleware("http")
async def observe(request: Request, call_next):
    started = time.perf_counter()
    response = await call_next(request)
    route = request.scope.get("route")
    path = getattr(route, "path", "unmatched")  # template path keeps label cardinality low
    REQUESTS.labels(request.method, path, str(response.status_code)).inc()
    LATENCY.labels(request.method, path).observe(time.perf_counter() - started)
    return response


@app.get("/health/live")
def live() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/ready")
def ready() -> dict[str, str]:
    # Phase repos add real readiness checks here (database, model artefact, upstreams).
    return {"status": "ready", "version": __version__, "environment": settings.environment}


class HelloRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)


class HelloResponse(BaseModel):
    message: str


@app.post("/api/v1/hello", response_model=HelloResponse)
def hello(body: HelloRequest) -> HelloResponse:
    return HelloResponse(message=greet(body.name))


def greet(name: str) -> str:
    """Example exercise. In the starter repo this body becomes a TODO."""
    # >>> SOLUTION: week-00 hello endpoint
    return f"Hello, {name.strip()}! Welcome to the FDE series."
    # <<< SOLUTION
