import json
from collections import defaultdict

FILE_PATH = "resources/json/french-cities.json"

with open(FILE_PATH, "r") as f:
    data = json.load(f)

regions = defaultdict(list)

for row in data:
    regions[row["admin_name"]].append(row)


def compute_data_for_region(cities) -> tuple[int, int, str]:
    populations = [
        int(city["population"]) for city in cities if city["population"] != ""
    ]

    def sort_city(city) -> int:
        return int(city["population"]) if city["population"] != "" else 0

    biggest_city = max(
        cities,
        key=lambda city: int(city["population"]) if city["population"] != "" else 0,
    )
    return (
        sum(populations),
        int(sum(populations) / len(populations)),
        biggest_city["city"],
    )


for region, values in regions.items():
    print(f"{region}: {compute_data_for_region(values)}")
