from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/ABZ-Aaron/prefect-server-test.git",
        entrypoint="pipelines/code.py:my_flow",
    ).deploy(
        name="my-github-deployment",
        work_pool_name="my-work-pool",
    )