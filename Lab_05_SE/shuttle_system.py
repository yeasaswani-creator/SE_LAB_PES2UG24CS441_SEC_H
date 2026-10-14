
"""Manage campus shuttle routes, trip logs, and fleet data."""

import json
import secrets
from datetime import datetime

# Global state
routes = {
    "R1": {"name": "Main Gate - Library", "trips": []},
    "R2": {"name": "Hostel - Sports Complex", "trips": []},
    "R3": {"name": "Admin Block - Metro", "trips": []},
}
MIN_CAPACITY = 10


def add_trip_log(route_id, passenger_count, logs=None):
    """Add a passenger count to a route's trip history."""
    if logs is None:
        logs = []

    routes[route_id]["trips"].append(passenger_count)
    logs.append(
        f"{datetime.now()}: {route_id} carried {passenger_count}"
    )
    return logs


def remove_route(route_id):
    """Remove a route from the shuttle system."""
    routes.pop(route_id, None)


def average_load(route_id):
    """Calculate the average passenger load for a route."""
    trips = routes[route_id]["trips"]

    if not trips:
        return 0

    return sum(trips) / len(trips)


def underused_routes():
    """Find routes operating below minimum capacity."""
    flagged = []

    for route_id, route in routes.items():
        trips = route["trips"]

        if not trips:
            continue

        if not all(
            isinstance(count, (int, float)) and not isinstance(count, bool)
            for count in trips
        ):
            continue

        if average_load(route_id) < MIN_CAPACITY:
            flagged.append(route_id)

    return flagged


def assign_driver(route_id):
    """Select a driver for an existing route."""
    if route_id not in routes:
        raise ValueError(f"Unknown route: {route_id}")

    drivers = ["Prakash", "Leela", "Imran", "Tom"]
    return secrets.choice(drivers)


def sync_fleet_data(file="fleet.json"):
    """Save and reload shuttle fleet data."""
    with open(file, "w", encoding="utf-8") as fleet_file:
        json.dump(routes, fleet_file, indent=2)

    with open(file, "r", encoding="utf-8") as fleet_file:
        saved_routes = json.load(fleet_file)

    routes.clear()
    routes.update(saved_routes)


def main():
    """Run the shuttle system demonstration."""
    add_trip_log("R1", 32)
    add_trip_log("R1", 28)
    add_trip_log("R2", 4)
    add_trip_log("R2", -6)
    add_trip_log("R3", "full")

    print("Driver for R1:", assign_driver("R1"))
    print("Underused:", underused_routes())
    print("R1 average:", average_load("R1"))

    sync_fleet_data()
    remove_route("R3")

    choice = input("Route to look up (Enter for R2): ") or "R2"

    if choice in routes:
        print("Trips on", choice, ":", routes[choice]["trips"])
    else:
        print("Route not found:", choice)

    if "R3" in routes:
        print("R3 average:", average_load("R3"))
    else:
        print("R3 has been removed.")


if __name__ == "__main__":
    main()
