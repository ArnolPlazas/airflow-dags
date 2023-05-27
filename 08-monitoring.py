from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


from datetime import datetime


def myFunction():
    raise Exception


with DAG(
    dag_id="8.monitoring",
    description="Monitoring our DAG",
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    end_date=datetime(2023, 12, 31)  
) as dag:

    task1 =  BashOperator(task_id="task_1",
                        bash_command="sleep 2 && echo 'Task 1'")

    task2 =  BashOperator(task_id="task_2",
                        bash_command="sleep 2 && echo 'Task 2'")

    task3 =  BashOperator(task_id="task_3",
                        bash_command="sleep 2 && echo 'Task 3'")

    task4 =  PythonOperator(task_id="task_4",
                        python_callable=myFunction) 

    task5 =  BashOperator(task_id="task_5",
                        bash_command="sleep 2 && echo 'Task 5'")                  
    

    task1 >> task2 >> task3 >> task4 >> task5