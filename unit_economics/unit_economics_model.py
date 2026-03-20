def calculate_unit_economics(resources, business_metrics):
    total_cost = sum([r["cost"] for r in resources])

    results = {}

    for metric, value in business_metrics.items():
        if value > 0:
            cost_per_unit = total_cost / value
        else:
            cost_per_unit = 0

        results[metric] = {
            "total_cost": total_cost,
            "units": value,
            "cost_per_unit": round(cost_per_unit, 2)
        }

    return results
