from fastapi import APIRouter, status

from app.schemas.expense import ExpenseBudgetSummary, ExpenseCreate, ExpenseRead, ExpenseUpdate
from app.services import expense_service


router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.get("/vehicle/{vehicle_id}", response_model=list[ExpenseRead])
def list_expenses(vehicle_id: int) -> list[ExpenseRead]:
    return expense_service.list_expenses(vehicle_id)


@router.get("/vehicle/{vehicle_id}/monthly-summary", response_model=ExpenseBudgetSummary)
def get_monthly_summary(vehicle_id: int) -> ExpenseBudgetSummary:
    return expense_service.get_monthly_summary(vehicle_id)


@router.post("", response_model=ExpenseRead, status_code=status.HTTP_201_CREATED)
def create_expense(payload: ExpenseCreate) -> ExpenseRead:
    return expense_service.create_expense(payload)


@router.put("/{expense_id}", response_model=ExpenseRead)
def update_expense(expense_id: int, payload: ExpenseUpdate) -> ExpenseRead:
    return expense_service.update_expense(expense_id, payload)


@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(expense_id: int) -> None:
    expense_service.delete_expense(expense_id)
