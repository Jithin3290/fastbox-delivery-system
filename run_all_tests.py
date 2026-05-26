import os

from src.loader import load_json
from src.utils import normalize_data
from src.assignment import assign_packages
from src.simulator import simulate_delivery

from src.report_generator import (
    generate_report,
    save_report
)

from src.csv_exporter import (
    export_best_agent
)

from src.ascii_visualizer import (
    print_routes
)


# Folder containing all JSON test files
DATA_FOLDER = "data"

# Folder where reports will be saved
OUTPUT_FOLDER = "output"

# Create output folder automatically if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def run_test(file_name):
    """
    Run a single JSON test case.
    """

    # Build full file path
    file_path = os.path.join(
        DATA_FOLDER,
        file_name
    )

    print("\n" + "=" * 60)
    print(f"Running Test Case: {file_name}")
    print("=" * 60)

    # Load JSON data
    data = load_json(file_path)

    # Stop execution if JSON loading fails
    if not data:
        print("Failed to load JSON.")
        return

    # Normalize JSON structure
    # This handles different input formats
    warehouses, agents, packages = (
        normalize_data(data)
    )

    # Assign each package to nearest agent
    assignments = assign_packages(
        packages,
        agents,
        warehouses
    )

    # Simulate delivery process
    results = simulate_delivery(
        assignments,
        agents,
        warehouses
    )

    # Print ASCII delivery routes
    print_routes(assignments)

    # Generate final report
    report = generate_report(results)

    # Create report JSON filename
    report_file = file_name.replace(
        ".json",
        "_report.json"
    )

    # Build report file path
    report_path = os.path.join(
        OUTPUT_FOLDER,
        report_file
    )

    # Save JSON report
    save_report(
        report,
        report_path
    )

    # Create CSV filename
    csv_file = file_name.replace(
        ".json",
        "_top_performer.csv"
    )

    # Build CSV file path
    csv_path = os.path.join(
        OUTPUT_FOLDER,
        csv_file
    )

    # Export top performer CSV
    export_best_agent(
        report,
        csv_path
    )

    # Validate package delivery count
    total_delivered = sum(
        agent_data["packages_delivered"]
        for key, agent_data in report.items()
        if isinstance(agent_data, dict)
    )

    expected_packages = len(packages)

    print("\nVALIDATION")
    print("-" * 60)

    if total_delivered == expected_packages:

        print(
            f"PASS: "
            f"{total_delivered}/{expected_packages} "
            f"packages delivered successfully"
        )

    else:

        print(
            f"FAIL: "
            f"{total_delivered}/{expected_packages} "
            f"packages delivered"
        )

    # Print formatted report
    print("\nFINAL REPORT")
    print("-" * 60)

    for agent, details in report.items():

        # Agent data dictionary
        if isinstance(details, dict):

            print(f"\nAgent: {agent}")

            print(
                f"Packages Delivered : "
                f"{details['packages_delivered']}"
            )

            print(
                f"Total Distance    : "
                f"{details['total_distance']}"
            )

            print(
                f"Total Delay       : "
                f"{details['total_delay']}"
            )

            print(
                f"Efficiency        : "
                f"{details['efficiency']}"
            )

        # Best agent string
        else:

            print(f"\nBest Agent: {details}")

    # Display generated file paths
    print("\nFILES GENERATED")
    print("-" * 60)

    print(f"JSON Report : {report_path}")
    print(f"CSV Report  : {csv_path}")

    print("\nTest Completed Successfully")


def main():
    """
    Execute all JSON test files automatically.
    """

    # Get all JSON files from data folder
    json_files = sorted([
        file_name
        for file_name in os.listdir(DATA_FOLDER)
        if file_name.endswith(".json")
    ])

    print("\nFASTBOX DELIVERY SYSTEM TEST SUITE")
    print("=" * 60)

    # Run all test cases
    for file_name in json_files:

        run_test(file_name)

    print("\n" + "=" * 60)
    print("ALL TEST CASES EXECUTED")
    print("=" * 60)


# Program entry point
if __name__ == "__main__":
    main()