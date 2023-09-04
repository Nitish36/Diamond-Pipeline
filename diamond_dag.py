from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from diamond_mod import write_df


with DAG(
    dag_id="etl_end_to_end",
    start_date=datetime(2023, 8, 4),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    reading_data = PythonOperator(
        task_id="reading_data",
        python_callable=write_df,
        provide_context=True
    )

    reading_data