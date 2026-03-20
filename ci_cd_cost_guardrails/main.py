import json
import sys
from utils.loader import load_json, load_yaml
from utils.exporter import export_result
from evaluators.cost_diff_evaluator import evaluate_cost_diff
from evaluators.policy_evaluator import evaluate_policies

def main():
    baseline = load_json("ci_cd_cost_guardrails/inputs/baseline_config.json")
    proposed = load_json("ci_cd_cost_guardrails/inputs/proposed_config.json")
    policies = load_yaml("ci_cd_cost_guardrails/policies/cost_policies.yaml")
    config = load_yaml("ci_cd_cost_guardrails/config.yaml")
    metrics = evaluate_cost_diff(baseline, proposed)
    decision = evaluate_policies(metrics, policies)

    result = {**metrics, **decision}


    export_result(result, config["default_output_path"])

    if result["status"] == "FAIL":
        print("\n❌ DEPLOYMENT BLOCKED")
    elif result["status"] == "WARN":
        print("\n⚠️ REVIEW REQUIRED")
    else:
        print("\n✅ DEPLOYMENT APPROVED")

    print(f"Service: {result['service_name']}")
    print(f"Monthly Cost Increase: ${result['monthly_cost_increase']}")
    print(f"Percent Cost Increase: {result['percent_cost_increase']}%")
    print(f"Triggered Policies: {', '.join(result['triggered_policies']) if result['triggered_policies'] else 'None'}")
    print(f"Recommendation: {result['recommendation']}")

    print("\nFull Result:")
    print(json.dumps(result, indent=4))
    if result["status"] == "FAIL":
        sys.exit(1)

if __name__ == "__main__":
    main()
