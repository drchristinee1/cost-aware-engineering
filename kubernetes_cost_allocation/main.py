import json
import yaml

from collectors.cost_loader import load_cluster_costs
from collectors.usage_loader import load_pod_requests_usage
from collectors.storage_loader import load_persistent_volumes

from allocators.request_allocator import calculate_request_shares, allocate_compute_cost
from allocators.shared_cost_allocator import allocate_shared_cost
from allocators.storage_allocator import allocate_storage_cost

from analyzers.inefficiency_analyzer import (
    calculate_usage_shares,
    calculate_usage_based_cost,
    calculate_inefficiency,
)

from utils.export import export_allocation_report


def load_config(config_path: str) -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def summarize_costs(cluster_costs: list, shared_cost_types: list) -> tuple:
    total_compute_cost = 0
    total_shared_cost = 0

    for cost in cluster_costs:
        if cost["cost_type"] == "compute":
            total_compute_cost += cost["amount"]
        elif cost["cost_type"] in shared_cost_types:
            total_shared_cost += cost["amount"]

    return total_compute_cost, total_shared_cost


def build_report(cluster_name: str, workloads: list, cluster_costs: list) -> dict:
    total_cluster_cost = round(sum(c["amount"] for c in cluster_costs), 2)
    total_allocated_cost = round(sum(w["total_allocated_cost"] for w in workloads), 2)
    unallocated_cost = round(total_cluster_cost - total_allocated_cost, 2)

    return {
        "cluster_name": cluster_name,
        "summary": {
            "total_cluster_cost": total_cluster_cost,
            "total_allocated_cost": total_allocated_cost,
            "unallocated_cost": unallocated_cost
        },
        "workloads": workloads
    }


def main():
    config = load_config("config.yaml")

    cpu_weight = config["weights"]["cpu"]
    memory_weight = config["weights"]["memory"]
    shared_cost_types = config["shared_cost_types"]

    cluster_costs = load_cluster_costs("data/cluster_costs.csv")
    workloads = load_pod_requests_usage("data/pod_requests_usage.csv")
    volumes = load_persistent_volumes("data/persistent_volumes.csv")

    if not workloads:
        print("No workload data found.")
        return

    cluster_name = workloads[0]["cluster_name"]

    total_compute_cost, total_shared_cost = summarize_costs(cluster_costs, shared_cost_types)

    workloads = calculate_request_shares(workloads, cpu_weight, memory_weight)
    workloads = allocate_compute_cost(workloads, total_compute_cost)
    workloads = allocate_shared_cost(workloads, total_shared_cost)
    workloads = allocate_storage_cost(workloads, volumes)

    total_compute_and_shared_cost = total_compute_cost + total_shared_cost

    workloads = calculate_usage_shares(workloads, cpu_weight, memory_weight)
    workloads = calculate_usage_based_cost(workloads, total_compute_and_shared_cost)
    workloads = calculate_inefficiency(workloads)

    report = build_report(cluster_name, workloads, cluster_costs)

    export_allocation_report(report, "outputs/allocation_report.json")

    print("\n✅ Kubernetes cost allocation report generated successfully.")
    print("📄 Output saved to outputs/allocation_report.json")
    print("\nSummary:")
    print(json.dumps(report["summary"], indent=4))


if __name__ == "__main__":
    main()
