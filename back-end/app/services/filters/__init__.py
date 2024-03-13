from typing import Any


class BaseFilter:
    @staticmethod
    def filter(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        raise RuntimeError("Abstract method")
