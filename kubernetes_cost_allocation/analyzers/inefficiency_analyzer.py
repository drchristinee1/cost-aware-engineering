def calculate_usage_shares(workloads: list, cpu_weight: float = 0.5, memory_weight: float = 0.5) -> list:
    total_cpu_usage = sum(w["cpu_usage_cores"] for w in workloads)
    total_memory_usage = sum(w["memory_usage_gb"] for w in workloads)

    for workload in workloads:
        cpu_usage_share = (
            workload["cpu_usage_cores"] / total_cpu_usage
            if total_cpu_usage > 0 else 0
        )
        memory_usage_share = (
            workload["memory_usage_gb"] / total_memory_usage
            if total_memory_usage > 0 else 0
        )

        weighted_usage_share = (cpu_usage_share * cpu_weight) + (memory_usage_share * memory_weight)

        workload["weighted_usage_share"] = weighted_usage_share

    return workloads


def calculate_usage_based_cost(workloads: list, total_compute_and_shared_cost: float) -> list:
    for workload in workloads:
        workload["usage_based_cost"] = round(
            workload["weighted_usage_share"] * total_compute_and_shared_cost,
            2
        )

    return workloads


def calculate_inefficiency(workloads: list) -> list:
    for workload in workloads:
        request_total = workload["compute_request_cost"] + workload["shared_cost_allocated"]
        usage_total = workload["usage_based_cost"]

        over_allocation_cost = max(request_total - usage_total, 0)
        under_allocation_cost = max(usage_total - request_total, 0)

        workload["over_allocation_cost"] = round(over_allocation_cost, 2)
        workload["under_allocation_cost"] = round(under_allocation_cost, 2)

        if over_allocation_cost > 0:
            workload["allocation_status"] = "OVER_PROVISIONED"
        elif under_allocation_cost > 0:
            workload["allocation_status"] = "UNDER_PROVISIONED"
        else:
            workload["allocation_status"] = "BALANCED"

        workload["request_based_cost"] = round(request_total, 2)
        workload["inefficiency_cost"] = round(over_allocation_cost, 2)
        workload["total_allocated_cost"] = round(
            workload["request_based_cost"] + workload["storage_cost"], 2
        )

        workload["efficiency_ratio"] = round(
            usage_total / request_total, 2
        ) if request_total > 0 else 0

    return workloads
