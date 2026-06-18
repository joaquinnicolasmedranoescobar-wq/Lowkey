from datetime import date as dt_date
from pydantic import BaseModel, Field

class ExpenseBase(BaseModel):
    vehicle_id: str | None = None
    category: str | None = None
    date: dt_date | None = None
    amount: float | None = None
    description: str | None = None

class ExpenseCreate(ExpenseBase):
    vehicle_id: str
    category: str
    date: dt_date
    amount: float

class ExpenseUpdate(ExpenseBase):
    pass

class ExpenseRead(ExpenseBase):
    id: str | None = None

class ExpenseCategoryBreakdown(BaseModel):
    category: str | None = None
    amount: float | None = None

class ExpenseBudgetSummary(BaseModel):
    vehicle_id: str | None = None
    month: str | None = None
    budget_limit: float | None = None
    total_used: float | None = None
    usage_percentage: float | None = None
    categories: list[ExpenseCategoryBreakdown] = Field(default_factory=list)