from pydantic import BaseModel


class VehicleBase(BaseModel):
    name: str | None = None
    plate: str | None = None
    brand: str | None = None
    model: str | None = None
    mileage: int | None = None
    fuel_type: str | None = None
    notes: str | None = None


class VehicleCreate(VehicleBase):
    name: str
    plate: str
    brand: str
    model: str
    mileage: int


class VehicleUpdate(VehicleBase):
    pass


class VehicleRead(VehicleBase):
    id: int | None = None