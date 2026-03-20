import json
from detection.anomaly_detector import detect_anomalies
from action_layer.action_generator import generate_actions
from action_layer.jira_ticket_builder import build_jira_ticket

def load_sample_data():
    return [
        {"driver": "EC2", "resource": "i-123", "cost": 120, "owner": "team-a"},
        {"driver": "RDS", "resource": "db-1", "cost": 300, "owner": "team-b"},
        {"driver": "S3", "resource": "bucket-1", "cost": 50, "owner": "team-a"},
    ]

def save_output(actions, tickets):
    with open("output/actions.json", "w") as f:
        json.dump(actions, f, indent=4)

    with open("output/jira_tickets.json", "w") as f:
        json.dump(tickets, f, indent=4)

def main():
    data = load_sample_data()
    anomalies = detect_anomalies(data)
    actions = generate_actions(anomalies)
    tickets = [build_jira_ticket(action) for action in actions]
    save_output(actions, tickets)

    print("✅ Modular FinOps pipeline with Jira simulation executed")
    print("\nActions:")
    print(json.dumps(actions, indent=4))
    print("\nJira Tickets:")
    print(json.dumps(tickets, indent=4))

if __name__ == "__main__":
    main()
