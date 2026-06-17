from fastapi import APIRouter, status
from app.schemas.order import OrderCreate, OrderRead
from app.services import order_service

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/checkout", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
def checkout(payload: OrderCreate):
    """Crea un pedido, valida stock y descuenta inventario."""
    return order_service.create_order(payload)

@router.get("", response_model=list[OrderRead])
def list_orders(limit: int = 10, offset: int = 0):
    return order_service.list_orders(limit, offset)

@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: str):
    return order_service.get_order(order_id)