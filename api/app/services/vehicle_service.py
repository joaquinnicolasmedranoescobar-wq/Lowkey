from app.schemas.vehicle import VehicleCreate, VehicleRead, VehicleUpdate


def list_vehicles() -> list[VehicleRead]:
    # TODO: fetch all vehicles from persistence.
    raise NotImplementedError("TODO")


def get_vehicle(vehicle_id: int) -> VehicleRead:
    # TODO: fetch one vehicle by id.
    raise NotImplementedError("TODO")


def create_vehicle(payload: VehicleCreate) -> VehicleRead:
    # TODO: validate and persist a new vehicle.
    raise NotImplementedError("TODO")


def update_vehicle(vehicle_id: int, payload: VehicleUpdate) -> VehicleRead:
    # TODO: update the vehicle fields.
    raise NotImplementedError("TODO")


def delete_vehicle(vehicle_id: int) -> None:
    # TODO: delete the vehicle and related data.
    raise NotImplementedError("TODO")