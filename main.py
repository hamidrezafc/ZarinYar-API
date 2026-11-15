
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="ZarinYar API",
    description="Official API for ZarinYar",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "service": "ZarinYar API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/api/v1/health")
def health():
    return {
        "status": "healthy",
        "service": "ZarinYar API",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/api/v1/data-status")
def data_status():
    return {
        "gold": "not_connected",
        "currency": "not_connected",
        "crypto": "not_connected",
        "message": "Waiting for verified data sources"
    }
