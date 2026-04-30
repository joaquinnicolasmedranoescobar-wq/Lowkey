from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_vehicles: int | None = None
    total_expenses: float | None = None
    pending_maintenances: int | None = None


class VehicleSummary(BaseModel):
    vehicle_id: int | None = None
    total_maintenance_cost: float | None = None
    total_expense_cost: float | None = None
    pending_items: int | None = None