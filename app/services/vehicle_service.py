from bson import ObjectId
from fastapi import HTTPException, status
from app.db.session import get_database_session
from app.schemas.vehicle import VehicleCreate, VehicleRead, VehicleUpdate

def list_vehicles() -> list[VehicleRead]:
    db = get_database_session()
    cursor = db.vehicles.find().sort("_id", -1)
    return [VehicleRead(id=str(doc["_id"]), **doc) for doc in cursor]

def get_vehicle(vehicle_id: str) -> VehicleRead:
    db = get_database_session()
    doc = db.vehicles.find_one({"_id": ObjectId(vehicle_id)})
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehículo no encontrado")
    return VehicleRead(id=str(doc["_id"]), **doc)

def create_vehicle(payload: VehicleCreate) -> VehicleRead:
    db = get_database_session()
    data = payload.dict(exclude_unset=True)
    result = db.vehicles.insert_one(data)
    created = db.vehicles.find_one({"_id": result.inserted_id})
    return VehicleRead(id=str(created["_id"]), **created)

def update_vehicle(vehicle_id: str, payload: VehicleUpdate) -> VehicleRead:
    db = get_database_session()
    update_data = {k: v for k, v in payload.dict(exclude_unset=True).items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No hay datos para actualizar")
    result = db.vehicles.update_one({"_id": ObjectId(vehicle_id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehículo no encontrado")
    updated = db.vehicles.find_one({"_id": ObjectId(vehicle_id)})
    return VehicleRead(id=str(updated["_id"]), **updated)

def delete_vehicle(vehicle_id: str) -> None:
    db = get_database_session()
    result = db.vehicles.delete_one({"_id": ObjectId(vehicle_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehículo no encontrado")
    # Opcional: eliminar en cascada mantenimientos y gastos
    db.maintenances.delete_many({"vehicle_id": vehicle_id})
    db.expenses.delete_many({"vehicle_id": vehicle_id})