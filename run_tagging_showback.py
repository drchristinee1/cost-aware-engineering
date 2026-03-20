import json

def load_mock_resources():
    return [
        {
            "resource": "i-123",
            "service": "EC2",
            "cost": 120,
            "owner": "team-a",
            "environment": "prod",
            "product": "payments",
            "cost_center": "cc-1001"
        },
        {
            "resource": "db-1",
            "service": "RDS",
            "cost": 300,
            "owner": "",
            "environment": "prod",
            "product": "analytics",
            "cost_center": ""
        },
        {
            "resource": "bucket-1",
            "service": "S3",
            "cost": 50,
            "owner": "team-a",
            "environment": "",
            "product": "",
            "cost_center": "cc-1002"
        }
    ]

def detect_tagging_issues(resources):
    required_tags = ["owner", "environment", "product", "cost_center"]
    issues = []

    for item in resources:
        for tag in required_tags:
            value = item.get(tag, "")
            if not value:
                issues.append({
                    "resource": item["resource"],
                    "missing_tag": tag,
                    "priority": "high"
                })

    return issues

def build_showback(resources):
    report = {}

    for item in resources:
        owner = item.get("owner") or "unassigned"
        report[owner] = report.get(owner, 0) + item["cost"]

    return report

def main():
    resources = load_mock_resources()

    tagging_issues = detect_tagging_issues(resources)
    showback = build_showback(resources)

    print("✅ Tagging Issues:")
    print(json.dumps(tagging_issues, indent=4))

    print("\n💰 Showback:")
    print(json.dumps(showback, indent=4))

if __name__ == "__main__":
    main()
