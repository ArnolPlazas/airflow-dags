from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(
    dag_id="bash_operator",
    description="used bash operator",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@once",
) as dag:
    op =  BashOperator(task_id="hello_with_bash",
                        bash_command="echo 'Hello wolrd!'")

    op