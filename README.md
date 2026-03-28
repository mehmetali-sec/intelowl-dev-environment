# IntelOwl Development Environment Setup Log

This repository documents my journey of setting up and configuring **IntelOwl** as part of my preparation for **GSoC 2026**. 

### 🎯 Objective
As a 2nd-year Computer Engineering student aiming for a **SOC Analyst** role in the banking sector, my goal was to deploy a fully functional threat intelligence stack to understand its microservices architecture.

### 🛠 Tech Stack Used
* **Infrastructure:** Docker & Docker Compose
* **Backend:** Python (Django / uWSGI)
* **Task Queue:** Celery & Redis
* **Database:** PostgreSQL
* **Environment:** macOS (MacBook Air)

### 🚀 Implementation Steps
1. **Containerization:** Deployed multiple services using `default.yml` and specific overrides for Postgres and Redis.
2. **Database Migrations:** Successfully executed Django migrations within the `uwsgi` container.
3. **Superuser Creation:** Configured administrative access for the dashboard.
4. **Troubleshooting:** - Resolved `Access Denied` issues by inspecting `uwsgi` logs.
   - Fixed Redis connection timeouts by verifying worker status.
   - Configured **Traffic Light Protocol (TLP)** settings for secure data analysis.

### 🔍 Initial Tests
- Performed a sample analysis on the **EICAR test file hash**.
- Verified integration with global analyzers.
- Analyzed the behavior of Celery workers during high-load requests.

---
*This setup serves as the foundation for my proposed GSoC project: **Financial Anti-Phishing & Brand Protection Modules.***
