from src.distance import calculate_distance


def simulate_delivery(assignments, agents, warehouses):

    results = {}

    for agent_id in agents.keys():

        results[agent_id] = {
            "packages_delivered": 0,
            "total_distance": 0
        }

    for assignment in assignments:

        agent_id = assignment["agent_id"]

        warehouse_location = warehouses[
            assignment["warehouse"]
        ]

        destination = assignment["destination"]

        agent_location = agents[agent_id]

        pickup_distance = calculate_distance(
            agent_location,
            warehouse_location
        )

        delivery_distance = calculate_distance(
            warehouse_location,
            destination
        )

        total_trip_distance = (
            pickup_distance +
            delivery_distance
        )

        results[agent_id]["packages_delivered"] += 1

        results[agent_id]["total_distance"] += (
            total_trip_distance
        )

    return results