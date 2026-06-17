from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class OrderItem(BaseModel):
    part_id: str
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItem]
    # Se pueden añadir más campos: dirección, método de pago, etc.

class OrderItemDetail(BaseModel):
    part_id: str
    name: str
    quantity: int
    unit_price: float
    subtotal: float

class OrderRead(BaseModel):
    id: str
    items: List[OrderItemDetail]
    total: float
    created_at: datetime
    status: str  # pending, completed, cancelled