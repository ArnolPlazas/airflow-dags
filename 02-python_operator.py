from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime



def print_hello():
    print('Hello Platzi!')


with DAG(
    dag_id="python_operator_dependecies",
    description="used python operator with dependecies",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@once",
) as dag:
    t1 = PythonOperator(task_id="t1",
                        python_callable=print_hello)

    t2 = BashOperator(task_id="t2",
                        bash_command="echo  hello t2!")

    t3 = BashOperator(task_id="t3",
                        bash_command="echo  hello t3!")
    
    t4 = BashOperator(task_id="t4",
                        bash_command="echo  hello t4!")

    
    # t1.set_downstream(t2)
    # t2.set_downstream([t3, t4])
    t1 >> t2 >> [t3, t4]