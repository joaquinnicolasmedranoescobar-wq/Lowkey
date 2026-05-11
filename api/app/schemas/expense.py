from datetime import date

from pydantic import BaseModel, Field


class ExpenseBase(BaseModel):
    vehicle_id: int | None = None
    category: str | None = None
    date: date | None = None
    amount: float | None = None
    description: str | None = None


class ExpenseCreate(ExpenseBase):
    vehicle_id: int
    category: str
    date: date
    amount: float


class ExpenseUpdate(ExpenseBase):
    pass


class ExpenseRead(ExpenseBase):
    id: int | None = None


class ExpenseCategoryBreakdown(BaseModel):
    category: str | None = None
    amount: float | None = None


class ExpenseBudgetSummary(BaseModel):
    vehicle_id: int | None = None
    month: str | None = None
    budget_limit: float | None = None
    total_used: float | None = None
    usage_percentage: float | None = None
    categories: list[ExpenseCategoryBreakdown] = Field(default_factory=list)