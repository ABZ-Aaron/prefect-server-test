from prefect import flow, get_run_logger

@flow
def hello_flow(env: str = "dev"):
    logger = get_run_logger()
    logger.info(f"👋 Hello from {env} environment!")
