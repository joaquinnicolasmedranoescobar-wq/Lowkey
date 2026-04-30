from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import dashboard, expenses, maintenances, vehicles


app = FastAPI(
    title="Lowkey API",
    description="Base API for vehicle maintenance, expenses, and statistics.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vehicles.router, prefix="/api/v1")
app.include_router(maintenances.router, prefix="/api/v1")
app.include_router(expenses.router, prefix="/api/v1")
app.include_router(dashboard.router, prefix="/api/v1")


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """Basic health check endpoint."""
    return {
        "status": "ok",
        "message": "TODO: connect this endpoint to the real service health state.",
    }