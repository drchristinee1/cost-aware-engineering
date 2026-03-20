def route_action(item):
    driver = item["driver"]

    if driver == "EC2":
        team = "infrastructure-team"
        priority = "medium"
        ticket = "INFRA-AUTO"
    elif driver == "RDS":
        team = "database-team"
        priority = "high"
        ticket = "DB-AUTO"
    elif driver == "S3":
        team = "storage-team"
        priority = "medium"
        ticket = "STORAGE-AUTO"
    else:
        team = "finops-team"
        priority = "low"
        ticket = "FINOPS-AUTO"

    return {
        "team": team,
        "priority": priority,
        "ticket": ticket
    }
