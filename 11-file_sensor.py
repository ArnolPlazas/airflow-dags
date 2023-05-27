from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

from datetime import datetime



with DAG(dag_id="11-filesensor",
        description="File sensor",
        schedule_interval="@daily",
        start_date=datetime(2023, 1, 10),
        end_date=datetime(2023, 1, 13)) as dag:

    t1 = BashOperator(task_id="creating_file",
                    bash_command="sleep 5 && touch /tmp/file.txt") 

    t2 = FileSensor(task_id="waiting_file",
                    filepath="/tmp/file.txt")

    t3 = BashOperator(task_id="end_task",
                    bash_command="echo 'The file arrived!'") 

    t1 >> t2 >> t3