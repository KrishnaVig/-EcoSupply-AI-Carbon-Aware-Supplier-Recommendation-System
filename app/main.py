from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.data import MATERIALS, SAMPLE_INPUT, SUPPLIERS
from app.optimizer import run_optimizer
from app.schemas import OptimizeRequest, OptimizeResponse

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="Sustainable Materials Optimizer",
    description="Hackathon starter backend with a demo frontend and hard-coded supplier data.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def serve_index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/api/sample-input")
def get_sample_input() -> dict:
    return SAMPLE_INPUT


@app.get("/api/materials")
def get_materials() -> list[dict]:
    return MATERIALS


@app.get("/api/suppliers/{material}")
def get_suppliers(material: str) -> list[dict]:
    material_suppliers = [
        supplier for supplier in SUPPLIERS if supplier["material"] == material.lower()
    ]
    if not material_suppliers:
        raise HTTPException(status_code=404, detail="No suppliers found for this material.")
    return material_suppliers


@app.post("/api/optimize", response_model=OptimizeResponse)
def optimize(payload: OptimizeRequest) -> dict:
    material_suppliers = [
        supplier for supplier in SUPPLIERS if supplier["material"] == payload.material.lower()
    ]
    if not material_suppliers:
        raise HTTPException(status_code=404, detail="No suppliers found for this material.")

    try:
        return run_optimizer(payload, material_suppliers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
