from airflow import DAG
from airflow.operators.python import PythonOperator



def print_hello():
    print('Hello Platzi!')


from datetime import datetime

with DAG(
    dag_id="python_operator",
    description="used python operator",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@once",
) as dag:
    op = PythonOperator(task_id="hello_with_python",
                        python_callable=print_hello)