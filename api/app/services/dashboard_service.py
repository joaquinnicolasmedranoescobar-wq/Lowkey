from datetime import datetime, timedelta
from bson import ObjectId
from fastapi import HTTPException, status
from app.db.session import get_database_session
from app.schemas.dashboard import DashboardSummary, VehicleSummary, DashboardStatistics, ExpenseTrendPoint

def get_dashboard_summary() -> DashboardSummary:
    db = get_database_session()
    total_vehicles = db.vehicles.count_documents({})
    # Gastos del mes actual
    now = datetime.now()
    start_of_month = datetime(now.year, now.month, 1)
    pipeline_expenses = [
        {"$match": {"date": {"$gte": start_of_month}}},
        {"$group": {"_id": None, "total": {"$sum": "$amount"}}}
    ]
    result = list(db.expenses.aggregate(pipeline_expenses))
    total_expenses = result[0]["total"] if result else 0.0
    # Mantenimientos pendientes: aquellos cuya fecha es futura (asumiendo que se programan)
    # En este ejemplo consideramos pendientes si la fecha es hoy o futura
    pending = db.maintenances.count_documents({"date": {"$gte": now.date()}})
    return DashboardSummary(
        total_vehicles=total_vehicles,
        total_expenses=total_expenses,
        pending_maintenances=pending
    )

def get_vehicle_summary(vehicle_id: str) -> VehicleSummary:
    db = get_database_session()
    vehicle = db.vehicles.find_one({"_id": ObjectId(vehicle_id)})
    if not vehicle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehículo no encontrado")
    # Suma de costes de mantenimiento
    maint_pipeline = [
        {"$match": {"vehicle_id": vehicle_id}},
        {"$group": {"_id": None, "total": {"$sum": "$cost"}}}
    ]
    maint_result = list(db.maintenances.aggregate(maint_pipeline))
    total_maintenance_cost = maint_result[0]["total"] if maint_result else 0.0
    # Suma de gastos
    exp_pipeline = [
        {"$match": {"vehicle_id": vehicle_id}},
        {"$group": {"_id": None, "total": {"$sum": "$amount"}}}
    ]
    exp_result = list(db.expenses.aggregate(exp_pipeline))
    total_expense_cost = exp_result[0]["total"] if exp_result else 0.0
    # Pendientes: mantenimientos con fecha >= hoy
    pending = db.maintenances.count_documents({"vehicle_id": vehicle_id, "date": {"$gte": datetime.now().date()}})
    return VehicleSummary(
        vehicle_id=vehicle_id,
        total_maintenance_cost=total_maintenance_cost,
        total_expense_cost=total_expense_cost,
        pending_items=pending
    )

def get_dashboard_statistics() -> DashboardStatistics:
    db = get_database_session()
    # Coste medio por vehículo: sumar todos los gastos y dividir entre número de vehículos con gastos
    total_vehicles = db.vehicles.count_documents({})
    if total_vehicles == 0:
        avg_cost = 0.0
    else:
        pipeline = [
            {"$group": {"_id": "$vehicle_id", "total": {"$sum": "$amount"}}},
            {"$group": {"_id": None, "avg": {"$avg": "$total"}}}
        ]
        result = list(db.expenses.aggregate(pipeline))
        avg_cost = result[0]["avg"] if result else 0.0
    # Mantenimientos en el trimestre (últimos 3 meses)
    three_months_ago = datetime.now() - timedelta(days=90)
    quarterly_count = db.maintenances.count_documents({"date": {"$gte": three_months_ago.date()}})
    # Tendencia de gasto por categoría: comparar mes actual con mes anterior
    now = datetime.now()
    start_current = datetime(now.year, now.month, 1)
    start_previous = datetime(now.year, now.month-1, 1) if now.month > 1 else datetime(now.year-1, 12, 1)
    end_previous = start_current - timedelta(days=1)
    # Gastos del mes actual por categoría
    pipeline_current = [
        {"$match": {"date": {"$gte": start_current}}},
        {"$group": {"_id": "$category", "total": {"$sum": "$amount"}}}
    ]
    current_cats = {r["_id"]: r["total"] for r in db.expenses.aggregate(pipeline_current)}
    # Gastos del mes anterior
    pipeline_prev = [
        {"$match": {"date": {"$gte": start_previous, "$lte": end_previous}}},
        {"$group": {"_id": "$category", "total": {"$sum": "$amount"}}}
    ]
    prev_cats = {r["_id"]: r["total"] for r in db.expenses.aggregate(pipeline_prev)}
    # Calcular variación
    all_cats = set(current_cats.keys()) | set(prev_cats.keys())
    trend = []
    for cat in all_cats:
        current = current_cats.get(cat, 0)
        prev = prev_cats.get(cat, 0)
        if prev == 0:
            variation = 100.0 if current > 0 else 0.0
        else:
            variation = ((current - prev) / prev) * 100
        trend.append(ExpenseTrendPoint(category=cat, variation_percentage=round(variation, 1)))
    return DashboardStatistics(
        average_cost_per_vehicle=round(avg_cost, 2),
        quarterly_maintenance_count=quarterly_count,
        expense_trend=trend
    )