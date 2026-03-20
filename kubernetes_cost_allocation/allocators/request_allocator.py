def calculate_request_shares(workloads: list, cpu_weight: float = 0.5, memory_weight: float = 0.5) -> list:
    total_cpu_requests = sum(w["cpu_request_cores"] for w in workloads)
    total_memory_requests = sum(w["memory_request_gb"] for w in workloads)

    for workload in workloads:
        cpu_share = (
            workload["cpu_request_cores"] / total_cpu_requests
            if total_cpu_requests > 0 else 0
        )
        memory_share = (
            workload["memory_request_gb"] / total_memory_requests
            if total_memory_requests > 0 else 0
        )

        weighted_share = (cpu_share * cpu_weight) + (memory_share * memory_weight)

        workload["cpu_request_share"] = cpu_share
        workload["memory_request_share"] = memory_share
        workload["weighted_request_share"] = weighted_share

    return workloads


def allocate_compute_cost(workloads: list, total_compute_cost: float) -> list:
    for workload in workloads:
        workload["compute_request_cost"] = round(
            workload["weighted_request_share"] * total_compute_cost, 2
        )

    return workloads
