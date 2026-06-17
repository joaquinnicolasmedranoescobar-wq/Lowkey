from fastapi import APIRouter, status

from app.schemas.vehicle import VehicleCreate, VehicleRead, VehicleUpdate
from app.services import vehicle_service


router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


@router.get("", response_model=list[VehicleRead])
def list_vehicles() -> list[VehicleRead]:
    return vehicle_service.list_vehicles()


@router.get("/{vehicle_id}", response_model=VehicleRead)
def get_vehicle(vehicle_id: str) -> VehicleRead:
    return vehicle_service.get_vehicle(vehicle_id)


@router.post("", response_model=VehicleRead, status_code=status.HTTP_201_CREATED)
def create_vehicle(payload: VehicleCreate) -> VehicleRead:
    return vehicle_service.create_vehicle(payload)


@router.put("/{vehicle_id}", response_model=VehicleRead)
def update_vehicle(vehicle_id: str, payload: VehicleUpdate) -> VehicleRead:
    return vehicle_service.update_vehicle(vehicle_id, payload)


@router.delete("/{vehicle_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vehicle(vehicle_id: str) -> None:
    vehicle_service.delete_vehicle(vehicle_id)