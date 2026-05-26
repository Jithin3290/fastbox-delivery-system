from src.loader import load_json
from src.assignment import assign_packages
from src.simulator import simulate_delivery
from src.report_generator import (
    generate_report,
    save_report
)
from src.csv_exporter import export_best_agent
from src.utils import normalize_data
from src.ascii_visualizer import print_routes

def main():
    """
    Main function to run the delivery simulation and generate reports.
    """
    data = load_json("data/base_case.json")
    if not data:
        return

    warehouses, agents, packages = normalize_data(data)

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
    print_routes(assignments)
    report = generate_report(results)

    save_report(
        report,
        "output/report.json"
    )

    export_best_agent(
        report,
        "output/top_performer.csv"
    )

    print("\nFINAL REPORT")
    print("=" * 50)

    for agent, details in report.items():

        print(f"{agent}: {details}")

    print("\nFiles Generated Successfully")
    print("output/report.json")
    print("output/top_performer.csv")


if __name__ == "__main__":
    main()