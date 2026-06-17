from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class PartBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    brand: str
    price: float
    stock: int = 0
    image: Optional[str] = None
    compatibility: List[str] = []  # modelos de vehículo compatibles
    reference: Optional[str] = None

class PartCreate(PartBase):
    pass

class PartUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    image: Optional[str] = None
    compatibility: Optional[List[str]] = None
    reference: Optional[str] = None

class PartRead(PartBase):
    id: str
    created_at: datetime
    updated_at: datetime