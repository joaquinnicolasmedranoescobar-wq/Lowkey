from app.schemas.dashboard import DashboardSummary, VehicleSummary


def get_dashboard_summary() -> DashboardSummary:
    # TODO: aggregate global dashboard metrics.
    raise NotImplementedError("TODO")


def get_vehicle_summary(vehicle_id: int) -> VehicleSummary:
    # TODO: aggregate vehicle-specific metrics.
    raise NotImplementedError("TODO")