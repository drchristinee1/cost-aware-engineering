import csv


def load_persistent_volumes(file_path: str) -> list:
    volumes = []

    with open(file_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            volumes.append({
                "cluster_name": row["cluster_name"],
                "namespace": row["namespace"],
                "workload": row["workload"],
                "volume_name": row["volume_name"],
                "storage_gb": float(row["storage_gb"]),
                "monthly_storage_cost": float(row["monthly_storage_cost"])
            })

    return volumes
