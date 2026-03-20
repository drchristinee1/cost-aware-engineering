import json

from run_tagging_showback import load_mock_resources, detect_tagging_issues, build_showback
from unit_economics.unit_economics_model import calculate_unit_economics

def load_business_metrics():
    return {
        "transactions": 10000,
        "customers": 250,
        "api_calls": 50000
    }

def main():
    resources = load_mock_resources()

    # 1. Governance
    tagging_issues = detect_tagging_issues(resources)

    # 2. Showback
    showback = build_showback(resources)

    # 3. Unit Economics
    business_metrics = load_business_metrics()
    unit_economics = calculate_unit_economics(resources, business_metrics)

    final_output = {
        "tagging_issues": tagging_issues,
        "showback": showback,
        "unit_economics": unit_economics
    }

    print("\n🚀 FULL FINOPS SYSTEM OUTPUT\n")
    print(json.dumps(final_output, indent=4))

if __name__ == "__main__":
    main()
