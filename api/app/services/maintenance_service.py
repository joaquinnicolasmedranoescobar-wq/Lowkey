from app.schemas.maintenance import MaintenanceCreate, MaintenanceRead, MaintenanceUpdate


def list_maintenances(vehicle_id: int) -> list[MaintenanceRead]:
    # TODO: fetch maintenances for a vehicle.
    raise NotImplementedError("TODO")


def create_maintenance(payload: MaintenanceCreate) -> MaintenanceRead:
    # TODO: persist a new maintenance record.
    raise NotImplementedError("TODO")


def update_maintenance(maintenance_id: int, payload: MaintenanceUpdate) -> MaintenanceRead:
    # TODO: update the maintenance record.
    raise NotImplementedError("TODO")


def delete_maintenance(maintenance_id: int) -> None:
    # TODO: remove the maintenance record.
    raise NotImplementedError("TODO")