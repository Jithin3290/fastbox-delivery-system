from src.distance import calculate_distance


def assign_packages(packages, agents, warehouses):
    """
    Assign package to nearest agent.
    """

    assignments = []

    for package in packages:

        warehouse_id = package["warehouse"]

        warehouse_location = warehouses[warehouse_id]

        nearest_agent = None
        shortest_distance = float("inf")

        for agent_id, agent_location in agents.items():

            distance = calculate_distance(
                agent_location,
                warehouse_location
            )

            if distance < shortest_distance:

                shortest_distance = distance
                nearest_agent = agent_id

        assignments.append({
            "package_id": package["id"],
            "agent_id": nearest_agent,
            "warehouse": warehouse_id,
            "destination": package["destination"]
        })

    return assignments