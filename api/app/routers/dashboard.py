from fastapi import APIRouter

from app.schemas.dashboard import DashboardStatistics, DashboardSummary, VehicleSummary
from app.services import dashboard_service


router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary", response_model=DashboardSummary)
def get_dashboard_summary() -> DashboardSummary:
    return dashboard_service.get_dashboard_summary()


@router.get("/vehicle/{vehicle_id}", response_model=VehicleSummary)
def get_vehicle_summary(vehicle_id: int) -> VehicleSummary:
    return dashboard_service.get_vehicle_summary(vehicle_id)


@router.get("/statistics", response_model=DashboardStatistics)
def get_dashboard_statistics() -> DashboardStatistics:
    return dashboard_service.get_dashboard_statistics()
