from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime



with DAG(dag_id="10.1-externalTaskSensor",
        description="DAG principal",
        schedule_interval="@daily",
        start_date=datetime(2023, 1, 10),
        end_date=datetime(2023, 1, 13)) as dag:

    t1 = BashOperator(task_id="t1.1",
                    bash_command="sleep 5 && echo 'DAG finalizado!'",
                    depends_on_past=True) 

    t1