import json

def export_result(result, output_path):
    with open(output_path, "w") as f:
        json.dump(result, f, indent=4)
