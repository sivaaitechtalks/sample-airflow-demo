🚀 Airflow Local Development Guide (VS Code + UI)

This guide walks you through setting up Airflow locally, creating a simple DAG, and running it both via CLI and the UI. It also covers best practices for git repo structure.

📁 1. Prepare Your Environment

Activate your virtual environment (venv or conda).

Verify Airflow installation using pip show apache-airflow.

Confirm the environment interpreter with which python.

🏠 2. Set Your AIRFLOW_HOME

Choose your project root, e.g.:

sample-airflow/sample-airlow-demo


Set AIRFLOW_HOME so Airflow uses your project’s dags/, logs/, and airflow.cfg.

🗄️ 3. Initialize the Metadata Database

Run:

DB setup: airflow db migrate

Optional full reset: airflow db reset --yes then migrate again

This creates / upgrades the metadata database.

🚀 4. Start Airflow
Option A: Recommended for local setup

Run: airflow standalone

Starts:

Webserver

Scheduler

Triggerer

DAG processor

API server

Also auto-creates an admin user.

Option B: Start services manually

airflow webserver -p <port>

airflow scheduler

🔐 5. Handle Login / Credentials

When running airflow standalone, Airflow prints auto-generated username & password.

If not printed:

Check the generated file:
simple_auth_manager_passwords.json.generated

If needed:

Reset DB → run standalone → a fresh user will be created.

If signup is allowed, you can create an account directly in the UI.

🔌 6. Fix Port Conflicts (if any)

Use lsof -i :8080 or equivalent to identify blocking processes.

Kill the process or run webserver on another port.

Restart Airflow services.

📂 7. DAG File Structure (Concept)

All DAG files must be inside:

AIRFLOW_HOME/dags


Each DAG file should:

Define a unique dag_id

Include task definitions

Avoid heavy imports (fails scheduler/import)

🧪 8. Test DAG Locally Before UI

Use CLI test:

airflow tasks test <dag_id> <task_id> <execution_date>


Runs the task code locally

Does not require scheduler

Helps catch import or runtime errors

🌐 9. Run and Observe DAG in UI

Open:

http://localhost:8080


Ensure your DAG appears in the list.

Trigger the DAG manually from the UI.

Check:

Graph View

Tree View

Task Logs (to confirm task outputs)

If DAG doesn't appear:

Verify AIRFLOW_HOME is correct

Check dag-processor logs for import errors

Ensure the DAG file has no syntax/runtime errors

🧹 10. Debugging Tips

If DAG import errors occur:

Run the DAG file using python your_dag.py to identify issues.

If UI shows 401 Unauthorized:

Use credentials printed by standalone

Or regenerate via DB reset

If logs not writing:

Ensure logs/ directory exists and is writable

📦 11. What to Push to GitHub (Repo Hygiene)
✅ Commit These

dags/

plugins/

Dockerfile

docker-compose.yml

requirements.txt

Terraform files (infra)

.env.example (never real secrets)

.github/workflows/*

README.md

❌ Avoid Committing These

(Add to .gitignore)

logs/

airflow.db or any Airflow metadata DB file

*.log

Virtual env directories (.venv/, env/)

__pycache__/

.idea/, .vscode/

Generated passwords file (simple_auth_manager_passwords.json.generated)

🏁 12. End-to-End Quick Checklist

Activate venv

Set AIRFLOW_HOME

Run: airflow db migrate

Start: airflow standalone

Log in using generated credentials

Place DAG into dags/

Test task: airflow tasks test

Trigger in UI

Check logs

Push code (excluding logs/db)