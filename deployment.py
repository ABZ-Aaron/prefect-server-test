from prefect import flow

github_url = "https://github.com/ABZ-Aaron/prefect-server-test.git"

if __name__ == "__main__":
    
    deployment_name = "my-github-deployment_one"
    entrypoint = "pipelines/pipeline_one.py:my_flow"
    flow.from_source(
        source=github_url,
        entrypoint=entrypoint,
    ).deploy(
        name=deployment_name,
        work_pool_name="dev-workpool-a",
    )
    
    deployment_name = "my-github-deployment_two"
    entrypoint = "pipelines/pipeline_two.py:my_flow"
    flow.from_source(
        source=github_url,
        entrypoint=entrypoint,
    ).deploy(
        name=deployment_name,
        work_pool_name="prod-workpool-a",
    )