from app.schemas.dashboard import DashboardStatistics, DashboardSummary, VehicleSummary


def get_dashboard_summary() -> DashboardSummary:
    # TODO: Aggregate global home-screen metrics: active vehicles, total monthly expenses, and pending maintenances.
    raise NotImplementedError("TODO")


def get_vehicle_summary(vehicle_id: int) -> VehicleSummary:
    # TODO: Aggregate vehicle-specific totals for maintenance costs, expense costs, and pending tasks.
    raise NotImplementedError("TODO")


def get_dashboard_statistics() -> DashboardStatistics:
    # TODO: Build statistics-screen data: average cost per vehicle, quarterly maintenance count, and trend per expense category.
    raise NotImplementedError("TODO")
