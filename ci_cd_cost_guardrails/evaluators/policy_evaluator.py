def evaluate_policies(metrics, policies):
    t = policies["thresholds"]

    triggered = []

    if metrics["monthly_cost_increase"] > t["max_monthly_cost_increase"]:
        triggered.append("monthly_cost")

    if metrics["percent_cost_increase"] > t["max_percent_increase"]:
        triggered.append("percent_cost")

    if metrics["cpu_increase_percent"] > t["max_cpu_request_increase_percent"]:
        triggered.append("cpu")

    if metrics["memory_increase_percent"] > t["max_memory_request_increase_percent"]:
        triggered.append("memory")

    if metrics["replica_increase"] > t["max_replica_increase"]:
        triggered.append("replicas")

    if triggered:
        status = "FAIL"
    else:
        status = "PASS"

    return {
        "status": status,
        "triggered_policies": triggered,
        "recommendation": (
            "Reduce resource requests or require approval before deployment"
            if status == "FAIL"
            else "Review cost impact before deployment"
            if status == "WARN"
            else "Change is within cost guardrails"
        )
    }
