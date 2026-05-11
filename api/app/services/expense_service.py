from app.schemas.expense import ExpenseBudgetSummary, ExpenseCreate, ExpenseRead, ExpenseUpdate


def list_expenses(vehicle_id: int) -> list[ExpenseRead]:
    # TODO: Query all expense records for this vehicle ordered by date descending and map to ExpenseRead.
    raise NotImplementedError("TODO")


def get_monthly_summary(vehicle_id: int) -> ExpenseBudgetSummary:
    # TODO: Aggregate current-month expenses by category, calculate total used vs configured budget, and return percentages.
    raise NotImplementedError("TODO")


def create_expense(payload: ExpenseCreate) -> ExpenseRead:
    # TODO: Validate vehicle existence, persist a new expense, and return the created expense including generated id.
    raise NotImplementedError("TODO")


def update_expense(expense_id: int, payload: ExpenseUpdate) -> ExpenseRead:
    # TODO: Load expense by id, update only provided fields, persist, and return the updated expense.
    raise NotImplementedError("TODO")


def delete_expense(expense_id: int) -> None:
    # TODO: Delete the expense and ensure related monthly and dashboard aggregates are recalculated.
    raise NotImplementedError("TODO")