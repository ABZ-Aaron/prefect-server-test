# flows/my_flow.py
from prefect import flow, get_run_logger

CONFIG = {
    "dev": {
        "sink_table": "my_schema.my_table_dev",
        "write_mode": "append",
    },
    "prod": {
        "sink_table": "my_schema.my_table",
        "write_mode": "overwrite",
    },
}

@flow
def my_flow(env: str = "dev", message: str = "hello"):
    logger = get_run_logger()
    if env not in CONFIG:
        raise ValueError(f"Unknown env: {env}")
    cfg = CONFIG[env]

    logger.info(f"Running env={env}")
    logger.info(f"Writing to {cfg['sink_table']} with mode={cfg['write_mode']}")
    logger.info(f"message={message}")

    print(cfg)
    # ... your ETL/ELT here ...
    
if __name__ == "__main__":
    my_flow()