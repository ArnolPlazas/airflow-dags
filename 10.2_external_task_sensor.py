from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor



from datetime import datetime



with DAG(dag_id="10.2-externalTaskSensor",
        description="DAG Secundario",
        schedule_interval="@daily",
        start_date=datetime(2023, 1, 10),
        end_date=datetime(2023, 1, 13)) as dag:


    t1 = ExternalTaskSensor(task_id="t1.2",
                external_dag_id="10.1-externalTaskSensor", # DAG que activa este DAG
                external_task_id="t1.1", # Tarea especifica que activa este DAG
                poke_interval=10) # cantidad de segundos que va estar preguntado si la tarea o el DAG que activa este DAG ya termino.

    t2 = BashOperator(task_id="t2.2",
                    bash_command="sleep 5 && echo 'DAG 2 finalizado!'",
                    depends_on_past=True) 

    t1 >> t2