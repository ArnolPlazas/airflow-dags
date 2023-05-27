from airflow import DAG
from airflow.operators.empty import EmptyOperator

from datetime import datetime



with DAG(
    dag_id="6-orquestation",
    description="prove orquestation",
    schedule_interval="0 7 * * 1",
    start_date=datetime(2023, 1, 1),
    end_date=datetime(2023, 12, 31),
) as dag:

    task1 =  EmptyOperator(task_id="task_1")

    task2 =  EmptyOperator(task_id="task_2")

    task3 =  EmptyOperator(task_id="task_3")

    task4 =  EmptyOperator(task_id="task_4")                  
    

    task1 >> task2 >> task3 >> task4