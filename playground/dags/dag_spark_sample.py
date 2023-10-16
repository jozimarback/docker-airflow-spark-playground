from datetime import datetime
from airflow.models.dag import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

with DAG(
    dag_id="dag_spark_sample",
    schedule=None,
    start_date=datetime(2023, 10, 12),
    catchup=False,
    tags=["spark"],
) as dag:

    task_spark = SparkSubmitOperator(
        task_id='etl_spark',
        conn_id='spark',
        application="/usr/local/spark/job/sparkjob.py",        
        application_args=["/usr/local/spark/resources/all_players_ea_24_fc.csv"],
        verbose=1,
        conf={"spark.master":"spark://spark:7077"},
        dag=dag
    )

    task_spark