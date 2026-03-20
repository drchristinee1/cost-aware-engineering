import json
from shift_left.architecture_cost_advisor import evaluate_architecture_scenarios

def load_mock_scenarios():
    return [
        {
            "scenario": "baseline",
            "monthly_compute_cost": 300,
            "monthly_storage_cost": 100,
            "monthly_database_cost": 200,
            "transactions": 10000
        },
        {
            "scenario": "high_traffic_growth",
            "monthly_compute_cost": 500,
            "monthly_storage_cost": 150,
            "monthly_database_cost": 300,
            "transactions": 12000
        },
        {
            "scenario": "database_heavy_design",
            "monthly_compute_cost": 250,
            "monthly_storage_cost": 120,
            "monthly_database_cost": 500,
            "transactions": 7000
        }
    ]

def main():
    scenarios = load_mock_scenarios()
    results = evaluate_architecture_scenarios(scenarios)

    print("🏗️ Architecture Cost Advisor")
    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    main()
