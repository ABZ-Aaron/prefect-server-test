import os
from datetime import timedelta
from prefect import flow
from prefect.client.schemas.schedules import IntervalSchedule

# Base GitHub source URL for Prefect 3+
# It can be public or use a Prefect-managed GitHub block for private repos
GITHUB_URL = "https://github.com/ABZ-Aaron/prefect-server-test.git"

# Environment (default = dev for local runs)
ENV = os.getenv("PREFECT_ENV", "dev")

# Define flows and configurations
FLOWS = [
    {
        "name": "hello_flow",
        "entrypoint": "pipelines/pipeline_one.py:hello_flow",
        "base_tags": ["greeting"],
        "schedule": {
            "dev": IntervalSchedule(interval=timedelta(minutes=5)),
            "prod": IntervalSchedule(interval=timedelta(hours=1)),
        },
    },
    {
        "name": "data_flow",
        "entrypoint": "pipelines/pipeline_two.py:data_flow",
        "base_tags": ["data"],
        "schedule": {
            "dev": None,
            "prod": IntervalSchedule(interval=timedelta(hours=6)),
        },
    },
]

def main():
    print(f"🚀 Deploying flows for environment: {ENV}")

    for cfg in FLOWS:
        deployment_name = f"{cfg['name']}-{ENV}"
        work_pool = f"{ENV}-workpool-a"
        schedule = cfg["schedule"].get(ENV)

        print(f"📦 Creating deployment: {deployment_name} -> {work_pool}")

        # Prefect 3 style: source-based deployment from GitHub
        flow.from_source(
            source=GITHUB_URL,
            entrypoint=cfg["entrypoint"],
        ).deploy(
            name=deployment_name,
            work_pool_name=work_pool,
            parameters={"env": ENV},
            schedule=schedule,
            tags=[ENV, *cfg["base_tags"]],
            description=f"{cfg['name']} ({ENV} environment)",
        )

    print("✅ All deployments created successfully!")

if __name__ == "__main__":
    main()
