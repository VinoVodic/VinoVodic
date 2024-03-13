from typing import Any
from . import BaseFilter


class ActivitesFilter(BaseFilter):
    @staticmethod
    def filter(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        for row in data:
            row.pop("dejnosti")

        return data
