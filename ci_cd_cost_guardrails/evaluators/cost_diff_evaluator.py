from utils.calculations import percent_change

def evaluate_cost_diff(baseline, proposed):
    baseline_cost = baseline["estimated_monthly_cost"]
    proposed_cost = proposed["estimated_monthly_cost"]

    monthly_increase = proposed_cost - baseline_cost
    percent_increase = percent_change(baseline_cost, proposed_cost)

    cpu_increase = percent_change(
        baseline["cpu_request_cores"],
        proposed["cpu_request_cores"]
    )

    memory_increase = percent_change(
        baseline["memory_request_gb"],
        proposed["memory_request_gb"]
    )

    replica_increase = proposed["replicas"] - baseline["replicas"]

    return {
        "service_name": proposed["service_name"],
        "baseline_cost": baseline_cost,
        "proposed_cost": proposed_cost,
        "monthly_cost_increase": monthly_increase,
        "percent_cost_increase": percent_increase,
        "cpu_increase_percent": cpu_increase,
        "memory_increase_percent": memory_increase,
        "replica_increase": replica_increase
    }
