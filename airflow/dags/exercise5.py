import json
from datetime import datetime

from airflow.decorators import dag, task


@dag(schedule=None, start_date=datetime(2024, 1, 1), catchup=False)
def exercise5():
    @task
    def read_users(path: str) -> str:
        with open(path, "r") as f:
            users = json.load(f)

        return json.dumps(users)

    @task
    def print_users(raw_users: str) -> None:
        for user in json.loads(raw_users):
            print(user)

    users = read_users("./airflow/dags/data/users.json")
    print_users(users)


_ = exercise5()
