from app.schemas.expense import ExpenseCreate, ExpenseRead, ExpenseUpdate


def list_expenses(vehicle_id: int) -> list[ExpenseRead]:
    # TODO: fetch expenses for a vehicle.
    raise NotImplementedError("TODO")


def create_expense(payload: ExpenseCreate) -> ExpenseRead:
    # TODO: persist a new expense record.
    raise NotImplementedError("TODO")


def update_expense(expense_id: int, payload: ExpenseUpdate) -> ExpenseRead:
    # TODO: update the expense record.
    raise NotImplementedError("TODO")


def delete_expense(expense_id: int) -> None:
    # TODO: remove the expense record.
    raise NotImplementedError("TODO")