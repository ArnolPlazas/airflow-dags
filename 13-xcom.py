from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from datetime import datetime

def myfunction(**context):
    print(int(context["ti"].xcom_pull(task_ids='task2')) - 24)

default_args = {"depends_on_past": True}

with DAG(dag_id="13-XCom",
        description="Examples using XCom",
        schedule_interval="@once",
        start_date=datetime(2023, 1, 15),
        end_date=datetime(2023, 1, 16),
        default_args=default_args,
        max_active_runs=1) as dag:

    t1 = BashOperator(task_id="task1",
                    bash_command="sleep 5 && echo $((3 * 8))")
                    
    t2 = BashOperator(task_id="task2",
                      bash_command="sleep 3 && echo {{ ti.xcom_pull(task_ids='task1')}}") # ti : task intance # xcom_pull: traernos el resultado de otra tarea
    
    t3 = PythonOperator(task_id="task3",
                        python_callable=myfunction)
    
    t1 >> t2 >> t3