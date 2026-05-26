import json


def generate_report(results):

    best_agent = None
    best_efficiency = float("inf")

    for agent_id, data in results.items():

        delivered = data["packages_delivered"]
        total_distance = data["total_distance"]

        if delivered > 0:

            efficiency = (
                total_distance / delivered
            )

        else:
            efficiency = 0

        data["total_distance"] = round(
            total_distance,
            2
        )

        data["efficiency"] = round(
            efficiency,
            2
        )

        if delivered > 0 and efficiency < best_efficiency:

            best_efficiency = efficiency
            best_agent = agent_id

    results["best_agent"] = best_agent

    return results


def save_report(report, output_path):

    with open(output_path, "w") as file:

        json.dump(
            report,
            file,
            indent=4
        )