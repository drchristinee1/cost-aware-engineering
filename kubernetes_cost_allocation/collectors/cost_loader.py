import csv


def load_cluster_costs(file_path: str) -> list:
    costs = []

    with open(file_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            costs.append({
                "cluster_name": row["cluster_name"],
                "date": row["date"],
                "cost_type": row["cost_type"],
                "cost_subtype": row["cost_subtype"],
                "amount": float(row["amount"])
            })

    return costs
