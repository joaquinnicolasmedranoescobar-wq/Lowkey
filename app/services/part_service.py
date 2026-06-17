from bson import ObjectId
from datetime import datetime
from typing import Optional, List, Dict, Any
from fastapi import HTTPException, status
from app.db.session import get_database_session
from app.schemas.part import PartCreate, PartRead, PartUpdate

def _build_filters(
    category: Optional[str] = None,
    brand: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    stock_status: Optional[str] = None,
    search: Optional[str] = None,
) -> Dict[str, Any]:
    """Construye el filtro de MongoDB a partir de los parámetros de consulta."""
    filters = {}
    if category:
        filters["category"] = category
    if brand:
        filters["brand"] = brand
    if min_price is not None or max_price is not None:
        price_filter = {}
        if min_price is not None:
            price_filter["$gte"] = min_price
        if max_price is not None:
            price_filter["$lte"] = max_price
        filters["price"] = price_filter
    if stock_status:
        if stock_status == "in":
            filters["stock"] = {"$gt": 0}
        elif stock_status == "low":
            filters["stock"] = {"$gt": 0, "$lt": 5}  # umbral de pocas unidades
        # "all" no añade filtro de stock
    if search:
        # Búsqueda en nombre, descripción, referencia y marca
        filters["$or"] = [
            {"name": {"$regex": search, "$options": "i"}},
            {"description": {"$regex": search, "$options": "i"}},
            {"reference": {"$regex": search, "$options": "i"}},
            {"brand": {"$regex": search, "$options": "i"}},
        ]
    return filters

def _get_sort(sort: Optional[str]) -> List[tuple]:
    """Convierte el parámetro sort en una lista de tuplas para MongoDB."""
    if sort == "price_asc":
        return [("price", 1)]
    elif sort == "price_desc":
        return [("price", -1)]
    elif sort == "name":
        return [("name", 1)]
    elif sort == "new":
        return [("created_at", -1)]
    else:  # default: destacados (por ejemplo, por stock o popularidad)
        return [("stock", -1), ("created_at", -1)]

def list_parts(
    category: Optional[str] = None,
    brand: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    stock_status: Optional[str] = None,
    search: Optional[str] = None,
    sort: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> List[PartRead]:
    db = get_database_session()
    filters = _build_filters(category, brand, min_price, max_price, stock_status, search)
    sort_criteria = _get_sort(sort)
    cursor = db.parts.find(filters).sort(sort_criteria).skip(offset).limit(limit)
    return [PartRead(id=str(doc["_id"]), **doc) for doc in cursor]

def count_parts(
    category: Optional[str] = None,
    brand: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    stock_status: Optional[str] = None,
    search: Optional[str] = None,
) -> int:
    db = get_database_session()
    filters = _build_filters(category, brand, min_price, max_price, stock_status, search)
    return db.parts.count_documents(filters)

def get_part(part_id: str) -> PartRead:
    db = get_database_session()
    doc = db.parts.find_one({"_id": ObjectId(part_id)})
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pieza no encontrada")
    return PartRead(id=str(doc["_id"]), **doc)

def create_part(payload: PartCreate) -> PartRead:
    db = get_database_session()
    data = payload.dict()
    data["created_at"] = datetime.utcnow()
    data["updated_at"] = datetime.utcnow()
    result = db.parts.insert_one(data)
    created = db.parts.find_one({"_id": result.inserted_id})
    return PartRead(id=str(created["_id"]), **created)

def update_part(part_id: str, payload: PartUpdate) -> PartRead:
    db = get_database_session()
    update_data = {k: v for k, v in payload.dict(exclude_unset=True).items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No hay datos para actualizar")
    update_data["updated_at"] = datetime.utcnow()
    result = db.parts.update_one({"_id": ObjectId(part_id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pieza no encontrada")
    updated = db.parts.find_one({"_id": ObjectId(part_id)})
    return PartRead(id=str(updated["_id"]), **updated)

def delete_part(part_id: str) -> None:
    db = get_database_session()
    result = db.parts.delete_one({"_id": ObjectId(part_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pieza no encontrada")