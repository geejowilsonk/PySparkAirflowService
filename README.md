docker exec -it pysparkairflowservice-airflow-webserver-1 bash -c "
  airflow users create \
    --username admin \
    --password admin \
    --firstname af_User \
    --lastname af_User \
    --role Admin \
    --email admin@org.com && \
  airflow scheduler"