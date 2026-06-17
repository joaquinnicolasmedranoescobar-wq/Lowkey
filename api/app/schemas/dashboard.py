from pydantic import BaseModel, Field

class DashboardSummary(BaseModel):
    total_vehicles: int | None = None
    total_expenses: float | None = None
    pending_maintenances: int | None = None

class VehicleSummary(BaseModel):
    vehicle_id: str | None = None
    total_maintenance_cost: float | None = None
    total_expense_cost: float | None = None
    pending_items: int | None = None

class ExpenseTrendPoint(BaseModel):
    category: str | None = None
    variation_percentage: float | None = None

class DashboardStatistics(BaseModel):
    average_cost_per_vehicle: float | None = None
    quarterly_maintenance_count: int | None = None
    expense_trend: list[ExpenseTrendPoint] = Field(default_factory=list)