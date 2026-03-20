def evaluate_architecture_scenarios(scenarios):
    results = []

    for scenario in scenarios:
        name = scenario["scenario"]
        monthly_compute_cost = scenario["monthly_compute_cost"]
        monthly_storage_cost = scenario["monthly_storage_cost"]
        monthly_database_cost = scenario["monthly_database_cost"]
        transactions = scenario["transactions"]

        estimated_monthly_cost = (
            monthly_compute_cost
            + monthly_storage_cost
            + monthly_database_cost
        )

        if transactions > 0:
            cost_per_transaction = round(estimated_monthly_cost / transactions, 4)
        else:
            cost_per_transaction = 0

        if cost_per_transaction > 0.10:
            advice = "High cost per transaction. Review architecture efficiency, caching, and scaling strategy."
        elif monthly_database_cost > monthly_compute_cost:
            advice = "Database cost dominates. Review sizing, query efficiency, and storage patterns."
        elif monthly_storage_cost > 200:
            advice = "Storage cost is growing. Review lifecycle policies and data retention strategy."
        else:
            advice = "Architecture cost profile looks reasonable. Continue monitoring growth and efficiency."

        results.append({
            "scenario": name,
            "estimated_monthly_cost": estimated_monthly_cost,
            "transactions": transactions,
            "cost_per_transaction": cost_per_transaction,
            "advice": advice
        })

    return results
