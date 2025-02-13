from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG('simple_spark_job', schedule_interval=None, default_args=default_args, catchup=False) as dag:

    run_spark_job = DockerOperator(
        task_id='run_spark_job',
        image='bitnami/spark:latest',
        api_version='auto',
        auto_remove='success',
        command='spark-submit /opt/airflow/pyspark_jobs/spark_app.py',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        mounts=[
            Mount(source='/Users/gjo/PycharmProjects/PySparkAirflowService/pyspark_jobs', target='/opt/airflow/pyspark_jobs', type='bind')
        ],  # Mount DAGs folder to Spark container
    )
