from prefect import flow, get_run_logger

@flow
def data_flow(env: str = "dev"):
    logger = get_run_logger()
    logger.info(f"📦 Running data flow in {env} environment!")
