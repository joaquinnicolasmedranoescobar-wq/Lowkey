from app.schemas.vehicle import VehicleCreate, VehicleRead, VehicleUpdate


def list_vehicles() -> list[VehicleRead]:
    # TODO: Fetch all vehicles from storage, sorted by creation date or last activity, and map to VehicleRead.
    raise NotImplementedError("TODO")


def get_vehicle(vehicle_id: int) -> VehicleRead:
    # TODO: Retrieve one vehicle by id and raise a not-found error if it does not exist.
    raise NotImplementedError("TODO")


def create_vehicle(payload: VehicleCreate) -> VehicleRead:
    # TODO: Validate unique constraints (like plate), persist vehicle data, and return the created record.
    raise NotImplementedError("TODO")


def update_vehicle(vehicle_id: int, payload: VehicleUpdate) -> VehicleRead:
    # TODO: Retrieve the vehicle, apply provided field updates, persist changes, and return updated data.
    raise NotImplementedError("TODO")


def delete_vehicle(vehicle_id: int) -> None:
    # TODO: Delete the vehicle and cascade/remove linked maintenances and expenses safely.
    raise NotImplementedError("TODO")
