from datetime import date

from pydantic import BaseModel


class MaintenanceBase(BaseModel):
    vehicle_id: int | None = None
    type: str | None = None
    date: date | None = None
    km: int | None = None
    cost: float | None = None
    description: str | None = None


class MaintenanceCreate(MaintenanceBase):
    vehicle_id: int
    type: str
    date: date
    km: int
    cost: float


class MaintenanceUpdate(MaintenanceBase):
    pass


class MaintenanceRead(MaintenanceBase):
    id: int | None = None