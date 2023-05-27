from airflow import DAG

from datetime import datetime

from helloOperator import HelloOperator

with DAG(
    dag_id="custom_operator",
    description="used custom operator",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@once",
) as dag:
    t1 =  HelloOperator(task_id="hello_with_custom",
                        name='Arnol')

    t1