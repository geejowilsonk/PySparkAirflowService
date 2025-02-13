docker exec -it pysparkservice-airflow-webserver-1 bash -c "
  airflow users create \
    --username admin \
    --password admin \
    --firstname airflow \
    --lastname airflow \
    --role Admin \
    --email admin@example.org && \
  airflow scheduler"