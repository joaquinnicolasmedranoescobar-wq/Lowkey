from bson import ObjectId
from datetime import datetime
from fastapi import HTTPException, status
from app.db.session import get_database_session
from app.schemas.expense import ExpenseCreate, ExpenseRead, ExpenseUpdate, ExpenseBudgetSummary, ExpenseCategoryBreakdown

BUDGET_LIMIT = 400.0  # presupuesto mensual fijo

def list_expenses(vehicle_id: str) -> list[ExpenseRead]:
    db = get_database_session()
    cursor = db.expenses.find({"vehicle_id": vehicle_id}).sort("date", -1)
    return [ExpenseRead(id=str(doc["_id"]), **doc) for doc in cursor]

def get_monthly_summary(vehicle_id: str) -> ExpenseBudgetSummary:
    db = get_database_session()
    # Fecha actual: primer día del mes actual
    now = datetime.now()
    start_of_month = datetime(now.year, now.month, 1)
    pipeline = [
        {"$match": {
            "vehicle_id": vehicle_id,
            "date": {"$gte": start_of_month}
        }},
        {"$group": {
            "_id": "$category",
            "total": {"$sum": "$amount"}
        }}
    ]
    results = list(db.expenses.aggregate(pipeline))
    total_used = sum(r["total"] for r in results)
    categories = [ExpenseCategoryBreakdown(category=r["_id"], amount=r["total"]) for r in results]
    usage_percentage = (total_used / BUDGET_LIMIT * 100) if BUDGET_LIMIT else 0
    return ExpenseBudgetSummary(
        vehicle_id=vehicle_id,
        month=now.strftime("%Y-%m"),
        budget_limit=BUDGET_LIMIT,
        total_used=total_used,
        usage_percentage=usage_percentage,
        categories=categories
    )

def create_expense(payload: ExpenseCreate) -> ExpenseRead:
    db = get_database_session()
    vehicle = db.vehicles.find_one({"_id": ObjectId(payload.vehicle_id)})
    if not vehicle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehículo no encontrado")
    data = payload.dict(exclude_unset=True)
    result = db.expenses.insert_one(data)
    created = db.expenses.find_one({"_id": result.inserted_id})
    return ExpenseRead(id=str(created["_id"]), **created)

def update_expense(expense_id: str, payload: ExpenseUpdate) -> ExpenseRead:
    db = get_database_session()
    update_data = {k: v for k, v in payload.dict(exclude_unset=True).items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No hay datos para actualizar")
    result = db.expenses.update_one({"_id": ObjectId(expense_id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gasto no encontrado")
    updated = db.expenses.find_one({"_id": ObjectId(expense_id)})
    return ExpenseRead(id=str(updated["_id"]), **updated)

def delete_expense(expense_id: str) -> None:
    db = get_database_session()
    result = db.expenses.delete_one({"_id": ObjectId(expense_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gasto no encontrado")