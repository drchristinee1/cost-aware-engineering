def allocate_shared_cost(workloads: list, total_shared_cost: float) -> list:
    for workload in workloads:
        workload["shared_cost_allocated"] = round(
            workload["weighted_request_share"] * total_shared_cost, 2
        )

    return workloads
