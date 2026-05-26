from src.distance import calculate_distance
import random

# Fixed seed for reproducible testing
random.seed(42)


def simulate_delivery(assignments, agents, warehouses):

    results = {}

    # Initialize result structure
    for agent_id in agents.keys():

        results[agent_id] = {
            "packages_delivered": 0,
            "total_distance": 0,
            "total_delay": 0
        }

    # Process each assignment
    for assignment in assignments:

        agent_id = assignment["agent_id"]

        warehouse_location = warehouses[
            assignment["warehouse"]
        ]

        destination = assignment["destination"]

        agent_location = agents[agent_id]

        # Distance from agent to warehouse
        pickup_distance = calculate_distance(
            agent_location,
            warehouse_location
        )

        # Distance from warehouse to destination
        delivery_distance = calculate_distance(
            warehouse_location,
            destination
        )

        # Total trip distance
        total_trip_distance = (
            pickup_distance +
            delivery_distance
        )

        # Simulated random delay
        delay = random.randint(1, 5)

        # Store delay for visualization
        assignment["delay"] = delay

        # Update report data
        results[agent_id]["packages_delivered"] += 1

        results[agent_id]["total_distance"] += (
            total_trip_distance
        )

        results[agent_id]["total_delay"] += delay

    return results