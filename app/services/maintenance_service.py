from bson import ObjectId
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from app.db.session import get_database_session
from app.schemas.maintenance import MaintenanceCreate, MaintenanceRead, MaintenanceUpdate, MaintenanceAlert

def list_maintenances(vehicle_id: str) -> list[MaintenanceRead]:
    db = get_database_session()
    cursor = db.maintenances.find({"vehicle_id": vehicle_id}).sort("date", -1)
    return [MaintenanceRead(id=str(doc["_id"]), **doc) for doc in cursor]

def list_recent_maintenances(vehicle_id: str, limit: int = 3) -> list[MaintenanceRead]:
    db = get_database_session()
    cursor = db.maintenances.find({"vehicle_id": vehicle_id}).sort("date", -1).limit(limit)
    return [MaintenanceRead(id=str(doc["_id"]), **doc) for doc in cursor]

def get_upcoming_maintenance_alert(vehicle_id: str) -> MaintenanceAlert:
    db = get_database_session()
    # Obtener el vehículo para conocer el kilometraje actual
    vehicle = db.vehicles.find_one({"_id": ObjectId(vehicle_id)})
    if not vehicle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehículo no encontrado")
    current_km = vehicle.get("mileage", 0)
    # Buscar el último mantenimiento para estimar próximo (ejemplo: cada 10.000 km)
    last = db.maintenances.find_one({"vehicle_id": vehicle_id}, sort=[("km", -1)])
    if last:
        next_km = last["km"] + 10000
        due_in_km = max(0, next_km - current_km)
        next_task = "Revisión general (cada 10.000 km)"
    else:
        due_in_km = 10000 - (current_km % 10000) if current_km > 0 else 10000
        next_task = "Primera revisión"
    # También calcular días aproximados (suponiendo 50 km/día)
    due_in_days = int(due_in_km / 50) if due_in_km > 0 else 0
    return MaintenanceAlert(
        vehicle_id=vehicle_id,
        next_task=next_task,
        due_in_days=due_in_days,
        due_in_km=due_in_km
    )

def create_maintenance(payload: MaintenanceCreate) -> MaintenanceRead:
    db = get_database_session()
    # Verificar que el vehículo existe
    vehicle = db.vehicles.find_one({"_id": ObjectId(payload.vehicle_id)})
    if not vehicle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehículo no encontrado")
    data = payload.dict(exclude_unset=True)
    result = db.maintenances.insert_one(data)
    created = db.maintenances.find_one({"_id": result.inserted_id})
    return MaintenanceRead(id=str(created["_id"]), **created)

def update_maintenance(maintenance_id: str, payload: MaintenanceUpdate) -> MaintenanceRead:
    db = get_database_session()
    update_data = {k: v for k, v in payload.dict(exclude_unset=True).items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No hay datos para actualizar")
    result = db.maintenances.update_one({"_id": ObjectId(maintenance_id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mantenimiento no encontrado")
    updated = db.maintenances.find_one({"_id": ObjectId(maintenance_id)})
    return MaintenanceRead(id=str(updated["_id"]), **updated)

def delete_maintenance(maintenance_id: str) -> None:
    db = get_database_session()
    result = db.maintenances.delete_one({"_id": ObjectId(maintenance_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mantenimiento no encontrado")