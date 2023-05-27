from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator


from datetime import datetime, date


def _choose(**context):
    if context["logical_date"].date() < date(2023, 1, 15):
        return "finish_14"
    else:
        return "start_15"

default_args = {
    'start_date': datetime(2023, 1, 10),
    'end_date': datetime(2023, 1, 16)
    }

with DAG("14-branching",
        schedule_interval="@daily",
        default_args=default_args) as dag:

    branching = BranchPythonOperator(task_id="branch",
                                    python_callable=_choose)
    
    finish_14 = BashOperator(task_id="finish_14",
                    bash_command="echo ' Running {{ ds }}'")
    
    start_15 = BashOperator(task_id="start_15",
                    bash_command="echo ' Running {{ ds }}'")

    branching >> [finish_14, start_15]

             