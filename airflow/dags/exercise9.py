from datetime import datetime

from airflow.decorators import dag
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


@dag(schedule=None, start_date=datetime(2023, 1, 11), catchup=False)
def exercise9():
    drop_table = SQLExecuteQueryOperator(
        task_id="drop_table",
        conn_id="sqlite_test",
        sql="DROP TABLE IF EXISTS users;",
    )

    create_table = SQLExecuteQueryOperator(
        task_id="create_table",
        conn_id="sqlite_test",
        sql="CREATE TABLE users (id text, name text, city text, school text, age int, is_teacher int);",
    )

    add_data = SQLExecuteQueryOperator(
        task_id="add_data",
        conn_id="sqlite_test",
        sql='INSERT INTO users VALUES("0001", "Pierre", "Paris", "EPITA" , 36, 1);',
    )

    drop_table >> create_table >> add_data


_ = exercise9()
