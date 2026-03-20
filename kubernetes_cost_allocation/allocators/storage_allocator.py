def allocate_storage_cost(workloads: list, volumes: list) -> list:
    storage_map = {}

    for volume in volumes:
        key = (volume["cluster_name"], volume["namespace"], volume["workload"])
        storage_map[key] = storage_map.get(key, 0) + volume["monthly_storage_cost"]

    for workload in workloads:
        key = (workload["cluster_name"], workload["namespace"], workload["workload"])
        workload["storage_cost"] = round(storage_map.get(key, 0), 2)

    return workloads
