from src.loader import load_json
from src.assignment import assign_packages
from src.simulator import simulate_delivery
from src.report_generator import (
    generate_report,
    save_report
)
from src.csv_exporter import export_best_agent


def main():

    data = load_json("data/data.json")

    if not data:
        return

    warehouses = data["warehouses"]
    agents = data["agents"]
    packages = data["packages"]

    assignments = assign_packages(
        packages,
        agents,
        warehouses
    )

    results = simulate_delivery(
        assignments,
        agents,
        warehouses
    )

    report = generate_report(results)

    save_report(
        report,
        "output/report.json"
    )

    export_best_agent(
        report,
        "output/top_performer.csv"
    )

    print("\nFINAL REPORT\n")
    print(report)


if __name__ == "__main__":
    main()