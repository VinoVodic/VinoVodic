from typing import Any
from ...filters import BaseFilter


class Pipe:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.filters: list[BaseFilter] = []

    def add_filter(self, filter) -> None:
        self.filters.append(filter)

    def execute(self) -> None:
        for f in self.filters:
            self.data = f.filter(self.data)
