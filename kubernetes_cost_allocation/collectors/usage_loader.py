import csv


def load_pod_requests_usage(file_path: str) -> list:
    workloads = []

    with open(file_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            workloads.append({
                "cluster_name": row["cluster_name"],
                "namespace": row["namespace"],
                "workload": row["workload"],
                "workload_type": row["workload_type"],
                "pod": row["pod"],
                "owner": row["owner"],
                "team": row["team"],
                "product": row["product"],
                "environment": row["environment"],
                "cpu_request_cores": float(row["cpu_request_cores"]),
                "memory_request_gb": float(row["memory_request_gb"]),
                "cpu_usage_cores": float(row["cpu_usage_cores"]),
                "memory_usage_gb": float(row["memory_usage_gb"]),
                "runtime_hours": float(row["runtime_hours"])
            })

    return workloads
