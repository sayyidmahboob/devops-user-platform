# DevOps User Platform

A lightweight platform that simulates user onboarding, automated testing, DevOps pipelines, feature flag deployments, and workflow automation.

This project demonstrates how modern product teams manage feature releases using automated validation, monitoring, and reporting workflows.

---

# Project Objective

The objective of this project is to simulate a small-scale product environment where user onboarding, feature deployment, and system monitoring are managed through automation and DevOps principles.

The platform combines authentication flows, automated test execution, deployment decision logic, and reporting workflows into a single system.

---

# Core Capabilities

The platform includes the following capabilities:

User Authentication

* Email and password based signup and login
* OTP-based login simulation for testing passwordless flows

DevOps Simulation

* Automated test execution before deployment
* Feature flag validation
* Deployment decision based on test outcomes

Automation Workflows

* Pipeline monitoring
* Stakeholder reporting
* Issue escalation

Analytics and Monitoring

* Basic product usage tracking
* Deployment status monitoring

Customer Support Flow

* User issue reporting
* Automated Jira ticket creation

---

# Authentication Methods

The system supports two authentication flows.

Email & Password Login
Users can register and login using standard credentials.

OTP Login (Simulation)
A simplified OTP authentication flow is included for testing passwordless login systems.

Example test numbers:

| Phone Number | OTP    |
| ------------ | ------ |
| 9999999999   | 123456 |
| 8888888888   | 654321 |

This avoids the need for external SMS APIs while still demonstrating the authentication workflow.

---

# DevOps Pipeline Simulation

The platform includes a simulated CI/CD pipeline workflow.

Code Change
↓
Automated Test Execution
↓
Feature Flag Validation
↓
Deployment Decision

If all tests pass, the feature is deployed.
If tests fail, the system simulates a rollback.

This demonstrates how automated pipelines help maintain release reliability.

---

# Automated Test Coverage

The system includes automated tests for the following areas:

Signup Tests – 10 cases
Login Tests – 10 cases
Feature Tests – 10 cases

Total: 30 automated tests.

These tests simulate validation checks commonly executed in CI/CD pipelines.

---

# Automation Layer

Automation workflows are implemented using **n8n**.

Workflows include:

Pipeline monitoring
Stakeholder reporting
Customer issue escalation

This layer demonstrates how operational tasks can be automated to reduce manual intervention.

---

# Technology Stack

Frontend
HTML
CSS
JavaScript

Backend
Python (FastAPI)

Database
SQLite / PostgreSQL

Automation
n8n

DevOps Simulation
GitHub + automated test scripts

Analytics
Google Sheets / Tableau (for reporting)

Issue Tracking
Jira

---

# Project Structure

```
devops-user-platform
│
├── frontend
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── css
│   └── js
│
├── backend
│   ├── main.py
│   ├── config.py
│   ├── api
│   ├── models
│   └── services
│
├── database
│   └── schema.sql
│
├── tests
│   ├── test_signup.py
│   ├── test_login.py
│   └── test_features.py
│
├── devops
│   └── pipeline.yml
│
├── automation
│   └── n8n
│
├── dashboard
│
├── docs
│   ├── PRD.md
│   └── architecture.md
│
└── scripts
```

---

# Project Timeline

The project is being built within a 20-day development window.

Day 1–3
Planning, architecture design, repository setup

Day 4–7
Frontend authentication flows

Day 8–10
Backend API implementation

Day 11–13
Automated test cases

Day 14–16
DevOps pipeline simulation

Day 17–18
Automation workflows (n8n)

Day 19
Analytics dashboard

Day 20
Testing and documentation

---

# Learning Outcomes

This project demonstrates practical exposure to:

Product thinking
Authentication system design
DevOps pipeline concepts
Automated testing strategies
Feature flag deployment
Workflow automation
Operational monitoring

---

# Author

This project was created as a learning exercise to understand how modern product teams combine development, testing, automation, and monitoring into a unified delivery workflow.
