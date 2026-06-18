from datetime import date as dt_date
from pydantic import BaseModel

class MaintenanceBase(BaseModel):
    vehicle_id: str | None = None
    type: str | None = None
    date: dt_date | None = None
    km: int | None = None
    cost: float | None = None
    description: str | None = None

class MaintenanceCreate(MaintenanceBase):
    vehicle_id: str
    type: str
    date: dt_date
    km: int
    cost: float

class MaintenanceUpdate(MaintenanceBase):
    pass

class MaintenanceRead(MaintenanceBase):
    id: str | None = None

class MaintenanceAlert(BaseModel):
    vehicle_id: str | None = None
    next_task: str | None = None
    due_in_days: int | None = None
    due_in_km: int | None = None