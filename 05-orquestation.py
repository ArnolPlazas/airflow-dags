from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(
    dag_id="5.1-orquestation",
    description="prove orquestation",
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    end_date=datetime(2023, 12, 31),
    # argumentos que airflow tiene por defecto y que podemos cambiar.
    # 'depends_on_past': True -> cada una de las tareas depende de como se haya ejecutado la tarea anterior.
    default_args={'depends_on_past': True}, 
    max_active_runs=1 # Se ejecute maximo una vez en este caso por dia
) as dag:

    task1 =  BashOperator(task_id="task_1",
                        bash_command="sleep 2 && echo 'Task 1'")

    task2 =  BashOperator(task_id="task_2",
                        bash_command="sleep 2 && echo 'Task 2'")

    task3 =  BashOperator(task_id="task_3",
                        bash_command="sleep 2 && echo 'Task 3'")

    task4 =  BashOperator(task_id="task_4",
                        bash_command="sleep 2 && echo 'Task 4'")                  
    

    task1 >> task2 >> [task3, task4]