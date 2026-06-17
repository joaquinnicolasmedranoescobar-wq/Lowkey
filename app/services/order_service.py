from bson import ObjectId
from datetime import datetime
from typing import List
from fastapi import HTTPException, status
from app.db.session import get_database_session
from app.schemas.order import OrderCreate, OrderRead, OrderItemDetail

def create_order(payload: OrderCreate) -> OrderRead:
    db = get_database_session()
    items_details = []
    total = 0.0

    for item in payload.items:
        part = db.parts.find_one({"_id": ObjectId(item.part_id)})
        if not part:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Pieza con id {item.part_id} no encontrada"
            )
        if part["stock"] < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Stock insuficiente para {part['name']}. Disponible: {part['stock']}"
            )
        subtotal = part["price"] * item.quantity
        total += subtotal
        items_details.append(
            OrderItemDetail(
                part_id=item.part_id,
                name=part["name"],
                quantity=item.quantity,
                unit_price=part["price"],
                subtotal=subtotal
            )
        )
        # Descontar stock
        db.parts.update_one(
            {"_id": ObjectId(item.part_id)},
            {"$inc": {"stock": -item.quantity}}
        )

    order_data = {
        "items": [item.dict() for item in items_details],
        "total": total,
        "created_at": datetime.utcnow(),
        "status": "completed"
    }
    result = db.orders.insert_one(order_data)
    created = db.orders.find_one({"_id": result.inserted_id})
    return OrderRead(id=str(created["_id"]), **created)

def list_orders(limit: int = 10, offset: int = 0) -> List[OrderRead]:
    db = get_database_session()
    cursor = db.orders.find().sort("created_at", -1).skip(offset).limit(limit)
    return [OrderRead(id=str(doc["_id"]), **doc) for doc in cursor]

def get_order(order_id: str) -> OrderRead:
    db = get_database_session()
    doc = db.orders.find_one({"_id": ObjectId(order_id)})
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido no encontrado")
    return OrderRead(id=str(doc["_id"]), **doc)