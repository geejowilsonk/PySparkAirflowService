# PySpark Airflow Service

## Overview

This project sets up an Airflow environment using Docker Compose, integrated with Apache Spark. The setup includes:

- PostgreSQL as the Airflow metadata database
- Airflow Webserver & Scheduler
- Apache Spark 

## Setup and Running the Services


2. Start the services using Docker Compose:

   ```sh
   docker-compose up 
   ```

3. Create an Airflow user and start the scheduler:
 This will creates the airflow user and can be logged in to to the airflow ui
   ```sh
   docker exec -it pysparkairflowservice-airflow-webserver-1 bash -c "
     airflow users create \
       --username admin \
       --password admin \
       --firstname af_User \
       --lastname af_User \
       --role Admin \
       --email admin@org.com && \
     airflow scheduler"
   ```

4. Access the Airflow web UI:

   - Open your browser and go to [http://localhost:8080](http://localhost:8080)
   - Login with username: `admin`, password: `admin`

5. To check the logs and status of running containers:

   ```sh
   docker-compose logs -f
   ```

## Stopping the Services

To stop and remove the containers:

```sh
   docker-compose down
```

## Running a Spark Job

- use airflow for that.
1) DAG - run_spark_job - which use airflow to spin up a docker container and run spark jobs
2) DAG - spark_parallel_execution - This will run spark jobs in parallel.

## Troubleshooting

- If Airflow does not start, ensure that the database is initialized correctly:
  ```sh
  docker exec -it pysparkairflowservice-airflow-webserver-1 airflow db upgrade
  ```
- If Spark jobs do not run, check the cluster status in the Spark UI at [http://localhost:8081](http://localhost:8081).

