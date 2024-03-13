from typing import Any
from . import BaseFilter


class CoordinatesFilter(BaseFilter):
    @staticmethod
    def filter(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        new_data = []

        for row in data:
            if len(row["coords"]) != 0:
                coords = row["coords"].split("=")[-1].split(",")
                row["coords"] = coords[::-1]
                new_data.append(row)

        return new_data
