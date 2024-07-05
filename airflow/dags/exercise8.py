import json
from datetime import datetime

from airflow.decorators import dag, task
from airflow.providers.http.operators.http import HttpOperator


def response_filter(response):
    return response.json()["results"]


@dag(schedule=None, start_date=datetime(2024, 1, 1), catchup=False)
def exercise8():
    people = HttpOperator(
        task_id="get_people",
        http_conn_id="http_sw",
        endpoint="people",
        method="GET",
        log_response=True,
        response_filter=response_filter,
    )

    @task
    def write_users(path: str, data):
        with open(path, "w") as f:
            json.dump(data, f)

    write_users("./airflow/dags/data/exercise8.json", people.output)


exercise8()
