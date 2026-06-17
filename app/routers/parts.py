from fastapi import APIRouter, Query, status
from typing import Optional
from app.schemas.part import PartCreate, PartRead, PartUpdate
from app.services import part_service

router = APIRouter(prefix="/parts", tags=["Parts"])

@router.get("", response_model=list[PartRead])
def list_parts(
    category: Optional[str] = Query(None, description="Filtrar por categoría"),
    brand: Optional[str] = Query(None, description="Filtrar por marca"),
    min_price: Optional[float] = Query(None, description="Precio mínimo"),
    max_price: Optional[float] = Query(None, description="Precio máximo"),
    stock_status: Optional[str] = Query(None, description="all, in, low"),
    search: Optional[str] = Query(None, description="Búsqueda en nombre, descripción, referencia, marca"),
    sort: Optional[str] = Query("featured", description="price_asc, price_desc, name, new"),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    return part_service.list_parts(
        category=category,
        brand=brand,
        min_price=min_price,
        max_price=max_price,
        stock_status=stock_status,
        search=search,
        sort=sort,
        limit=limit,
        offset=offset
    )

@router.get("/count", response_model=int)
def count_parts(
    category: Optional[str] = Query(None),
    brand: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    stock_status: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
):
    return part_service.count_parts(
        category=category,
        brand=brand,
        min_price=min_price,
        max_price=max_price,
        stock_status=stock_status,
        search=search
    )

@router.get("/{part_id}", response_model=PartRead)
def get_part(part_id: str):
    return part_service.get_part(part_id)

@router.post("", response_model=PartRead, status_code=status.HTTP_201_CREATED)
def create_part(payload: PartCreate):
    return part_service.create_part(payload)

@router.put("/{part_id}", response_model=PartRead)
def update_part(part_id: str, payload: PartUpdate):
    return part_service.update_part(part_id, payload)

@router.delete("/{part_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_part(part_id: str):
    part_service.delete_part(part_id)