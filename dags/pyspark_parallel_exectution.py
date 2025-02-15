"""
This DAG submits three Spark jobs to the existing Spark container defined in Docker Compose.
Instead of creating new Spark containers, we run 'spark-submit' inside the running Spark master.

- Job 1 runs first.
- Job 2 and Job 3 will run in parallel once Job 1 succeeds.
"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'spark_parallel_execution',
    default_args=default_args,
    description='A DAG that runs Spark jobs inside an existing Spark container',
    schedule_interval=None,
)

# Run Spark Job 1
run_spark_job_1 = BashOperator(
    task_id='run_spark_job_1',
    bash_command="docker exec pysparkairflowservice-spark-1 spark-submit --master local /tmp/pyspark_jobs/spark_app.py",
    dag=dag,
)

# Run Spark Job 2 (Triggered after Job 1)
run_spark_job_2 = BashOperator(
    task_id='run_spark_job_2',
    bash_command="docker exec pysparkairflowservice-spark-1 spark-submit --master local /tmp/pyspark_jobs/spark_app.py",
    dag=dag,
)

# Run Spark Job 3 (Triggered after Job 1)
run_spark_job_3 = BashOperator(
    task_id='run_spark_job_3',
    bash_command="docker exec pysparkairflowservice-spark-1 spark-submit --master local /tmp/pyspark_jobs/spark_app.py",
    dag=dag,
)

# DAG Dependencies
run_spark_job_1 >> [run_spark_job_2, run_spark_job_3]  # Job 2 and Job 3 run in parallel after Job 1
