from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG('simple_spark_job', schedule_interval=None, default_args=default_args, catchup=False) as dag:
    """
    This Airflow task uses the DockerOperator to run a Spark job inside a Bitnami Spark container. 
    It pulls the latest Spark image and runs a `spark-submit` command to execute a PySpark script 
    located in the `pyspark_jobs` directory inside the container. 

    A directory from the host machine (`pyspark_jobs`) 
    is mounted inside the container at `/opt/airflow/pyspark_jobs` so that the script can be accessed 
    by the Spark process. This ensures that the PySpark job is executed within the container without 
    modifying the container image itself.
    """
    run_spark_job = DockerOperator(
        task_id='run_spark_job',
        image='bitnami/spark:latest',
        api_version='auto',
        auto_remove='success',
        command='spark-submit /opt/airflow/pyspark_jobs/spark_app.py',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        mounts=[
            #This source absolute path has to be changed accordingly.
            Mount(source='/Users/gjo/PycharmProjects/PySparkAirflowService/pyspark_jobs', target='/opt/airflow/pyspark_jobs', type='bind')
        ],  # Mount DAGs folder to Spark container
    )
