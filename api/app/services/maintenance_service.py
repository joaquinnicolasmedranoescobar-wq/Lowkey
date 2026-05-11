from app.schemas.maintenance import (
    MaintenanceAlert,
    MaintenanceCreate,
    MaintenanceRead,
    MaintenanceUpdate,
)


def list_maintenances(vehicle_id: int) -> list[MaintenanceRead]:
    # TODO: Query maintenances for this vehicle ordered by date descending and map rows to MaintenanceRead.
    raise NotImplementedError("TODO")


def list_recent_maintenances(vehicle_id: int) -> list[MaintenanceRead]:
    # TODO: Return only the latest maintenance entries for the timeline card (for example the last 3 records).
    raise NotImplementedError("TODO")


def get_upcoming_maintenance_alert(vehicle_id: int) -> MaintenanceAlert:
    # TODO: Calculate the next due maintenance based on mileage/date rules and return days/km remaining.
    raise NotImplementedError("TODO")


def create_maintenance(payload: MaintenanceCreate) -> MaintenanceRead:
    # TODO: Validate vehicle existence, save maintenance in storage, and return the created record with its id.
    raise NotImplementedError("TODO")


def update_maintenance(maintenance_id: int, payload: MaintenanceUpdate) -> MaintenanceRead:
    # TODO: Load maintenance by id, apply provided fields, persist changes, and return the updated record.
    raise NotImplementedError("TODO")


def delete_maintenance(maintenance_id: int) -> None:
    # TODO: Delete maintenance by id and ensure dependent dashboard aggregates are refreshed if needed.
    raise NotImplementedError("TODO")