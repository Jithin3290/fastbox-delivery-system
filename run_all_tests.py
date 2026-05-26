import os

from src.loader import load_json
from src.utils import normalize_data
from src.assignment import assign_packages
from src.simulator import simulate_delivery
from src.report_generator import generate_report


DATA_FOLDER = "data"


def run_test(file_name):

    file_path = os.path.join(
        DATA_FOLDER,
        file_name
    )

    print(f"\nRunning Test: {file_name}")

    data = load_json(file_path)

    if not data:
        return

    warehouses, agents, packages = (
        normalize_data(data)
    )

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

    print(report)


def main():

    for file_name in os.listdir(DATA_FOLDER):

        if file_name.endswith(".json"):

            run_test(file_name)


if __name__ == "__main__":
    main()