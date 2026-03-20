from datetime import datetime
import uuid

def build_jira_ticket(action):
    ticket_id = f"{action['ticket']}-{str(uuid.uuid4())[:6].upper()}"

    return {
        "ticket_id": ticket_id,
        "assigned_team": action["team"],
        "owner": action["owner"],
        "status": "OPEN",
        "summary": f"{action['driver']} cost anomaly - {action['resource']}",
        "description": action["action"],
        "priority": action["priority"].upper(),
        "created_at": str(datetime.now())
    }
