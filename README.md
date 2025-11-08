# prefect-server-test


-- set the required api endpoint
export PREFECT_API_URL=http://127.0.0.1:4200/api

-- Start prefect server
prefect server start

-- Run deployments
python deployment.py

-- Start a worker in the work pool. Our deployment
-- is assigned to this work pool. So our worker 
-- is going to listen to runs sent to this workpool 
-- and execute.
prefect worker start --pool 'my-work-pool'

-- Run deployment
prefect deployment run 'my-flow 'my-github-deployment_two'
