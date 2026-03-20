from datetime import datetime
from action_layer.router import route_action

def generate_actions(anomalies):
    actions = []

    for item in anomalies:
        driver = item["driver"]

        # Driver-specific intelligence
        if driver == "EC2":
            recommendation = "Consider stopping or terminating idle instance"
        elif driver == "RDS":
            recommendation = "Review database sizing and utilization"
        elif driver == "S3":
            recommendation = "Apply lifecycle policy or remove unused storage"
        else:
            recommendation = "Review resource for optimization"

        routing = route_action(item)

        action = {
            "driver": driver,
            "resource": item["resource"],
            "owner": item["owner"],
            "team": routing["team"],
            "priority": routing["priority"],
            "ticket": routing["ticket"],
            "action": recommendation,
            "timestamp": str(datetime.now())
        }

        actions.append(action)

    return actions
