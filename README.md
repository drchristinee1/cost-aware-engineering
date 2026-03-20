# cost-aware-engineering

Prototype FinOps platform for cost-aware engineering, unit economics, and automated cloud cost accountability.

## Overview

This repository demonstrates a modular FinOps execution pipeline that moves cloud cost management left — from reactive billing review to proactive engineering action.

Instead of stopping at cost visibility, the system translates cost signals into:

- driver-aware recommendations
- owner and team routing
- priority assignment
- Jira-style execution artifacts

## Why this matters

Many FinOps workflows stop at reporting. This prototype is designed to show how FinOps can operate as an engineering enablement system:

- Detect cost anomalies
- Interpret the underlying cost driver
- Generate context-aware actions
- Route actions to the correct team
- Simulate execution through ticket creation

## Current working pipeline

The current prototype implements this flow:

```text
Detection Layer
-> Driver Intelligence Layer
-> Action Generation Layer
-> Routing Layer
-> Jira Simulation Layer


---

## Example output

### Action output

```json
{
  "driver": "RDS",
  "resource": "db-1",
  "owner": "team-b",
  "team": "database-team",
  "priority": "high",
  "ticket": "DB-AUTO",
  "action": "Review database sizing and utilization"
}




### Jira ticket output

```json
{
  "ticket_id": "DB-AUTO-XXXXXX",
  "assigned_team": "database-team",
  "owner": "team-b",
  "status": "OPEN",
  "summary": "RDS cost anomaly - db-1",
  "description": "Review database sizing and utilization",
  "priority": "HIGH"
}

