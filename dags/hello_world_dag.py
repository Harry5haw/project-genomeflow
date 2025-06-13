# Import the necessary modules from the Airflow package
from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# This is the main definition of your pipeline (the DAG)
with DAG(
    dag_id="hello_world_dag",  # The unique name for your DAG, as it appears in the UI
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),  # The date when your DAG will start being scheduled
    schedule=None,  # We set this to None so it only runs when we trigger it manually
    catchup=False,  # Prevents the DAG from running for past, un-run dates
    tags=["example"], # Optional tags to help organize your DAGs in the UI
) as dag:
    
    # This is the first and only task in our pipeline
    # It uses the BashOperator to run a simple shell command
    hello_task = BashOperator(
        task_id="hello_task",  # A unique name for this task within the DAG
        bash_command="echo 'Hello World! This is my first Airflow pipeline!'", # The command to run
    )