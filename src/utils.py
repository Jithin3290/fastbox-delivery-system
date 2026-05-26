def normalize_data(data):
    """
    Convert different JSON formats
    into one consistent structure.
    """

    # Normalize warehouses
    if isinstance(data["warehouses"], list):

        warehouses = {
            warehouse["id"]: warehouse["location"]
            for warehouse in data["warehouses"]
        }

    else:
        warehouses = data["warehouses"]

    # Normalize agents
    if isinstance(data["agents"], list):

        agents = {
            agent["id"]: agent["location"]
            for agent in data["agents"]
        }

    else:
        agents = data["agents"]

    # Normalize packages
    packages = []

    for package in data["packages"]:

        normalized_package = {
            "id": package["id"],
            "warehouse": (
                package.get("warehouse")
                or package.get("warehouse_id")
            ),
            "destination": package["destination"]
        }

        packages.append(normalized_package)

    return warehouses, agents, packages