from fastapi import APIRouter, status

from app.schemas.maintenance import (
    MaintenanceAlert,
    MaintenanceCreate,
    MaintenanceRead,
    MaintenanceUpdate,
)
from app.services import maintenance_service


router = APIRouter(prefix="/maintenances", tags=["Maintenances"])


@router.get("/vehicle/{vehicle_id}", response_model=list[MaintenanceRead])
def list_maintenances(vehicle_id: int) -> list[MaintenanceRead]:
    return maintenance_service.list_maintenances(vehicle_id)


@router.get("/vehicle/{vehicle_id}/recent", response_model=list[MaintenanceRead])
def list_recent_maintenances(vehicle_id: int) -> list[MaintenanceRead]:
    return maintenance_service.list_recent_maintenances(vehicle_id)


@router.get("/vehicle/{vehicle_id}/upcoming-alert", response_model=MaintenanceAlert)
def get_upcoming_maintenance_alert(vehicle_id: int) -> MaintenanceAlert:
    return maintenance_service.get_upcoming_maintenance_alert(vehicle_id)


@router.post("", response_model=MaintenanceRead, status_code=status.HTTP_201_CREATED)
def create_maintenance(payload: MaintenanceCreate) -> MaintenanceRead:
    return maintenance_service.create_maintenance(payload)


@router.put("/{maintenance_id}", response_model=MaintenanceRead)
def update_maintenance(maintenance_id: int, payload: MaintenanceUpdate) -> MaintenanceRead:
    return maintenance_service.update_maintenance(maintenance_id, payload)


@router.delete("/{maintenance_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_maintenance(maintenance_id: int) -> None:
    maintenance_service.delete_maintenance(maintenance_id)