from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

templated_command = """

{% for file in params.filenames %}
    echo "{{ ds }}"
    echo "{{ file }}"
{% endfor %}

"""

with DAG(dag_id="12-Templating",
        description="Examples using templates",
        schedule_interval="@daily",
        start_date=datetime(2023, 1, 10),
        end_date=datetime(2023, 1, 16),
        max_active_runs=1) as dag:

    t1 = BashOperator(task_id="task1",
                    bash_command=templated_command,
                    params={'filenames': ['file1.txt', 'file2.txt']},
                    depends_on_past = True)
                    
    t1