import json


def load_json(file_path):
    """
    Load JSON file safely.
    """

    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("File not found.")
        return None

    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return None