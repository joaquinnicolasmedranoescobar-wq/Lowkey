from datetime import date

from pydantic import BaseModel


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