import csv

FILE_PATH = "resources/csv/users.csv"


class User:
    def __init__(self, id: int, name: str, city: str, school: str) -> None:
        self.id = id
        self.name = name
        self.city = city
        self.school = school

    def __repr__(self) -> str:
        return f"[{self.id}] {self.name} at {self.school} in {self.city}"


def parse_user(line: list[str]) -> User:
    id, name, city, school = line
    return User(int(id), name, city, school)


users = []
with open(FILE_PATH, "r") as f:
    reader = csv.reader(f)
    # to skip the header
    next(reader)
    users = [parse_user(line) for line in reader]

for user in users:
    print(user)
