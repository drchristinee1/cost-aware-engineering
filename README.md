# cost-aware-engineering

Prototype FinOps platform for cost-aware engineering, unit economics, and automated cloud cost accountability.

## Overview

This repository demonstrates a modular FinOps execution pipeline that moves cloud cost management left — from reactive billing review to proactive engineering action.

Instead of stopping at cost visibility, the system translates cost signals into:

- driver-aware recommendations
- owner and team routing
- priority assignment
- Jira-style execution artifacts
## 🚀 Capabilities

### 1. Cost Signal → Action Engine
- Detect anomalies and cost drivers
- Generate structured remediation actions
- Route to owners (Jira-style output)

### 2. Tagging Governance Engine
- Detect missing required tags (owner, environment, product, cost_center)
- Prioritize tagging gaps
- Enable cost accountability

### 3. Showback Engine
- Aggregate cloud spend by owner
- Surface unassigned cost
- Support financial accountability and chargeback models

### 4. Architecture Cost Advisor
This module simulates how architecture choices affect monthly cloud cost and cost per transaction before deployment.

It is designed to support shift-left FinOps by helping teams evaluate design tradeoffs earlier, instead of waiting for billing surprises.

### What it evaluates
- estimated monthly cost
- transaction volume
- cost per transaction
- architecture guidance

### Example output

```json
[
  {
    "scenario": "baseline",
    "estimated_monthly_cost": 600,
    "transactions": 10000,
    "cost_per_transaction": 0.06,
    "advice": "Architecture cost profile looks reasonable. Continue monitoring growth and efficiency."
  },
  {
    "scenario": "database_heavy_design",
    "estimated_monthly_cost": 870,
    "transactions": 7000,
    "cost_per_transaction": 0.1243,
    "advice": "High cost per transaction. Review architecture efficiency, caching, and scaling strategy."
  }

### 5. Kubernetes Cost Allocation Engine
- Allocate shared Kubernetes cluster cost to workloads, namespaces, teams, and products
- Use request-based allocation for reserved platform demand
- Compare request-based cost vs usage-based cost
- Surface inefficiency and over-allocation
- Directly attribute persistent volume cost
- Create a foundation for container showback, chargeback, and unit economics]
## 🔗 Unified FinOps System

This repository implements a full FinOps control loop:

```text
Cost Signals
   ↓
Tagging Governance (Who owns the cost?)
   ↓
Showback (Where is cost allocated?)
   ↓
Unit Economics (What is cost per business outcome?)
---

## 🧠 Example: Tagging + Showback Output

### Tagging Issues
```json
[
  {
    "resource": "db-1",
    "missing_tag": "owner",
    "priority": "high"
  }
]

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

