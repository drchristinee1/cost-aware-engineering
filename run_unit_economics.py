import json
from unit_economics.unit_economics_model import calculate_unit_economics

def load_mock_data():
    resources = [
        {"resource": "ec2-1", "cost": 200},
        {"resource": "rds-1", "cost": 300},
        {"resource": "s3-1", "cost": 100}
    ]

    business_metrics = {
        "transactions": 10000,
        "customers": 250,
        "api_calls": 50000
    }

    return resources, business_metrics

def main():
    resources, business_metrics = load_mock_data()

    results = calculate_unit_economics(resources, business_metrics)

    print("💰 Unit Economics:")
    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    main()
