from typing import Any

from app.models import Winery


class WineryService:
    def get_winery_by_id(self, winery_id: int) -> dict[str, Winery]:
        raise NotImplementedError

    def get_wineries_by_city(self, city_id: int) -> dict[str, list[Winery]]:
        raise NotImplementedError

    def get_all_wineries(self) -> dict[str, list[Winery]]:
        raise NotImplementedError

    def get_wineries(
        self,
        data: dict[str, Any],
    ) -> dict[str, Winery] | dict[str, list[Winery]]:
        raise NotImplementedError
