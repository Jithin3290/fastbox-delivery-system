def print_routes(assignments):
    """
    Display delivery routes in ASCII format.
    """
    print("\nDELIVERY ROUTES")
    print("=" * 60)

    for assignment in assignments:

        package_id = assignment["package_id"]

        agent_id = assignment["agent_id"]

        warehouse = assignment["warehouse"]

        destination = assignment["destination"]

        delay = assignment.get("delay", 0)

        print(
            f"🚚 {agent_id} "
            f"-> 🏬 {warehouse} "
            f"-> 📦 {package_id} "
            f"-> 📍 {destination} "
            f"-> ⏱ Delay: {delay} mins"
        )