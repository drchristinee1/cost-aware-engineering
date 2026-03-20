import json


def export_allocation_report(report: dict, output_path: str) -> None:
    with open(output_path, "w") as f:
        json.dump(report, f, indent=4)
